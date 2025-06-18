import random
import string

def generate_unique_email_not_valid():
    """Генерация уникального email-адреса для тестирования."""
    domain = "@@@dfg"
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return random_string + domain

def generate_unique_email_valid():
    """Генерация уникального невалидного email-адреса для тестирования."""
    domain = "@gmail.com"
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return random_string + domain