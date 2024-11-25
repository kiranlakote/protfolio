from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    menu_items = [
        {"href": "#home", "name": "Home"},
        {"href": "#about", "name": "About"},
        # {"href": "#service", "name": "Service"},
        {"href": "#experience", "name": "Experience"},
        {"href": "#contact", "name": "Contact"},
    ]

    hero_data = {
        "name": "Kiran Kumar Lakote",
        "roles": "Senior Software Engineer, Full Stack Developer, Tech Enthusiast",
        "hero_image": "static/img/hero.png",
    }

    about_data = {
        "title": "About Me",
        "subtitle": "6.9 Years Experience",
        "description": "Accomplished Senior Software Engineer with 7+ years of experience in designing, developing, and delivering high-quality software solutions. A proven track record in leading cross-functional teams and fostering collaborative environments to achieve business objectives. Expertise in relationship building, decision-making, and communication enhances team performance and ensures alignment with organizational goals. Committed to driving software process improvements, resulting in significant increases in efficiency, productivity, and software quality.",
        "skills": [
            {"name": "Web Development", "percentage": 90},
            {"name": "AngularJS ", "percentage": 75},
            {"name": "PHP (CodeIgniter, Laravel, OpenCart)", "percentage": 85},
            {"name": "Python (Django, Flask)", "percentage": 80},
            {"name": "Database Management", "percentage": 78},
            {"name": "Elastic Stack", "percentage": 90},
            {"name": "AWS Management (EC2, S3, SpotRequest)", "percentage": 79},
            {"name": "Rest API", "percentage": 90},
            {"name": "Android Design", "percentage": 60},
        ],
    }

    service_data = {
    }
    # service_data = {
    #     "title": "Services",
    #     "subtitle": "What I Offer",
    #     "services": [
    #         {
    #             "icon": "fa fa-laptop",
    #             "name": "Web Design",
    #             "description": "Lorem ipsum dolor sit amet elit. Phase nec preti mi. Curabi facilis ornare velit non",
    #         },
    #         {
    #             "icon": "fa fa-laptop-code",
    #             "name": "Web Development",
    #             "description": "Lorem ipsum dolor sit amet elit. Phase nec preti mi. Curabi facilis ornare velit non",
    #         },
    #         {
    #             "icon": "fab fa-android",
    #             "name": "Apps Design",
    #             "description": "Lorem ipsum dolor sit amet elit. Phase nec preti mi. Curabi facilis ornare velit non",
    #         },
    #         {
    #             "icon": "fab fa-apple",
    #             "name": "Apps Development",
    #             "description": "Lorem ipsum dolor sit amet elit. Phase nec preti mi. Curabi facilis ornare velit non",
    #         }
    #     ]
    # }

    experience_data = {
        "title": "Experience",
        "subtitle": "What I Have Done",
        "experiences": [
            {
                "title": "Senior Software Engineer",
                "company": "Skills OutsourceThink Pvt Ltd",
                "date": "Feb 2020 - Current",
                "description": "Optimized Elasticsearch queries, reducing data processing latency by 30% and improving reporting efficiency. Designed and implemented scalable logging pipelines using ELK, increasing system reliability by 25%. Directed a cross-functional team of 5 developers, enhancing productivity by 40% through streamlined workflows. Automated data verification processes with Python scripts, increasing accuracy by 15%. Integrated third-party APIs and services to enhance software functionality and interoperability. Resolved complex issues related to software applications quickly and effectively.",
            },
            {
                "title": "Software Engineer",
                "company": "Strawberry Box Medias",
                "date": "Feb 2019 - Feb 2020",
                "description": "Created automated software for front-desk processes, decreasing manual tasks by 35%. Designed APIs for mobile applications, enhancing scalability by 50%. Improved UI/UX for Android apps, leading to a 20% increase in user satisfaction ratings. Collaborated in Agile teams to ensure on-time delivery with 95% client satisfaction. Integrated third-party APIs into existing systems as needed for enhanced functionalities.",
            },
            {
                "title": "Full Stack Developer",
                "company": "Lexes Technologies",
                "date": "Jan 2018 - Jan 2019",
                "description": "Created a web application for locating service providers, reducing search times by 40%. Customized application features for clients, achieving a 100% client satisfaction rate. Enhanced front-end architecture, improving load times by 25%. Authored technical documentation to streamline future development efforts",
            }
        ]
    }

    footer_data = {
        "social_links": [
            {"href": "#", "icon": "fab fa-linkedin-in"},
            {"href": "#", "icon": "fab fa-facebook-f"},
            # {"href": "#", "icon": "fab fa-twitter"},
            {"href": "#", "icon": "fab fa-instagram"},
            
        ],
        "name": "Kiran Kumar Lakote",
        "address": "Bangalore, India",
        "phone": "+91 9035825565",
        "email": "kirankumarlakote@gmail.com",
        "site_name": "KiranFolio"
    }

    return render_template('index.html', menu_items=menu_items,
                           hero_data=hero_data, 
                           about_data=about_data, 
                           service_data=service_data, 
                           experience_data=experience_data,
                           footer_data=footer_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)