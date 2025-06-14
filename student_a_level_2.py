def get_page_html(form_data):
    page_html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Focused View of Climate Change</title>
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
                color: #ffffff;
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
                color: white;
            }
            .filters select, .filters input {
                padding: 10px;
                border-radius: 8px;
                border: none;
                background: #e0efff;
                color: #002244;
                font-weight: bold;
            }
            table {
                width: 85%;
                margin: 20px auto;
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
                color: white;
            }
            tbody tr:nth-child(even) td {
                background-color: rgba(255,255,255,0.08);
            }
            .region-header {
                background-color: rgba(255,255,255,0.2);
                color: white;
                padding: 10px 20px;
                width: 85%;
                margin: 0 auto;
                font-weight: bold;
                border-top-left-radius: 12px;
                border-top-right-radius: 12px;
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

        <div class="filters">
            <div>
                <label>State:</label>
                <select><option>Western Australia</option></select>
            </div>
            <div>
                <label>Start Latitude:</label>
                <input type="text" value={start_lat}>
            </div>
            <div>
                <label>End Latitude:</label>
                <input type="text" value="-17.00">
            </div>
            <div>
                <label>Climate Metric:</label>
                <select><option>Maximum Temp</option></select>
            </div>
        </div>

        <div class="region-header">Western Australia</div>
        <table>
            <thead>
                <tr>
                    <th>Site Name</th>
                    <th>Region</th>
                    <th>Latitude</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Broome Airport</td>
                    <td>Broome</td>
                    <td>-17.95</td>
                </tr>
                <tr>
                    <td>Derby Aero</td>
                    <td>Derby West Kimberley</td>
                    <td>-17.37</td>
                </tr>
            </tbody>
        </table>

        <div class="region-header">Western Australia</div>
        <table>
            <thead>
                <tr>
                    <th>Region</th>
                    <th>Number Weather Stations</th>
                    <th>Average Max Temperature</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Broome</td>
                    <td>2</td>
                    <td>27.2</td>
                </tr>
                <tr>
                    <td>Derby West Kimberley</td>
                    <td>1</td>
                    <td>23.1</td>
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