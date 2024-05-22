import json
import traceback
from flask import jsonify

def log_error(exception, func_name):
    error_log = {
        'error': str(exception),
        'function': func_name,
        'traceback': traceback.format_exc()
    }
    with open('error_log.json', 'a') as f:
        json.dump(error_log, f)
        f.write('\n')

def create_error_response(exception, func_name):
    log_error(exception, func_name)
    response = {
        'error': str(exception),
        'message': 'An unexpected error occurred. Please try again later.'
    }
    return jsonify(response), 500
