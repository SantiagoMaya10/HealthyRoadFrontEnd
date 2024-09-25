# CSS styles for the sign-in page, including form input, buttons, and responsiveness
sign_in_css = """
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;  /* Light background for the page */
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;  /* Center the form horizontally */
    align-items: center;  /* Center the form vertically */
    height: 100vh;  /* Full viewport height */
}

.container {
    background-color: white;  /* White background for the form container */
    padding: 40px;
    border-radius: 10px;  /* Rounded corners for the form */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);  /* Light shadow for a 3D effect */
    width: 100%;
    max-width: 400px;  /* Limit the width of the form */
}

h2 {
    text-align: center;  /* Center align the form heading */
    margin-bottom: 20px;
    color: #333;  /* Dark color for the heading */
}

label {
    font-size: 14px;
    color: #555;  /* Medium gray color for labels */
    margin-bottom: 8px;
    display: block;
}

input[type="text"], input[type="password"] {
    width: 100%;  /* Full width for input fields */
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;  /* Light border for input fields */
    border-radius: 4px;
    font-size: 14px;
    box-sizing: border-box;  /* Ensure padding is included in the element's total width */
}

input[type="submit"] {
    width: 100%;  /* Full width for the submit button */
    padding: 12px;
    background-color: #d66767;  /* Red background for the button */
    border: none;
    color: white;
    font-size: 16px;
    cursor: pointer;  /* Pointer cursor on hover */
    border-radius: 4px;
    transition: background-color 0.3s ease;  /* Smooth transition on hover */
}

input[type="submit"]:hover {
    background-color: #dc1313;  /* Darker red on hover */
}

input[type="submit"]:disabled {
    background-color: #cccccc;  /* Gray background when disabled */
    cursor: not-allowed;  /* Not-allowed cursor when disabled */
}

.message {
    text-align: center;
    color: red;
    margin-top: 20px;
    font-size: 14px;
}

.container a {
    display: block;
    text-align: center;
    margin-top: 10px;
    color: #007bff;  /* Blue color for links */
    text-decoration: none;
    font-size: 14px;
}

.container a:hover {
    text-decoration: underline;  /* Underline links on hover */
}

/* Responsive adjustments */
@media (max-width: 600px) {
    .container {
        padding: 20px;
    }

    h2 {
        font-size: 24px;  /* Adjust font size for small screens */
    }

    input[type="submit"] {
        font-size: 14px;
        padding: 10px;
    }
}
"""

def sign_in_style():
    """
    Returns the CSS styles for the sign-in page.

    The CSS includes:
    - Basic styles for the sign-in form, input fields, submit button, and error messages.
    - Hover and disabled states for the submit button.
    - Responsive design that adjusts padding and font sizes for smaller screens.
    - Styling for links that guide users to other actions (e.g., sign-up page).

    Returns:
        str: The CSS code as a string.
    """
    return sign_in_css  # Return the CSS styles as a string
