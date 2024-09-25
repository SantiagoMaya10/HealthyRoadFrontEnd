# Class to retrieve db connections
from databaseconfig.dbconfig import MySqLConnectionCreator
# fasthtml elements
from fasthtml.common import  Div, Head, Html,Body


def save_user_info(name: str, lastname: str, email: str, username:str, password:str, privacy_policy: bool):
    """saves user info to database when signing up.
    It is saved to user table.

    Args:
        name (str): user first name
        lastname (str): user last name
        email (str): user email
        username (str): username, must be unique
        password (str): password chosen by user
        privacy_policy (bool): accepte privacy policy

    Returns:
        Div : returns a div with succesfull message
    """
    config_class = MySqLConnectionCreator()

    conn = config_class.db_conn

    cursor = conn.cursor()
    insert_query = """
        INSERT INTO user (name, lastname, email, username, password, accepted_privacy_policy)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (name, lastname, email, username, password, privacy_policy))
    conn.commit() # Commit the transaction
    print(f"User {username} inserted successfully.")

    config_class.close_db_connection(conn)

    # Respond with a success message
    message = Div(
        f"User {username} successfully registered! Redirecting to sign-in...",
        cls="message"
    )
    
    return Html(
        Head(),
        Body(
            message
        )
    )

