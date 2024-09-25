# CSS styles for the "Find Distance" page, including layout, table, and footer styling
find_distance_css = """
html, body {
    height: 100%;
    margin: 0;
    padding: 0;
    box-sizing: border-box;  /* Ensure padding and borders are included in total element width and height */
}

body {
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    min-height: 100vh;  /* Ensure body takes up at least the full height of the viewport */
}

.restaurant-table-container {
    flex: 1;  /* Allow the container to expand and take up available space */
    overflow-y: auto;  /* Allow vertical scrolling if content exceeds the viewport */
}

.restaurant-table {
    width: 100%;  /* Table takes up full width */
    border-collapse: collapse;  /* Remove space between table cells */
    margin-top: 20px;
}

.restaurant-table th, .restaurant-table td {
    padding: 10px;
    border: 1px solid #ddd;  /* Light border around table cells */
    text-align: left;  /* Left-align text in table cells */
}

.restaurant-table th {
    background-color: #f2f2f2;  /* Light background for table headers */
    font-weight: bold;
}

.restaurant-table td {
    background-color: #fff;  /* White background for table cells */
}

.restaurant-table tr:nth-child(even) {
    background-color: #f9f9f9;  /* Alternate row colors for better readability */
}

.compare-section {
    margin-top: 20px;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;  /* Light border around the compare section */
}

footer {
    text-align: center;
    padding: 10px;
    background-color: #f2f2f2;  /* Light background color for the footer */
    position: relative;
    width: 100%;
    bottom: 0;
}
"""

def find_distance_style():
    """
    Returns the CSS styles for the "Find Distance" page.

    The CSS includes:
    - Basic layout styles for the HTML and body to ensure the page takes up the full viewport height.
    - Styles for the restaurant table, including borders, alternating row colors, and padding.
    - A section for comparing distances, styled with padding and a border.
    - Footer styling to keep it fixed at the bottom of the page.

    Returns:
        str: The CSS code as a string.
    """
    return find_distance_css  # Return the CSS styles as a string
