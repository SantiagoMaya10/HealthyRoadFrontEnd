navbar_css = """
.navbar {
    background-color: #6a1b9a;  /* Purple background for the navbar */
    overflow: hidden;
    padding: 10px 20px;
}

.navbar a {
    float: left;  /* Align project name to the left */
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}

.navbar a:hover {
    background-color: #ddd;
    color: black;
}
"""

def navbar_style():
    return navbar_css
