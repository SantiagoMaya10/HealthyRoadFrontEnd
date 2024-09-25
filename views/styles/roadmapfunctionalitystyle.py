road_conditions_css = """
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 0;
}

.navbar {
    background-color: purple;
    padding: 10px;
    text-align: left;
    position: fixed; /* Fix the navbar at the top */
    top: 0;
    width: 100%;
    z-index: 1000; /* Ensure the navbar stays above other elements */
}

.navbar a {
    color: white;
    text-decoration: none;
    font-size: 20px;
}

.main-content {
    padding: 20px;
    margin-top: 60px; /* Add top margin equal to navbar height to prevent overlap */
    margin-bottom: 60px; /* Add bottom margin equal to footer height to prevent overlap */
}

.table-container {
    max-height: calc(100vh - 140px); /* Total viewport height minus navbar and footer heights plus margins */
    overflow-y: auto; /* Enable vertical scrolling */
    border: 1px solid #ddd;
}

.road-table {
    width: 100%;
    border-collapse: collapse;
}

.road-table th, .road-table td {
    padding: 10px;
    border: 1px solid #ddd;
    text-align: left;
}

.road-table th {
    background-color: #f2f2f2;
}

.road-input-section {
    margin-top: 20px;
}

.footer {
    background-color: purple;
    color: white;
    text-align: center;
    padding: 10px;
    position: fixed; /* Fix the footer at the bottom */
    width: 100%;
    bottom: 0;
    z-index: 1000; /* Ensure the footer stays above other elements */
}
"""

def road_conditions_style():
    return road_conditions_css
