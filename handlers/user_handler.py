from aiohttp.web import Response
from jsonschema import validate
from models import user_schema, query_schema, increase_amount_schema
from jsonschema.exceptions import ValidationError
from json import dumps
from json.decoder import JSONDecodeError


async def set_user(request):
    """ Method for adding a user.
        MUST receive, via JSON:
          - username
          - name
          - dni
    """
    try:
        input_data = await request.json()
        validate(input_data, user_schema)
        exist_user = await request.app['db']['users'].find_one(
            {"username": input_data['username']})
        if exist_user:
            return Response(body=dumps({"status": "User already exists"}),
                            content_type="application/json")

        input_data['amount'] = 0
        request.app['db']['users'].insert_one(input_data)
        return Response(body=dumps({"status": "User added"}),
                        content_type="application/json")
    except ValidationError:
        return Response(body=dumps({"status": "Error in sent fields"}),
                        content_type="application/json")
    except JSONDecodeError:
        return Response(body=dumps({"status": "Format error"}),
                        content_type="application/json")
    except Exception:
        return Response(body=dumps(
            {"Error": "Uh oh... Something went wrong! We are working on it!"}),
                        content_type="application/json")


async def get_user_balance(request):
    """ Method for obtain user balance.
        Must receive, via JSON:
        - username
    """

    try:
        input_data = await request.json()
        validate(input_data, query_schema)
        exist_user = await request.app['db']['users'].find_one(
            {"username": input_data['username']})
        if not exist_user:
            return Response(body=dumps({"status": "User not exists"}),
                            content_type="application/json")

        return Response(body=dumps({"amount": exist_user['amount']}),
                        content_type="application/json")
    except ValidationError:
        return Response(body=dumps({"status": "Error in sent fields"}),
                        content_type="application/json")

    except JSONDecodeError:
        return Response(body=dumps({"status": "Format error"}),
                        content_type="application/json")
    except Exception:
        return Response(body=dumps(
            {"Error": "Uh oh... Something went wrong! We are working on it!"}),
                        content_type="application/json")


async def increase_user_balance(request):
    """ Method for increasing user balance.
         Must receive, via JSON:
         - username
         - amount
    """
    try:
        input_data = await request.json()
        validate(input_data, increase_amount_schema)
        if input_data['amount'] <= 0:
            return Response(body=dumps({"status": "Invalid amount"}),
                            content_type="application/json")

        exist_user = await request.app['db']['users'].find_one(
            {"username": input_data['username']})
        if not exist_user:
            return Response(body=dumps({"status": "User not exists"}),
                            content_type="application/json")

        new_amount = exist_user['amount'] + input_data['amount']
        await request.app['db']['users'].update_one(
            {"username": input_data['username']},
            {'$set': {
                "amount": new_amount
            }})
        return Response(body=dumps({"message": 'amount updated'}),
                        content_type="application/json")
    except ValidationError:
        return Response(body=dumps({"status": "Error in sent fields"}),
                        content_type="application/json")

    except JSONDecodeError:
        return Response(body=dumps({"status": "Format error"}),
                        content_type="application/json")
    except Exception:
        return Response(body=dumps(
            {"Error": "Uh oh... Something went wrong! We are working on it!"}),
                        content_type="application/json")
