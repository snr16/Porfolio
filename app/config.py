"""
Generic configuration for the portfolio website.
This file contains placeholder data that you can replace with your own information.
"""

# Portfolio Configuration
PORTFOLIO_CONFIG = {
    'personal_info': {
        'name': 'Your Name',
        'title': 'Your Professional Title',
        'bio': 'A brief description about yourself and your professional background. Highlight your key skills and what you are passionate about.',
        'email': 'your.email@example.com',
        'phone': '+1 (123) 456-7890',
        'location': 'City, State',
        'github': 'https://github.com/yourusername',
        'linkedin': 'https://linkedin.com/in/yourusername'
    },
    'education': [
        {
            'institution': 'University Name',
            'degree': 'Degree Name',
            'date': 'Year - Year',
            'gpa': 'GPA'
        },
        {
            'institution': 'Another University',
            'degree': 'Another Degree',
            'date': 'Year - Year',
            'gpa': 'GPA'
        }
    ],
    'experience': [
        {
            'company': 'Company Name',
            'position': 'Job Title',
            'date': 'Month Year - Month Year',
            'achievements': [
                'Key achievement or responsibility 1',
                'Key achievement or responsibility 2',
                'Key achievement or responsibility 3'
            ]
        },
        {
            'company': 'Another Company',
            'position': 'Another Job Title',
            'date': 'Month Year - Month Year',
            'achievements': [
                'Key achievement or responsibility 1',
                'Key achievement or responsibility 2',
                'Key achievement or responsibility 3'
            ]
        }
    ],
    'skills': {
        'categories': [
            {
                'name': 'Programming Languages',
                'icon': 'fas fa-code',
                'items': [
                    {'name': 'Python', 'icon': 'fab fa-python'},
                    {'name': 'JavaScript', 'icon': 'fab fa-js'},
                    {'name': 'Java', 'icon': 'fab fa-java'}
                ]
            },
            {
                'name': 'Web Technologies',
                'icon': 'fas fa-globe',
                'items': [
                    {'name': 'HTML', 'icon': 'fab fa-html5'},
                    {'name': 'CSS', 'icon': 'fab fa-css3-alt'},
                    {'name': 'React', 'icon': 'fab fa-react'}
                ]
            },
            {
                'name': 'Databases',
                'icon': 'fas fa-database',
                'items': [
                    {'name': 'MySQL', 'icon': 'fas fa-database'},
                    {'name': 'MongoDB', 'icon': 'fas fa-database'},
                    {'name': 'PostgreSQL', 'icon': 'fas fa-database'}
                ]
            },
            {
                'name': 'Cloud & DevOps',
                'icon': 'fas fa-cloud',
                'items': [
                    {'name': 'AWS', 'icon': 'fab fa-aws'},
                    {'name': 'Docker', 'icon': 'fab fa-docker'},
                    {'name': 'Git', 'icon': 'fab fa-git-alt'}
                ]
            }
        ],
        'certifications': [
            {
                'name': 'Certification Name',
                'icon': 'fas fa-certificate',
                'date': 'Year',
                'link': 'https://www.credential.net/your-credential-id'
            },
            {
                'name': 'Another Certification',
                'icon': 'fas fa-certificate',
                'date': 'Year',
                'link': 'https://www.credential.net/your-credential-id'
            }
        ]
    },
    'projects': [
        {
            'name': 'Project Name',
            'description': 'A brief description of the project, what it does, and your role in it.',
            'technologies': 'Technologies used (e.g., Python, Flask, React, MongoDB)',
            'github': 'https://github.com/yourusername/projectname'
        },
        {
            'name': 'Another Project',
            'description': 'A brief description of the project, what it does, and your role in it.',
            'technologies': 'Technologies used (e.g., JavaScript, Node.js, Express, PostgreSQL)',
            'github': 'https://github.com/yourusername/projectname'
        },
        {
            'name': 'Third Project',
            'description': 'A brief description of the project, what it does, and your role in it.',
            'technologies': 'Technologies used (e.g., Python, Django, PostgreSQL)',
            'github': 'https://github.com/yourusername/projectname'
        }
    ]
}

# Theme Configuration
THEME_CONFIG = {
    'primary_color': '#007bff',
    'secondary_color': '#6c757d',
    'background_color': '#ffffff',
    'text_color': '#212529',
    'font_family': 'Roboto, sans-serif'
} 