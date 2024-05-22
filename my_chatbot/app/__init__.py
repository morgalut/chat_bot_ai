# C:\Users\Mor\Desktop\curss2\p8\my_bot_project\my_chatbot\app\__init__.py

from flask import Flask
from app.utils.database_utils import initialize_database

def create_app():
    app = Flask(__name__)
    
    from .blueprints.search import search_bp
    from .blueprints.chat import chat_bp
    from .blueprints.visualize import visualize_bp

    app.register_blueprint(search_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(visualize_bp)

    initialize_database()  # Ensure database is initialized on app start

    return app
