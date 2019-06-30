from aiohttp import web
from handlers import * 

def set_routes(app):
    app.add_routes([
        web.get('/', hello),
        web.post('/post_messages', post_messages),
        web.post('/add_user', set_user),
        web.post('/get_user_balance', get_user_balance),
        web.post('/increase_user_balance', increase_user_balance),
        web.post('/transfer', transfer)
    ])
    
