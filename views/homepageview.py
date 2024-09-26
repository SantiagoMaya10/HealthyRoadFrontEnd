from fasthtml.common import *  # Import FastHTML components for building HTML elements
from views.styles.homepagestyle import divs_style  # Import CSS styles for the HealthyRoad page
from views.styles.footerstyle import footer_style  # Import CSS for the footer
from views.styles.navbarstyle import navbar_style  # Import CSS for the navbar

def build_healthyroad_page():
    """
    Builds the home page for 'HealthyRoad' project.
    
    The page includes a navbar, two functionalities, and a footer.
    """
    # Create the navbar
    navbar = Div(
        A('HealthyRoad', href='/', cls='logo'),  # Link to home, project name in the upper left
        cls='navbar'  # Set the CSS class for styling
    )

    # Create the footer
    footer = Div(
        P('© 2024. All rights reserved.'),
        cls='footer'  # Set the CSS class for styling
    )

    # Create the page layout
    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title('HealthyRoad'),
        Style(navbar_style(), footer_style(), divs_style())  # Include the CSS
    ),
    Body(
        navbar,  # Add the navbar
            Div(  # Main content div
                Div(
                H3('Note: Remember the menaning of the classification types'),
                P('D00 (Longitudinal Crack), D10 (Transverse Crack), D20 (Alligator Crack), D40 (Potholes)'),
                cls='classification-note'  # CSS class for styling
            ),
            Div(  # First functionality div
                H3('Track Road Conditions'),
                P('Monitor road conditions in real time and classify them based on quality.'),
                Button('Learn More', onclick="window.location.href='/track-road-conditions';"),
                cls='functionality'  # Set the CSS class for styling
            ),
            Div(  # Second functionality div
                H3('Road Safety Analysis'),
                P('Analyze road safety metrics and get detailed reports on potential hazards.'),
                Button('Start Analysis', onclick="window.location.href='/road-safety-analysis';"),
                cls='functionality'  # Set the CSS class for styling
            ),
            cls='main-content'  # Set the CSS class for the main content div
        ),
        footer  # Add the footer
    )
)

