import hashlib
from utils import xor


class HMAC:
    """
    An implementation of the Keyed-Hash Message Authentication Code (HMAC).
    """

    @classmethod
    def convert(cls, ipad: bytes, key: bytes) -> bytes:
        """
        perform XOR between each character of ipad and key.
        
        This method assumes that ipad and key have the same length.
        """
        result = b''
        for i, j in zip(ipad, key):
            result += bytes(format(ord(i), 'b') ^ format(ord(j), 'b'))
        return result

    @classmethod
    def hmac(cls, key: str, message: str) -> bytes:
        """

        """
        ipad = ''.join([chr(0x36) for _ in range(64)]).decode()
        opad = ''.join([chr(0x5c) for _ in range(64)]).decode()

        ikey_pad = HMAC.convert(ipad, key)
        okey_pad = HMAC.convert(opad, key)

        return hashlib.sha1(okey_pad + hashlib.sha1(ikey_pad + message))
