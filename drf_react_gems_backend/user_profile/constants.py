NAME_RULES = {
    "max_length": 255,
    "pattern": "(^[A-Za-z]{1,255}$)|(^[A-Za-z]{1,}[\s\-]{1}[A-Za-z]{1,253}$)",
    "pattern_error_message": "First Name can only contain letters, spaces, hyphens, and must start and end with a letter",
    "null": False,
    "blank": False,
}


