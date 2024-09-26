from fasthtml.common import *
from usecases.roadmapsfunctionalityusecase import get_unique_roads
from views.styles.roadmapfunctionalitystyle import road_conditions_style
from views.styles.navbarstyle import navbar_style
from views.styles.footerstyle import footer_style


def build_road_conditions_page(redirect_to):
    """
    Builds the 'Track Road Conditions' page, displaying a table of roads and a form to input a road_id.
    """
    # Fetch the list of distinct roads (road_id and road_name)
    roads = get_unique_roads()
    
    # Create the navbar
    navbar = Div(
        A('HealthyRoad', href='/', cls='logo'),
        cls='navbar'
    )
    
    # Create the footer
    footer = Div(
        P('© 2024 HealthyRoad. All rights reserved.'),
        cls='footer'
    )
    
    # Build the HTML page
    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title('Select Road'),
            Style(
                road_conditions_style(),
                navbar_style(),
                footer_style()
            )
        ),
        Body(
            navbar,
            Div(
                H2('Available Roads to explore'),
                
                # Table displaying the roads
                Table(
                    Thead(
                        Tr(
                            Th('Road ID'),
                            Th('Road Name')
                        )
                    ),
                    Tbody(
                        *[
                            Tr(
                                Td(str(road['road_id'])),
                                Td(road['road_name'])
                            )
                            for road in roads
                        ]
                    ),
                    cls='road-table'
                ),
                
                # Form for inputting road ID
                Div(
                    Form(
                        Label('Enter Road ID to acces functionality:'),
                        Input(type='number', name='road_id', required=True),
                        Br(),
                        Input(type='submit', value='View Map'),
                        action= redirect_to,
                        method='POST'
                    ),
                    cls='road-input-section'
                ),
                cls='main-content'
            ),
            footer
        )
    )
