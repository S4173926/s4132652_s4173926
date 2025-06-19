import pyhtml
import datetime

def get_page_html(form_data):
    filtered_data = []
    sum_month = form_data.get('sum_month')
    if sum_month is None:
        sum_month = "__"
    else:
        sum_month = sum_month[0]
    sum_year = form_data.get('sum_year')
    if sum_year is None:
        sum_year = "1970"
    else:
        sum_year = sum_year[0]
    state1 = form_data.get('A.A.T.')
    if state1 is None:
         pass
    else:
         state1 = state1[0]
    state2 = form_data.get('A.E.T.')
    if state2 is None:
         pass
    else:
         state2 = state2[0]
    state3 = form_data.get('N.S.W.')
    if state3 is None:
         pass
    else:
         state3 = state3[0]
    state4 = form_data.get('N.T.')
    if state4 is None:
         pass
    else:
         state4 = state4[0]
    state5 = form_data.get('QLD')
    if state5 is None:
         pass
    else:
         state5 = state5[0]
    state6 = form_data.get('S.A.')
    if state6 is None:
         pass
    else:
         state6 = state6[0]
    state7 = form_data.get('TAS')
    if state7 is None:
         pass
    else:
         state7 = state7[0]
    state8 = form_data.get('VIC')
    if state8 is None:
         pass
    else:
         state8 = state8[0]
    state9 = form_data.get('W.A.')
    if state9 is None:
         pass
    else:
         state9 = state9[0]
    state_list = [state1, state2, state3, state4, state5,
                  state6, state7, state8, state9]
    sum_metric = form_data.get('weather_Metric_sum')
    if sum_metric is None:
        sum_metric = "Precipitation"
    else:
         sum_metric = sum_metric[0]
    station_id = form_data.get('station_min')
    if station_id is None:
        station_id = "1000" 
    else:
         station_id = station_id[0]
    station_id_max = form_data.get('station_max')
    if station_id_max is None:
        station_id_max = "2000"
    else:
         station_id_max = station_id_max[0]
    date_min = form_data.get('datemin')
    if date_min is None:
        date_min = "1970-01-01"
    else:
         date_min = date_min[0]
    date_max = form_data.get('datemax')
    if date_max is None:
        date_max = "1970-01-02"
    else:
         date_max = date_max[0]
    weather_metric = form_data.get('weather_Metric')
    if weather_metric is None:
        weather_metric = "Precipitation"
    else:
         weather_metric = weather_metric[0]
    start_date = datetime.datetime.strptime(date_min, "%Y-%m-%d")
    start_date = start_date.date()
    end_date = datetime.datetime.strptime(date_max, "%Y-%m-%d")
    end_date = end_date.date()
    state_list = [state for state in state_list if state is not None]
    if state_list == []:
        state_list = ["W.A."]
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
            <li><a href="/page3b">Exploring Climate</a></li>
        </ul>
        </header>
        <div class="container">
            <aside class="sidebar">
                <h3>Search Climate Metric</h3>

                <form action="/page2b" method="GET">

                <label>Station ID(1000~300010):</label>
                <input type="text" name="station_min" min="1000" max="300010" placeholder="1000">
                <input type="text" name="station_max" min="1000" max="300010" placeholder="300010">

                <label>Date(01/01/1970~31/12/2020):</label>
                <input type="date" name="datemin" min="1970-01-01" max="2020-12-31" placeholder="{date_min}">
                <input type="date" name="datemax" min="1970-01-01" max="2020-12-31" placeholder="{date_max}">

                <label>Metric:</label>
                <select name="weather_Metric" id="weather-attributes">
                    <option value="Precipitation">Precipitation</option>
                    <option value="RainDaysNum">RainDaysNum</option>
                    <option value="Evaporation">Evaporation</option>
                    <option value="EvapDaysNum">EvapDaysNum</option>
                    <option value="MaxTemp">MaxTemp</option>
                    <option value="MinTemp">MinTemp</option>
                    <option value="MinTempDays">MinTempDays</option>
                    <option value="Humid00">Humid00</option>
                    <option value="Humid03">Humid03</option>
                    <option value="Humid06">Humid06</option>
                    <option value="Humid09">Humid09</option>
                    <option value="Humid12">Humid12</option>
                    <option value="Humid15">Humid15</option>
                    <option value="Humid18">Humid18</option>
                    <option value="Humid21">Humid21</option>
                    <option value="Sunshine">Sunshine</option>
                    <option value="Okta00">Okta00</option>
                    <option value="Okta03">Okta03</option>
                    <option value="Okta06">Okta06</option>
                    <option value="Okta09">Okta09</option>
                    <option value="Okta12">Okta12</option>
                    <option value="Okta15">Okta15</option>
                    <option value="Okta18">Okta18</option>
                    <option value="Okta21">Okta21</option>
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
    searching = f"select location, DMY, {weather_metric} from weather_data where location >= {station_id} and location <= {station_id_max} and trim({weather_metric}) != '' and {weather_metric} is not null;"
    data = pyhtml.get_results_from_query("climate.db", searching)
    for row in data:
                date_in_range = row[1]
                date_in_range = date_in_range.split('/')
                date_in_range.reverse()
                date_in_range = '-'.join(date_in_range)
                date_in_range = datetime.datetime.strptime(date_in_range, "%Y-%m-%d")
                date_in_range = date_in_range.date()
                if start_date <= date_in_range <= end_date:
                    filtered_data.append(row)
    token = {}
    for row in filtered_data:
        if row[0] not in token:
            token[row[0]] = []
        token[row[0]].append(row)
        

    #filtered_data.sort(key=lambda x: datetime.datetime.strptime(x[1], "%d/%m/%Y"))
    for key, rows in token.items():
        rows.sort(key=lambda x: datetime.datetime.strptime(x[1], "%d/%m/%Y"))
        for row in rows:
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
        <div class="container">
            <aside class="sidebar">
                <h3>Summarise the data</h3>

                <form action="/page2b" method="GET">
                <label>States:</label>
                <label for="A.A.T."> A.A.T.</label>
                <input type="checkbox" name="A.A.T." value="A.A.T.">
                <label for="A.E.T."> A.E.T.</label> 
                <input type="checkbox" name="A.E.T." value="A.E.T.">
                <label for="N.S.W."> N.S.W.</label>
                <input type="checkbox" name="N.S.W." value="N.S.W.">
                <label for="N.T."> N.T.</label>
                <input type="checkbox" name="N.T." value="N.T.">
                <label for="QLD"> QLD</label>
                <input type="checkbox" name="QLD" value="QLD">
                <label for="S.A."> S.A.</label>
                <input type="checkbox" name="S.A." value="S.A.">
                <label for="TAS"> TAS</label>
                <input type="checkbox" name="TAS" value="TAS">
                <label for="VIC"> VIC</label>
                <input type="checkbox" name="VIC" value="VIC">
                <label for="W.A."> W.A.</label>
                <input type="checkbox" name="W.A." value="W.A.">
                <label>Metric:</label>
                <select name="weather_Metric_sum" id="weather-attributes">
                    <option value="Precipitation">Precipitation</option>
                    <option value="RainDaysNum">RainDaysNum</option>
                    <option value="Evaporation">Evaporation</option>
                    <option value="EvapDaysNum">EvapDaysNum</option>
                    <option value="Sunshine">Sunshine</option>
                    <option value="Okta00">Okta00</option>
                    <option value="Okta03">Okta03</option>
                    <option value="Okta06">Okta06</option>
                    <option value="Okta09">Okta09</option>
                    <option value="Okta12">Okta12</option>
                    <option value="Okta15">Okta15</option>
                    <option value="Okta18">Okta18</option>
                    <option value="Okta21">Okta21</option>
                </select>
                <label>Year(1970-2020):</label>
                <input type="number" name="sum_year" min="1970" max="2020" placeholder="1970">
                <label>Month:</label>
                <select name="sum_month">
                    <option value="__">All</option>
                    <option value="01">January</option>
                    <option value="02">February</option>
                    <option value="03">March</option>
                    <option value="04">April</option>
                    <option value="05">May</option>
                    <option value="06">June</option>
                    <option value="07">July</option>
                    <option value="08">August</option>
                    <option value="09">September</option>
                    <option value="10">October</option>
                    <option value="11">November</option>
                    <option value="12">December</option>
                </select>
                <button>Apply</button>
                </form>
            </aside>
            <main class="main">
            <table>
                <tr>
                    <th>State</th>
                    <th>{sum_metric} Total</th>
                </tr>"""
    state_list = ", ".join(f"'{state}'" for state in state_list if state is not None)
    sum_result = f"select s.name,sum(wd.{sum_metric}) from state s join weather_station ws on s.id = ws.state_id join weather_data wd on ws.site_id = wd.location where wd.dmy like '%/{sum_month}/{sum_year}' and s.name in ({state_list}) group by s.name;"
    total_data = pyhtml.get_results_from_query("climate.db", sum_result)
    for row in total_data:
        page_html += f"""
                <tr>
                    <td>{row[0]}</td>
                    <td>{row[1]}</td>
                </tr>\n"""
    page_html += """
            </table>
            </main>
        </div>
    </body>
    </html>
    """
    return page_html
