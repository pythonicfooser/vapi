from aiohttp import web
from handlers import set_user, get_user_balance,\
                     increase_user_balance, transfer


def set_routes(app):
    app.add_routes([
        web.post('/add_user', set_user),
        web.post('/get_user_balance', get_user_balance),
        web.post('/increase_user_balance', increase_user_balance),
        web.post('/transfer', transfer)
    ])
