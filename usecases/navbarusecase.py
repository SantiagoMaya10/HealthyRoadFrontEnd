# fasthtml elements
from fasthtml.common import Div, A

def build_navbar(session_user=None):
    """Returns a div depending on wether there is
    an active session by validating if the session_user
    cookie is present or not.

    Args:
        session_user (str, optional): Current session_user cookie.
        Defaults to None.

    Returns:
        Div: if session present return username.
        Otherwise return login navbar
    """
    if session_user:
        # Display username with a dropdown for profile and logout
        return Div(
            Div(
                A(f'{session_user}', href='#', cls='dropbtn'),
                Div(
                    A('update-password', href='/update-password-page'),
                    A('Log Out', href='/sign-out'),
                    cls='dropdown-content'
                ),
                cls='dropdown'
            ),
            cls='navbar'
        )
    else:
        # Show Login and Sign Up links if user is not logged in
        return Div(
            A('Login', href='/sign-in-page'),
            A('Sign Up', href='/sign-up'),
            cls='navbar'
        )