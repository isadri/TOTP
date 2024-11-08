class HOTP:
    """
    An implementation of the HMAC-Based One-Time Password (HOTP) algorithm.
    """

    @classmethod
    def str_to_num(cls, s: str) -> int:
        """
        Return the number whose binary representation is s.
        """
