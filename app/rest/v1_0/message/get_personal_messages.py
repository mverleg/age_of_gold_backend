from flask import request, make_response
from flask_restful import Api
from flask_restful import Resource
from sqlalchemy import desc, func
from app.models.message.personal_message import PersonalMessage
from app.models.user import User
from app.rest import app_api
from app.rest.rest_util import get_failed_response
from app.util.util import get_auth_token, check_token


class GetPersonalMessages(Resource):

    # noinspection PyMethodMayBeStatic
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    # noinspection PyMethodMayBeStatic
    def post(self):
        json_data = request.get_json(force=True)
        auth_token = get_auth_token(request.headers.get('Authorization'))
        if auth_token == '':
            return get_failed_response("an error occurred")

        user_from = check_token(auth_token)
        if not user_from:
            return get_failed_response("an error occurred")

        to_user = json_data["from_user"]
        user_to = User.query.filter(func.lower(User.username) == func.lower(to_user)).first()

        print("going to retrieve personal messages")
        # We only retrieve the last 60 messages because we think there is no reason to scroll further back
        personal_messages = PersonalMessage.query.filter(
            (PersonalMessage.user_id == user_from.id, PersonalMessage.receiver_id == user_to.id)
            | (PersonalMessage.user_id == user_to.id, PersonalMessage.receiver_id == user_from.id)).order_by(
            desc(PersonalMessage.timestamp)).limit(60).all()
        print("We retrieved some personal messages %s" % personal_messages)
        # messages = [m.serialize for m in personal_messages]

        get_message_response = make_response({
            'result': True,
            'messages': []
        }, 200)
        return get_message_response


api = Api(app_api)
api.add_resource(GetPersonalMessages, '/api/v1.0/get/message/personal', endpoint='get_message_personal')
