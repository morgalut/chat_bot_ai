from flask import Blueprint, jsonify
from ..utils.selenium_utils import get_open_source_search_history
from ..utils.database_utils import initialize_database
from ..utils.decorators import error_handling

search_bp = Blueprint('search', __name__)

@search_bp.route('/search_history', methods=['GET'])
@error_handling
def search_history():
    history = get_open_source_search_history()
    initialize_database(history)
    return jsonify(history)
