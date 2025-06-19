def get_page_html(form_data):
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Identify Similar Weather Stations</title>
    <style>
        html, body {
            height: 100%;
            margin: 0;
            display: flex;
            flex-direction: column;
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #333;
        }
        header {
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            height: 12vh;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
        }
        header img {
            height: 40px;
        }
        header ul {
            list-style: none;
            display: flex;
            margin: 0;
            padding: 0;
        }
        header li {
            margin: 0 10px;
        }
        header a {
            color: white;
            text-decoration: none;
            font-weight: 600;
        }
        header a:hover {
            text-decoration: underline;
        }
        h1 {
            text-align: center;
            margin: 30px 0 20px;
            font-size: 2.4em;
            color: #0077b6;
        }
        .filters {
            width: 85%;
            margin: 0 auto 30px auto;
            padding: 25px;
            border-radius: 12px;
            background: #f1f9ff;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
        }
        .filters div {
            display: flex;
            flex-direction: column;
            min-width: 180px;
        }
        .filters label {
            font-weight: bold;
            margin-bottom: 5px;
        }
        .filters select, .filters input {
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        .filters button {
            margin-top: auto;
            padding: 10px 20px;
            background: #0077b6;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }
        table {
            width: 85%;
            margin: 0 auto 40px auto;
            border-collapse: collapse;
            background: #ffffff;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
        th, td {
            padding: 12px;
            border-bottom: 1px solid #ccc;
            text-align: left;
        }
        th {
            background-color: #e0f3ff;
            color: #003f63;
        }
        footer {
            margin-top: auto;
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }
        footer a {
            color: #ffeb3b;
            text-decoration: underline;
        }
        footer a:hover {
            color: #ffffff;
        }
    </style>
</head>
<body>

<header>
    <img src="rmit.png" alt="RMIT Logo">
    <ul>
        <li><a href="/">Page 1A</a></li>
        <li><a href="/page2a">Page 2A</a></li>
        <li><a href="/page3a">Page 3A</a></li>
        <li><a href="/page1b">Page 1B</a></li>
        <li><a href="/page2b">Page 2B</a></li>
        <li><a href="/page3b">Page 3B</a></li>
        <li><a href="/help">HELP</a></li>
    </ul>
</header>

<h1>Identify Similar Weather Stations</h1>

<div class="filters">
    <div>
        <label>Time Periods</label>
        <select><option>2005 to 2015</option></select>
    </div>
    <div>
        <label>Reference Station</label>
        <select><option>Melbourne Airport</option></select>
    </div>
    <div>
        <label>Number of Stations</label>
        <input type="number" value="2">
    </div>
    <div>
        <label>&nbsp;</label>
        <button>FIND</button>
    </div>
</div>

<table>
    <thead>
        <tr>
            <th>Weather Station</th>
            <th>Average Temp (2005–2009)</th>
            <th>Average Temp (2010–2015)</th>
            <th>% Change</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Melbourne Airport (selected)</strong></td>
            <td>22.5 °C</td>
            <td>22.7 °C</td>
            <td>+0.38%</td>
        </tr>
        <tr>
            <td>Ballarat</td>
            <td>17.2 °C</td>
            <td>17.6 °C</td>
            <td>+0.23%</td>
        </tr>
        <tr>
            <td>Bendigo</td>
            <td>16.9°C</td>
            <td>17.0°C</td>
            <td>+0.29%</td>
        </tr>
    </tbody>
</table>

<footer>
    <p>FAQ: For more info visit our <a href="/faq">FAQ Page</a>.</p>
</footer>

</body>
</html>"""