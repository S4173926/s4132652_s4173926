def get_page_html(form_data):
    page_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Help | Weather Data Web App</title>
    <style>
        html, body {
            height: 100%;
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #333;
            display: flex;
            flex-direction: column;
        }

        header {
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            height: 12vh;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
        }

        header img {
            height: 40px;
        }

        header ul {
            list-style: none;
            display: flex;
            margin: 0;
            padding: 0;
        }

        header li {
            margin: 0 10px;
        }

        header a {
            color: white;
            text-decoration: none;
            font-weight: 600;
        }

        header a:hover {
            text-decoration: underline;
        }

        h1 {
            text-align: center;
            margin: 30px 0 20px;
            font-size: 2.4em;
            color: #0077b6;
        }

        .content {
            width: 80%;
            margin: 0 auto;
            background: #f1f9ff;
            padding: 30px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            font-size: 1.1em;
        }

        .content p {
            margin: 15px 0;
            line-height: 1.6;
        }

        .content a {
            color: #0077b6;
            font-weight: bold;
            text-decoration: none;
        }

        .content a:hover {
            text-decoration: underline;
        }

        footer {
            margin-top: auto;
            background: linear-gradient(to right, #0077b6, #00b4d8);
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }

        footer a {
            color: #ffeb3b;
            text-decoration: underline;
        }

        footer a:hover {
            color: #ffffff;
        }
    </style>
</head>
<body>

<header>
    <img src="rmit.png" alt="RMIT Logo">
    <ul>
        <li><a href="/">Page 1A</a></li>
        <li><a href="/page2a">Page 2A</a></li>
        <li><a href="/page3a">Page 3A</a></li>
        <li><a href="/page1b">About Us</a></li>
        <li><a href="/page2b">Climate Metric</a></li>
        <li><a href="/page3b">Exploring Climate</a></li>
        <li><a href="/help">HELP</a></li>
    </ul>
</header>

<h1>Help & Support</h1>

<div class="content">
    <p>If you need assistance using this weather data application, feel free to reach out:</p>
    <p><strong>Phone:</strong> (04) 248 4379</p>
    <p><strong>Phone:</strong> (+61) 468 885 427</p>
    <p><strong>Email:</strong> <a href="mailto:s4132652@student.rmit.edu.au">s4132652@student.rmit.edu.au</a></p>
    <p><strong>Email:</strong> <a href="mailto:s4173926@student.rmit.edu.au">s4173926@student.rmit.edu.au</a></p>
    <p>This site is developed for educational purposes as part of the INTE/COSC unit at RMIT University. For technical support or questions about the data, contact the developer using the information above.</p>
</div>

<footer>
    <p>FAQ: For more information, please visit our <a href="/faq">FAQ page</a>.</p>
</footer>

</body>
</html>
"""
    return page_html