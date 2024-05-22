from flask import Blueprint, request, jsonify

from app.utils.decorators import error_handling
from ..utils.database_utils import log_error
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import sqlite3

chat_bp = Blueprint('chat', __name__)

def train_model():
    try:
        conn = sqlite3.connect('search_results.db')
        c = conn.cursor()
        c.execute('SELECT search_title, category FROM results')
        data = c.fetchall()
        conn.close()

        if not data:
            return None, None

        searches = [row[0] for row in data]
        categories = [row[1] for row in data]

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(searches)

        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(X, categories)  # Fit the model with search titles and their categories

        return vectorizer, model
    except Exception as e:
        log_error(e, 'train_model')
        return None, None

vectorizer, model = train_model()


@chat_bp.route('/chat', methods=['POST'])
@error_handling
def chat():
    user_input = request.json.get('message')
    if vectorizer and model:
        user_input_vectorized = vectorizer.transform([user_input])
        predicted_category = model.predict(user_input_vectorized)
        response = f"Based on your recent searches, you might be interested in: {predicted_category[0]}"
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Model not trained properly'}), 500
