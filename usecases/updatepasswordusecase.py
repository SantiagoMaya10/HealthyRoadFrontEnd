from databaseconfig.dbconfig import MySqLConnectionCreator  # Import the MySQL connection handler to interact with the database

def update_password_usecase(new_password: str, username: str):
    """
    Updates the password for a user in the database based on their username.

    This function updates the user's password by executing an SQL `UPDATE` query.
    The changes are committed to the database, and the connection is closed after 
    the operation.

    Args:
        new_password (str): The new password to be set for the user.
        username (str): The username of the user whose password is being updated.
    
    Returns:
        None
    """
    # Create MySQL connection
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor()

    # SQL query to update the user's password based on the username
    query = """UPDATE user 
               SET password = %s
               WHERE username = %s """    

    # Execute the query with the provided new password and username
    cursor.execute(query, (new_password, username))
    
    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    connector.close_db_connection(conn)
