from shared_files.models import UserModel, TagModel

def main(block_input, backpack):

    if UserModel.exists():
        UserModel.delete_table()
    
    if TagModel.exists():
        TagModel.delete_table()

    return "Deleted tables"