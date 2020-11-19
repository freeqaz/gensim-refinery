from pynamodb.exceptions import DoesNotExist

from shared_files.models import UserModel, TagModel

def main(block_input, backpack):
   username = block_input["queryStringParameters"].get("username")
   if username is None:
      return "username has not been provided"

   try:
      user = UserModel.get(username)
   except DoesNotExist:
      return "user does not exist"

   tags = []
   for tag_name in user.tag_names:
      queried_tags = TagModel.query(tag_name)
      if queried_tags is None:
         return "no results"

      tags.extend([t.__dict__ for t in queried_tags])
       
   return tags
