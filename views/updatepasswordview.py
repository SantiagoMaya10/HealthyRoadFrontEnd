from fasthtml.common import *  # Import FastHTML components for building HTML elements
from views.styles.updatepasswordstyle import update_password_style  # Import CSS styles specific to the update password page

def build_change_password_page():
    """
    Builds the 'Change Password' page with a form for users to update their passwords.

    The page includes:
    - A navigation bar with a link back to the homepage.
    - A container that holds the password change form, which includes a field for the new password.
    - A submit button to update the password.
    - A footer with copyright information.

    Returns:
        Html: The complete HTML structure for the change password page.
    """
    # Create the navbar with a link to the homepage
    navbar = Div(cls='navbar')(
        A('Home', href='/')  # Link back to homepage
    )

    # Create the footer with copyright information
    footer = Div(cls='footer')(
        P('© 2024. All rights reserved.')  # Footer text
    )

    # Create the password change form
    password_change_form = Div(cls='password-change-form')(
        H2('Change Password'),  # Form heading
        Form(action='/update-password', method='POST')(
            Label('New Password:'),  # Label for the new password input
            Input(type='password', name='new_password', required=True),  # Input field for the new password
            Br(),  # Line break for spacing
            Input(type='submit', value='Update Password')  # Submit button to update the password
        )
    )

    # Build and return the complete HTML structure
    return Html(
        Head(
            Meta(charset='UTF-8'),  # Specify the character encoding for the document
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),  # Ensure the page is responsive on mobile devices
            Title('Change Password'),  # Set the page title
            Style(update_password_style())  # Include the update password page specific CSS styles
        ),
        Body(
            navbar,  # Navbar section
            password_change_form,  # Main content section with the password change form
            footer  # Footer section
        )
    )
