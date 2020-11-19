import os

from pynamodb.models import Model
from pynamodb.attributes import ListAttribute, JSONAttribute, NumberAttribute, ListAttribute, UnicodeAttribute

# This example users PynamoDB, see the following link for more info:
# https://github.com/pynamodb/PynamoDB

class UserModel(Model):
    """
    The User table
    """
    class Meta:
        table_name = "users"
        region = os.environ.get( "AWS_REGION" )

    username = UnicodeAttribute(
        hash_key=True
    )

    user_id = UnicodeAttribute()

    tag_names = ListAttribute()

class TagModel(Model):
    class Meta:
        table_name = "tags"
        region = os.environ.get( "AWS_REGION" )
    
    name = UnicodeAttribute(
        hash_key=True
    )

    user_id = UnicodeAttribute(
        range_key=True
    )

    comment_sentiments = ListAttribute()
    comment_summaries = ListAttribute()