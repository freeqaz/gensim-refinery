import os

from shared_files.models import UserModel, TagModel

def main(block_input, backpack):
    """
    You can run this block manually to create the "User" table in the
    NoSQL database, once you've done that the rest of the endpoints will
    work to insert, remove, and update the table data.
    """
    print( "Creating table..." )
    
    response = UserModel.create_table(
        # Wait until the table is created before continuing
        wait=True,
        # Number of read compacity units for the table
        read_capacity_units=1,
        # Number of write compacity units for the table
        write_capacity_units=1
    )

    response = TagModel.create_table(
        # Wait until the table is created before continuing
        wait=True,
        # Number of read compacity units for the table
        read_capacity_units=1,
        # Number of write compacity units for the table
        write_capacity_units=1
    )

    return True