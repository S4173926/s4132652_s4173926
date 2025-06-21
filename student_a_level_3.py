import sqlite3

def get_station_options():
    conn = sqlite3.connect("climate.db")
    c = conn.cursor()
    c.execute("SELECT DISTINCT name FROM weather_station ORDER BY name ASC")
    stations = [row[0] for row in c.fetchall()]
    conn.close()
    return stations

def get_metric_options():
    return [
        ('MaxTemp', 'Maximum Temperature'),
        ('MinTemp', 'Minimum Temperature'),
        ('Precipitation', 'Precipitation'),
        ('Evaporation', 'Evaporation'),
        ('Sunshine', 'Sunshine')
    ]

def get_page_html(form_data):
    ref_station = form_data.get("ref_station", [""])[0]
    t1_start = form_data.get("t1_start", ["2005"])[0]
    t1_end = form_data.get("t1_end", ["2009"])[0]
    t2_start = form_data.get("t2_start", ["2010"])[0]
    t2_end = form_data.get("t2_end", ["2015"])[0]
    metric = form_data.get("metric", ["MaxTemp"])[0]
    n = form_data.get("n", ["2"])[0]

    try:
        n = int(n)
    except:
        n = 2

    station_options = []
    for station in get_station_options():
        selected = "selected" if station == ref_station else ""
        station_options.append(f'<option value="{station}" {selected}>{station}</option>')

    metric_options_html = []
    for code, label in get_metric_options():
        selected = "selected" if code == metric else ""
        metric_options_html.append(f'<option value="{code}" {selected}>{label}</option>')

    rows_html = "<tr><td colspan='4'>Please submit the form to see results.</td></tr>"
    if ref_station:
        conn = sqlite3.connect("climate.db")
        c = conn.cursor()
        c.execute("SELECT site_id FROM weather_station WHERE name = ?", (ref_station,))
        ref_row = c.fetchone()
        if ref_row:
            ref_id = ref_row[0]
            query = f"""
            WITH t1 AS (
                SELECT location, AVG(CAST([{metric}] AS FLOAT)) AS avg1
                FROM weather_data
                WHERE [{metric}] != '' AND substr(DMY, 7, 4) BETWEEN ? AND ?
                GROUP BY location
            ),
            t2 AS (
                SELECT location, AVG(CAST([{metric}] AS FLOAT)) AS avg2
                FROM weather_data
                WHERE [{metric}] != '' AND substr(DMY, 7, 4) BETWEEN ? AND ?
                GROUP BY location
            ),
            combined AS (
                SELECT ws.name, t1.avg1, t2.avg2
                FROM weather_station ws
                JOIN t1 ON ws.site_id = t1.location
                JOIN t2 ON ws.site_id = t2.location
                WHERE t1.avg1 IS NOT NULL AND t2.avg2 IS NOT NULL
            )
            SELECT name, avg1, avg2 FROM combined
            """
            c.execute(query, (t1_start, t1_end, t2_start, t2_end))
            results = c.fetchall()
            ref_change = None
            station_data = []
            for name, avg1, avg2 in results:
                if avg1 and avg2:
                    change = ((avg2 - avg1) / avg1) * 100
                    if name == ref_station:
                        ref_change = change
                    station_data.append((name, avg1, avg2, change))
            if ref_change is not None:
                station_data.sort(key=lambda x: abs(x[3] - ref_change))
                rows = station_data[:n+1]
                rows_html = ""
                for name, avg1, avg2, change in rows:
                    highlight = "<strong>" if name == ref_station else ""
                    end_tag = "</strong>" if name == ref_station else ""
                    rows_html += f"""
                        <tr>
                            <td>{highlight}{name}{end_tag}</td>
                            <td>{round(avg1, 2)} °C</td>
                            <td>{round(avg2, 2)} °C</td>
                            <td>{round(change, 2)}%</td>
                        </tr>
                    """
        conn.close()

    return f"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Deep Dive A - Identify Similar Weather Stations</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            background-color: #f8f9fa;
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
        header img {{ height: 40px; }}
        header ul {{ list-style: none; display: flex; margin: 0; padding: 0; }}
        header li {{ margin: 0 10px; }}
        header a {{ color: white; text-decoration: none; font-weight: 600; }}
        header a:hover {{ text-decoration: underline; }}
        h1 {{ text-align: center; margin-top: 20px; font-size: 2.5em; color: #0077b6; }}
        .container {{ display: grid; grid-template-columns: 1fr 3fr; gap: 20px; padding: 20px 30px; }}
        .sidebar, .main {{ background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
        .sidebar h3, .main h2 {{ color: #0077b6; }}
        label {{ display: block; margin-top: 10px; font-weight: bold; }}
        input, select {{ width: 100%; padding: 8px; margin-top: 5px; border-radius: 8px; border: 1px solid #ccc; font-size: 14px; }}
        button {{ margin-top: 15px; padding: 10px 20px; background-color: #00b4d8; border: none; color: white; font-weight: bold; border-radius: 8px; cursor: pointer; transition: background-color 0.3s ease; }}
        table {{ font-family: arial, sans-serif; border-collapse: collapse; width: 100%; margin-top: 20px; }}
        td, th {{ border: 1px solid black; text-align: left; padding: 8px; }}
        tr:nth-child(even) {{ background-color: #dddddd; }}
        footer {{
            margin-top: 40px;
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }}
        footer a {{ color: #ffeb3b; text-decoration: underline; }}
    </style>
</head>
<body>
<header>
    <img src='rmit.png' alt='RMIT Logo'>
    <ul>
        <li><a href='/'>Home</a></li>
        <li><a href='/page2a'>Shallow Glance A</a></li>
        <li><a href='/page3a'>Deep-dive A</a></li>
        <li><a href='/page1b'>About Us</a></li>
        <li><a href='/page2b'>Climate Metric</a></li>
        <li><a href='/page3b'>Exploring Climate</a></li>
        <li><a href='/help'>HELP</a></li>
    </ul>
</header>
<h1>Identify Similar Weather Stations</h1>
<div class='container'>
    <div class='sidebar'>
        <form method='get' action='/page3a'>
            <label>Period 1 Start Year</label>
            <input type='number' name='t1_start' value='{t1_start}' required>
            <label>Period 1 End Year</label>
            <input type='number' name='t1_end' value='{t1_end}' required>
            <label>Period 2 Start Year</label>
            <input type='number' name='t2_start' value='{t2_start}' required>
            <label>Period 2 End Year</label>
            <input type='number' name='t2_end' value='{t2_end}' required>
            <label>Reference Station</label>
            <select name='ref_station' required>{''.join(station_options)}</select>
            <label>Climate Metric</label>
            <select name='metric' required>{''.join(metric_options_html)}</select>
            <label>Number of Stations</label>
            <input type='number' name='n' value='{n}' required>
            <button type='submit'>FIND</button>
        </form>
    </div>
    <div class='main'>
        <h2>Similarity Results</h2>
        <table>
            <thead>
                <tr><th>Weather Station</th><th>Avg {metric} ({t1_start}–{t1_end})</th><th>Avg {metric} ({t2_start}–{t2_end})</th><th>% Change</th></tr>
            </thead>
            <tbody>{rows_html}</tbody>
        </table>
    </div>
</div>
<footer>
    <p>FAQ: For more info visit our <a href='/faq'>FAQ Page</a>.</p>
</footer>
</body>
</html>
"""