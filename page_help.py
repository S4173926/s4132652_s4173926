def get_page_html(form_data):
    page_html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Help | Weather Data Web App</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(to bottom, #005b96, #003f63);
                color: white;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }

            header {
                background: white;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }

            header img {
                height: 50px;
            }

            nav {
                display: flex;
                gap: 15px;
            }

            nav a {
                color: #004080;
                font-weight: bold;
                text-decoration: none;
            }

            h1 {
                text-align: center;
                margin: 40px 0 20px;
                font-size: 2.3em;
                color: #ffffff;
            }

            .content {
                background-color: rgba(255,255,255,0.08);
                width: 80%;
                margin: 0 auto;
                padding: 25px 30px;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                font-size: 1.1em;
            }

            .content p {
                margin: 15px 0;
                line-height: 1.6;
            }

            .content strong {
                color: #ffffff;
            }

            footer {
                margin-top: auto;
                background-color: #f0f8ff;
                text-align: center;
                padding: 20px;
                font-size: 0.9em;
                color: #333;
                border-top: 1px solid #ccc;
            }
        </style>
    </head>
    <body>

        <header>
            <img src="images/rmit.png" alt="RMIT Logo">
            <nav>
                <a href="/">Page 1A</a>
                <a href="/page2a">Page 2A</a>
                <a href="/page3a">Page 3A</a>
                <a href="/page1b">Page 1B</a>
                <a href="/page2b">Page 2B</a>
                <a href="/page3b">Page 3B</a>
                <a href="/help">HELP</a>
            </nav>
        </header>

        <h1>Help & Support</h1>

        <div class="content">
            <p>If you need assistance using this weather data application, feel free to reach out:</p>
            <p><strong>Phone:</strong> (04) 248 4379</p>
            <p><strong>Email:</strong> <a href="mailto:s4132652@student.rmit.edu.au" style="color: #add8ff;">s4132652@student.rmit.edu.au</a></p>
            <p>This site is developed for educational purposes as part of the INTE/COSC unit at RMIT University. For technical support or questions about the data, contact the developer using the information above.</p>
        </div>

        <footer>
            <p>FAQ: For more information, please visit our <a href="/faq">FAQ page</a>.</p>
        </footer>

    </body>
    </html>
    """
    return page_html