from pyhtml import get_results_from_query

def get_page_html(form_data):
    # Step 1: Get user input
    state = form_data.get("state", ["Western Australia"])[0]
    metric = form_data.get("metric", ["MaxTemp"])[0]
    lat_start = float(form_data.get("lat_start", ["-18.0"])[0])
    lat_end = float(form_data.get("lat_end", ["-16.0"])[0])

    # Step 2: Get station data
    station_rows = get_results_from_query(
        "climate.db",
        f"""
        SELECT ws.name, r.name AS region, ws.latitude
        FROM weather_station ws
        JOIN state s ON ws.state_id = s.id
        JOIN region r ON ws.region_id = r.id
        WHERE s.name = '{state}' AND ws.latitude BETWEEN {lat_start} AND {lat_end};
        """
    )

    # Step 3: Get summary data
    summary_rows = get_results_from_query(
        "climate.db",
        f"""
        SELECT r.name AS region,
               COUNT(DISTINCT ws.site_id) AS count,
               ROUND(AVG(CAST(wd."{metric}" AS FLOAT)), 1) AS avg_temp
        FROM weather_station ws
        JOIN state s ON ws.state_id = s.id
        JOIN region r ON ws.region_id = r.id
        JOIN weather_data wd ON wd.location = ws.site_id AND wd."{metric}" IS NOT NULL
        WHERE s.name = '{state}' AND ws.latitude BETWEEN {lat_start} AND {lat_end}
        GROUP BY r.name;
        """
    )

    # Step 4: Build state dropdown
    state_rows = get_results_from_query("climate.db", "SELECT name FROM state ORDER BY name;")
    state_dropdown_html = "\n".join(
        f'<option value="{row[0]}" {"selected" if row[0] == state else ""}>{row[0]}</option>'
        for row in state_rows
    )

    # Step 5: Build metric dropdown
    metric_columns = [
        "MaxTemp", "MinTemp", "Precipitation", "Evaporation", "Sunshine",
        "Humid00", "Humid03", "Humid06", "Humid09", "Humid12", "Humid15", "Humid18", "Humid21",
        "Okta00", "Okta03", "Okta06", "Okta09", "Okta12", "Okta15", "Okta18"
    ]
    metric_dropdown_html = "\n".join(
        f'<option value="{m}" {"selected" if metric == m else ""}>{m}</option>'
        for m in metric_columns
    )

    # Step 6: Build tables
    station_table = "\n".join(
        f"<tr><td>{name}</td><td>{region}</td><td>{lat}</td></tr>"
        for name, region, lat in station_rows
    ) or "<tr><td colspan='3'>No matching stations found</td></tr>"

    summary_table = "\n".join(
        f"<tr><td>{region}</td><td>{count}</td><td>{avg_temp}</td></tr>"
        for region, count, avg_temp in summary_rows
    ) or "<tr><td colspan='3'>No summary available</td></tr>"

    return f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Focused View of Climate Change</title>
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
        .filters {{
            width: 85%;
            margin: 0 auto 30px auto;
            padding: 25px;
            border-radius: 12px;
            background: #f1f9ff;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
        }}
        .filters div {{
            display: flex;
            flex-direction: column;
            min-width: 180px;
        }}
        .filters label {{
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .filters select, .filters input {{
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }}
        .filters button {{
            margin-top: auto;
            padding: 10px 20px;
            background: #0077b6;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
        }}
        table {{
            width: 85%;
            margin: 20px auto;
            border-collapse: collapse;
            background: #ffffff;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }}
        th, td {{
            padding: 12px;
            border-bottom: 1px solid #ccc;
            text-align: left;
        }}
        th {{ background-color: #e0f3ff; color: #003f63; }}
        .region-header {{
            background-color: #e0f3ff;
            color: #003f63;
            padding: 10px 20px;
            width: 85%;
            margin: 0 auto;
            font-weight: bold;
            border-radius: 6px 6px 0 0;
        }}
        footer {{
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            margin-top: auto;
        }}
        footer a {{ color: #ffeb3b; text-decoration: underline; }}
    </style>
</head>
<body>

<header>
    <img src='rmit.png' alt='RMIT Logo'>
    <ul>
        <li><a href='/'>Page 1A</a></li>
        <li><a href='/page2a'>Page 2A</a></li>
        <li><a href='/page3a'>Page 3A</a></li>
        <li><a href='/page1b'>Page 1B</a></li>
        <li><a href='/page2b'>Page 2B</a></li>
        <li><a href='/page3b'>Page 3B</a></li>
        <li><a href='/help'>HELP</a></li>
    </ul>
</header>

<h1>Focused View of Climate Change by Weather Station</h1>

<form method='get' action='/page2a'>
<div class='filters'>
    <div>
        <label for='state'>State:</label>
        <select name='state'>
            {state_dropdown_html}
        </select>
    </div>
    <div>
        <label>Start Latitude:</label>
        <input type='text' name='lat_start' value='{lat_start}'>
    </div>
    <div>
        <label>End Latitude:</label>
        <input type='text' name='lat_end' value='{lat_end}'>
    </div>
    <div>
        <label>Climate Metric:</label>
        <select name='metric'>
            {metric_dropdown_html}
        </select>
    </div>
    <div>
        <button type='submit'>Filter</button>
    </div>
</div>
</form>

<div class='region-header'>{state}</div>
<table>
    <thead>
        <tr><th>Site Name</th><th>Region</th><th>Latitude</th></tr>
    </thead>
    <tbody>{station_table}</tbody>
</table>

<div class='region-header'>{state}</div>
<table>
    <thead>
        <tr><th>Region</th><th>Number Weather Stations</th><th>Average {metric}</th></tr>
    </thead>
    <tbody>{summary_table}</tbody>
</table>

<footer>
    <p>FAQ: For more info visit our <a href='/faq'>FAQ Page</a>.</p>
</footer>

</body>
</html>
"""