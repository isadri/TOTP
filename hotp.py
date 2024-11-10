from hashlib import sha1
import hmac
import base64


class HOTP:
    """
    An implementation of the HMAC-Based One-Time Password (HOTP) algorithm.
    """

    @classmethod
    def generate(cls, secret: bytes, counter: int) -> int:
        """
        Return the number whose binary representation is s.
        """
        hasher = hmac.new(secret, cls.int_to_bytes(counter),
                            digestmod=sha1).digest()
        offset = hasher[-1] & 0xf
        binary = ((hasher[offset] & 0x7f) << 24
                    | (hasher[offset + 1] & 0xff) << 16
                    | (hasher[offset + 2] & 0xff) << 8
                    | (hasher[offset + 3]))
        return binary % (10 ** 6)

    @staticmethod
    def int_to_bytes(value: int) -> bytes:
        """
        convert value of type int to a value of type bytes.
        """
        text = bytearray()
        while value:
            text.append(value & 0xff)
            value >>= 8
        return bytes(reversed(text))
