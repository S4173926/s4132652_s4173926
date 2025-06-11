import pyhtml
def get_page_html(form_data):
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

                <label>Metric:</label>
                <select>
                    <option value="temp">Temperature</option>
                    <option value="rain">Rainfall</option>
                </select>

                <label>Station ID:</label>
                <select>
                    <option value="temp">Temperature</option>
                    <option value="rain">Rainfall</option>
                </select>

                <label>Year Range:</label>
                <input type="text" name="year_range" placeholder="1970-2020">
                <input type="text" name="year_range" placeholder="1970-2020">

                <button>Apply</button>
            </aside>

            <main class="main">
            
            </main>
        </div>
    </body>
    </html>
    """
    return page_html