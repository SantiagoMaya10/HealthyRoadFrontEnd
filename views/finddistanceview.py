from fasthtml.common import *  # Import FastHTML components for building HTML elements
from views.styles.homepagestyle import home_page_styles  # Import CSS for home page styling
from views.styles.footerstyle import site_footer  # Import CSS for footer styling
from views.styles.finddistancestyle import find_distance_style  # Import CSS for the find distance page
from usecases.findallrestaurantsusecase import find_all_restaurants  # Import the use case to retrieve restaurants data

def build_find_restaurants_distance_page():
    """
    Builds the 'Find Restaurants Distance' page with a table of restaurants and a form to calculate distances.

    The page includes:
    - A table that lists restaurants with their details such as ID, name, latitude, longitude, address, 
      average price, and average user rating.
    - A form where users can input two restaurant IDs to calculate the Manhattan distance between them.
    - The page uses htmx to submit the form asynchronously and update the result without refreshing the page.

    Returns:
        Html: The HTML structure for the 'Find Restaurants Distance' page.
    """
    
    # Fetch the restaurant data from the use case
    restaurants = find_all_restaurants()

    # Build the page with HTML elements
    return Html(
        Head(
            Meta(charset='UTF-8'),  # Meta tag for character encoding
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),  # Ensure the page is responsive
            Title('Explore Restaurants'),  # Page title
            Style(home_page_styles(), site_footer(), find_distance_style()),  # Add the necessary stylesheets
            Script(src="https://unpkg.com/htmx.org")  # Add the htmx script for AJAX functionality
        ),
        Body(
            # Navbar with a link to go back to the home page
            Div(cls='navbar')(
                A('Home', href='/')
            ),
            # Title section
            Div(cls='explore-title')(
                H1('Explore Restaurants in Medellin')
            ),
            # Table section displaying the list of restaurants
            Div(cls='restaurant-table-container')(
                H3('List of Restaurants'),
                Table(cls='restaurant-table')(
                    Thead(
                        Tr(
                            Th('ID'),  # Table headers
                            Th('Name'),
                            Th('Latitude'),
                            Th('Longitude'),
                            Th('Address'),
                            Th('Average price USD'),
                            Th('Average user rating')
                        )
                    ),
                    Tbody(
                        # Loop through the restaurants data and populate the table rows
                        *[
                            Tr(
                                Td(str(restaurant['id'])),
                                Td(restaurant['name']),
                                Td(str(restaurant['location_lat'])),
                                Td(str(restaurant['location_lon'])),
                                Td(restaurant['address']),
                                Td(restaurant['average_price_usd']),
                                Td(restaurant['visitors_average_rating']),
                            )
                            for restaurant in restaurants
                        ]
                    )
                )
            ),
            # Section with a form to compare distances between two restaurants
            Div(cls='compare-section')(
                H3('Find the Manhattan distance between two restaurants'),
                Form(
                    hx_post='/find-distance-restaurants',  # htmx: Send POST request to this endpoint
                    hx_target='#distance-result',  # htmx: Target div for injecting the result
                    hx_swap='innerHTML',  # htmx: Replace the inner content of the target div with the response
                    method='POST'
                )(
                    Label('Enter first restaurant ID:'),
                    Input(type='number', name='restaurant1_id', required=True),  # Input field for the first restaurant ID
                    Br(),
                    Label('Enter second restaurant ID:'),
                    Input(type='number', name='restaurant2_id', required=True),  # Input field for the second restaurant ID
                    Br(),
                    Input(type='submit', value='Calculate')  # Submit button to trigger distance calculation
                )
            ),
            Div(id='distance-result'),  # This div will display the result after the form submission
            # Add some spacing before the footer
            Br(), Br(), Br(), Br(), Br(), Br(), Br(),
            # Footer section
            Div(cls='footer')(
                P('© 2024 Gastro Tour Medellin. All rights reserved.')
            )
        )
    )
