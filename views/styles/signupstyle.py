# CSS styles for the sign-up page, including input fields, buttons, and checkboxes
css = """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;  /* Light gray background */
}

.container {
    max-width: 400px;  /* Limit the container width */
    margin: 0 auto;  /* Center the container */
    padding: 20px;
    background-color: white;  /* White background for the container */
    border-radius: 5px;  /* Rounded corners */
    box-shadow: 0 0 10px rgba(0,0,0,0.1);  /* Light shadow for a subtle 3D effect */
}

input[type="text"], input[type="email"], input[type="password"] {
    width: 100%;  /* Full width for input fields */
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;  /* Light border for input fields */
    border-radius: 4px;
}

input[type="submit"] {
    background-color: #d75c5c;  /* Red background for the submit button */
    color: white;
    padding: 10px;
    border: none;
    border-radius: 4px;  /* Rounded corners for the button */
    cursor: pointer;  /* Pointer cursor on hover */
    margin-top: 10px;
}

input[type="submit"]:hover {
    background-color: #dc1313;  /* Darker red on hover */
}

.checkbox-container {
    display: flex;
    align-items: center;  /* Align checkbox with text */
    margin-top: 10px;
}

.checkbox-container input {
    margin-right: 10px;  /* Add space between checkbox and label */
}

#register-btn:disabled {
    background-color: #cccccc;  /* Gray background when the button is disabled */
    cursor: not-allowed;  /* Not-allowed cursor when disabled */
}

.message {
    margin-top: 20px;
    font-size: 14px;  /* Small font for error or success messages */
}
"""

def sign_up_styles():
    """
    Returns the CSS styles for the sign-up page.

    The CSS includes:
    - Basic styles for the body, form container, and form inputs.
    - Styles for the submit button, including hover and disabled states.
    - Styling for a checkbox container and its alignment with the label.
    - A section for messages (e.g., success or error messages) with small text formatting.

    Returns:
        str: The CSS code as a string.
    """
    return css  # Return the CSS styles as a string
