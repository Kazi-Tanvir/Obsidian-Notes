---
tags:
- javascript
- security
- crypto
- web-crypto-api
- subtle-crypto
- encryption
- hashing
- hmac
date: 2026-08-26
---

# Day 26 - Web Crypto API: SubtleCrypto, AES-GCM Encryption, SHA-256 Hashing & HMAC Signatures

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Web Crypto Architecture (globalThis.crypto.subtle)

The Web Crypto API provides low-level, high-performance, cryptographically secure primitives natively implemented in browser and Node.js runtimes. Cryptographic operations run asynchronously in background threads with hardware acceleration (e.g. Intel AES-NI instructions), avoiding main-thread V8 blocking.

### 2. Core Cryptographic Primitives

#### A. Cryptographically Secure Pseudo-Random Numbers (CSPRNG)

- Never use Math.random() for cryptographic tokens, session IDs, or nonces (it uses non-cryptographic algorithms like Xoroshiro128+).

- Always use crypto.getRandomValues() to generate cryptographically strong entropy.

```javascript
// Generating a 96-bit (12-byte) Cryptographic Initialization Vector (IV)
const iv = crypto.getRandomValues(new Uint8Array(12));
```

#### B. Cryptographic Hashing with SHA-256

A one-way deterministic mathematical function that maps arbitrary binary data to a fixed 256-bit hash.

```typescript
export async function sha256(message: string): Promise<string> {
const encoder = new TextEncoder();
const data = encoder.encode(message);
const hashBuffer = await crypto.subtle.digest("SHA-256", data);
// Convert ArrayBuffer to Hex String
const hashArray = Array.from(new Uint8Array(hashBuffer));
return hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
}
```

#### C. Symmetric Authenticated Encryption with AES-GCM (Galois/Counter Mode)

AES-GCM provides both **confidentiality** (encryption) and **integrity/authenticity** (detects tampering via an authentication tag).

- **Key Length**: 256-bit (AES-GCM with length 256).

- **Initialization Vector (IV)**: Must be unique for every single encryption operation using the same key (standard is 12 bytes / 96 bits).

```javascript
// 1. Generate AES-256-GCM Key
export async function generateAesKey(): Promise<CryptoKey> {
return crypto.subtle.generateKey(
```

{ name: "AES-GCM", length: 256 },

true, // extractable

["encrypt", "decrypt"]

```typescript
);
}
// 2. Encrypt Plaintext (Returns IV + Ciphertext with Auth Tag)
export async function encryptData(key: CryptoKey, plaintext: string): Promise<{ iv: Uint8Array; ciphertext: ArrayBuffer }> {
const encoder = new TextEncoder();
const data = encoder.encode(plaintext);
const iv = crypto.getRandomValues(new Uint8Array(12)); // 96-bit unique IV
const ciphertext = await crypto.subtle.encrypt(
```

{ name: "AES-GCM", iv },

key,

data

```javascript
);
return { iv, ciphertext };
}
// 3. Decrypt Ciphertext
export async function decryptData(key: CryptoKey, iv: Uint8Array, ciphertext: ArrayBuffer): Promise<string> {
const decryptedBuffer = await crypto.subtle.decrypt(
```

{ name: "AES-GCM", iv },

key,

ciphertext

```javascript
);
const decoder = new TextDecoder();
return decoder.decode(decryptedBuffer);
}
```

#### D. Message Authentication Codes (HMAC-SHA256)

HMAC provides message integrity and authenticity verification using a shared secret key, resisting length-extension attacks.

```typescript
// Sign and Verify Webhook Payloads
export async function signPayload(secretKey: string, payload: string): Promise<string> {
const encoder = new TextEncoder();
const key = await crypto.subtle.importKey(
```

"raw",

```javascript
encoder.encode(secretKey),
```

{ name: "HMAC", hash: "SHA-256" },

false,

["sign", "verify"]

```javascript
);
const signatureBuffer = await crypto.subtle.sign("HMAC", key, encoder.encode(payload));
return Array.from(new Uint8Array(signatureBuffer))
.map((b) => b.toString(16).padStart(2, "0"))
.join("");
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### SubtleCrypto Methods & Algorithm Reference:

| **Operation** | **Algorithm** | **Standard Key Size** | **Key Usages** |
| --- | --- | --- | --- |
| **Symmetric Encryption** | AES-GCM | 256 bits (32 bytes) | ["encrypt", "decrypt"] |
| **Password Key Derivation** | PBKDF2 / HKDF | 100,000+ iterations | ["deriveKey", "deriveBits"] |
| **Hashing** | SHA-256 / SHA-512 | N/A (One-way) | digest() |
| **Message Authentication** | HMAC (SHA-256) | 256+ bits | ["sign", "verify"] |
| **Asymmetric Signatures** | ECDSA / Ed25519 | P-256 / P-384 | ["sign", "verify"] |

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: The Catastrophic IV Reuse Attack in AES-GCM

Analyze the security failure in the code below. Explain why encrypting two different messages with the same AES-GCM key and identical Initialization Vector (IV) destroys ciphertext authenticity:

```javascript
const key = await generateAesKey();
const fixedIv = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]); // Static IV!
const msg1 = await crypto.subtle.encrypt({ name: "AES-GCM", iv: fixedIv }, key, new TextEncoder().encode("Transfer $10 to Alice"));
const msg2 = await crypto.subtle.encrypt({ name: "AES-GCM", iv: fixedIv }, key, new TextEncoder().encode("Transfer $1000 to Bob"));
```

*Hint*: Research Galois field multiplication in GCM authentication and keystream XOR cancellation when reusing nonces.

### Challenge 2: Timing Attack-Safe Signature Verification

The following signature verification uses standard string equality (===), making it vulnerable to **Side-Channel Timing Attacks**. Refactor it to use a constant-time verification algorithm via crypto.subtle.verify:

```typescript
// Vulnerable Signature Verification
async function verifySignatureVulnerable(secret: string, payload: string, providedHexSig: string) {
const calculatedSig = await signPayload(secret, payload);
return calculatedSig === providedHexSig; // Vulnerable to character-by-character timing leak!
}
```

*Hint*: Import the secret as an HMAC CryptoKey and call crypto.subtle.verify("HMAC", key, signatureBuffer, dataBuffer).

### Challenge 3: End-to-End Zero-Knowledge Client Encryption Engine

Build a complete **Zero-Knowledge Encryption Engine** in TypeScript:

1.  deriveKeyFromPassword(password: string, salt: Uint8Array): Uses PBKDF2 with 600,000 iterations and SHA-256 to derive an AES-256-GCM encryption key.

2.  encryptVaultItem(password: string, plainText: string):

    - Generates a fresh 16-byte random Salt and 12-byte random IV.

    - Derives key and encrypts using AES-GCM.

    - Packs Salt + IV + Ciphertext into a single URL-safe Base64 string payload.

3.  decryptVaultItem(password: string, packedPayload: string):

    - Unpacks Salt, IV, and Ciphertext from the Base64 string.

    - Derives key and decrypts back to original UTF-8 plaintext.

    - Handles tampering exceptions gracefully by throwing AuthenticationTagMismatchException.
