import base64
import os
from typing import Optional

from fastapi import Depends, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.api_v1 import api_router_v1
from app.api.rest_util import get_failed_response
from app.config.config import settings
from app.database import get_db
from app.models import User
from app.util.util import check_token, get_auth_token


@api_router_v1.post("/reset/avatar", status_code=200)
async def reset_avatar(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db),
) -> dict:
    auth_token = get_auth_token(request.headers.get("Authorization"))

    if auth_token == "":
        get_failed_response("An error occurred", response)

    user_avatar: Optional[User] = await check_token(db, auth_token)
    if not user_avatar:
        get_failed_response("An error occurred", response)

    user_avatar.set_default_avatar(True)
    db.add(user_avatar)
    await db.commit()

    file_folder = settings.UPLOAD_FOLDER
    file_name = user_avatar.avatar_filename_default()
    file_path = os.path.join(file_folder, "%s.png" % file_name)

    if not os.path.isfile(file_path):
        return get_failed_response("An error occurred", response)
    else:
        with open(file_path, "rb") as fd:
            image_as_base64 = base64.encodebytes(fd.read()).decode()

        return {"result": True, "message": image_as_base64}
