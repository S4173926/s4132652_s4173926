import pyhtml

def get_page_html(form_data):
    print("About to return page 2")
    
    # SQL query example
    sql_query = "SELECT * FROM movie;"
    results = pyhtml.get_results_from_query("database/movies.db", sql_query)

    # Start HTML with style
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Policy Planning Tool - Jason Chen</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f9fb;
            margin: 0;
            padding: 0;
        }}
        header {{
            background: linear-gradient(to right, #0077b6, #00b4d8);
            padding: 15px 30px;
            color: white;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        nav a {{
            margin: 0 12px;
            color: white;
            text-decoration: none;
            font-weight: bold;
        }}
        nav a:hover {{
            text-decoration: underline;
        }}
        .container {{
            padding: 30px;
        }}
        .flex-row {{
            display: flex;
            justify-content: space-between;
            gap: 20px;
        }}
        .input-box {{
            flex: 1;
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }}
        label {{
            display: block;
            font-weight: bold;
            margin-top: 10px;
        }}
        input, select {{
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border-radius: 6px;
            border: 1px solid #ccc;
        }}
        .section-title {{
            font-size: 1.2em;
            color: #0077b6;
            margin-top: 25px;
        }}
        .chart, .map {{
            background: #e9f5f9;
            padding: 20px;
            border: 2px dashed #90e0ef;
            border-radius: 10px;
            text-align: center;
            margin-top: 15px;
        }}
        .button-row {{
            margin-top: 25px;
            text-align: center;
        }}
        .button-row button {{
            margin: 0 10px;
            padding: 10px 20px;
            border: none;
            background-color: #00b4d8;
            color: white;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }}
        .button-row button:hover {{
            background-color: #0096c7;
        }}
        .table {{
            margin-top: 20px;
            border-collapse: collapse;
            width: 100%;
            background: white;
        }}
        .table th, .table td {{
            padding: 10px;
            border: 1px solid #ddd;
        }}
        .table th {{
            background-color: #caf0f8;
            color: #03045e;
        }}
    </style>
</head>
<body>

<header>
    <div><strong>LOGO</strong></div>
    <nav>
        <a href="#">HOME</a>
        <a href="#">DASHBOARD</a>
        <a href="#">MAPS</a>
        <a href="#">REPORTS</a>
        <a href="#">POLICY TOOL</a>
        <a href="#">Profile</a>
    </nav>
</header>

<div class="container">
    <div class="flex-row">
        <div class="input-box">
            <label>Select Zone:</label>
            <input type="text" placeholder="Suburb Name">

            <div class="section-title">Zone Climate (Summary)</div>
            <ul>
                <li>Hot Summers</li>
                <li>Variable Rainfall</li>
                <li>Occasional Storms</li>
            </ul>
        </div>

        <div class="input-box">
            <label>Select Scenario:</label>
            <select>
                <option>2030</option>
                <option>2050</option>
                <option>2070</option>
            </select>
            <button style="margin-top: 10px;">Next</button>

            <div class="section-title">Future Projection</div>
            <div class="chart">[Projection Graph Placeholder]</div>
        </div>
    </div>

    <div class="section-title">Map: Sea Level Rise + Heat Zones</div>
    <div class="map">[Urban Zone Map Placeholder]</div>

    <div class="button-row">
        <button>&larr; Back</button>
        <button>Generate Report</button>
        <button>Save Template</button>
    </div>

    <div class="section-title">Data Preview from DB (mock example)</div>
    <table class="table">
        <tr><th>ID</th><th>Title</th><th>Genre</th></tr>
    """
    for row in results:
        page_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>\n"

    page_html += """
    </table>
</div>

</body>
</html>
"""
    return page_html