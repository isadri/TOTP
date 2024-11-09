import calendar
from datetime import datetime
from math import floor
import time
from hotp import HOTP


class TOTP:
    """
    An implementation of the Time-based One-Time Password (TOTP) algorithm.
    """

    def __init__(self) -> None:
        self.time_steps: int = 30

    def generate(self, key: bytes) -> int:
        """
        Generate a TOTP value.
        """
        nbr = floor(calendar.timegm(datetime.now().utctimetuple()) / self.time_steps)
        return HOTP.generate(key, nbr)
