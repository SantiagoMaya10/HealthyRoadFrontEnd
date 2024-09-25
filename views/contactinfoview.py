from fasthtml.common import *  # Import FastHTML components for building HTML elements
from views.styles.contactinfostyle import contact_info_style  # Import the CSS styles for the about/contact info page
import os  # Import the os module to access environment variables (e.g., LinkedIn and email)

def build_about_page():
    """
    Builds the 'About the Creator' page with a navbar, content section, and footer.

    The page includes:
    - A link back to the homepage in the navbar.
    - Content describing the creator, their undergraduate program, LinkedIn profile, and email contact.
    - A footer with a copyright notice.

    The LinkedIn URL and email are retrieved from environment variables for flexibility.

    Returns:
        Html: The HTML structure for the about page.
    """
    
    # Create the navbar with a link back to the homepage
    navbar = Div(cls='navbar')(
        A('Home', href='/')  # Link back to homepage
    )

    # Create the footer with a copyright notice
    footer = Div(cls='footer')(
        P('© 2024. All rights reserved.')
    )

    # Create the about page content with personal information
    about_content = Div(cls='about-content')(
        H1('About the Creator'),
        P('Name: Luis Santiago Maya Restrepo'),
        P('Undergraduate: 9th semester of Systems Engineering at the National University of Colombia'),
        P('LinkedIn: ', A('Luis Santiago Maya Restrepo on LinkedIn', href=os.getenv("LINKEDIN"), target='_blank')),  # LinkedIn URL from environment variable
        P(f'Contact me via e-mail: {os.getenv("EMAIL")}')  # Email from environment variable
    )

    # Build the full page structure: HTML head, body with navbar, content, and footer
    return Html(
        Head(
            Meta(charset='UTF-8'),  # Meta tag for character encoding
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),  # Meta tag for responsive design
            Title('About the Creator'),  # Page title
            Style(contact_info_style())  # Link to the page-specific CSS styles
        ),
        Body(
            navbar,  # Navbar section
            about_content,  # Main content section
            footer  # Footer section
        )
    )
