import pyhtml

def get_page_html(form_data):
    print("About to return page 3")

    page_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page 3A - Forms, Databases and Advanced Queries</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            background-color: #0d47a1;
            color: white;
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
            margin-top: 30px;
        }

        form {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            margin: 30px;
            border-radius: 12px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        select, input[type="submit"] {
            padding: 8px 12px;
            border-radius: 6px;
            border: none;
            font-size: 1rem;
        }

        select {
            min-width: 180px;
        }

        input[type="submit"] {
            background-color: #64b5f6;
            color: #fff;
            font-weight: bold;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #42a5f5;
        }

        table {
            width: 90%;
            margin: 0 auto 40px auto;
            border-collapse: collapse;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            overflow: hidden;
        }

        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #90caf9;
            color: white;
        }

        th {
            background-color: #1565c0;
        }

        tr:hover {
            background-color: rgba(255,255,255,0.05);
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

    <h1>Identify Similar Weather Stations</h1>

    <form action="/page3a" method="GET">
        <div>
            <label for="var_star">Movie Star</label>
            <select name="var_star" multiple>"""

    query = "select * from star;"
    results = pyhtml.get_results_from_query("database/movies.db", query)
    var_star = form_data.get('var_star')

    if var_star:
        var_star = [int(star) for star in var_star]

    for row in results:
        page_html += f'<option value="{row[0]}"'
        if var_star and row[0] == var_star[0]:
            page_html += ' selected="selected"'
        page_html += f'>{row[1]}</option>'

    page_html += """</select>
        </div>"""

    page_html += """
        <div>
            <label for="var_movie">Movie</label>
            <select name="var_movie" """

    if var_star:
        query = f"""
        SELECT movie.mvnumb, movie.mvtitle 
        FROM movie 
        JOIN movstar ON movie.mvnumb = movstar.mvnumb 
        WHERE movstar.starnumb = {var_star[0]};
        """
        results = pyhtml.get_results_from_query("database/movies.db", query)
        page_html += ">"
        for row in results:
            page_html += f'<option value="{row[0]}">{row[1]}</option>'
    else:
        page_html += 'disabled><option>Choose a star</option>'

    page_html += """</select>
        </div>

        <input type="submit" value="Show starred movies">
    </form>"""

    # Optional result table
    page_html += """
    <table>
        <tr><th>Movie Star</th><th>Movie</th></tr>
        <tr><td>Sample Star</td><td>Sample Movie</td></tr>
    </table>
</body>
</html>
"""
    return page_html