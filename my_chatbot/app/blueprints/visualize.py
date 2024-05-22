from flask import Blueprint, jsonify
from ..utils.visualization_utils import plot_data
from ..utils.decorators import error_handling

visualize_bp = Blueprint('visualize', __name__)

@visualize_bp.route('/plot', methods=['POST'])
@error_handling
def plot():
    # Example data for plotting
    data = [1, 2, 3, 4, 5]
    plot_data(data, title='Sample Plot', xlabel='Index', ylabel='Value')
    return jsonify({'status': 'Plot created'})
