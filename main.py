from aiohttp.web import Application, run_app 
from utils import set_routes 
import asyncio
import motor.motor_asyncio


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
    return client 

async def init_app():
    app = Application()
    set_routes(app)
    mongo_client = await init_db()
    app['db'] = mongo_client['main_db'] 
    return app

if __name__ == "__main__":
    app = init_app()
    run_app(app) 
