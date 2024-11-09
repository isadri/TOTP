from math import floor
import time
from hotp import HOTP


class TOTP:
    """
    An implementation of the Time-based One-Time Password (TOTP) algorithm.
    """

    def __init__(self) -> None:
        self.TIME_STEP = 30
        self.initial_time = time.time()

    def generate(self, key: bytes) -> int:
        """
        Generate a TOTP value.
        """
        nbr_time_steps = floor((time.time() - self.initial_time) / self.TIME_STEP)
        return HOTP.generate(key, str(nbr_time_steps).encode())
