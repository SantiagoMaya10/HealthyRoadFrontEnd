import matplotlib.pyplot as plt  # Import the plotting module from matplotlib
from io import BytesIO  # Import BytesIO to handle byte stream of image data
import base64  # Import base64 to encode image data in base64 format
from databaseconfig.dbconfig import MySqLConnectionCreator  # Import MySQL connection creator from custom database configuration
import matplotlib  # Import the main matplotlib library to set the backend

# Establish 'Agg' (Anti-Grain Geometry) backend attribute
# to avoid GUI problems. It is a non-interactive backend
# since we don't want to render the plots in a window, just create a file to render on the frontend.
matplotlib.use('Agg')

def generate_scatter_plot():
    """
    Generates a scatter plot of restaurant price vs visitor rating,
    encodes the image as a base64 string, and returns the image data.

    The function queries the restaurant database to fetch the name, 
    average price (in USD), and average visitor rating. It uses this 
    data to create a scatter plot with the price on the x-axis and 
    the visitor rating on the y-axis. The restaurant names are shown 
    as labels for each point on the graph.

    Returns:
        str: The base64-encoded string of the generated scatter plot image.
    """
    # Create MySQL connection
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor()
    
    # Query the database for restaurant data
    query = """SELECT name, average_price_usd, visitors_average_rating
               FROM restaurant
               WHERE average_price_usd IS NOT NULL
               AND visitors_average_rating IS NOT NULL
            """
    cursor.execute(query)
    # Fetch results as tuples
    restaurants = cursor.fetchall()  
    cursor.close()  # Close the cursor
    connector.close_db_connection(conn)  # Close the database connection
    
    # Create a scatter plot
    fig, ax = plt.subplots(figsize=(25, 10))

    # Extract restaurant data (using tuple indices)
    prices = [restaurant[1] for restaurant in restaurants]  # Index 1 for `average_price_usd`
    ratings = [restaurant[2] for restaurant in restaurants]  # Index 2 for `visitors_average_rating`
    names = [restaurant[0] for restaurant in restaurants]    # Index 0 for `name`

    # Create the scatter plot
    scatter = ax.scatter(prices, ratings)

    # Add labels for each point
    for i, name in enumerate(names):
        ax.annotate(name, (prices[i], ratings[i]), textcoords="offset points", xytext=(0, 10), ha='center', rotation=90)

    # Set axis labels
    ax.set_xlabel('Precio (USD)')
    ax.set_ylabel('Rating de Visitantes')
    ax.set_title('Precio vs Rating en Restaurantes de Medellín')

    # Save the plot as a PNG image and encode it to base64
    buffer = BytesIO()  # Create a byte buffer to hold image data
    plt.savefig(buffer, format="png")  # Save the figure into the buffer
    buffer.seek(0)  # Rewind the buffer's position to the beginning
    image_base64 = base64.b64encode(buffer.getvalue()).decode()  # Encode image as base64
    buffer.close()  # Close the buffer

    return image_base64  # Return the base64-encoded image string
