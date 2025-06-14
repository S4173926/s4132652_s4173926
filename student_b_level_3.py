import pyhtml
def get_page_html(form_data):
    print("About to return page 3")
    #Create the top part of the webpage
    #Note that the drop down list ('select' HTML element) has been given the name "var_star"
    #We will use this same name in our code further below to obtain what the user selected.
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
            <li><a href="/page2a">Page 2A</a></li>
            <li><a href="/page3a">Page 3A</a></li>
            <li><a href="/page1b">About Us</a></li>
            <li><a href="/page2b">Climate Metric</a></li>
            <li><a href="/page3b">Exploring Climate</a></li>
        </ul>
        </header>
        <div class="container">
            <aside class="sidebar">
                <h3>Search and Explore Climate Metrics Similarities</h3>

                <form action="/page3b" method="GET">

                <label>Period:</label>
                <select name="period">
                    <option value="year">Year</option>
                    <option value="month">Month</option>
                </select>

                <label>Start Year(1970-2020):</label>
                <input type="number" name="start_year" min="1970" max="2020" placeholder="2005">
                <label>End Year(1970-2020):</label>
                <input type="number" name="end_year" min="1970" max="2020" placeholder="2015">
                <label>Years grouped:</label>
                <select name="years_grouped">
                    <option value="5">half decades</option>
                    <option value="1">per Year</option>
                    <option value="2">half total Years</option>
                    <option value="10">decades</option>
                </select>

                <label>Which Year(1970-2020):</label>
                <input type="number" name="which_year" min="1970" max="2020" placeholder="1970">
                <label>Start Month:</label>
                <select name="start_month">
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
                    <option value="__">All</option>
                </select>
                <label>End Month:</label>
                <select name="end_month">
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
                    <option value="__">All</option>
                </select>
                <label>Month grouped:</label>
                <select name="month_grouped">
                    <option value="1">per Month</option>
                    <option value="2">half years</option>
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
                <button>Apply</button>
                </form>
            </aside>
            <main class="main">
            <table>
                <tr>
                    <th>Metric Name</th>
                    <th>Total (2005-2009)</th>
                    <th>Total (2010-2015)</th>
                    <th>% Change</th>
                    <th>Difference from Precipitation (%)</th>
                </tr>
                <tr>
                    <td>Precipitation</td>
                    <td>4250 mm</td>
                    <td>4370 mm</td>
                    <td>+2.80%</td>
                    <td>0.0% (selected)</td>
                </tr>
                <tr>
                    <td>Evaporation</td>
                    <td>7100 mm</td>
                    <td>7125 mm</td>
                    <td>+0.35%</td>
                    <td>-2.45%</td>
                </tr>
                <tr>
                    <td>Average Temp</td>
                    <td>22.5 &deg;C</td>
                    <td>22.9 &deg;C</td>
                    <td>+1.77%</td>
                    <td>-1.03%</td>
                </tr>
                <tr>
                    <td>Sunshine</td>
                    <td>19,300 hrs</td>
                    <td>19,415 hrs</td>
                    <td>+0.59%</td>
                    <td>-2.21%</td>
                </tr>
                <tr>
                    <td>Cloud Cover</td>
                    <td>3250 oktas</td>
                    <td>3200 oktas</td>
                    <td>-1.50%</td>
                    <td>-1.30%</td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    """
    return page_html