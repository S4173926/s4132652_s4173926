def get_page_html(form_data):
    print("About to return page home page...")
    page_html="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>About us</title>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        <h1>About this website</h1>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/page2a">Page 2A</a></li>
            <li><a href="/page3a">Page 3A</a></li>
            <li><a href="/page1b">Page 1B</a></li>
            <li><a href="/page2b">Page 2B</a></li>
            <li><a href="/page3b">Page 3B</a></li>
        </ul>
        <p>This is the first dynamically generated page!</p>
        <p><a href="/">Go to Page 1A</a></p>
        <p><a href="/page2a">Go to Page 2A</a></p>
        <p><a href="/page3a">Go to Page 3A</a></p>
        <p><a href="/page1b">Go to Page 1B</a></p>
        <p><a href="/page2b">Go to Page 2B</a></p>
        <p><a href="/page3b">Go to Page 3B</a></p>
        <img src="images/rmit.png" style="width: 30%; height: auto;">
    </body>
    </html>
    """
    return page_html