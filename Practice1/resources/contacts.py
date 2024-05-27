from flask.views import MethodView
from flask_smorest import Blueprint

from schemas.user_contact import ContactSchema


blp = Blueprint("Contacts", __name__, description="Operations on Contacts")


@blp.route("/addcontact")
class AddContact(MethodView):
    @blp.arguments(ContactSchema)
    @blp.response(201, ContactSchema)
    def post(self, contact_data):
        return contact_data
