def clean(text: str) -> str: return " ".join(text.split())
def limit(text: str, chars: int) -> str:
    if chars<0: raise ValueError("chars must be non-negative")
    return text[:chars]
