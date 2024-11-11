from datetime import datetime
from hotp import HOTP
import time
from typing import Optional


class TOTP:
    """
    An implementation of the Time-based One-Time Password (TOTP) algorithm.
    """

    def __init__(self, time_steps: Optional[int] = 30) -> None:
        self.time_steps: int = time_steps

    def generate(self, key: str) -> str:
        """
        Generate a TOTP value.
        """
        nbr = int(time.mktime(datetime.now().timetuple()) / self.time_steps)
        return HOTP.generate(key, nbr)
