def get_page_html(form_data):
    print("Rendering Level 2A layout...")

    page_html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Focused Climate View</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to bottom, #F9D47A, #F7B547);
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }
            header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 20px;
                background: white;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            nav a {
                margin-left: 15px;
                text-decoration: none;
                font-weight: bold;
                color: #004080;
            }
            h1 {
                text-align: center;
                color: #003366;
                margin: 40px 0 20px;
                font-size: 1.9em;
            }
            .filters {
                background-color: #FFF8E4;
                width: 85%;
                margin: 0 auto 30px auto;
                padding: 20px;
                border-radius: 16px;
                display: flex;
                justify-content: space-between;
                gap: 15px;
                flex-wrap: wrap;
            }
            .filters div {
                display: flex;
                flex-direction: column;
            }
            .filters label {
                font-weight: bold;
                margin-bottom: 5px;
            }
            .filters select, .filters input {
                padding: 8px;
                border-radius: 8px;
                border: 1px solid #ccc;
                min-width: 150px;
            }
            table {
                width: 85%;
                margin: 20px auto;
                border-collapse: collapse;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            thead {
                background-color: #004643;
                color: white;
            }
            th, td {
                padding: 12px;
                text-align: left;
            }
            tbody tr:nth-child(even) td {
                background-color: #FFFBEF;
            }
            .region-header {
                background-color: #004643;
                color: white;
                padding: 10px;
                font-weight: bold;
            }
            footer {
                text-align: center;
                background-color: #f0f8ff;
                padding: 20px;
                font-size: 0.9em;
                color: #333;
                border-top: 1px solid #ccc;
                margin-top: auto;
            }
        </style>
    </head>
    <body>

        <header>
            <img src="images/rmit.png" height="50" alt="RMIT Logo">
            <nav>
                <a href="/page1a">Page 1A</a>
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
                <input type="text" value="-20.00">
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