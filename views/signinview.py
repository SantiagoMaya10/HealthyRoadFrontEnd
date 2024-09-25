from fasthtml.common import *  # Import FastHTML components for building HTML elements
from views.styles.signinstyle import sign_in_style  # Import CSS styles specific to the sign-in page

def build_sign_in_page(login_message=Div()):
    """
    Builds the 'Sign In' page with a form for user authentication.

    The page includes:
    - A navigation bar (navbar) with links to 'Home', 'Login', and 'Sign Up'.
    - A container that holds the sign-in form, which includes fields for username and password.
    - A submit button to log in.
    - A link to the sign-up page for users who don't have an account.
    - An optional login message area to display error or success messages.

    Args:
        login_message (Div, optional): A FastHTML Div element to display messages (e.g., login errors). Defaults to an empty Div.

    Returns:
        Html: The complete HTML structure for the sign-in page.
    """
    return Html(lang='en')(
        Head(
            Meta(charset='UTF-8'),  # Specify the character encoding for the document
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),  # Ensure responsive design on mobile devices
            Title('Sign In'),  # Set the title of the page
            Style(sign_in_style()),  # Include the sign-in page specific CSS styles
        ),
        Body(
            # Container for the sign-in form
            Div(cls='container')(
                H2('Sign In'),  # Header for the sign-in form
                # Sign-in form with POST method to submit user credentials
                Form(action='/log-in-user-logic', method="POST")(
                    Label('Username:', fr='username'),  # Label for the username input
                    Input(type='text', id='username', name='username', required=''),  # Input field for username
                    Label('Password:', fr='password'),  # Label for the password input
                    Input(type='password', id='password', name='password', required=''),  # Input field for password
                    Input(type='submit', value='Sign In'),  # Submit button to log in
                    A("Don't have an account? Sign up here", href='/sign-up')  # Link to the sign-up page
                ),
                login_message  # Placeholder for displaying login messages (e.g., errors)
            )
        )
    )
