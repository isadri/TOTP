# totp

## HMAC Introduction

Providing a way to check the integrity of information transmitted over or stored in an unreliable medium is a prime necessity in the world of open computing and communications. Mechanisms that provide such integrity check based on a secret key are usually called __message authentication codes (MAC)__. Typically, message authentication codes are used between two parites that share a secret key in order to validate information transmitted between these parties. HMAC can be used in combination with any iterated cryptographic hash function. HMAC also uses a secret key for calculation and verification of the message authentication values, SHA-1 is the most widely used cryptographic hash function and it is the one that is used in our implementation.

HMAC uses two passes of hash computation. Before either pass, the secret key is used to derive two keys (inner and outer). Next, the first pass of the hash algorithm produces an internal hash derived from the message and the inner key. The second pass produces the final HMAC code derived from the inner hash result and the outer key.

SHA-1 hash function is a cryptographic hash function where data is hashed by iterating a basic compression function on blocks of 64 bytes of size. The size of the output of HMAC is the same as that of the underlying hash function (i.e., 20 bytes in the case of SHA-1).

The implementation defines the inner key and the outer key, [RFC 2102](https://datatracker.ietf.org/doc/html/rfc2104), as follows:

```text
ipad = the byte 0x36 repeated 64 times.
opad = the byte 0x5c repeated 64 times.
```

If the key is smaller than 64 bytes then we append zeros to the right of the key, if the key is longer than 64 bytes then the key is hashed using SHA-1.



## TOTP Introduction

TOTP is the time-based variant of the HOTP algorithm. The HOTP algorithm uses a counter as the moving factor in the computation, the TOTP algorithm replaces that counter with a value derived from a time refrence and a time step.
