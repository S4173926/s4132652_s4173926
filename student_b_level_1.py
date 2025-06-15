import pyhtml
def get_page_html(form_data):
    print("About to return page home page...")
    page_html="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>About Us</title>
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
        
        <main>
        <section class="about">
        <h1>About this website</h1>
        <p>As those years climate change becomes to a big proble that people need to face in everday. 
        In this website, we aim to help people understand the impact of climate change
          on urban areas, particularly focusing on heatwaves and rainfall patterns by using
            data and support people who need tracking current climate change data.
        </p>
        <h2>How to use this website</h2>
        <p>To use this webiste, you can find methods at the top of the page,
        and you can click the links to navigate to different pages. After you in searching page
        you can searching state, climate metric or specific thing you looking for.</p>
        </section>

        <section class="members">
        <h3>Team Members</h3>
        """
    sql_members = "select * from member;"
    members = pyhtml.get_results_from_query("climate.db",sql_members)
    for i in members:
        print(i)
        page_html += f"\n<p>Student_number: {str(i[0])} Name: {str(i[1])} {str(i[2])}</p>"
    page_html += """
        <div class="personas">
        <h3>personas</h3>
        <p>key personas for this website are:</p>
        <p>key personas for this website are:</p>
        </div>
        </section>
        </main>
    </body>
    </html>
    """
    return page_html