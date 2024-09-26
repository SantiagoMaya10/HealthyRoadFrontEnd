from fasthtml.common import FastHTML, serve, Form  # Import FastHTML components for building HTML elements and serving the app
from fastapi import Request, Form  # Import FastAPI's Request and Form for handling HTTP requests and form data
from fastapi.responses import HTMLResponse  # Import response types for returning HTML content and handling redirects

from views.homepageview import build_healthyroad_page  
from views.roadmapfunctionality import build_road_conditions_page
from views.piechartview import build_piechart_page

from usecases.createmapusecase import create_road_map  # Import use case to create an interactive map of restaurants

# Initialize the FastHTML application
app = FastHTML()

@app.get("/")
def home(request: Request):
    """
    Handles GET requests to the home page.

    Retrieves the session user from cookies and builds the home page with a customized navbar.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        Html: The rendered home page HTML.
    """
    session_user = request.cookies.get("session_user")  # Retrieve the session user from cookies
    return build_healthyroad_page() # Build and return the home page with the navbar

@app.get("/track-road-conditions")
def track_road_conditions_page(request: Request):
    """
    Serves the 'Track Road Conditions' page:
    - Displays a list of unique roads.
    - Provides an input to search for a road by road_id.
    """
    return build_road_conditions_page("/view-road-map")

@app.post("/view-road-map")
async def view_road_map(request: Request, road_id: int = Form(...)):
    """
    Receives the road_id from the form and displays the map with locations.
    """
    road_map_html = create_road_map(road_id)  # Generate the map
    return HTMLResponse(content=road_map_html)  # Ret




@app.get("/road-safety-analysis")
def track_road_conditions_page(request: Request):
    """
    Serves the 'Track Road Conditions' page:
    - Displays a list of unique roads.
    - Provides an input to search for a road by road_id.
    """
    return build_road_conditions_page("/generate-pie-chart")


@app.post("/generate-pie-chart")
async def generate_pie_chart_endpoint(request: Request, road_id: int = Form(...)):
    """
    Endpoint to generate a pie chart for a given road_id.
    """
    return build_piechart_page(road_id)




# Start serving the FastHTML application
serve()
