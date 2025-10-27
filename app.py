from flask import Flask, redirect, url_for
from geothermal_bp import bp as geothermal_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(geothermal_bp, url_prefix="/geothermal")

    @app.route("/")
    def home():
        # Send users to the geothermal tool by default
        return redirect(url_for("geothermal.index"))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
