from flask import Flask
from app.api.controllers import orders_blueprint
from app.config import load_config

def create_app():
    app = Flask(__name__)
    app.config.from_object(load_config())

    # registrar rotas
    app.register_blueprint(orders_blueprint, url_prefix="/orders")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
