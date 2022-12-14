import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_email(value):
    email_reg = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    regex = re.compile(email_reg)

    if not regex.match(value):
        return "false_email"

def validate_password(password):
    if len(password) <= 10 and len(password)>=6:
        return "true_pw"

def validate_phone(value):
    phone_reg= r"^\+?1?\d{8,15}$"
    regex = re.compile(phone_reg)

    if not regex.match(value):
        return "false_phone"