from fasthtml.common import FastHTML, serve, Form  # Import FastHTML components for building HTML elements and serving the app
from fastapi import Request, Form  # Import FastAPI's Request and Form for handling HTTP requests and form data
from fastapi.responses import HTMLResponse, RedirectResponse  # Import response types for returning HTML content and handling redirects

from views.homepageview import build_home_page  # Import function to build the home page view
from views.signupview import build_sign_up_page  # Import function to build the sign-up page view
from views.signinview import build_sign_in_page  # Import function to build the sign-in page view
from views.finddistanceview import build_find_restaurants_distance_page  # Import function to build the restaurant distance page view
from views.contactinfoview import build_about_page  # Import function to build the contact/info page view
from views.updatepasswordview import build_change_password_page  # Import function to build the change password page view
from views.scatterplotview import build_scatter_plot_page  # Import function to build the scatter plot page view

from usecases.saveuserusecase import save_user_info  # Import use case to save user information during sign-up
from usecases.privacypolicyusecase import build_privacy_policy  # Import use case to build the privacy policy page
from usecases.signinusecase import sign_in_user  # Import use case to handle user sign-in logic
from usecases.navbarusecase import build_navbar  # Import use case to build the navigation bar based on user session
from usecases.finddistanceusecase import find_distance_use_case  # Import use case to calculate distance between two restaurants
from usecases.createmapusecase import create_map  # Import use case to create an interactive map of restaurants
from usecases.updatepasswordusecase import update_password_usecase  # Import use case to handle password updates

from databaseconfig.dbconfig import MySqLConnectionCreator  # Import MySQL connection creator for database interactions

# Initialize the FastHTML application
app = FastHTML()

@app.get("/")
def home(request: Request):
    """
    Handles GET requests to the home page.

    Retrieves the session user from cookies and builds the home page with a customized navbar.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        Html: The rendered home page HTML.
    """
    session_user = request.cookies.get("session_user")  # Retrieve the session user from cookies
    return build_home_page(build_navbar(session_user))  # Build and return the home page with the navbar

@app.get("/find-distance-page")
def find_distance_page(request: Request):
    """
    Handles GET requests to the restaurant distance exploration page.

    Retrieves the session user and builds the restaurant distance page.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        Html: The rendered restaurant distance page HTML.
    """
    session_user = request.cookies.get("session_user")  # Retrieve the session user from cookies
    return build_find_restaurants_distance_page()  # Build and return the restaurant distance page

@app.post("/find-distance-restaurants")
async def find_distance_two_restaurants(request: Request):
    """
    Handles POST requests to calculate the Manhattan distance between two restaurants.

    Extracts restaurant IDs from form data, calculates the distance, and returns the result.

    Args:
        request (Request): The incoming HTTP request object containing form data.

    Returns:
        str: The calculated Manhattan distance or an error message.
    """
    form_data = await request.form()  # Access form data from the request
    restaurant1_id = int(form_data['restaurant1_id'])  # Retrieve and convert the first restaurant ID to integer
    restaurant2_id = int(form_data['restaurant2_id'])  # Retrieve and convert the second restaurant ID to integer
    return find_distance_use_case(restaurant1_id, restaurant2_id)  # Calculate and return the distance

@app.get("/restaurants-map")
async def get_restaurants_map():
    """
    Handles GET requests to the restaurants map page.

    Generates an interactive map of restaurants and returns it as an HTML response.

    Returns:
        HTMLResponse: The rendered map HTML content.
    """
    map_html = create_map()  # Generate the interactive map HTML
    return HTMLResponse(content=map_html)  # Return the map as an HTML response

@app.get("/sign-up")
def sing_up():
    """
    Handles GET requests to the sign-up page.

    Builds and returns the sign-up page HTML.

    Returns:
        Html: The rendered sign-up page HTML.
    """
    return build_sign_up_page()  # Build and return the sign-up page

@app.post("/create-user")
def create_user(
    name: str = Form(...),
    lastname: str = Form(...),
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    privacy_policy: bool = Form(...)
):
    """
    Handles POST requests to create a new user account.

    Extracts user information from form data and saves it to the database.

    Args:
        name (str): User's first name.
        lastname (str): User's last name.
        email (str): User's email address.
        username (str): Desired username.
        password (str): Desired password.
        privacy_policy (bool): Agreement to privacy policy.

    Returns:
        RedirectResponse: Redirects the user to the sign-in page upon successful registration.
    """
    return save_user_info(name, lastname, email, username, password, privacy_policy)  # Save user info and redirect

@app.get("/sign-in-page")
def sign_in_page():
    """
    Handles GET requests to the sign-in page.

    Builds and returns the sign-in page HTML.

    Returns:
        Html: The rendered sign-in page HTML.
    """
    return build_sign_in_page()  # Build and return the sign-in page

@app.post("/log-in-user-logic")
def sign_in(
    username: str = Form(...),
    password: str = Form(...)
):
    """
    Handles POST requests to authenticate a user.

    Verifies user credentials and manages session cookies upon successful login.

    Args:
        username (str): User's username.
        password (str): User's password.

    Returns:
        RedirectResponse or Html: Redirects to home page on success or returns sign-in page with error on failure.
    """
    return sign_in_user(username, password)  # Authenticate user and handle response

@app.get("/privacy-policy")
def get_privacy_policy():
    """
    Handles GET requests to the privacy policy page.

    Builds and returns the privacy policy page HTML.

    Returns:
        Html: The rendered privacy policy page HTML.
    """
    return build_privacy_policy()  # Build and return the privacy policy page

@app.get("/sign-out")
async def sign_out():
    """
    Handles GET requests to sign out a user.

    Removes the session cookie and redirects the user to the home page.

    Returns:
        RedirectResponse: Redirects the user to the home page after signing out.
    """
    response = RedirectResponse(url="/", status_code=303)  # Create a redirect response to home page
    response.delete_cookie("session_user")  # Delete the session_user cookie to sign out
    return response  # Return the redirect response

@app.get("/contact-info")
def get_contact_info():
    """
    Handles GET requests to the contact information page.

    Builds and returns the contact/info page HTML.

    Returns:
        Html: The rendered contact information page HTML.
    """
    return build_about_page()  # Build and return the contact/info page

@app.get("/update-password-page")
def update_password_page():
    """
    Handles GET requests to the change password page.

    Builds and returns the change password page HTML.

    Returns:
        Html: The rendered change password page HTML.
    """
    return build_change_password_page()  # Build and return the change password page

@app.post("/update-password")
async def update_password(request: Request):
    """
    Handles POST requests to update a user's password.

    Extracts the new password from form data and updates it in the database for the logged-in user.

    Args:
        request (Request): The incoming HTTP request object containing form data.

    Returns:
        RedirectResponse: Redirects the user to the home page after updating the password.
    """
    form_data = await request.form()  # Access form data from the request
    new_password = str(form_data['new_password'])  # Retrieve and convert the new password to string
    session_user = request.cookies.get("session_user")  # Retrieve the session user from cookies
    update_password_usecase(new_password, session_user)  # Update the user's password in the database
    return RedirectResponse(url="/", status_code=303)  # Redirect to the home page

@app.get("/scatter-plot")
def scatter_plot_page():
    """
    Handles GET requests to the scatter plot page.

    Builds and returns the scatter plot page HTML, displaying a plot of prices vs ratings.

    Returns:
        Html: The rendered scatter plot page HTML.
    """
    return build_scatter_plot_page()  # Build and return the scatter plot page

@app.get("/is-db-connected")
def test_db_connection():
    """
    Handles GET requests to test the database connection.

    Attempts to connect to the database and returns a success message if successful.

    Returns:
        str: Success message indicating the database connection is successful.
    """
    connector = MySqLConnectionCreator()  # Initialize the MySQL connection creator
    connection = connector.db_conn  # Establish a database connection
    connector.close_db_connection(connection)  # Close the database connection
    return "DB connection is successful"  # Return success message

# Start serving the FastHTML application
serve()
