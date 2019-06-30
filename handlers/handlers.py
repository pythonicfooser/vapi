from aiohttp.web import Response 
from json import dumps

async def hello(request):
    return Response(text='Hi foo') 

async def post_messages(request):
    print(await request.json())
    # db = await request.app['db']
    request.app['db']['main'].insert_one({'x': 3})
    return Response(body=dumps({"hi": "ho"}), content_type="application/json")

