def get_page_html(form_data):
    page_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Database Web-App Demo</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            background-color: #e3f2fd;
            color: #333;
        }

        header {
            background-color: #1565c0;
            padding: 10px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .logo {
            height: 50px;
        }

        .nav-links {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            font-size: 1rem;
        }

        .nav-links a:hover {
            text-decoration: underline;
        }

        h1 {
            text-align: center;
            margin: 30px 0 10px 0;
            color: #0d47a1;
        }

        .weather-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin: 10px 20px 30px 20px;
            padding: 10px;
        }

        .weather-box {
            flex: 1;
            min-width: 200px;
            margin: 10px;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            color: #333;
        }

        .year { background-color: #bbdefb; }
        .temp { background-color: #ffe082; }
        .rain { background-color: #f8bbd0; }
        .stations { background-color: #c8e6c9; }

        .weather-box h2 {
            margin-top: 0;
            font-size: 1.1rem;
        }

        .weather-box p {
            font-size: 1.5rem;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <header>
        <img src="images/rmit.png" alt="RMIT Logo" class="logo">
        <div class="nav-links">
            <a href="/">Page 1A</a>
            <a href="/page2a">Page 2A</a>
            <a href="/page3a">Page 3A</a>
            <a href="/page1b">Page 1B</a>
            <a href="/page2b">Page 2B</a>
            <a href="/page3b">Page 3B</a>
        </div>
    </header>

    <h1>WEATHER DATA</h1>

    <div class="weather-container">
        <div class="weather-box year">
            <h2>YEAR RANGE</h2>
            <p>2000–2023</p>
        </div>
        <div class="weather-box temp">
            <h2>LOWEST TEMPERATURE</h2>
            <p>–45.6°C</p>
        </div>
        <div class="weather-box rain">
            <h2>HIGHEST RAINFALL</h2>
            <p>480.2 mm</p>
        </div>
        <div class="weather-box stations">
            <h2>MOST WEATHER STATIONS</h2>
            <p>Northwest</p>
        </div>
    </div>
</body>
</html>
"""
    return page_html