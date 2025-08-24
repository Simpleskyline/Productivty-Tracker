from flask import Flask, render_template
from flask_cors import CORS
from .database import init_db
from .routes.activities import activities_bp
from .routes.goals import goals_bp
from .routes.reminders import reminders_bp
from .routes.reports import reports_bp
from .routes.sessions import sessions_bp

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    CORS(app)

    # init DB
    init_db(app)

    # register blueprints
    app.register_blueprint(activities_bp)
    app.register_blueprint(goals_bp)
    app.register_blueprint(reminders_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(sessions_bp)

    # serve homepage
    @app.route("/")
    def index():
        return render_template("main.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
