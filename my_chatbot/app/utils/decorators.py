from functools import wraps
from flask import request
from .error_handler import create_error_response

def error_handling(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return create_error_response(e, f.__name__)
    return decorated_function
