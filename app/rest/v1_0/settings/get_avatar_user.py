from flask import request, make_response
from flask_restful import Api
from flask_restful import Resource
from sqlalchemy import func
import os

from app.config import Config
from app.models.user import User
from app.rest.rest_util import get_failed_response
from app.rest import app_api
import base64

from app.util.util import get_auth_token, check_token


class GetAvatarUser(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    # noinspection PyMethodMayBeStatic
    def post(self):
        auth_token = get_auth_token(request.headers.get("Authorization"))
        if auth_token == "":
            return get_failed_response("Something went wrong")

        user_avatar = check_token(auth_token)
        if not user_avatar:
            return get_failed_response("Something went wrong")

        file_folder = Config.UPLOAD_FOLDER
        if user_avatar.is_default():
            file_name = user_avatar.avatar_filename_default()
        else:
            file_name = user_avatar.avatar_filename()

        file_path = os.path.join(file_folder, "%s.png" % file_name)

        if not os.path.isfile(file_path):
            return get_failed_response("An error occurred")
        else:
            with open(file_path, "rb") as fd:
                image_as_base64 = base64.encodebytes(fd.read()).decode()

            avatar_response = make_response(
                {"result": True, "avatar": image_as_base64}, 200
            )

            return avatar_response


api = Api(app_api)
api.add_resource(GetAvatarUser, "/api/v1.0/get/avatar/user", endpoint="get_avatar_user")
