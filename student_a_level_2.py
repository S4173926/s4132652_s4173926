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
    metric_labels = {
    "MaxTemp": "Maximum Temperature (°C)",
    "MinTemp": "Minimum Temperature (°C)",
    "Precipitation": "Precipitation (mm)",
    "Evaporation": "Evaporation (mm)",
    "Sunshine": "Sunshine (hours)",
    "Humid00": "Humidity at 00:00 (%)", "Humid03": "Humidity at 03:00 (%)",
    "Humid06": "Humidity at 06:00 (%)", "Humid09": "Humidity at 09:00 (%)",
    "Humid12": "Humidity at 12:00 (%)", "Humid15": "Humidity at 15:00 (%)",
    "Humid18": "Humidity at 18:00 (%)", "Humid21": "Humidity at 21:00 (%)",
    "Okta00": "Cloud Cover at 00:00 (oktas)", "Okta03": "Cloud Cover at 03:00 (oktas)",
    "Okta06": "Cloud Cover at 06:00 (oktas)", "Okta09": "Cloud Cover at 09:00 (oktas)",
    "Okta12": "Cloud Cover at 12:00 (oktas)", "Okta15": "Cloud Cover at 15:00 (oktas)",
    "Okta18": "Cloud Cover at 18:00 (oktas)"
    }
    metric_dropdown_html = "\n".join(
        f'<option value="{m}" {"selected" if metric == m else ""}>{metric_labels.get(m, m)}</option>'
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

    # Final HTML
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Focused View of Climate Change</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #005b96, #003f63);
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            color: white;
        }}
        header {{
            background: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}
        header img {{ height: 50px; }}
        nav {{ display: flex; gap: 15px; }}
        nav a {{ color: #004080; font-weight: bold; text-decoration: none; }}
        h1 {{
            text-align: center;
            margin: 40px 0 25px;
            font-size: 2.1em;
        }}
        .filters {{
            background-color: rgba(255,255,255,0.1);
            width: 85%;
            margin: 0 auto 30px auto;
            padding: 25px;
            border-radius: 16px;
            display: flex;
            justify-content: space-between;
            gap: 15px;
            flex-wrap: wrap;
        }}
        .filters div {{
            display: flex;
            flex-direction: column;
            min-width: 180px;
        }}
        .filters label {{
            font-weight: bold;
            margin-bottom: 5px;
            color: white;
        }}
        .filters select, .filters input {{
            padding: 10px;
            border-radius: 8px;
            border: none;
            background: #e0efff;
            color: #002244;
            font-weight: bold;
        }}
        .filters button {{
            margin-top: auto;
            padding: 10px 20px;
            font-weight: bold;
            background: #004080;
            color: white;
            border: none;
            border-radius: 8px;
        }}
        table {{
            width: 85%;
            margin: 20px auto;
            border-collapse: collapse;
            border-radius: 12px;
            overflow: hidden;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(4px);
        }}
        thead {{ background-color: rgba(255,255,255,0.2); }}
        th, td {{
            padding: 14px 12px;
            text-align: left;
            color: white;
        }}
        tbody tr:nth-child(even) td {{
            background-color: rgba(255,255,255,0.08);
        }}
        .region-header {{
            background-color: rgba(255,255,255,0.2);
            color: white;
            padding: 10px 20px;
            width: 85%;
            margin: 0 auto;
            font-weight: bold;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
        }}
        footer {{
            margin-top: auto;
            background-color: #f0f8ff;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            color: #333;
            border-top: 1px solid #ccc;
        }}
    </style>
</head>
<body>

    <header>
        <img src="images/rmit.png" alt="RMIT Logo">
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

    <h1>Focused View of Climate Change by Weather Station</h1>

    <form method="get" action="/page2a">
    <div class="filters">
        <div>
            <label for="state">State:</label>
            <select name="state">
                {state_dropdown_html}
            </select>
        </div>
        <div>
            <label>Start Latitude:</label>
            <input type="text" name="lat_start" value="{lat_start}">
        </div>
        <div>
            <label>End Latitude:</label>
            <input type="text" name="lat_end" value="{lat_end}">
        </div>
        <div>
            <label>Climate Metric:</label>
            <select name="metric">
                {metric_dropdown_html}
            </select>
        </div>
        <div>
            <button type="submit">Filter</button>
        </div>
    </div>
    </form>

    <div class="region-header">{state}</div>
    <table>
        <thead>
            <tr><th>Site Name</th><th>Region</th><th>Latitude</th></tr>
        </thead>
        <tbody>{station_table}</tbody>
    </table>

    <div class="region-header">{state}</div>
    <table>
        <thead>
            <tr><th>Region</th><th>Number Weather Stations</th><th>Average {metric}</th></tr>
        </thead>
        <tbody>{summary_table}</tbody>
    </table>

    <footer>
        <p>FAQ: For more info visit our <a href="/faq">FAQ Page</a>.</p>
    </footer>

</body>
</html>
"""