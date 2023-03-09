from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from datetime import timedelta
from main import bcrypt
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix="/auth")


@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="Email already registered")
    user = User()
    user.name = user_fields["name"]
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    user.admin = False
    db.session.add(user)
    db.session.commit()
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    return jsonify({"user":user.email, "token": access_token })


@auth.route("/login", methods=["POST"])
def auth_login():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(email=user_fields["email"]).first()
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and password")
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    return jsonify({"user":user.email, "token": access_token })