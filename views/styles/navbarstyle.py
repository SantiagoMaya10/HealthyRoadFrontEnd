# CSS styles for the navigation bar (navbar), including dropdown functionality
navbar_css = """
.navbar {
    background-color: #d66767;  /* Red background for the navbar */
    overflow: hidden;
    padding: 10px 20px;
}

.navbar a {
    float: right;  /* Align navbar links to the right */
    color: #f2f2f2;  /* Light color for links */
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}

.navbar a:hover {
    background-color: #ddd;  /* Change background on hover */
    color: black;  /* Change text color on hover */
}

/* Dropdown container */
.dropdown {
    float: right;  /* Align dropdown to the right side */
    overflow: hidden;  /* Ensure dropdown content doesn't overflow */
}

/* Dropdown button */
.dropdown .dropbtn {
    color: #f2f2f2;  /* Light color for dropdown button */
    padding: 14px 16px;
    font-size: 17px;
    border: none;
    cursor: pointer;  /* Make the button clickable */
    background-color: inherit;  /* Inherit background from navbar */
    text-decoration: none;
}

.dropdown:hover .dropbtn {
    background-color: #ddd;  /* Change background on hover */
    color: black;  /* Change text color on hover */
}

/* Dropdown content (hidden by default) */
.dropdown-content {
    display: none;  /* Initially hidden */
    position: absolute;  /* Position dropdown relative to parent */
    background-color: #f9f9f9;  /* Light background for dropdown */
    min-width: 160px;  /* Minimum width for dropdown */
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);  /* Shadow effect for dropdown */
    z-index: 1;  /* Ensure dropdown appears above other content */
    right: 0;  /* Align to the right side */
}

/* Links inside the dropdown */
.dropdown-content a {
    float: none;  /* Align links to the left */
    color: black;  /* Black text for dropdown links */
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
    background-color: #ddd;
    color: black;
}

/* Show the dropdown on hover */
.dropdown:hover .dropdown-content {
    display: block;  /* Display dropdown when hovering over button */
}
"""

def navbar_style():
    """
    Returns the CSS styles for the navigation bar (navbar), including dropdown functionality.

    The CSS includes:
    - Basic styles for the navbar, such as background color and padding.
    - Hover effects for navbar links and dropdown buttons.
    - Styling for dropdown menus, including positioning, background color, and hover effects.
    - Dropdown content is initially hidden and displayed on hover.

    Returns:
        str: The CSS code as a string.
    """
    return navbar_css  # Return the CSS styles as a string
