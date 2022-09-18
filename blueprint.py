from flask import Blueprint

api_blueprint = Blueprint('api', __name__)
Student_id = 6


@api_blueprint.route(f"/hello-world-{Student_id}")
def home():
    return f"Hello world {Student_id}"
