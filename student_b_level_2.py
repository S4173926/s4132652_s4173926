import pyhtml

def get_page_html(form_data):
    station_id = form_data.get('station_min')
    if station_id is None:
        station_id = "1000" 
    station_id_max = form_data.get('station_max')
    if station_id_max is None:
        station_id_max = "300010"
    date_min = form_data.get('datemin')
    if date_min is None:
        date_min = "1970-01-01"
    date_max = form_data.get('datemax')
    if date_max is None:
        date_max = "1970-01-02"
    weather_metric = form_data.get('weather_Metric')
    if weather_metric is None:
        weather_metric = "Precipitation"
    print("Station ID range:", station_id, "to", station_id_max, 
          "Date range:", date_min, "to", date_max, 
          "Weather Metric:", weather_metric)
    page_html=f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Climate Metric</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
        <a href="/"><img src="rmit.png" alt="Logo"></a>
        <ul>
            <li><a href="/page2a">Page 2A</a></li>
            <li><a href="/page3a">Page 3A</a></li>
            <li><a href="/page1b">About Us</a></li>
            <li><a href="/page2b">Climate Metric</a></li>
            <li><a href="/page3b">Page 3B</a></li>
        </ul>
        </header>
        <div class="container">
            <aside class="sidebar">
                <h3>Search Climate Metric</h3>

                <form action="/page2b" method="GET">

                <label>Station ID(1000~300010):</label>
                <input type="text" name="station_min" min="1000" max="300010" value="1000">
                <input type="text" name="station_max" min="1000" max="300010" value="300010">

                <label>Date(01/01/1970~31/12/2020):</label>
                <input type="date" name="datemin" min="1970-01-01" max="2020-12-31" value="1970-01-01">
                <input type="date" name="datemax" min="1970-01-01" max="2020-12-31" value="2020-12-31">

                <label>Metric:</label>
                <select name="weather_Metric" id="weather-attributes">
                    <option value="Precipitation">Precipitation</option>
                    <option value="PrecipQual">PrecipQual</option>
                    <option value="RainDaysNum">RainDaysNum</option>
                    <option value="RainDaysMeasure">RainDaysMeasure</option>
                    <option value="Evaporation">Evaporation</option>
                    <option value="EvapQual">EvapQual</option>
                    <option value="EvayDaysNum">EvayDaysNum</option>
                    <option value="MaxTemp">MaxTemp</option>
                    <option value="MaxTempQual">MaxTempQual</option>
                    <option value="MaxTempDays">MaxTempDays</option>
                    <option value="MinTemp">MinTemp</option>
                    <option value="MinTempQual">MinTempQual</option>
                    <option value="MinTempDays">MinTempDays</option>
                    <option value="Humid00">Humid00</option>
                    <option value="Humid00Qual">Humid00Qual</option>
                    <option value="Humid03">Humid03</option>
                    <option value="Humid03QUal">Humid03QUal</option>
                    <option value="Humid06">Humid06</option>
                    <option value="Humid06Qual">Humid06Qual</option>
                    <option value="Humid09">Humid09</option>
                    <option value="Humid09Qual">Humid09Qual</option>
                    <option value="Humid12">Humid12</option>
                    <option value="Humid12Qual">Humid12Qual</option>
                    <option value="Humid15">Humid15</option>
                    <option value="Humid15Qual">Humid15Qual</option>
                    <option value="Humid18">Humid18</option>
                    <option value="Humid18Qual">Humid18Qual</option>
                    <option value="Humid21">Humid21</option>
                    <option value="Humid21Qual">Humid21Qual</option>
                    <option value="Sunshine">Sunshine</option>
                    <option value="SunshineQual">SunshineQual</option>
                    <option value="Okta00">Okta00</option>
                    <option value="Okta00Qual">Okta00Qual</option>
                    <option value="Okta03">Okta03</option>
                    <option value="Okta03Qual">Okta03Qual</option>
                    <option value="Okta06">Okta06</option>
                    <option value="Okta06Qual">Okta06Qual</option>
                    <option value="Okta09">Okta09</option>
                    <option value="Okta09Qual">Okta09Qual</option>
                    <option value="Okta12">Okta12</option>
                    <option value="Okta12Qual">Okta12Qual</option>
                    <option value="Okta15">Okta15</option>
                    <option value="Okta15Qual">Okta15Qual</option>
                    <option value="Okta18">Okta18</option>
                    <option value="Okta18Qual">Okta18Qual</option>
                    <option value="Okta21">Okta21</option>
                    <option value="Okta21Qual">Okta21Qual</option>
                </select>

                <button>Apply</button>
                </form>
            </aside>

            <main class="main">
            <table>
                <tr>
                    <th>Station ID</th>
                    <th>Date</th>
                    <th>{weather_metric}</th>
                </tr>"""
    searching = f"select location, DMY, {weather_metric} from weather_data where location >= {station_id} and location <= {station_id_max} and DMY >= '{date_min}' and DMY <= '{date_max}';"
    data = pyhtml.get_results_from_query("climate.db", searching)
    for row in data:
                page_html += f"""
                <tr>
                    <td>{row[0]}</td>
                    <td>{row[1]}</td>
                    <td>{row[2]}</td>
                </tr>\n"""
    page_html += f"""
            </table>
            </main>
        </div>
    </body>
    </html>
    """
    return page_html