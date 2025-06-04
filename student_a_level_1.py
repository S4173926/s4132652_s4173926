def get_page_html(form_data):
    page_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jason Chen's Climate Dashboard</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            background-color: #f8f9fa;
            color: #333;
        }
        header {
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            padding: 15px 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        header img {
            height: 45px;
        }
        nav a {
            color: white;
            margin-right: 20px;
            text-decoration: none;
            font-weight: bold;
        }
        nav a:hover {
            text-decoration: underline;
        }
        .container {
            display: grid;
            grid-template-columns: 1fr 3fr;
            gap: 20px;
            padding: 20px 30px;
        }
        .sidebar, .main {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        .sidebar h3, .main h2 {
            color: #0077b6;
        }
        label {
            display: block;
            margin-top: 10px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 14px;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #00b4d8;
            border: none;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0096c7;
        }
        .map, .trend-chart, .summary-chart {
            background-color: #edf6f9;
            border: 2px dashed #90e0ef;
            padding: 20px;
            border-radius: 10px;
            margin-top: 15px;
            text-align: center;
        }
        .highlight {
            background-color: #ff6b6b;
            color: white;
            padding: 5px 10px;
            border-radius: 6px;
            display: inline-block;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

<header>
    <img src="images/rmit.png" alt="Logo">
    <nav>
        <a href="#">Home</a>
        <a href="#">Dashboard</a>
        <a href="#">Maps</a>
        <a href="#">Reports</a>
        <a href="#">About</a>
        <a href="#">Profile</a>
    </nav>
</header>

<div class="container">
    <aside class="sidebar">
        <h3>Search City / LGA</h3>
        <p><strong>Temperature:</strong> 18°C</p>
        <p><strong>Rainfall:</strong> 10mm</p>

        <label>Suburb:</label>
        <input type="text" name="suburb">

        <label>Year Range:</label>
        <input type="text" name="year_range" placeholder="1970-2020">

        <label>Data Type:</label>
        <select name="data_type">
            <option value="temp">Temperature</option>
            <option value="rain">Rainfall</option>
        </select>

        <button>Apply</button>

        <div class="summary-chart">
            <p><strong>Summary Chart Placeholder</strong></p>
        </div>
    </aside>

    <main class="main">
        <h2>Map of Urban Zones</h2>
        <div class="map">
            <p class="highlight">High Heatwave Risk</p>
            <p>[Urban zone map with heat risk areas]</p>
        </div>

        <h2>Climate Trends</h2>
        <div class="trend-chart">
            <p>[Climate trend chart placeholder]</p>
        </div>
    </main>
</div>

</body>
</html>
"""
    return page_html