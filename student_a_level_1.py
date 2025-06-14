from pyhtml import get_results_from_query

def get_page_html(form_data):
    print("About to return home page...")

    # Get data from the SQLite database
    min_year, max_year = get_results_from_query(
        "climate.db",
        """
        SELECT 
          MIN(CAST(SUBSTR(DMY, LENGTH(DMY) - 3, 4) AS INTEGER)),
          MAX(CAST(SUBSTR(DMY, LENGTH(DMY) - 3, 4) AS INTEGER))
        FROM weather_data
        WHERE DMY LIKE '%/%/%';
        """
    )[0]

    lowest_temp, coldest_station, coldest_state = get_results_from_query(
        "climate.db",
        """
        SELECT CAST(MinTemp AS FLOAT), ws.name, s.name
        FROM weather_data wd
        JOIN weather_station ws ON ws.site_id = wd.location
        JOIN state s ON s.id = ws.state_id
        WHERE MinTemp IS NOT NULL
        ORDER BY CAST(MinTemp AS FLOAT) ASC
        LIMIT 1;
        """
    )[0]

    highest_rain, rainiest_station, rainiest_state = get_results_from_query(
        "climate.db",
        """
        SELECT CAST(Precipitation AS FLOAT), ws.name, s.name
        FROM weather_data wd
        JOIN weather_station ws ON ws.site_id = wd.location
        JOIN state s ON s.id = ws.state_id
        WHERE Precipitation IS NOT NULL
        ORDER BY CAST(Precipitation AS FLOAT) DESC
        LIMIT 1;
        """
    )[0]

    most_state, most_count = get_results_from_query(
        "climate.db",
        """
        SELECT s.name, COUNT(*) as total 
        FROM weather_station ws 
        JOIN state s ON ws.state_id = s.id 
        GROUP BY s.name 
        ORDER BY total DESC 
        LIMIT 1;
        """
    )[0]

    # Build HTML
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weather Data Summary</title>
    <style>
        html, body {{
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #005b96, #003f63);
            display: flex;
            flex-direction: column;
        }}

        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: white;
            padding: 10px 20px;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        }}

        header img {{
            height: 50px;
        }}

        nav {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}

        nav a {{
            text-decoration: none;
            color: #004080;
            font-weight: bold;
        }}

        h1 {{
            text-align: center;
            font-size: 2.5em;
            color: white;
            margin: 30px 0 10px 0;
        }}

        main {{
            display: flex;
            justify-content: space-around;
            margin: 30px 20px 60px 20px;
            text-align: center;
            flex-wrap: wrap;
        }}

        .box {{
            flex: 1;
            margin: 10px;
            border-radius: 15px;
            padding: 25px 15px;
            color: #ffffff;
            background-color: rgba(255, 255, 255, 0.1);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            min-width: 180px;
        }}

        .box img {{
            height: 40px;
            margin-bottom: 10px;
        }}

        .box h2 {{
            font-size: 1.1em;
            margin: 10px 0;
            color: #ffffff;
        }}

        .box p {{
            font-size: 1.7em;
            font-weight: bold;
            color: #ffffff;
            margin: 5px 0;
        }}

        footer {{
            background-color: #f0f8ff;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            color: #333;
            border-top: 1px solid #ccc;
            margin-top: auto;
        }}
    </style>
</head>
<body>

<header>
    <img src="/static/images/rmit.png" alt="RMIT Logo">
    <nav>
        <a href="/">Page 1A</a>
        <a href="/page2a">Page 2A</a>
        <a href="/page3a">Page 3A</a>
        <a href="/page1b">Page 1B</a>
        <a href="/page2b">Page 2B</a>
        <a href="/page3b">Page 3B</a>
        <a href="/help">HELP</a>
    </nav>
</header>

<h1>WEATHER DATA</h1>

<main>
    <div class="box year">
        <img src="/static/images/icon-calendar.png" alt="Calendar Icon">
        <h2>YEAR RANGE</h2>
        <p>{min_year}–{max_year}</p>
    </div>
    <div class="box temp">
        <img src="/static/images/icon-thermometer.png" alt="Thermometer Icon">
        <h2>LOWEST TEMPERATURE</h2>
        <p>{lowest_temp}°C<br>({coldest_station}, {coldest_state})</p>
    </div>
    <div class="box rain">
        <img src="/static/images/icon-rain.png" alt="Rain Icon">
        <h2>HIGHEST RAINFALL</h2>
        <p>{highest_rain} mm<br>({rainiest_station}, {rainiest_state})</p>
    </div>
    <div class="box stations">
        <img src="/static/images/icon-map.png" alt="Map Icon">
        <h2>MOST WEATHER STATIONS</h2>
        <p>{most_state}<br>({most_count} stations)</p>
    </div>
</main>

<footer>
    <p>FAQ: For more information, please contact support or visit our <a href="/faq">FAQ page</a>.</p>
</footer>

</body>
</html>
"""
    return page_html