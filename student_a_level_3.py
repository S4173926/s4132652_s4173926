def get_page_html(form_data):
    page_html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Identify Similar Weather Stations</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to bottom, #005b96, #003f63);
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
                color: white;
            }
            header {
                background: white;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }
            header img {
                height: 50px;
            }
            nav {
                display: flex;
                gap: 15px;
            }
            nav a {
                color: #004080;
                font-weight: bold;
                text-decoration: none;
            }
            h1 {
                text-align: center;
                margin: 40px 0 25px;
                font-size: 2.1em;
                color: #003366;
            }
            .filters {
                background-color: rgba(255,255,255,0.1);
                width: 85%;
                margin: 0 auto 30px auto;
                padding: 25px;
                border-radius: 16px;
                display: flex;
                justify-content: space-between;
                gap: 15px;
                flex-wrap: wrap;
            }
            .filters div {
                display: flex;
                flex-direction: column;
                min-width: 180px;
            }
            .filters label {
                font-weight: bold;
                margin-bottom: 5px;
                color: #ffffff;
            }
            .filters select, .filters input {
                padding: 10px;
                border-radius: 8px;
                border: none;
                background: #e0efff;
                color: #002244;
                font-weight: bold;
            }
            .filters button {
                margin-top: 22px;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                background-color: #0077cc;
                color: white;
                font-weight: bold;
                cursor: pointer;
            }
            table {
                width: 85%;
                margin: 0 auto 40px auto;
                border-collapse: collapse;
                border-radius: 12px;
                overflow: hidden;
                background: rgba(255,255,255,0.1);
                backdrop-filter: blur(4px);
            }
            thead {
                background-color: rgba(255,255,255,0.2);
            }
            th, td {
                padding: 14px 12px;
                text-align: left;
                color: #ffffff;
            }
            tbody tr:nth-child(even) td {
                background-color: rgba(255,255,255,0.08);
            }
            footer {
                margin-top: auto;
                background-color: #f0f8ff;
                text-align: center;
                padding: 20px;
                font-size: 0.9em;
                color: #333;
                border-top: 1px solid #ccc;
            }
        </style>
    </head>
    <body>

        <header>
            <img src="rmit.png" alt="RMIT Logo">
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
                    <td>Melbourne Airport (selected)</td>
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
                    <td>0.29%</td>
                </tr>
            </tbody>
        </table>

        <footer>
            <p>FAQ: For more info visit our <a href="/faq">FAQ Page</a>.</p>
        </footer>

    </body>
    </html>
    """
    return page_html