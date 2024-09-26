import matplotlib.pyplot as plt
import io
from databaseconfig.dbconfig import MySqLConnectionCreator
from collections import Counter
import matplotlib.pyplot as plt
import io


def generate_pie_chart(percentages):
    """
    Generates a pie chart from the damage percentages.
    
    Args:
        percentages (dict): Damage types and their percentages.
    
    Returns:
        bytes: Image data in PNG format.
    """
    labels = list(percentages.keys())
    sizes = list(percentages.values())
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Damage Type Distribution')
    
    # Save the figure to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return buf.getvalue()



# Function to fetch classifications
def get_classifications_by_road_id(road_id):
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor()
    
    query = """
        SELECT classifications 
        FROM road_classification 
        WHERE road_id = %s
    """
    cursor.execute(query, (road_id,))
    results = cursor.fetchall()
    
    cursor.close()
    connector.close_db_connection(conn)
    
    # Extract classifications from results
    classifications = [row[0] if row[0] else '' for row in results]
    return classifications

# Function to process classifications
def process_classifications(classifications_list):
    damage_counts = Counter()
    for classifications in classifications_list:
        if not classifications:
            damage_counts['Healthy'] += 1
        else:
            damages = [damage.strip() for damage in classifications.split(',')]
            for damage in damages:
                damage_counts[damage] += 1
    return damage_counts

# Function to calculate percentages
def calculate_percentages(damage_counts):
    total = sum(damage_counts.values())
    percentages = {damage: (count / total) * 100 for damage, count in damage_counts.items()}
    return percentages

# Function to generate pie chart
def generate_pie_chart(percentages, road_id):
    labels = list(percentages.keys())
    sizes = list(percentages.values())
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title(f'Damage Type Distribution for Road ID {road_id}')
    
    # Save the figure to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return buf.getvalue()
