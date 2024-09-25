import folium # library to create interactive maps
# Class to retrieve db connections
from databaseconfig.dbconfig import MySqLConnectionCreator

def create_map():
    """Fetches all restaurants from database
    and then creates an interactive map with folium
    locating each restaurant in the map and its address

    Returns:
        str : An str which is an HTML document 
        with the map
    """
    # Fetch restaurants from the database
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name, location_lat, location_lon, address FROM restaurant")
    restaurants = cursor.fetchall()
    cursor.close()
    connector.close_db_connection(conn)
    # Create a Folium map centered in Medellín
    medellin_map = folium.Map(location=[6.2442, -75.5812], zoom_start=12)

    # Add restaurant markers to the map
    for restaurant in restaurants:
        folium.Marker(
            location=[restaurant['location_lat'], restaurant['location_lon']],
            popup=f"{restaurant['name']}<br>{restaurant['address']}",
            icon=folium.Icon(color="blue", icon="cutlery", prefix="fa")
        ).add_to(medellin_map)

    # Save map to HTML
    return medellin_map._repr_html_()  # This returns the map as an HTML string