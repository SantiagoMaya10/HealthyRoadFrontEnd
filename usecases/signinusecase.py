from databaseconfig.dbconfig import MySqLConnectionCreator  # Import the MySQL connection handler
from mysql.connector import Error  # Import error handling for MySQL operations
from fastapi.responses import RedirectResponse  # Import FastAPI's RedirectResponse to handle redirects
from views.signinview import build_sign_in_page  # Import the sign-in page view builder
from fasthtml.common import Div  # Import Div to build HTML content with FastHTML


def sign_in_user(username: str, password: str):
    """
    Handles the user sign-in process. Verifies user credentials and sets 
    a session cookie if the credentials are correct. If the user is 
    authenticated, the function redirects to the homepage. If authentication 
    fails, it returns the sign-in page with an error message.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        RedirectResponse: A response that redirects the user to the homepage if successful.
        Otherwise, returns the sign-in page with an error message.
    """
    # Verify the user credentials
    user = _verify_user_exists(username, password)

    if user:
        # Set a session cookie with the username (or user ID)
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="session_user", value=username, httponly=True)

        # Redirect to home page if successful
        return response
    else:
        # Invalid credentials, display an error message
        return build_sign_in_page(Div(("Invalid username or password! Please try again."), cls="message"))


def _verify_user_exists(username: str, password: str):
    """
    Checks whether a user exists in the database with the provided username and password.

    Args:
        username (str): The username to be verified.
        password (str): The password to be verified.

    Returns:
        tuple or None: The user data if the user is found, otherwise None.
    """
    # Create MySQL connection
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor()

    try:
        # SQL query to check for a user with the provided username and password
        query = """
                SELECT * FROM user WHERE username = %s AND password = %s
            """
        cursor.execute(query, (username, password))
        # Fetch one result (the user)
        user = cursor.fetchone()
        return user  # Return user data if found, otherwise None

    except Error as e:
        # Print error if there's an issue querying the database
        print(f"Error fetching user: {e}")
        return None

    finally:
        # Close the database connection in all cases
        connector.close_db_connection(conn)
