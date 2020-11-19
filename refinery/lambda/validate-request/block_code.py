from jsonschema import validate, ValidationError

tag_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "comment": {"type": "string"}
    }
}

request_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "tags": {
            "type": "array",
            "items": tag_schema
        },
    },
}

def main(block_input, backpack):
    request_data = block_input['json']

    # raises exception if not valid
    try:
        validate(request_data, schema=request_schema)
    except ValidationError as e:
        raise e

    # save the username for later in the workflow
    backpack["username"] = request_data["username"]

    # process each of the tags
    return request_data["tags"]

