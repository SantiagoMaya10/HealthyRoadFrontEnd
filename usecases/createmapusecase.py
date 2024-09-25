import folium # library to create interactive maps
# Class to retrieve db connections
from databaseconfig.dbconfig import MySqLConnectionCreator

def create_road_map(road_id):
    """
    Generates a Folium map with the lat/lon markers for a specific road_id.
    """
    road = get_road_locations(road_id)
    
    if not road:
        return "<h3>No locations found for this road ID</h3>"

    # Center the map on the first location
    m = folium.Map(location=[road[0][0], road[0][1]], zoom_start=20)

    # Add markers for each location
    for lat, lon, classif, name in road:
        folium.Marker([lat, lon], popup=f"Road Id: {road_id} Road name: {name} Location: {lat}, {lon}, Damage(s): {classif}").add_to(m)

    return m._repr_html_()  # Return HTML for the map


def get_road_locations(road_id):
    """
    Fetches the lat/lon for a given road_id from the database.
    """
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor()
    
    query = """
        SELECT location_lat, location_lon, classifications, road_name 
        FROM road_classification 
        WHERE road_id = %s
    """
    cursor.execute(query, (road_id,))
    locations = cursor.fetchall()  # Get all locations (lat/lon) for this road
    
    cursor.close()
    connector.close_db_connection(conn)
    
    return locations