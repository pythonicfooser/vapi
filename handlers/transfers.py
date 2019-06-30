from aiohttp.web import Response
from jsonschema import validate
from models import transfer_amount_schema
from jsonschema.exceptions import ValidationError
from json import dumps
from json.decoder import JSONDecodeError


async def transfer(request):
    """ Function for increasing user balance.
         Must receive, via JSON:
         - from_username
         - to_username
         - amount
    """
    try:
        input_data = await request.json()
        validate(input_data, transfer_amount_schema)
        if input_data['amount'] <= 0:
            return Response(body=dumps({"status": "Invalid amount"}),
                            content_type="application/json")

        exist_from_user = await request.app['db']['users'].find_one(
            {"username": input_data['from_username']})
        exist_to_user = await request.app['db']['users'].find_one(
            {"username": input_data['to_username']})

        if not exist_from_user:
            return Response(body=dumps(
                {"status": f"User {input_data['from_username']} not exists"}),
                            content_type="application/json")

        if not exist_to_user:
            return Response(body=dumps(
                {"status": f"User {input_data['to_username']} not exists"}),
                            content_type="application/json")

        if input_data['amount'] > exist_from_user['amount']:
            return Response(body=dumps(
                {"status": "Amount to transfer bigger than available"}),
                            content_type="application/json")

        new_from_user_amount = exist_from_user['amount'] - input_data['amount']
        await request.app['db']['users'].update_one(
            {"username": input_data['from_username']},
            {'$set': {
                "amount": new_from_user_amount
            }})

        new_to_user_amount = exist_to_user['amount'] + input_data['amount']
        await request.app['db']['users'].update_one(
            {"username": input_data['to_username']},
            {'$set': {
                "amount": new_to_user_amount
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
