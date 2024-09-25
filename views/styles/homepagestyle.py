# CSS styles for the home page, including navbar, title section, and functionality blocks
css = """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;  /* Light background color for the page */
}

.navbar {
    background-color: #d66767;  /* Red background for the navigation bar */
    overflow: hidden;
    padding: 10px 20px;
}

.navbar a {
    float: right;  /* Align links to the right side of the navbar */
    color: #f2f2f2;  /* Light text color for navbar links */
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}

.navbar a:hover {
    background-color: #ddd;  /* Change background color on hover */
    color: black;  /* Change text color on hover */
}

.title {
    text-align: center;
    padding: 40px 0;
    background-color: #bb5151;  /* Dark red background for the title section */
    color: white;
    font-size: 60px;  /* Large font size for the title */
    font-weight: bold;
}

.functionalities {
    display: flex;
    justify-content: space-around;  /* Spread the functionality blocks evenly */
    margin: 150px 0;
    padding: 0 100px;
}

.functionality {
    background-color: white;
    padding: 20px;
    margin: 10px;
    border-radius: 8px;  /* Rounded corners for functionality blocks */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Light shadow for a 3D effect */
    width: 30%;  /* Each block takes up 30% of the width */
    text-align: center;
}

.functionality h3 {
    margin: 0 0 10px;  /* Add spacing below the heading */
}

.functionality p {
    color: #666;  /* Gray color for the paragraph text */
}

.functionality button {
    padding: 10px 20px;
    background-color: #d66767;  /* Red background for the button */
    color: white;
    border: none;
    border-radius: 5px;  /* Rounded corners for the button */
    cursor: pointer;
}

.functionality button:hover {
    background-color: #924f4f;  /* Darker red on hover */
}
"""

def home_page_styles():
    """
    Returns the CSS styles for the home page.

    The CSS includes:
    - Basic styles for the body, including background color and font settings.
    - Styling for the navigation bar, including hover effects for links.
    - Styling for the title section, with large, bold text and a background color.
    - Layout styles for the functionalities section, including flexbox for alignment.
    - Styling for functionality blocks, including background color, padding, and hover effects for buttons.

    Returns:
        str: The CSS code as a string.
    """
    return css  # Return the CSS styles as a string
