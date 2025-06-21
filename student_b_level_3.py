import pyhtml
def get_page_html(form_data):
    period = form_data.get("period")
    period = "" if period is None else period[0]
    button_period_next = form_data.get("next")
    button_period_next = "true" if button_period_next is None else button_period_next[0]
    button_back_period = form_data.get("back_period")
    button_back_period = "" if button_back_period is None else button_back_period[0]

    year_range = 0
    year_token = 0
    start_year = form_data.get("start_year")
    start_year = 0 if start_year is None else start_year[0]
    end_year = form_data.get("end_year")
    end_year = 0 if end_year is None else end_year[0]
    years_grouped = form_data.get("years_grouped")
    years_grouped = "" if years_grouped is None else years_grouped[0]
    year_range = int(end_year) - int(start_year)
    if years_grouped == "5" and year_range % 5 != 0 and start_year != 0 and end_year <= 2015:
        end_year += (year_range % 5)
    elif years_grouped == "2" and year_range % 2 != 0 and start_year != 0 and end_year <= 2018:
        end_year += (year_range % 2)
    elif years_grouped == "10" and year_range % 10 != 0 and start_year != 0 and end_year <= 2010:
        end_year += (year_range % 10)
    year_range = int(end_year) - int(start_year)
    if years_grouped == "1":
        year_token = year_range // 1
    elif years_grouped == "2":
        year_token = 2
    elif years_grouped == "5":
        year_token = year_range // 5
    elif years_grouped == "10":
        year_token = year_range // 10
    if year_token %2 == 1:
        year_token -= 1

    month_token = 0
    month_range = 0
    which_year = form_data.get("which_year")
    which_year = 0 if which_year is None else which_year[0]
    start_month = form_data.get("start_month")
    start_month = 0 if start_month is None else start_month[0]
    end_month = form_data.get("end_month")
    end_month = 0 if end_month is None else end_month[0]
    month_grouped = form_data.get("month_grouped")
    month_grouped = 0 if month_grouped is None else month_grouped[0]
    if start_month == "__" or end_month == "__":
        month_range = 12
        start_month = 1
        end_month = 12
    else:
        month_range = int(end_month) - int(start_month)
    if month_grouped == "1":
        month_token = month_range // 1
    elif month_grouped == "2":
        month_token = 2
    elif month_grouped == "3":
        month_token = month_range // 3
    if month_token % 2 == 1:
        month_token -= 1
    
    weather_Metric = form_data.get("weather_Metric")
    weather_Metric = "" if weather_Metric is None else weather_Metric[0]
    compare_Metric_Precipitation = form_data.get("compare_Metric_Precipitation")
    compare_Metric_Precipitation = "" if compare_Metric_Precipitation is None else compare_Metric_Precipitation[0]
    compare_Metric_RainDaysNum = form_data.get("compare_Metric_RainDaysNum")
    compare_Metric_RainDaysNum = "" if compare_Metric_RainDaysNum is None else compare_Metric_RainDaysNum[0]
    compare_Metric_Evaporation = form_data.get("compare_Metric_Evaporation")
    compare_Metric_Evaporation = "" if compare_Metric_Evaporation is None else compare_Metric_Evaporation[0]
    compare_Metric_EvapDaysNum = form_data.get("compare_Metric_EvapDaysNum")
    compare_Metric_EvapDaysNum = "" if compare_Metric_EvapDaysNum is None else compare_Metric_EvapDaysNum[0]
    compare_Metric_Sunshine = form_data.get("compare_Metric_Sunshine")
    compare_Metric_Sunshine = "" if compare_Metric_Sunshine is None else compare_Metric_Sunshine[0]
    compare_Metric_Okta = form_data.get("compare_Metric_Okta")
    compare_Metric_Okta = "" if compare_Metric_Okta is None else compare_Metric_Okta[0]
    compare_Metric_Temp = form_data.get("compare_Metric_Temp")
    compare_Metric_Temp = "" if compare_Metric_Temp is None else compare_Metric_Temp[0]
    metrics_list = [
        compare_Metric_Precipitation,
        compare_Metric_RainDaysNum,
        compare_Metric_Evaporation,
        compare_Metric_EvapDaysNum,
        compare_Metric_Sunshine,
        compare_Metric_Okta,
        compare_Metric_Temp
    ]
    metrics_list = [metric for metric in metrics_list if metric != ""]
    if metrics_list != [] and weather_Metric in metrics_list:
        metrics_list.remove(weather_Metric)
    metrics_list.insert(0, weather_Metric)
    
    print("About to return page 3")

    page_html="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Exploring Climate Metrics Similarities</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
        <a href="/"><img src="rmit.png" alt="Logo"></a>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/page2a">Shallow Glance A</a></li>
            <li><a href="/page3a">Deep-dive A</a></li>
            <li><a href="/page1b">About Us</a></li>
            <li><a href="/page2b">Climate Metric</a></li>
            <li><a href="/page3b">Exploring Climate</a></li>
            <li><a href="/help">HELP</a></li>
        </ul>
        </header>
        <div class="container">
            <aside class="sidebar">
                <h3>Search and Explore Climate Metrics Similarities</h3>

                <form action="/page3b" method="GET">"""
    if button_period_next == "true" or button_back_period == "true":
        page_html += """

                <label>Period:</label>
                <select name="period" value="year">
                    <option value="year">Year</option>
                    <option value="month">Month</option>
                </select>
                <button name="next" value="false">Next</button>"""

    if period == "year":
        page_html += """
                <label>Start Year(1970-2020):</label>
                <input type="number" name="start_year" min="1970" max="2020" placeholder="2005">
                <label>End Year(1970-2020):</label>
                <input type="number" name="end_year" min="1970" max="2020" placeholder="2015">
                <label>Years grouped:(*The input years must be grouped in a way that matches the specified year range)</label>
                <select name="years_grouped">
                    <option value="5">half decades</option>
                    <option value="1">per Year</option>
                    <option value="2">half total Years</option>
                    <option value="10">decades</option>
                </select>

                <label> Reference Metric:</label>
                <select name="weather_Metric" id="weather-attributes">
                    <option value="Precipitation">Precipitation</option>
                    <option value="RainDaysNum">RainDaysNum</option>
                    <option value="Evaporation">Evaporation</option>
                    <option value="EvapDaysNum">EvapDaysNum</option>
                    <option value="Sunshine">Sunshine</option>
                    <option value="Temp">Average Temperature</option>
                    <option value="Okta">Cloud Cover</option>
                </select>

                <label>Compare Metric:</label>
                <label for="precipitation">Precipitation</label>
                <input type="checkbox" name="compare_Metric_Precipitation" value="Precipitation">
                <label for="rain_days_num">Rain Days Number</label>
                <input type="checkbox" name="compare_Metric_RainDaysNum" value="RainDaysNum">
                <label for="evaporation">Evaporation</label>
                <input type="checkbox" name="compare_Metric_Evaporation" value="Evaporation">
                <label for="evap_days_num">Evaporation Days Number</label>
                <input type="checkbox" name="compare_Metric_EvapDaysNum" value="EvapDaysNum">
                <label for="sunshine">Sunshine</label>
                <input type="checkbox" name="compare_Metric_Sunshine" value="Sunshine">
                <label for="okta">Cloud Cover</label>
                <input type="checkbox" name="compare_Metric_Okta" value="Okta">
                <label for="average_temperature">Average Temperature</label>
                <input type="checkbox" name="compare_Metric_Temp" value="Temp">
                <button name="back_period" value="true">Back</button>    <button name="period" value="yea">Apply</button>"""
        
    elif period == "month":
        page_html += """
                <label>Which Year(1970-2020):</label>
                <input type="number" name="which_year" min="1970" max="2020" placeholder="1970">
                <label>Start Month:</label>
                <select name="start_month">
                    <option value="1">January</option>
                    <option value="2">February</option>
                    <option value="3">March</option>
                    <option value="4">April</option>
                    <option value="5">May</option>
                    <option value="6">June</option>
                    <option value="7">July</option>
                    <option value="8">August</option>
                    <option value="9">September</option>
                    <option value="10">October</option>
                    <option value="11">November</option>
                    <option value="12">December</option>
                    <option value="__">All</option>
                </select>
                <label>End Month:</label>
                <select name="end_month">
                    <option value="1">January</option>
                    <option value="2">February</option>
                    <option value="3">March</option>
                    <option value="4">April</option>
                    <option value="5">May</option>
                    <option value="6">June</option>
                    <option value="7">July</option>
                    <option value="8">August</option>
                    <option value="9">September</option>
                    <option value="10">October</option>
                    <option value="11">November</option>
                    <option value="12">December</option>
                    <option value="__">All</option>
                </select>
                <label>Month grouped:(*The input years must be grouped in a way that matches the specified month range):</label>
                <select name="month_grouped">
                    <option value="1">per Month</option>
                    <option value="2">half total months</option>
                    <option value="3">quarters</option>
                </select>

                <label> Reference Metric:</label>
                <select name="weather_Metric" id="weather-attributes">
                    <option value="Precipitation">Precipitation</option>
                    <option value="RainDaysNum">RainDaysNum</option>
                    <option value="Evaporation">Evaporation</option>
                    <option value="EvapDaysNum">EvapDaysNum</option>
                    <option value="Sunshine">Sunshine</option>
                    <option value="Temp">Average Temperature</option>
                    <option value="Okta">Cloud Cover</option>
                </select>

                <label>Compare Metric:</label>
                <label for="precipitation">Precipitation</label>
                <input type="checkbox" name="compare_Metric_Precipitation" value="Precipitation">
                <label for="rain_days_num">Rain Days Number</label>
                <input type="checkbox" name="compare_Metric_RainDaysNum" value="RainDaysNum">
                <label for="evaporation">Evaporation</label>
                <input type="checkbox" name="compare_Metric_Evaporation" value="Evaporation">
                <label for="evap_days_num">Evaporation Days Number</label>
                <input type="checkbox" name="compare_Metric_EvapDaysNum" value="EvapDaysNum">
                <label for="sunshine">Sunshine</label>
                <input type="checkbox" name="compare_Metric_Sunshine" value="Sunshine">
                <label for="okta">Cloud Cover</label>
                <input type="checkbox" name="compare_Metric_Okta" value="Okta">
                <label for="average_temperature">Average Temperature</label>
                <input type="checkbox" name="compare_Metric_Temp" value="Temp">
                <button name="back_period" value="true">Back</button>  <button>Apply</button>"""
        
    page_html += """

                </form>
            </aside>
            <main class="main">
            <table>
                <tr>
                    <th>Metric Name</th>"""
    sql_list = []
    for i in range(int(year_token)):
        page_html += f"<th>Total ({int(start_year) + i * int(years_grouped)})-({int(start_year) + (i + 1) * int(years_grouped) - 1})</th>"
        if i % 2 == 1:
            page_html += f"<th>% Change</th>\n<th>Difference from Precipitation (%)</th>"
        year_sql_range = f"substr(DMY,-4,4) between '{int(start_year) + i * int(years_grouped)}' and '{int(start_year) + (i + 1) * int(years_grouped) - 1}'"
        sql_list.append(year_sql_range)
    for i in range(int(month_token)):
        page_html += f"<th>Total ({int(start_month) + i * int(month_grouped)}-{int(start_month) + (i + 1) * int(month_grouped) - 1})</th>"
        if i % 2 == 1:
            page_html += f"<th>% Change</th>\n<th>Difference from Precipitation (%)</th>"
        month_sql_range = f"dmy like '%{which_year}%' and substr(DMY, -7, 2) between '{0 if int(start_month) + i * int(month_grouped) < 10 else ''}{int(start_month) + i * int(month_grouped)}' and '{0 if int(start_month) + (i + 1) * int(month_grouped) - 1 < 10 else ''}{int(start_month) + (i + 1) * int(month_grouped) - 1}'"
        sql_list.append(month_sql_range)
    page_html += f"""
                </tr>"""
    change_list = []
    for i in metrics_list:
        data_list = []
        for g in range (len(sql_list)):
            sql_data = f"select sum({i}) from weather_data where {sql_list[g]};"
            data = pyhtml.get_results_from_query("climate.db", sql_data)
            data_list.append(data[0][0] if data else 0)
        page_html += f"""
                <tr>
                    <td>{i}</td>"""
        for j in range(int(len(data_list)/2)):
            if i == weather_Metric:
                change_list.append(((data_list[j*2 + 1] - data_list[j*2]) / data_list[j*2] * 100)-1)
            page_html += f"<td>{data_list[j*2]}</td>"
            page_html += f"<td>{data_list[j*2 + 1]}</td>"
            page_html += f"<td>{((data_list[j*2 + 1] - data_list[j*2]) / data_list[j*2] * 100)-1:.2f}%</td>"
            page_html += f"<td>{0 if i == weather_Metric else (((data_list[j*2 + 1] - data_list[j*2]) / data_list[j*2] * 100)-1)-(- change_list[j]):.2f}% {'(selected)' if i == weather_Metric else ''}</td>"

        page_html += f"""
                    </tr>"""
    page_html += f"""
            </table>
        </div>
    </body>
    </html>
    """
    print(sql_list)
    return page_html