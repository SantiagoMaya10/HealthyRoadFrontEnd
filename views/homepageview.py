from fasthtml.common import *  # Import FastHTML components for building HTML elements
from views.styles.homepagestyle import home_page_styles  # Import CSS styles for the home page
from views.styles.footerstyle import site_footer  # Import CSS for the footer
from views.styles.navbarstyle import navbar_style  # Import CSS for the navbar

def build_home_page(navbar=Div(
            A('Login', href='/sign-in-page'),  # Link to the sign-in page
            A('Sign Up', href='/sign-up'),  # Link to the sign-up page
            cls='navbar'  # Add CSS class for navbar styling
        )):
    """
    Builds the home page for the 'Gastro Tour Medellin' project.

    The page includes:
    - A navbar with links for login and sign-up.
    - Sections that introduce various functionalities of the website, including:
        - Exploring restaurant distances
        - Viewing restaurant locations on a map
        - Comparing prices and ratings
    - A footer with links to the privacy policy, contact info, and a Patreon contribution link.

    Returns:
        Html: The HTML structure for the home page.
    """
    return Html(
        Head(
            Meta(charset='UTF-8'),  # Meta tag for character encoding
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),  # Ensure responsive design
            Title('Gastro Tour Medellin'),  # Set the page title
            Style(home_page_styles(), site_footer(), navbar_style())  # Include the necessary CSS stylesheets
        ),
        Body(
            navbar,  # Navbar with login and sign-up links
            Div('Gastro Tour Medellin', cls='title'),  # Title section with the project name
            Div(  # Main content section
                Div(  # Functionality 1: Explore restaurant distances
                    H3('Explore Restaurants Distance'),
                    P('Discover the best restaurants in Medellin and find Manhattan distances between them'),
                    Button('Explore Now', onclick="window.location.href='/find-distance-page';"),  # Button to navigate to the restaurant distance page
                    cls='functionality'
                ),
                Div(  # Functionality 2: View restaurant locations on a map
                    H3('Find Restaurants Location and Their Address in Medellin'),
                    P('Find the top restaurants in Medellin with an amazing interactive map'),
                    Button('View Map', onclick="window.location.href='/restaurants-map';"),  # Button to navigate to the map page
                    cls='functionality'
                ),
                Div(  # Functionality 3: Compare prices and ratings with a plot
                    H3('Compare Prices and Ratings'),
                    P('Compare prices vs ratings with an exclusive plot with all top restaurants'),
                    Button('See Offers', onclick="window.location.href='/scatter-plot';"),  # Button to navigate to the scatter plot page
                    cls='functionality'
                ),
                cls='functionalities'  # Wrapper class for all functionalities
            ),
            # Footer section
            Div(
                P('© 2024 Gastro Tour Medellin. All rights reserved.'),  # Copyright notice
                P(
                    A('Privacy Policy', href='/privacy-policy'),  # Link to the privacy policy
                    '|',  # Separator
                    A('Contact Us', href='/contact-info')  # Link to the contact info page
                ),
                Div(
                    A('Contribute on Patreon', href='https://patreon.com/user?u=122587768&utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink', target='_blank'),  # Patreon link
                    cls='social-icons'  # CSS class for social icons
                ),
                cls='footer'  # CSS class for the footer
            )
        ),
        lang='en'  # Set the language of the page to English
    )
