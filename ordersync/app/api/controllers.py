from flask import Blueprint

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.get("/health")
def health():
    return {"status": "ok"}
