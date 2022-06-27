from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    # 임시방편 self.csrf_impl.generate_csrf_token(self) 관련 에러
    app.config["SECRET_KEY"]="1273128736178"

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app

