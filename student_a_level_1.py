from pyhtml import get_results_from_query

def get_page_html(form_data):
    print("Rendering Page 1A – Weather Data Summary")

    min_year, max_year = get_results_from_query(
        "climate.db",
        '''
        SELECT MIN(CAST(SUBSTR(DMY, LENGTH(DMY) - 3, 4) AS INTEGER)),
               MAX(CAST(SUBSTR(DMY, LENGTH(DMY) - 3, 4) AS INTEGER))
        FROM weather_data
        WHERE DMY LIKE '%/%/%';
        '''
    )[0]

    lowest_temp, coldest_station, coldest_state = get_results_from_query(
        "climate.db",
        '''
        SELECT CAST(MinTemp AS FLOAT), ws.name, s.name
        FROM weather_data wd
        JOIN weather_station ws ON ws.site_id = wd.location
        JOIN state s ON s.id = ws.state_id
        WHERE MinTemp IS NOT NULL
        ORDER BY CAST(MinTemp AS FLOAT) ASC
        LIMIT 1;
        '''
    )[0]

    highest_rain, rainiest_station, rainiest_state = get_results_from_query(
        "climate.db",
        '''
        SELECT CAST(Precipitation AS FLOAT), ws.name, s.name
        FROM weather_data wd
        JOIN weather_station ws ON ws.site_id = wd.location
        JOIN state s ON s.id = ws.state_id
        WHERE Precipitation IS NOT NULL
        ORDER BY CAST(Precipitation AS FLOAT) DESC
        LIMIT 1;
        '''
    )[0]

    most_state, most_count = get_results_from_query(
        "climate.db",
        '''
        SELECT s.name, COUNT(*) as total
        FROM weather_station ws
        JOIN state s ON ws.state_id = s.id
        GROUP BY s.name
        ORDER BY total DESC
        LIMIT 1;
        '''
    )[0]

    return f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Weather Data Summary</title>
    <style>
        html, body {{
            height: 100%;
            margin: 0;
            display: flex;
            flex-direction: column;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(to bottom, #e3f2fd, #ffffff);
            color: #333;
        }}
        header {{
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            height: 12vh;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
        }}
        header img {{
            height: 40px;
        }}
        header ul {{
            list-style: none;
            display: flex;
            margin: 0;
            padding: 0;
        }}
        header li {{
            margin: 0 10px;
        }}
        header a {{
            color: white;
            text-decoration: none;
            font-weight: 600;
        }}
        header a:hover {{
            text-decoration: underline;
        }}
        h1 {{
            text-align: center;
            margin-top: 30px;
            font-size: 2.4em;
            color: #0077b6;
        }}
        .container {{
            display: flex;
            padding: 20px 40px;
            gap: 30px;
            flex-wrap: wrap;
            justify-content: center;
        }}
        .box {{
            flex: 1;
            min-width: 200px;
            background: white;
            border-radius: 12px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        .icon {{
            font-size: 36px;
            margin-bottom: 10px;
        }}
        .box h2 {{
            color: #0077b6;
            font-size: 1.2em;
            margin-bottom: 12px;
        }}
        .value {{
            font-size: 2em;
            font-weight: bold;
        }}
        .label {{
            font-size: 0.95em;
            color: #555;
        }}
        footer {{
            margin-top: auto;
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }}
        footer a {{
            color: #ffeb3b;
            text-decoration: underline;
        }}
        footer a:hover {{
            color: #ffffff;
        }}
    </style>
</head>
<body>

<header>
    <img src="rmit.png" alt="RMIT Logo">
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/page2a">Shallow Glance A</a></li>
        <li><a href="/page3a">Deep-dive A</a></li>
        <li><a href="/page1b">About Us</a></li>
        <li><a href="/page2b">Climate Metric</a></li>
        <li><a href="/page3b">Exploring Climate</a></li>
        <li><a href="/help">HELP</a></li>
    </ul>
</header>

<h1>Weather Data Summary</h1>

<div class="container">
    <div class="box">
        <div class="icon">📅</div>
        <h2>YEAR RANGE</h2>
        <p class="value">{min_year}–{max_year}</p>
    </div>
    <div class="box">
        <div class="icon">🌡️</div>
        <h2>LOWEST TEMPERATURE</h2>
        <p class="value">{lowest_temp}°C</p>
        <p class="label">({coldest_station}, {coldest_state})</p>
    </div>
    <div class="box">
        <div class="icon">🌧️</div>
        <h2>HIGHEST RAINFALL</h2>
        <p class="value">{highest_rain} mm</p>
        <p class="label">({rainiest_station}, {rainiest_state})</p>
    </div>
    <div class="box">
        <div class="icon">📍</div>
        <h2>MOST WEATHER STATIONS</h2>
        <p class="value">{most_state}</p>
        <p class="label">({most_count} stations)</p>
    </div>
</div>

<footer>
    <p>FAQ: For more information, please contact support or visit our <a href="/faq">FAQ page</a>.</p>
</footer>

</body>
</html>
"""