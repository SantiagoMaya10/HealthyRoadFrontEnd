divs_css = """
.main-content {
    display: flex;
    flex-direction: column;  /* Stack elements vertically */
    align-items: center;     /* Center align elements */
    margin: 50px 0;
    padding: 0 20px;
}

.classification-note {
    background-color: #e0e0e0;  /* Light gray background */
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
    text-align: center;
    width: 80%;
}

.classification-note h3 {
    margin-top: 0;
}

.classification-note p {
    margin-bottom: 0;
    color: #333;
}

.functionality {
    background-color: #c8c6c6;
    padding: 50px;
    margin: 20px 0;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 80%;  /* Adjusted width to match the note */
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
