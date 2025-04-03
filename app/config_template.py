"""
Generic configuration template for the portfolio website.
Copy this file to config.py and fill in your personal information.
"""

# Portfolio Configuration Template
PORTFOLIO_CONFIG = {
    'personal_info': {
        'name': '[Your Name]',
        'title': '[Your Title/Role]',
        'bio': '[Your Bio]',
        'email': '[your.email@example.com]',
        'phone': '[Your Phone]',
        'location': '[Your Location]',
        'github': '[https://github.com/yourusername]',
        'linkedin': '[https://linkedin.com/in/yourusername]'
    },
    'education': [
        {
            'institution': '[University Name]',
            'degree': '[Degree Name]',
            'date': '[Start Date - End Date]',
            'gpa': '[GPA]'
        }
    ],
    'experience': [
        {
            'company': '[Company Name]',
            'position': '[Position Title]',
            'date': '[Start Date - End Date]',
            'achievements': [
                '[Achievement 1]',
                '[Achievement 2]',
                '[Achievement 3]'
            ]
        }
    ],
    'skills': {
        'categories': [
            {
                'name': '[Category Name]',
                'icon': '[fas fa-icon-name]',
                'items': [
                    {'name': '[Skill 1]', 'icon': '[fas fa-skill-icon]'},
                    {'name': '[Skill 2]', 'icon': '[fas fa-another-icon]'}
                ]
            }
        ],
        'certifications': [
            {
                'name': '[Certification Name]',
                'icon': '[fas fa-certificate]',
                'date': '[Date]'
            }
        ]
    },
    'projects': [
        {
            'name': '[Project Name]',
            'description': '[Project Description]',
            'technologies': '[Technologies Used]',
            'github': '[https://github.com/yourusername/project]'
        }
    ]
}

# Theme Configuration Template
THEME_CONFIG = {
    'primary_color': '#007bff',
    'secondary_color': '#6c757d',
    'background_color': '#ffffff',
    'text_color': '#212529',
    'font_family': 'Roboto, sans-serif'
} 