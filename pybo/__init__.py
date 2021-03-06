from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flaskext.markdown import Markdown

# import config

naming_convention = {
    "ix":"ix_%(column_0_label)s",
    "uq":"uq_%(table_name)s_%(column_0_name)s",
    "ck":"ck_%(table_name)s_%(column_0_name)s",
    "fk":"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk":"pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def page_not_found(e):
    return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    #app.config.from_object(config)
    app.config.from_envvar('APP_CONFIG_FILE')

    # 임시방편 self.csrf_impl.generate_csrf_token(self) 관련 에러
    app.config["SECRET_KEY"]="1273128736178"

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)


    from . import models

    from .views import main_views, question_views, answer_views, auth_views, comment_views, vote_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)

    # 오류 페이지
    app.register_error_handler(404, page_not_found)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br','fenced_code'])
    return app

