import pyhtml

def get_page_html(form_data):
    print("About to return page 2")

    sql_query = "SELECT * FROM movie;"
    results = pyhtml.get_results_from_query("database/movies.db", sql_query)

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Reading from a .db file</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            background-color: #ffe082;
            color: #333;
        }}

        header {{
            background-color: #1565c0;
            padding: 10px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}

        .logo {{
            height: 50px;
        }}

        .nav-links {{
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }}

        .nav-links a {{
            color: white;
            text-decoration: none;
            font-weight: bold;
            font-size: 1rem;
        }}

        .nav-links a:hover {{
            text-decoration: underline;
        }}

        h1 {{
            text-align: center;
            margin-top: 30px;
            color: #0d47a1;
        }}

        .content {{
            padding: 20px 40px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
        }}

        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}

        th {{
            background-color: #004d40;
            color: white;
        }}

        tr:hover {{
            background-color: #f1f1f1;
        }}
    </style>
</head>
<body>
    <header>
        <img src="images/rmit.png" alt="RMIT Logo" class="logo">
        <div class="nav-links">
            <a href="/">Page 1a</a>
            <a href="/page2a">Page 2a</a>
            <a href="/page3a">Page 3a</a>
            <a href="/page1b">Page 1b</a>
            <a href="/page2b">Page 2b</a>
            <a href="/page3b">Page 3b</a>
        </div>
    </header>

    <h1>Page 2A - Example of retrieving data from a .db file</h1>

    <div class="content">
        <h2>Results from: <code>{sql_query}</code></h2>
        <table>
            <tr>"""
    
    # Add table headers
    if results:
        for col in range(len(results[0])):
            page_html += f"<th>Column {col+1}</th>"
        page_html += "</tr>"

        # Add table rows
        for row in results:
            page_html += "<tr>"
            for cell in row:
                page_html += f"<td>{cell}</td>"
            page_html += "</tr>"
    else:
        page_html += "<td colspan='100%'>No results found</td></tr>"

    page_html += """
        </table>
    </div>
</body>
</html>
"""
    return page_html