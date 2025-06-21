def get_page_html(form_data):
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Deep Dive A - Identify Similar Weather Stations</title>
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #333;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        header {
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            padding: 12px 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        header img {
            height: 45px;
        }
        nav ul {
            list-style: none;
            display: flex;
            margin: 0;
            padding: 0;
        }
        nav li {
            margin: 0 10px;
        }
        nav a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            padding: 6px 10px;
            border-radius: 6px;
        }
        nav a:hover {
            background-color: rgba(255, 255, 255, 0.2);
        }
        h1 {
            text-align: center;
            margin: 30px 0 10px;
            font-size: 2em;
            color: #005b96;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .form-box {
            flex: 1 1 300px;
            background-color: #eaf6fc;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
        }
        .form-box label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
        }
        .form-box select, .form-box input {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        .form-box button {
            width: 100%;
            background-color: #0077b6;
            color: white;
            padding: 12px;
            border: none;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
        }
        .form-box button:hover {
            background-color: #005b96;
        }
        .table-box {
            flex: 1 1 600px;
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        th, td {
            padding: 12px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #e0f3ff;
            color: #003f63;
        }
        td strong {
            color: #0077b6;
        }
        footer {
            margin-top: auto;
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.95em;
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
    <nav>
        <ul>
            <li><a href="/">Page 1A</a></li>
            <li><a href="/page2a">Page 2A</a></li>
            <li><a href="/page3a">Page 3A</a></li>
            <li><a href="/page1b">Page 1B</a></li>
            <li><a href="/page2b">Page 2B</a></li>
            <li><a href="/page3b">Page 3B</a></li>
            <li><a href="/help">HELP</a></li>
        </ul>
    </nav>
</header>

<h1>Identify Similar Weather Stations</h1>

<div class="container">

    <div class="form-box">
        <label>Time Periods</label>
        <select>
            <option>2005 to 2015</option>
        </select>

        <label>Reference Station</label>
        <select>
            <option>Melbourne Airport</option>
        </select>

        <label>Number of Stations</label>
        <input type="number" value="2">

        <button>FIND</button>
    </div>

    <div class="table-box">
        <table>
            <thead>
                <tr>
                    <th>Weather Station</th>
                    <th>Avg Temp (2005–2009)</th>
                    <th>Avg Temp (2010–2015)</th>
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
                    <td>16.9 °C</td>
                    <td>17.0 °C</td>
                    <td>+0.29%</td>
                </tr>
            </tbody>
        </table>
    </div>

</div>

<footer>
    <p>FAQ: For more info visit our <a href="/faq">FAQ Page</a>.</p>
</footer>

</body>
</html>"""