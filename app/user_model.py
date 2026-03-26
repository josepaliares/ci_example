from dataclasses import dataclass, field
from datetime import datetime
import re


EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PASSWORD_POLICY = {
    "min_length": 8,
    "upper": r"[A-Z]",
    "lower": r"[a-z]",
    "digit": r"\d",
    "special": r"[^A-Za-z0-9]",
}


@dataclass
class User:
    name: str
    email: str
    password: str
    date_of_birth: str = field(repr=False)

    def __post_init__(self):
        self.name = self.name.strip()
        self.email = self.email.strip()
        self.date_of_birth = self.date_of_birth.strip()

        if len(self.name) < 6:
            raise ValueError("name must be at least 6 characters")

        if not EMAIL_REGEX.fullmatch(self.email):
            raise ValueError("invalid email format")

        try:
            datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        except ValueError:
            raise ValueError("date_of_birth must be YYYY-MM-DD")

        self._validate_password(self.password)

    @staticmethod
    def _validate_password(password: str):
        if len(password) < PASSWORD_POLICY["min_length"]:
            raise ValueError("password must be at least " +
                             f"{PASSWORD_POLICY['min_length']} chars")
        if not re.search(PASSWORD_POLICY["upper"], password):
            raise ValueError("password must contain at least "
                             "one uppercase letter")
        if not re.search(PASSWORD_POLICY["lower"], password):
            raise ValueError("password must contain at least "
                             "one lowercase letter")
        if not re.search(PASSWORD_POLICY["digit"], password):
            raise ValueError("password must contain at least "
                             "one digit")
        if not re.search(PASSWORD_POLICY["special"], password):
            raise ValueError("password must contain at least "
                             "one special character")

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "date_of_birth": self.date_of_birth,
        }
