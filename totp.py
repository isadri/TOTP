import calendar
from datetime import datetime
from hotp import HOTP
import time


class TOTP:
    """
    An implementation of the Time-based One-Time Password (TOTP) algorithm.
    """

    def __init__(self) -> None:
        self.time_steps: int = 30

    def generate(self, key: str) -> str:
        """
        Generate a TOTP value.
        """
        nbr = int(time.mktime(datetime.now().timetuple()) / self.time_steps)
        return HOTP.generate(key, nbr)
