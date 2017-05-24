import uuid


def create_code(number=200):
    result = []
    while True is True:
        code = str(uuid.uuid1()).replace('-', '')
        if code not in result:
            result.append(code)
        if len(result) == number:
            break
    return result


# test
print(create_code())
