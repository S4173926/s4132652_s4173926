def get_page_html(form_data):
    print("About to return page home page...")
    page_html="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>About us</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
        <a href="/"><img src="rmit.png" alt="Logo"></a>
        <ul>
            <li><a href="/page2a">Page 2A</a></li>
            <li><a href="/page3a">Page 3A</a></li>
            <li><a href="/page1b">About us</a></li>
            <li><a href="/page2b">Page 2B</a></li>
            <li><a href="/page3b">Page 3B</a></li>
        </ul>
        </header>
        <main>
        <section class="about">
        <p><a href="/">Home</a> > <a href="/page1b">About us</a></p>
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
        </main>
    </body>
    </html>
    """
    return page_html