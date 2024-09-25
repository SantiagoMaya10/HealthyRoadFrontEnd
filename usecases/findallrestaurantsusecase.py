# Class to retrieve db connections
from databaseconfig.dbconfig import MySqLConnectionCreator

def find_all_restaurants():
    """Find all restaurants information and fields
    in database from restaurant table

    Returns:
        List[Dict[str, Any]]: a List with a dictionary 
        with key value pairs for restaurants
    """
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, location_lat, location_lon, address, average_price_usd, visitors_average_rating FROM restaurant")
    restaurants = cursor.fetchall()
    cursor.close()

    connector.close_db_connection(conn)

    return restaurants