def _is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False