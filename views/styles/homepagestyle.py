divs_css = """
.main-content {
    display: flex;
    justify-content: space-around;
    margin: 100px 0;
    padding: 0 100px;
}

.functionality {
    background-color: #c8c6c6;
    padding: 200px;
    margin: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 40%;
    text-align: center;
}

.functionality h3 {
    margin: 0 0 10px;
}

.functionality p {
    color: #666;
}

.functionality button {
    padding: 10px 20px;
    background-color: #6a1b9a;  /* Purple button to match the theme */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.functionality button:hover {
    background-color: #4a148c;
}
"""

def divs_style():
    return divs_css
