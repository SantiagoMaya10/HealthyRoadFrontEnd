# CSS styles for the update password page, including form input, submit button, and navbar/footer
css_update_pssw = """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;  /* Light background for the page */
}

.password-change-form {
    max-width: 400px;  /* Limit form width */
    margin: 50px auto;  /* Center the form with top margin */
    padding: 20px;
    background-color: white;  /* White background for the form */
    border-radius: 8px;  /* Rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Subtle shadow effect */
}

.password-change-form h2 {
    text-align: center;  /* Center the form title */
    margin-bottom: 20px;
}

.password-change-form label {
    display: block;
    margin: 10px 0 5px;  /* Space around the label */
    font-weight: bold;  /* Bold labels */
}

.password-change-form input[type="password"] {
    width: 100%;  /* Full width for input fields */
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;  /* Light border */
    border-radius: 5px;
}

.password-change-form input[type="submit"] {
    width: 100%;  /* Full width for the submit button */
    padding: 10px;
    background-color: #d66767;  /* Red background for the submit button */
    color: white;
    border: none;
    border-radius: 5px;  /* Rounded corners */
    cursor: pointer;  /* Pointer cursor on hover */
}

.password-change-form input[type="submit"]:hover {
    background-color: #924f4f;  /* Darker red on hover */
}

.navbar {
    background-color: #d66767;  /* Red background for the navbar */
    overflow: hidden;
    padding: 10px 20px;
}

.navbar a {
    float: right;  /* Align links to the right side of the navbar */
    color: #f2f2f2;  /* Light text color */
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}

.navbar a:hover {
    background-color: #ddd;  /* Light background on hover */
    color: black;  /* Dark text on hover */
}

.footer {
    background-color: #d66767;  /* Red background for the footer */
    color: white;
    text-align: center;
    padding: 10px;
    position: fixed;
    bottom: 0;
    width: 100%;  /* Full width for the footer */
}
"""

def update_password_style():
    """
    Returns the CSS styles for the update password page.

    The CSS includes:
    - Styling for the password change form, including input fields and the submit button.
    - Navbar and footer styling, matching the overall site design.
    - Hover effects for buttons and links.
    - Form layout with centered alignment and a subtle shadow effect.

    Returns:
        str: The CSS code as a string.
    """
    return css_update_pssw  # Return the CSS styles as a string
