# CSS styles for the scatter plot page, including navbar, scatter plot image, and footer
css_scatter_plot = """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;  /* Light background for the page */
}

.scatter-plot-content {
    text-align: center;  /* Center the scatter plot content */
    padding: 40px;  /* Add padding around the content */
}

.scatter-plot-content img {
    max-width: 100%;  /* Make sure the image doesn't exceed the container width */
    height: auto;  /* Automatically adjust the height to maintain aspect ratio */
}

.scatter-plot-content h2 {
    margin-bottom: 20px;
    font-size: 24px;  /* Set the font size for the header */
}

.navbar {
    background-color: #d66767;  /* Red background for the navbar */
    overflow: hidden;
    padding: 10px 20px;
}

.navbar a {
    float: right;  /* Align navbar links to the right */
    color: #f2f2f2;  /* Light color for navbar links */
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}

.navbar a:hover {
    background-color: #ddd;  /* Change background color on hover */
    color: black;  /* Change text color on hover */
}

.footer {
    background-color: #d66767;  /* Red background for the footer */
    color: white;
    text-align: center;
    padding: 10px;
    position: fixed;  /* Fix the footer at the bottom of the page */
    bottom: 0;
    width: 100%;  /* Make the footer span the full width */
}
"""

# Function to return the CSS for the scatter plot page
def scatter_page_styles():
    """
    Returns the CSS styles for the scatter plot page.

    The CSS includes:
    - Basic styles for the page body and the scatter plot content.
    - Ensures that the scatter plot image is responsive and maintains its aspect ratio.
    - Styling for the navigation bar (navbar) and footer, including hover effects for links.

    Returns:
        str: The CSS code as a string.
    """
    return css_scatter_plot  # Return the CSS styles as a string
