FIRST_NAME_RULES = {
    "max_length": 255,
    "pattern": "(^[A-Za-z]{1,255}$)|(^[A-Za-z]{1,}[\s\-]{1}[A-Za-z]{1,253}$)",
    "pattern_error_message": "First Name can only contain letters, spaces, hyphens, and must start and end with a letter",
    "null": False,
    "blank": False,
}

LAST_NAME_RULES = {
    "max_length": 255,
    "pattern": "(^[A-Za-z]{1,255}$)|(^[A-Za-z]{1,}[\s\-]{1}[A-Za-z]{1,253}$)",
    "pattern_error_message": "Last Name can only contain letters, spaces, hyphens, and must start and end with a letter",
    "null": False,
    "blank": False,
}

PHONE_NUMBER_RULES = {
    "max_length": 15,
    "pattern": "^[0-9]{7,15}$",
    "pattern_error_message": "This field can only contain digits",
    "null": False,
    "blank": False,
}

STREET_ADDRESS_RULES = {
    "max_length": 255,
    "pattern": "^([A-Za-z0-9])([A-Za-z0-9\s\-\.\,']{6,253})([A-Za-z0-9])$",
    "pattern_error_message": "This field can only contain letters, spaces, hyphens, apostrophes, and periods, and must start and end with a letter or digit",
    "null": False,
    "blank": False,
}

APARTMENT_RULES = {
    "max_length": 10,
    "pattern": "^[A-Za-z0-9]([A-Za-z0-9\s\-\.]{0,6}[A-Za-z0-9])?$",
    "pattern_error_message": "This field can only contain letters, spaces, hyphens, and periods, and must start and end with a letter or digit",
    "null": False,
    "blank": False,
}

POSTAL_CODE_RULES = {
    "max_length": 15,
    "pattern": "^([A-Za-z0-9]{1,})([A-Za-z0-9\s\-\.\,]{0,12})([A-Za-z0-9]{1})$",
    "pattern_error_message": "This field can only contain letters, spaces, hyphens, commas, and periods, and must start and end with a letter or digit",
    "null": False,
    "blank": False,
}
