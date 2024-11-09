from math import floor
import time
from hotp import HOTP


class TOTP:
    """
    An implementation of the Time-based One-Time Password (TOTP) algorithm.
    """

    def __init__(self) -> None:
        self.time_steps: int = 30
        self.initial_time: float = 0.0

    def generate(self, key: bytes) -> int:
        """
        Generate a TOTP value.
        """
        nbr_time_steps = floor((time.time() - self.initial_time) / self.time_steps)
        return HOTP.generate(key, nbr_time_steps)
