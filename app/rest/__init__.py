from flask import Blueprint

app_api = Blueprint("api", __name__)

from app.rest import map_rest, test
from app.rest.v1_0 import (
    email,
    get_avatar,
    get_hexagon,
    get_tile_info,
    get_user,
    login,
    message,
    refresh,
    register,
    settings,
    social,
    tile_change,
    token_login,
)
