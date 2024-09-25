from fasthtml.common import *  # Import FastHTML components for building HTML elements
from views.styles.signupstyle import sign_up_styles  # Import CSS styles specific to the sign-up page
from views.jsbehaviour.signupscripts import sign_up_js_scripts  # Import JavaScript behaviors for the sign-up page

def build_sign_up_page():
    """
    Builds the 'Sign Up' page with a registration form for new users.

    The page includes:
    - A navigation bar with links to 'Home'.
    - A container that holds the sign-up form, which includes fields for first name, last name, email, username, and password.
    - A checkbox to agree to the Privacy Policy and Personal Information Treatment.
    - A submit button to register.
    - An area to display messages (e.g., registration errors or success notifications).
    - Embedded JavaScript for form behavior and interactivity.

    The form uses htmx attributes to handle asynchronous form submission and update the page dynamically without a full reload.

    Returns:
        Html: The complete HTML structure for the sign-up page.
    """
    return Html(lang='en')(
        Head(
            Meta(charset='UTF-8'),  # Specify the character encoding for the document
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),  # Ensure the page is responsive on mobile devices
            Title('Sign Up'),  # Set the title of the page
            Style(sign_up_styles()),  # Include the sign-up page specific CSS styles
            Script(src='https://unpkg.com/htmx.org')  # Include the htmx library for handling AJAX requests and dynamic content
        ),
        Body(
            Div(cls='container')(
                H2('Sign Up'),  # Header for the sign-up form
                # Sign-up form with htmx attributes for asynchronous submission and dynamic content updates
                Form(
                    hx_post='/create-user',  # Endpoint to handle form submission via POST
                    hx_on='htmx:afterRequest: redirectToSignIn()',  # Trigger JavaScript function after the request completes
                    hx_target='.message',  # Target element to update with the server response
                    hx_swap='outerHTML'  # Replace the entire target element with the response
                )(
                    Label('First Name:', fr='name'),  # Label for the first name input
                    Input(type='text', id='name', name='name', required=''),  # Input field for first name
                    Label('Last Name:', fr='lastname'),  # Label for the last name input
                    Input(type='text', id='lastname', name='lastname', required=''),  # Input field for last name
                    Label('Email:', fr='email'),  # Label for the email input
                    Input(type='email', id='email', name='email', required=''),  # Input field for email
                    Label('Username:', fr='username'),  # Label for the username input
                    Input(type='text', id='username', name='username', required=''),  # Input field for username
                    Label('Password:', fr='password'),  # Label for the password input
                    Input(type='password', id='password', name='password', required=''),  # Input field for password
                    Div(cls='checkbox-container')(
                        Input(type='checkbox', id='privacy_policy', name='privacy_policy', required=''),  # Checkbox for agreeing to policies
                        Label(fr='privacy_policy')(
                            'I agree to the',
                            A('Privacy Policy', href='/privacy-policy', target='_blank'),  # Link to Privacy Policy
                            'and Personal Information Treatment'  # Additional agreement text
                        )
                    ),
                    Input(type='submit', id='register-btn', value='Register', disabled='')  # Submit button, initially disabled
                ),
                Div(cls='message')  # Placeholder for displaying messages (e.g., errors or success notifications)
            ),
            Script(sign_up_js_scripts())  # Embed JavaScript for additional sign-up page behaviors
        )
    )
