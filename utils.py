from datetime import datetime


def greet(name):
    return f"Hello {name}"


def current_year():
    return datetime.now().year
