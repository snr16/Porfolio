from flask import Blueprint, render_template, request, jsonify
from app import app
from app.utils.resume_parser import parse_resume
import os

main = Blueprint('main', __name__)

# Path to the resume file
RESUME_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resume.pdf')

# Print the resume path for debugging
print(f"Looking for resume at: {RESUME_PATH}")

# Parse the resume once when the app starts
resume_data = parse_resume(RESUME_PATH)

# Print parsed data for debugging
print("\nParsed Resume Data:")
print("Personal Info:", resume_data.get('personal_info', {}))
print("Education:", resume_data.get('education', []))
print("Experience:", resume_data.get('experience', []))
print("Skills:", resume_data.get('skills', {}))
print("Projects:", resume_data.get('projects', []))

@main.route('/')
def index():
    # For now, we'll use dummy data
    # Later we'll integrate with the resume parser
    dummy_data = {
        'personal_info': {
            'name': 'Your Name',
            'email': 'email@example.com',
            'phone': '+1 (123) 456-7890',
            'location': 'City, Country',
            'github': 'https://github.com/yourusername',
            'linkedin': 'https://linkedin.com/in/yourusername'
        },
        'education': [
            {
                'institution': 'University Name',
                'degree': 'Degree Name',
                'date': '2020 - 2024',
                'gpa': '3.8/4.0'
            }
        ],
        'experience': [
            {
                'company': 'Company Name',
                'position': 'Position Title',
                'date': 'Jan 2023 - Present',
                'achievements': [
                    'Achievement 1',
                    'Achievement 2',
                    'Achievement 3'
                ]
            }
        ],
        'projects': [
            {
                'name': 'Project Name',
                'technologies': 'Tech Stack',
                'description': 'Project description goes here.',
                'github': 'https://github.com/yourusername/project'
            }
        ],
        'skills': {
            'programming_languages': ['Python', 'JavaScript', 'Java'],
            'web_technologies': ['HTML', 'CSS', 'React'],
            'databases': ['MySQL', 'MongoDB'],
            'tools': ['Git', 'Docker', 'AWS']
        }
    }
    
    return render_template('index.html', data=dummy_data)

@main.route('/parse-resume', methods=['POST'])
def parse_resume_route():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
        
    resume_file = request.files['resume']
    if resume_file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
        
    if not resume_file.filename.endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are supported'}), 400
        
    # Save the file temporarily
    temp_path = os.path.join('uploads', resume_file.filename)
    resume_file.save(temp_path)
    
    try:
        # Parse the resume
        parsed_data = parse_resume(temp_path)
        
        # Clean up
        os.remove(temp_path)
        
        return jsonify(parsed_data)
    except Exception as e:
        # Clean up in case of error
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({'error': str(e)}), 500

@app.route('/about')
def about():
    personal_info = resume_data.get('personal_info', {})
    education = resume_data.get('education', [])
    return render_template('about.html', 
                          title='About',
                          personal_info=personal_info,
                          education=education)

@app.route('/experience')
def experience():
    experience = resume_data.get('experience', [])
    return render_template('experience.html', 
                          title='Experience',
                          experience=experience)

@app.route('/projects')
def projects():
    projects = resume_data.get('projects', [])
    return render_template('projects.html', 
                          title='Projects',
                          projects=projects)

@app.route('/skills')
def skills():
    skills = resume_data.get('skills', {})
    return render_template('skills.html', 
                          title='Skills',
                          skills=skills)

@app.route('/contact')
def contact():
    personal_info = resume_data.get('personal_info', {})
    return render_template('contact.html', 
                          title='Contact',
                          personal_info=personal_info) 