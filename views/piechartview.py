from fasthtml.common import *
from usecases.piechartusecase import (
    generate_pie_chart,
    get_classifications_by_road_id,
    process_classifications,
    calculate_percentages
)
from views.styles.navbarstyle import navbar_style
from views.styles.footerstyle import footer_style
from views.styles.piechartstyle import pie_chart_style  # Assuming you have a style for the pie chart page
import base64

def build_piechart_page(road_id: int):
    """
    Builds the pie chart page for a given road_id using FastHTML components.
    Includes the navbar, footer, and embeds the pie chart image.
    """
    # Step 1: Fetch data from the database
    classifications_list = get_classifications_by_road_id(road_id)
    
    if not classifications_list:
        # Return a page with a message if no data is found
        return Html(
            Head(
                Title(f"No Data for Road ID {road_id}"),
                Style(navbar_style(), footer_style())
            ),
            Body(
                Div(
                    A('HealthyRoad', href='/', cls='logo'),
                    cls='navbar'
                ),
                Div(
                    H3(f"No data found for Road ID {road_id}"),
                    cls='main-content'
                ),
                Div(
                    P('© 2024 HealthyRoad. All rights reserved.'),
                    cls='footer'
                )
            )
        )
    
    # Step 2: Process classifications
    damage_counts = process_classifications(classifications_list)
    
    # Step 3: Calculate percentages
    percentages = calculate_percentages(damage_counts)
    
    # Step 4: Generate the pie chart image
    image_data = generate_pie_chart(percentages, road_id)

    # Encode the image data to base64
    base64_image = base64.b64encode(image_data).decode('utf-8')

    # Create the FastHTML page to display the image
    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title(f"Damage Pie Chart for Road ID {road_id}"),
            Style(navbar_style(), footer_style(), pie_chart_style())
        ),
        Body(
            Div(
                A('HealthyRoad', href='/', cls='logo'),
                cls='navbar'
            ),
            Div(
                H2(f"Damage Pie Chart for Road ID {road_id}"),
                Img(src=f"data:image/png;base64,{base64_image}", alt="Damage Pie Chart"),
                cls='main-content'
            ),
            Div(
        P('© 2024. All rights reserved.'),
        cls='footer'  # Set the CSS class for styling
    )
        )
    )
