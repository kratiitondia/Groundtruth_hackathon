import re

PHONE_RE = re.compile(r"(\+?\d[\d \-]{7,}\d)")
ORDER_RE = re.compile(r"(order\s*#?\s*\w+)", re.IGNORECASE)
CARD_RE = re.compile(r"(\b(?:\d[ -]*?){13,19}\b)")

class PIIMasker:
    @staticmethod
    def mask(text: str) -> str:
        t = PHONE_RE.sub("[REDACTED_PHONE]", text)
        t = ORDER_RE.sub("[REDACTED_ORDER]", t)
        t = CARD_RE.sub("[REDACTED_CARD]", t)
        return t
