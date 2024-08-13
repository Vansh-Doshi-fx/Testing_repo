import re

def is_valid_phone_number(phone_number):
    pattern = re.compile(r'^\+?1?\d{10}$')
    return bool(pattern.match(phone_number))