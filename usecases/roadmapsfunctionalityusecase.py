from databaseconfig.dbconfig import MySqLConnectionCreator

def get_unique_roads():
    """
    Fetches all unique road_id and road_name from the database.
    """
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT DISTINCT road_id, road_name 
        FROM road_classification
    """
    cursor.execute(query)
    roads = cursor.fetchall()  # Fetch all unique roads
    
    cursor.close()
    connector.close_db_connection(conn)
    
    return roads
