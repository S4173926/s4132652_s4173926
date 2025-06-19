import pyhtml

def get_page_html(form_data):
    print("About to return home page...")

    sql_members = "SELECT * FROM member;"
    members = pyhtml.get_results_from_query("climate.db", sql_members)
    sql_personas = "SELECT * FROM personas;"
    personas = pyhtml.get_results_from_query("climate.db", sql_personas)

    page_html = """<!DOCTYPE html>
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
            <li><a href="/">Home</a></li>
            <li><a href="/page2a">Page 2A</a></li>
            <li><a href="/page3a">Page 3A</a></li>
            <li><a href="/page1b">About Us</a></li>
            <li><a href="/page2b">Climate Metric</a></li>
            <li><a href="/page3b">Exploring Climate</a></li>
            <li><a href="/help">HELP</a></li>
        </ul>
    </header>
    <main>
        <section class="about">
            <h1>About this website</h1>
            <p>
                Climate change has become a significant problem that people face every day.
                This website aims to help people understand the impact of climate change
                on urban areas, particularly focusing on heatwaves and rainfall patterns,
                by using data to support those who need to track current climate change data.
            </p>
            <h2>How to use this website</h2>
            <p>
                Use the navigation links at the top of the page to explore different features.
                You can search by state, climate metric, or other specific criteria on the search pages.
            </p>
        </section>

        <section class="members">
            <h3>Team Members</h3>
            <ul>
    """

    for member in members:
        student_number, first_name, last_name = member[:3]
        page_html += f"<li>Student Number: {student_number} - {first_name} {last_name}</li>\n"

    page_html += """
            </ul>
            <div class="personas">
                <h3>Personas</h3>
    """

    for persona in personas:
        _, name, age, background, goals, needs = persona[:6]
        goals_list = [g.strip() for g in goals.split("*") if g.strip()]
        needs_list = [n.strip() for n in needs.split("*") if n.strip()]
        page_html += f"""
                <div class="persona">
                    <p><strong>{name}</strong> (Age: {age})<br>Background: {background}</p>
                    <ul>
                        <li><strong>Goals:</strong></li>
        """
        for goal in goals_list:
            page_html += f"<li>{goal}</li>"
        page_html += """
                    </ul>
                    <ul>
                        <li><strong>Needs:</strong></li>
        """
        for need in needs_list:
            page_html += f"<li>{need}</li>"
        page_html += """
                    </ul>
                </div>
        """

    page_html += """
            </div>
        </section>
    </main>
</body>
</html>
"""
    return page_html