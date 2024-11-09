from math import floor
import time
from hotp import HOTP


class TOTP:
    """
    An implementation of the Time-based One-Time Password (TOTP) algorithm.
    """

    TIME_STEP = 30
    initial_time = time.time()

    @classmethod
    def generate(cls, key: bytes) -> int:
        """
        Generate a TOTP value.
        """
        nbr_time_steps = floor((time.time() - cls.initial_time) / cls.TIME_STEP)
        return HOTP.generate(key, str(nbr_time_steps).encode())
