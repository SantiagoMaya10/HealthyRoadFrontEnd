# CSS styles for the contact info page, including navbar, footer, and content styling
contact_info_css = """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;  /* Light background color */
}

.about-content {
    text-align: center;
    padding: 40px;
    margin: 20px auto;
    width: 80%;  /* Centered content with 80% width */
}

.title {
    text-align: center;
    padding: 40px 0;
    background-color: #bb5151;  /* Red background for the title */
    color: white;
    font-size: 60px;
    font-weight: bold;
}

.functionality {
    background-color: white;
    padding: 20px;
    margin: 10px auto;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Light shadow for 3D effect */
    width: 50%;
    text-align: center;
}

.functionality p {
    color: #666;
    font-size: 18px;
    margin: 10px 0;
}

.functionality a {
    color: #d66767;  /* Link color */
    text-decoration: none;
    font-weight: bold;
}

.functionality a:hover {
    color: #924f4f;  /* Darker color on hover */
}

.navbar {
    background-color: #d66767;  /* Red background for the navbar */
    overflow: hidden;
    padding: 10px 20px;
}

.navbar a {
    float: right;
    color: #f2f2f2;  /* Light text color for links */
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}

.navbar a:hover {
    background-color: #ddd;  /* Change background on hover */
    color: black;  /* Change text color on hover */
}

.footer {
    background-color: #d66767;  /* Red background for the footer */
    color: white;
    text-align: center;
    padding: 10px;
    position: fixed;
    bottom: 0;
    width: 100%;  /* Make the footer span the entire width */
}
"""

def contact_info_style():
    """
    Returns the CSS styles for the contact info page.

    The CSS includes:
    - Basic styles for the page layout such as background color, font, and margin/padding.
    - Styling for a title section with a red background and bold text.
    - Styling for a content section with shadow, rounded corners, and centered layout.
    - Styles for a navbar with links that change color on hover.
    - Footer styling that makes it fixed to the bottom of the page with a red background.
    
    Returns:
        str: The CSS code as a string.
    """
    return contact_info_css  # Return the CSS styles as a string
