def reverse_string(s: str) -> str:
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]