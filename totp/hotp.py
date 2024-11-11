from hashlib import sha1
import hmac
import base64


class HOTP:
    """
    An implementation of the HMAC-Based One-Time Password (HOTP) algorithm.
    """

    @classmethod
    def generate(cls, secret: str, counter: int) -> str:
        """
        Return the number whose binary representation is s.
        """
        msg = cls.int_to_bytes(counter)
        key = cls.byte_secret(secret)
        hasher = hmac.digest(key, msg, sha1)
        offset = hasher[-1] & 0xf
        binary = ((hasher[offset] & 0x7f) << 24 |
                (hasher[offset + 1] & 0xff) << 16 |
                (hasher[offset + 2] & 0xff) << 8 |
                (hasher[offset + 3]) & 0xff)

        result = str(binary % (10 ** 6))
        result = result.rjust(6, '0')
        return result

    @staticmethod
    def byte_secret(secret: str) -> bytes:
        """
        convert secret to bytes, padding with = if necessary and decode
        the result.
        """
        missing_padding = len(secret) % 8
        if missing_padding:
            secret += '=' * (8 - missing_padding)
        return base64.b32decode(secret, casefold=True)

    @staticmethod
    def int_to_bytes(value: int) -> bytes:
        """
        convert the int value to bytes value.
        """
        text = bytearray()
        while value:
            text.append(value & 0xff)
            value >>= 8
        return bytes(bytearray(reversed(text)).rjust(8, b'\0'))
