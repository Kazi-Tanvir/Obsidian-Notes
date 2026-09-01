tags:

- javascript

- design-patterns

- typescript

- creational-patterns

- structural-patterns

- architecture

- clean-code date: 2026-08-22

# Day 22 - Creational & Structural Design Patterns in Modern JavaScript & TypeScript

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Creational Design Patterns in Modern JavaScript/TypeScript

Creational patterns abstract the object instantiation process, making systems independent of how their objects are created, composed, and represented.

#### A. The Singleton Pattern

Ensures a class has only one instance while providing a global access point. In modern ESM, JavaScript modules are singletons by default because module evaluation is cached upon first import.

// Thread-safe / Closure-guarded Singleton in TypeScript

export class DatabaseConnectionPool {

private static instance: DatabaseConnectionPool \| null = null;

private readonly connectionString: string;

private constructor(connectionString: string) {

this.connectionString = connectionString;

}

public static getInstance(connectionString: string = \"postgres://localhost:5432\"): DatabaseConnectionPool {

if (!DatabaseConnectionPool.instance) {

DatabaseConnectionPool.instance = new DatabaseConnectionPool(connectionString);

Object.freeze(DatabaseConnectionPool.instance); // Prevent external mutation

}

return DatabaseConnectionPool.instance;

}

}

#### B. The Factory Method & Abstract Factory Pattern

Encapsulates object creation logic, allowing subclasses or caller configurations to determine which concrete class or interface to instantiate without tight coupling.

// Polymorphic Payment Gateway Factory

export interface PaymentProcessor {

processPayment(amount: number): Promise\<{ success: boolean; txId: string }\>;

}

export class StripeProcessor implements PaymentProcessor {

async processPayment(amount: number) {

return { success: true, txId: \`stripe\_\${Date.now()}\` };

}

}

export class PayPalProcessor implements PaymentProcessor {

async processPayment(amount: number) {

return { success: true, txId: \`paypal\_\${Date.now()}\` };

}

}

export class PaymentProcessorFactory {

public static createProcessor(provider: \"stripe\" \| \"paypal\"): PaymentProcessor {

switch (provider) {

case \"stripe\":

return new StripeProcessor();

case \"paypal\":

return new PayPalProcessor();

default:

throw new Error(\`Unsupported payment provider: \${provider}\`);

}

}

}

#### C. The Builder Pattern with Immutable Fluent API

Separates the construction of a complex object from its representation, allowing the same construction process to create diverse representations.

// Immutable Fluent Request Builder

export class HttpRequestBuilder {

private readonly url: string;

private readonly method: string;

private readonly headers: Record\<string, string\>;

private readonly body?: unknown;

constructor(url: string, method: string = \"GET\", headers: Record\<string, string\> = {}, body?: unknown) {

this.url = url;

this.method = method;

this.headers = headers;

this.body = body;

}

public setMethod(method: \"GET\" \| \"POST\" \| \"PUT\" \| \"DELETE\"): HttpRequestBuilder {

return new HttpRequestBuilder(this.url, method, { \...this.headers }, this.body);

}

public setHeader(key: string, value: string): HttpRequestBuilder {

return new HttpRequestBuilder(this.url, this.method, { \...this.headers, \[key\]: value }, this.body);

}

public setJsonBody(body: unknown): HttpRequestBuilder {

return new HttpRequestBuilder(this.url, this.method, { \...this.headers, \"Content-Type\": \"application/json\" }, body);

}

public build(): Request {

return new Request(this.url, {

method: this.method,

headers: this.headers,

body: this.body ? JSON.stringify(this.body) : undefined

});

}

}

### 2. Structural Design Patterns in Modern JS/TS

Structural patterns focus on how classes and objects are composed to form larger, flexible structures.

#### A. The Adapter Pattern

Converts the interface of a class into another interface clients expect, enabling incompatible classes to collaborate.

// Adapting Legacy XML Third-Party Service to Standard JSON Contract

interface ModernWeatherService {

getTemperature(city: string): Promise\<number\>;

}

class LegacyXmlWeatherApi {

public fetchXmlData(location: string): string {

return \`\<weather\>\<city\>\${location}\</city\>\<temp_f\>77\</temp_f\>\</weather\>\`;

}

}

export class WeatherApiAdapter implements ModernWeatherService {

constructor(private legacyApi: LegacyXmlWeatherApi) {}

async getTemperature(city: string): Promise\<number\> {

const xml = this.legacyApi.fetchXmlData(city);

// Parse XML and convert Fahrenheit to Celsius

const tempFMatch = xml.match(/\<temp_f\>(\\d+)\<\\/temp_f\>/);

const tempF = tempFMatch ? parseFloat(tempFMatch\[1\]) : 32;

return ((tempF - 32) \* 5) / 9;

}

}

#### B. The Decorator Pattern (TC39 Stage 3 Decorators)

Attaches additional responsibilities to methods, accessors, or classes dynamically without modifying the underlying class definition.

// TC39 Stage 3 Method Timing Decorator

export function LogExecutionTime\<This, Args extends any\[\], Return\>(

target: (this: This, \...args: Args) =\> Return,

context: ClassMethodDecoratorContext\<This, (this: This, \...args: Args) =\> Return\>

) {

const methodName = String(context.name);

return function (this: This, \...args: Args): Return {

const start = performance.now();

const result = target.apply(this, args);

const duration = performance.now() - start;

console.log(\`\[Method \${methodName}\] Execution Time: \${duration.toFixed(2)}ms\`);

return result;

};

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Design Pattern Classification Summary:

  -----------------------------------------------------------------------------------------------------------------------
  **Pattern**       **Category**      **Intent**                        **Key Advantage in JS/TS**
  ----------------- ----------------- --------------------------------- -------------------------------------------------
  **Singleton**     Creational        Single shared instance            Resource pooling (DB connections, caches)

  **Factory**       Creational        Dynamic instance generation       Decouples concrete instantiation from usage

  **Builder**       Creational        Step-by-step object assembly      Fluent, immutable parameter configuration

  **Adapter**       Structural        Interface translation             Integrates incompatible/legacy SDKs

  **Decorator**     Structural        Dynamic behavior extension        Cross-cutting concerns (logging, auth, metrics)

  **Facade**        Structural        Simplified high-level interface   Hides complexity of multi-subsystem workflows
  -----------------------------------------------------------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Factory vs Constructor Object Shape Optimization

Analyze the two object generation approaches below. Explain how V8\'s Hidden Classes (Shapes) and Inline Caches (ICs) behave when calling calculateTotal() on objects produced by Approach A vs Approach B.

// Approach A: Inline Object Literal Factory

function createItemA(id, price, tax) {

if (tax) {

return { id, price, tax };

}

return { id, price };

}

// Approach B: Monomorphic Class Constructor

class ItemB {

constructor(id, price, tax = 0) {

this.id = id;

this.price = price;

this.tax = tax;

}

}

*Hint*: Evaluate property initialization ordering and dictionary-mode bailouts under inconsistent object property counts.

### Challenge 2: Refactoring a Complex Monolithic API Client to the Builder Pattern

Refactor the following bloated, positional-argument function into a strongly-typed, immutable ApiQueryBuilder class with validation checks:

// Legacy Anti-Pattern: Monolithic function with 7 positional parameters

function searchProducts(

query: string,

category?: string,

minPrice?: number,

maxPrice?: number,

sortBy?: \"price\" \| \"date\",

page?: number,

limit?: number

) {

// executes search\...

}

*Hint*: Ensure validation rules (e.g., minPrice \<= maxPrice and limit \<= 100) throw descriptive errors upon calling .build().

### Challenge 3: Advanced TC39 Stage 3 Decorator Suite in TypeScript

Build a production-grade decorator suite in TypeScript:

1.  \@AutoRetry({ maxAttempts: number, backoffMs: number }): Retries failed asynchronous method executions with exponential backoff before throwing the final error.

2.  \@Memoize({ ttlMs: number }): Caches method return values based on serialized arguments with automatic TTL cache invalidation.

3.  \@ValidateArgs(schema: ZodSchema): Validates incoming method arguments against a Zod schema before invoking the underlying method body.

*Hint*: Use TC39 Stage 3 method decorator signatures (target, context: ClassMethodDecoratorContext) and wrap the original function in a higher-order executor.
