from aiohttp import web
from handlers import set_user, get_user_balance,\
                     increase_user_balance, transfer


def set_routes(app):
    api = "v1"
    prefix = "api"

    app.add_routes([
        web.post('/{api}/{prefix}/users/add', set_user),
        web.post('/{api}/{prefix}/users/balance', get_user_balance),
        web.post('/{api}/{prefix}/users/increase', increase_user_balance),
        web.post('/{api}/{prefix}/accounts/transfer', transfer)
    ])
