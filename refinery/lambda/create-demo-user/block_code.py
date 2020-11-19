import uuid

from shared_files.models import UserModel

def main(block_input, backpack):
    user = UserModel(username="demo", user_id=str(uuid.uuid4()), tag_names=[])
    user.save()
    return "Created user!"
