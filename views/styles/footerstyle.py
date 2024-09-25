# CSS styles for the site footer, including links, social icons, and layout
css = """
body {
    margin: 0;
    font-family: Arial, sans-serif;  /* Set default font for the page */
}

.footer {
    background-color: #bb5151;  /* Dark red background for the footer */
    color: white;
    padding: 10px;
    text-align: center;  /* Center align the text */
    position: fixed;  /* Keep the footer at the bottom of the page */
    bottom: 0;
    width: 100%;  /* Make footer span the full width of the page */
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);  /* Add a slight shadow to the footer */
}

.footer a {
    color: #f2f2f2;  /* Light text color for links */
    text-decoration: none;
    margin: 0 10px;  /* Add space between links */
}

.footer a:hover {
    text-decoration: underline;  /* Underline links on hover */
}

.footer p {
    margin: 10px 0;  /* Margin for paragraphs inside the footer */
}

.footer .social-icons {
    margin: 10px 0;  /* Margin for the social icons section */
}

.footer .social-icons a {
    margin: 0 10px;  /* Space between social icons */
    display: inline-block;
    color: #f2f2f2;  /* Light color for social icons */
    font-size: 24px;  /* Font size for social icons */
    text-decoration: none;
    text-decoration: underline;  /* Social icons underlined by default */
}

.footer .social-icons a:hover {
    color: #ddd;  /* Lighter color for social icons on hover */
}
"""

def site_footer():
    """
    Returns the CSS styles for the site footer.

    The CSS includes:
    - A fixed footer positioned at the bottom of the page with a red background.
    - Styling for footer links, including hover effects and spacing.
    - Styling for social media icons with a default underline and hover color change.
    - General layout adjustments to ensure the footer spans the entire width of the page and maintains a consistent look.

    Returns:
        str: The CSS code as a string.
    """
    return css  # Return the CSS styles as a string
