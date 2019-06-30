user_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "username": {
            "type": "string"
        },
        "dni": {
            "type": "string"
        }
    },
    "required": ["name", "username", "dni"]
}

query_schema = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string"
        }
    },
    "required": ["username"]
}

increase_amount_schema = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string"
        },
        "amount": {
            "type": "number"
        }
    },
    "required": ["username", "amount"]
}

transfer_amount_schema = {
    "type": "object",
    "properties": {
        "from_username": {
            "type": "string"
        },
        "to_username": {
            "type": "string"
        },
        "amount": {
            "type": "number"
        }
    },
    "required": ["from_username", "to_username", "amount"]
}
