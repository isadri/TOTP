from hashlib import sha1
import hmac


class HOTP:
    """
    An implementation of the HMAC-Based One-Time Password (HOTP) algorithm.
    """

    counter = 0

    @classmethod
    def generate(cls, key: bytes) -> int:
        """
        Return the number whose binary representation is s.
        """
        hmac_result = hmac.new(key, bytes(HOTP.counter), digestmod=sha1).digest()
        offset = hmac_result[-1] & 0xf
        bin_code = ((hmac_result[offset] & 0x7f) << 24
                    | (hmac_result[offset + 1] & 0xff) << 16
                    | (hmac_result[offset + 2] & 0xff) << 8
                    | (hmac_result[offset + 3]))
        return bin_code % (10 ** 6)
