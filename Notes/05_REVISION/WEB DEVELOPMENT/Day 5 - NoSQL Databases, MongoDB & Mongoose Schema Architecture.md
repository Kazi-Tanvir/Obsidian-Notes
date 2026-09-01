---
tags:
- database
- mongodb
- mongoose
- nosql
- backend
- document-db
date: 2026-08-05
---

# Day 5 - NoSQL Databases, MongoDB & Mongoose Schema Architecture

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Document Model vs Relational Paradigm

MongoDB is a distributed, document-oriented NoSQL database that stores data in flexible **BSON** (Binary JSON) documents.

#### Key Differences & Architectural Advantages:

- **Schema Flexibility**: Documents in a single collection can have varying fields (ideal for evolving domain models).

- **Horizontal Scalability (Sharding)**: Distributes data across multiple cluster nodes via a Shard Key.

- **Replica Sets & Availability**: Primary node handles writes; Secondary nodes replicate data. Write Concern (w: "majority") guarantees durability across nodes before acknowledging client writes.

### 2. Modeling Strategies: Embedding vs Referencing

In NoSQL document design, data modeling centers on query access patterns:

1.  **Embedding (Denormalization)**: Nesting sub-documents inside a parent document.

    - *Best for*: 1-to-1 or 1-to-Few relationships (e.g. User addresses).

    - *Advantage*: High-performance single-read operations without $lookup joins.

    - *Constraint*: BSON document hard limit is **16MB**. Avoid unbounded array growth!

2.  **Referencing (Normalization)**: Storing ObjectIds referencing documents in separate collections.

    - *Best for*: 1-to-Many or Many-to-Many relationships (e.g. Author to Articles, User to Orders).

    - *Advantage*: Eliminates data duplication and avoids 16MB document size overflow.

### 3. Mongoose ORM Architecture & Production Patterns

Mongoose provides a schema-based solution to model application data with type validation, middleware hooks, virtuals, and populate mechanisms.

```typescript
// Mongoose Production Schema with Hooks, Virtuals & Indexes
import { Schema, model, Document, Types } from 'mongoose';
export interface IOrder extends Document {
user: Types.ObjectId;
items: Array<{ productId: string; quantity: number; price: number }>;
totalAmount: number;
status: 'pending' | 'completed' | 'cancelled';
createdAt: Date;
}
const orderSchema = new Schema<IOrder>(
{
```

user: { type: Schema.Types.ObjectId, ref: 'User', required: true, index: true },

items: [

```javascript
{
```

productId: { type: String, required: true },

quantity: { type: Number, required: true, min: 1 },

price: { type: Number, required: true }

```javascript
}
```

],

totalAmount: { type: Number, required: true },

status: { type: String, enum: ['pending', 'completed', 'cancelled'], default: 'pending' }

},

{ timestamps: true }

```javascript
);
// Compound Index for High-Volume Querying
orderSchema.index({ user: 1, createdAt: -1 });
// Pre-save Hook for Automated Calculations
```

orderSchema.pre<IOrder>('save', function (next) {

```typescript
this.totalAmount = this.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
next();
});
export const OrderModel = model<IOrder>('Order', orderSchema);
// Atomic Transaction & Population Query
import mongoose from 'mongoose';
async function processOrderCheckout(userId: string, items: any[]) {
const session = await mongoose.startSession();
session.startTransaction();
try {
const order = await OrderModel.create(
```

[{ user: userId, items, status: 'completed' }],

{ session }

```javascript
);
// Populate user profile details without fetching password
const populatedOrder = await OrderModel.findById(order[0]._id)
.populate('user', 'name email -_id')
.session(session);
await session.commitTransaction();
session.endSession();
return populatedOrder;
} catch (error) {
await session.abortTransaction();
session.endSession();
throw error;
}
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **Operation / Concept** | **Mongoose / MongoDB Syntax** | **Description / Best Practice** |
| --- | --- | --- |
| **Atomic Field Update** | Model.updateOne({ _id }, { $inc: { views: 1 }, $set: { status: 'active' } })                                    Avoi | s race conditions vs read-and-save |
| **Array Push** | Model.updateOne({ _id }, { $push: { tags: 'node' } })                                                            App | nds element to array field |
| **Populate Join** | .populate('user', 'name email')                                                                                  Per | orms client-side $lookup join |
| **Aggregation Stage** | [{ $match: { status: 'completed' } }, { $group: { _id: '$user', total: { $sum: '$totalAmount' } } }]   High-performa | ce analytics pipeline |
| **Text Search Index** | schema.index({ title: 'text', description: 'text' })                                                             Ena | les $text: { $search: 'keywords' } |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Architecture Design (Real-Time Activity Stream Bucket Pattern)

Design a MongoDB document schema architecture for an analytics platform tracking **10 Million daily IoT sensor temperature metrics**.

**Requirements**:

1.  Demonstrate how naive 1-doc-per-reading creates indexing overhead and exceeds storage bounds.

2.  Apply the **Bucket Pattern** (grouping metrics by hour into a single document with pre-allocated arrays).

3.  Design the Mongoose schema and write an aggregation pipeline to calculate hourly average, max, and min temperature metrics.

### Problem 2: End-to-End Code Implementation Challenge

Build a robust **Mongoose Multi-Document Transactional Wallet Service**.

**Requirements**:

1.  Create UserWallet and TransactionHistory schemas.

2.  Implement a function transferBalance(senderId: string, receiverId: string, amount: number) using MongoDB Session Transactions (session.withTransaction).

3.  Ensure atomic balance deduction ($inc: { balance: -amount }) with balance sufficiency checks (balance: { $gte: amount }).

4.  Provide unit tests simulating 5 concurrent transfer requests against a single wallet balance.
