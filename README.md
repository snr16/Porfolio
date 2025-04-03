# Portfolio Website

A modern, responsive portfolio website built with Flask that automatically parses your resume to create a personalized portfolio.

## Features

- Automatic resume parsing to populate portfolio content
- Responsive design that works on all devices
- Dark theme with customizable colors
- Sections for personal information, education, experience, skills, and projects
- Project cards with images and links to GitHub repositories
- Skills section with categorized skills and icons
- Contact section with social media links

## Quick Start

1. Place your resume in PDF format in the root directory as `resume.pdf`
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python run.py
   ```
4. Visit `http://localhost:5000` in your browser

## Resume Parsing

The website automatically extracts information from your resume. The parser will extract:

### Personal Information
- Name
- Email
- Phone
- Location
- GitHub profile
- LinkedIn profile

### Education
- Institution name
- Degree
- Date range
- GPA

### Experience
- Company name
- Position
- Date range
- Achievements/Responsibilities

### Skills
- Programming languages
- Web technologies
- Databases
- Tools and platforms
- Certifications

### Projects (if listed in resume)
- Project name
- Description
- Technologies used
- Links

## End-to-End Customization Guide

This guide provides step-by-step instructions for customizing your portfolio website.

### 1. Configuration File Updates

The main configuration file is `app/config.py`. This file contains all the data that will be displayed on your portfolio.

#### Personal Information
```python
'personal_info': {
    'name': 'Your Name',
    'title': 'Your Title/Role',
    'bio': 'Your Bio',
    'email': 'your.email@example.com',
    'phone': 'Your Phone',
    'location': 'Your Location',
    'github': 'https://github.com/yourusername',
    'linkedin': 'https://linkedin.com/in/yourusername'
}
```

#### Education
```python
'education': [
    {
        'institution': 'University Name',
        'degree': 'Degree Name',
        'date': 'Start Date - End Date',
        'gpa': 'GPA'
    }
]
```

#### Experience
```python
'experience': [
    {
        'company': 'Company Name',
        'position': 'Position Title',
        'date': 'Start Date - End Date',
        'achievements': [
            'Achievement 1',
            'Achievement 2',
            'Achievement 3'
        ]
    }
]
```

#### Skills
```python
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
        }
    ],
    'certifications': [
        {
            'name': 'Certification Name',
            'icon': 'fas fa-certificate',
            'date': 'Year',
            'link': 'https://www.credential.net/your-credential-id'
        }
    ]
}
```

#### Projects
```python
'projects': [
    {
        'name': 'Project Name',
        'description': 'A brief description of the project, what it does, and your role in it.',
        'technologies': 'Technologies used (e.g., Python, Flask, React, MongoDB)',
        'github': 'https://github.com/yourusername/projectname'
    }
]
```

### 2. Adding a Profile Image

1. Create the images directory if it doesn't exist:
   ```
   mkdir -p app/static/images
   ```

2. Place your profile image in the `app/static/images/` directory
   - Make sure your image is square and at least 300x300 pixels for best results
   - Supported formats: JPG, PNG, WebP

3. Update the image path in `app/templates/index.html`:
   ```html
   <div class="hero-image">
       <img src="{{ url_for('static', filename='images/your-profile-image.jpg') }}" alt="Your Name">
   </div>
   ```

### 3. Theme Customization

#### Colors
Edit `app/static/css/style.css` to customize colors:

```css
:root {
    --primary-color: #00ff9d;
    --secondary-color: #6c63ff;
    --accent-color: #ff6b6b;
    --background-dark: #0a192f;
    --background-light: #112240;
    --text-primary: #e6f1ff;
    --text-secondary: #8892b0;
}
```

#### Fonts
To change the font, update the `font-family` property in `app/static/css/style.css`:

```css
body {
    font-family: 'Your Preferred Font', sans-serif;
}
```

### 4. Adding Project Images

1. Place your project images in the `app/static/images/projects/` directory
2. Update the project image paths in `app/templates/index.html`:
   ```html
   <div class="project-image">
       <img src="{{ url_for('static', filename='images/projects/your-project-image.jpg') }}" alt="Project Name">
   </div>
   ```

### 5. Customizing Routes

If you need to add new pages or modify the existing ones, edit `app/routes.py`:

```python
@app.route('/new-page')
def new_page():
    return render_template('new_page.html', data=PORTFOLIO_CONFIG)
```

### 6. Adding New Templates

1. Create a new HTML file in `app/templates/`
2. Extend the base template:
   ```html
   {% extends "base.html" %}
   
   {% block title %}Page Title{% endblock %}
   
   {% block content %}
   <!-- Your content here -->
   {% endblock %}
   ```

### 7. Running the Application

1. Make sure all your changes are saved
2. Run the application:
   ```
   python run.py
   ```
3. Visit `http://localhost:5000` in your browser

### 8. Troubleshooting

#### Port Conflicts
If port 5000 is in use, modify `run.py`:
```python
app.run(debug=True, port=YOUR_PORT_NUMBER)
```

#### Resume Parsing Issues
If the resume parser doesn't extract all the information correctly:
1. Check the format of your resume
2. Manually update the information in `app/config.py`

## Project Structure

```
portfolio-website/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   │       └── your-profile-image.jpg
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── __init__.py
│   ├── config.py
│   └── routes.py
├── resume.pdf
├── requirements.txt
└── run.py
```

## Contributing

Feel free to submit issues and enhancement requests! 