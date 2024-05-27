from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models.users import UserModel

from db import db
from schemas.user_contact import UserSchema


blp = Blueprint("Users", __name__, description="Operations on Users")


@blp.route("/adduser")
class AddUsers(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Store already exists")
        except SQLAlchemyError:
            abort(500, message="Error Occured while creating User!")
        return user


@blp.route("/getusers")
class GetUsers(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()
