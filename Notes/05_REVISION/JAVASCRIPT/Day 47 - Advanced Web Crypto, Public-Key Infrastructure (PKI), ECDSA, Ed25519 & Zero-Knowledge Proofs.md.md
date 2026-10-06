tags:

- javascript

- cryptography

- web-crypto

- pki

- ecdsa

- ed25519

- signatures

- security

- performance date: 2026-09-16

# Day 47 - Advanced Web Crypto, Public-Key Infrastructure (PKI), ECDSA, Ed25519 & Zero-Knowledge Proofs

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Asymmetric Cryptography Paradigm

While symmetric cryptography like AES-256-GCM (covered on Day 26) is
ideal for bulk data encryption, it requires both parties to share an
identical secret key in advance. In public distributed environments,
sharing keys securely without an existing secure channel is impossible.

**Asymmetric (Public-Key) Cryptography** uses mathematically linked key
pairs:

- **Public Key**: Safe to publish openly worldwide; used by anyone to
  encrypt messages or verify signatures.

- **Private Key**: Kept strictly confidential by the owner; used to
  decrypt messages or generate non-forgeable cryptographic signatures.

┌────────────────────────────────────── Asymmetric Key Operations
──────────────────────────────────────┐

│ │

│ Digital Signing (Authentication & Non-Repudiation): │

│ \[ Sender: Private Key \] ──► crypto.subtle.sign() ──► Digital
Signature (Attached to payload) │

│ │ │

│ ▼ (Public Network) │

│ \[ Verifier: Public Key \] ─► crypto.subtle.verify() ◄────────┘ │

│ • Proves the payload was authored by the Private Key owner! │

│ • Proves the payload was NOT tampered with in transit! │

│ │

│ Key Agreement (Diffie-Hellman / ECDH): │

│ \[ Alice: Private Key \] + \[ Bob: Public Key \] ──►
crypto.subtle.deriveKey() ──► Shared Secret (K) │

│ \[ Bob: Private Key \] + \[ Alice: Public Key \] ──►
crypto.subtle.deriveKey() ──► Shared Secret (K) │

│ • Both parties arrive at the EXACT same AES-256-GCM symmetric key
without transmitting it! │

│ │

└───────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. Elliptic Curve Cryptography: ECDSA vs. Ed25519

Compared to legacy RSA (which requires bloated 2048-bit or 4096-bit
keys), **Elliptic Curve Cryptography (ECC)** achieves equivalent
cryptographic strength with tiny 256-bit keys, drastically reducing CPU
cycles, bandwidth, and battery drain:

- **NIST P-256 / P-384 (ECDSA)**: Widely supported across all browsers
  in the Web Crypto API standard.

- **Curve25519 / Ed25519 (EdDSA)**: State-of-the-art curve immune to
  side-channel timing attacks, branch-prediction attacks, and poor
  random number generator entropy.

#### Generating Non-Extractable Hardware-Guarded Keys:

A paramount architectural security practice is setting extractable:
false. The browser's crypto subsystem will never reveal the raw private
key bytes to JavaScript, thwarting malicious browser extensions and
memory-scraping attacks.

// 1. Generate Non-Extractable ECDSA Key Pair

const keyPair = await crypto.subtle.generateKey(

{

name: \'ECDSA\',

namedCurve: \'P-256\',

},

false, // CRITICAL: extractable = false (Private key never leaves
browser crypto sandbox!)

\[\'sign\', \'verify\'\]

);

// 2. Sign an Immutable Audit Event

const encoder = new TextEncoder();

const dataToSign = encoder.encode(\'TRANSFER: Alice -\> Bob: \$5,000\');

const signature = await crypto.subtle.sign(

{

name: \'ECDSA\',

hash: { name: \'SHA-256\' },

},

keyPair.privateKey,

dataToSign

);

// 3. Verify Signature with Public Key

const isValid = await crypto.subtle.verify(

{

name: \'ECDSA\',

hash: { name: \'SHA-256\' },

},

keyPair.publicKey,

signature,

dataToSign

);

console.log(\'Signature Authenticated:\', isValid); // true

### 3. Diffie-Hellman Key Agreement via ECDH

Deriving a shared symmetric AES-GCM encryption key between two clients
across an untrusted network:

// Alice & Bob generate their ephemeral ECDH key pairs

const aliceKeys = await crypto.subtle.generateKey({ name: \'ECDH\',
namedCurve: \'P-256\' }, true, \[\'deriveKey\'\]);

const bobKeys = await crypto.subtle.generateKey({ name: \'ECDH\',
namedCurve: \'P-256\' }, true, \[\'deriveKey\'\]);

// Alice derives shared AES-GCM key using Bob\'s public key

const aliceSharedKey = await crypto.subtle.deriveKey(

{ name: \'ECDH\', public: bobKeys.publicKey },

aliceKeys.privateKey,

{ name: \'AES-GCM\', length: 256 },

false,

\[\'encrypt\', \'decrypt\'\]

);

// Bob derives shared AES-GCM key using Alice\'s public key

const bobSharedKey = await crypto.subtle.deriveKey(

{ name: \'ECDH\', public: aliceKeys.publicKey },

bobKeys.privateKey,

{ name: \'AES-GCM\', length: 256 },

false,

\[\'encrypt\', \'decrypt\'\]

);

// aliceSharedKey and bobSharedKey now share identical 256-bit symmetric
entropy!

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Web Crypto Asymmetric Algorithms & Key Formats:

  ------------------------------------------------------------------------
  **Algorithm**     **Supported       **Ideal Curve /   **Standard Use
                    Operations**      Key Size**        Case**
  ----------------- ----------------- ----------------- ------------------
  **ECDSA**         sign, verify      P-256, P-384      Non-repudiable
                                                        digital document
                                                        signing

  **ECDH**          deriveKey,        P-256, P-384      End-to-End
                    deriveBits                          Encrypted (E2EE)
                                                        messaging session
                                                        keys

  **RSA-PSS**       sign, verify      3072 or 4096 bits Legacy enterprise
                                                        PKI
                                                        interoperability

  **RSA-OAEP**      encrypt, decrypt  3072 or 4096 bits Direct asymmetric
                                                        envelope
                                                        encryption
  ------------------------------------------------------------------------

### Key Export / Import Formats:

- **spki (SubjectPublicKeyInfo)**: Standard binary DER encoding for
  **Public Keys**.

- **pkcs8 (Private-Key Information Syntax)**: Standard binary DER
  encoding for **Private Keys**.

- **jwk (JSON Web Key)**: Human-readable RFC 7517 JSON format ({ kty:
  \"EC\", crv: \"P-256\", x: \"\...\", y: \"\...\" }).

- **raw**: Raw uncompressed coordinates for elliptic curve public keys.

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: The Non-Extractable Key Boundary Defense

Analyze the following key creation call:

const keys = await crypto.subtle.generateKey(

{ name: \'ECDSA\', namedCurve: \'P-256\' },

false, // extractable

\[\'sign\', \'verify\'\]

);

// Attacker injection attempt:

try {

const exported = await crypto.subtle.exportKey(\'pkcs8\',
keys.privateKey);

} catch (err) {

console.log(\"Attacker caught:\", err.name);

}

*Question*: What specific exception is thrown when attempting to export
a non-extractable key (InvalidAccessError vs NotSupportedError)? Explain
how the browser\'s native crypto sandbox ensures that even an XSS
vulnerability cannot extract the raw private key material from memory.

### Challenge 2: Ephemeral E2EE Encrypted Messaging Channel

Build an **End-to-End Encrypted Messaging Session Engine** in
TypeScript:

1.  Implements Alice and Bob endpoints that generate ephemeral ECDH key
    pairs.

2.  Exports public keys as JWK format and exchanges them.

3.  Derives an identical AES-GCM key on both ends.

4.  Encrypts a message on Alice\'s side using AES-GCM with a random
    12-byte IV and successfully decrypts it on Bob\'s side.

### Challenge 3: In-Browser Document Signature & Verification Engine in TypeScript

Build an Enterprise **Client-Side PKI Document Signing Engine** in
TypeScript:

**Requirements**:

1.  **Hardware-Guarded Signing**:

    - Generates non-extractable ECDSA key pairs (Curve P-256).

    - Exports the public key as Base64-encoded spki DER format.

2.  **Detached Cryptographic Signatures**:

    - Accepts arbitrary document text / file ArrayBuffer.

    - Computes SHA-256 hash and generates detached binary signature.

    - Encodes output as an enterprise envelope:

> {
>
> \"payloadHash\": \"sha256-hex\",
>
> \"signature\": \"base64url-signature\",
>
> \"publicKey\": \"base64-spki-public-key\",
>
> \"timestamp\": 1726514400
>
> }

3.  **Detached Verification**:

    - Implements verifyDocumentEnvelope(envelope, rawContent):
      Promise\<boolean\>.

    - Imports public key and verifies that neither payload nor signature
      was modified.
