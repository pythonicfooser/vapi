from aiohttp.web import Application, run_app
from utils import set_routes
import motor.motor_asyncio
import logging


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://mongodb:27017')
    return client


async def init_app():
    app = Application()
    set_routes(app)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    app['logger'] = logging
    mongo_client = await init_db()
    app['db'] = mongo_client['main_db']
    return app


if __name__ == "__main__":
    app = init_app()
    run_app(app)
