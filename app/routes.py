from flask import Blueprint, render_template, request, jsonify, current_app, flash, redirect, url_for
from app import app, mail
from flask_mail import Message
# from app.utils.resume_parser import parse_resume
import os
from .config import PORTFOLIO_CONFIG, THEME_CONFIG

main = Blueprint('main', __name__)

# Path to the resume file
# RESUME_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resume.pdf')

# Print the resume path for debugging
# print(f"Looking for resume at: {RESUME_PATH}")

# Parse the resume once when the app starts
# resume_data = parse_resume(RESUME_PATH)

# Print parsed data for debugging
# print("\nParsed Resume Data:")
# print("Personal Info:", resume_data.get('personal_info', {}))
# print("Education:", resume_data.get('education', []))
# print("Experience:", resume_data.get('experience', []))
# print("Skills:", resume_data.get('skills', {}))
# print("Projects:", resume_data.get('projects', []))

@main.route('/')
def index():
    # Create a copy of the config data
    portfolio_data = PORTFOLIO_CONFIG.copy()
    
    # Use the generic configuration without trying to parse the resume
    # No need to transform skills data or extract projects from experience
    
    return render_template('index.html', 
                         data=portfolio_data,
                         theme=THEME_CONFIG)

# Contact form handler
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        if not all([name, email, subject, message]):
            flash('All fields are required.', 'error')
            return redirect(url_for('main.contact'))
        
        try:
            # Create email message
            msg = Message(
                subject=f"Portfolio Contact: {subject}",
                recipients=[app.config['MAIL_DEFAULT_SENDER']],
                body=f"""
                Name: {name}
                Email: {email}
                Subject: {subject}
                
                Message:
                {message}
                """
            )
            
            # Send email
            mail.send(msg)
            
            # Send confirmation to the user
            confirmation_msg = Message(
                subject="Thank you for contacting me",
                recipients=[email],
                body=f"""
                Dear {name},
                
                Thank you for reaching out! I have received your message and will get back to you as soon as possible.
                
                Best regards,
                {PORTFOLIO_CONFIG['personal_info']['name']}
                """
            )
            
            mail.send(confirmation_msg)
            
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('main.contact'))
            
        except Exception as e:
            current_app.logger.error(f"Error sending email: {str(e)}")
            flash('There was an error sending your message. Please try again later.', 'error')
            return redirect(url_for('main.contact'))
    
    return render_template('contact.html', 
                          title='Contact',
                          data=PORTFOLIO_CONFIG,
                          theme=THEME_CONFIG)

def get_language_icon(language):
    icons = {
        'Python': 'fab fa-python',
        'Java': 'fab fa-java',
        'Go': 'fab fa-golang',
        'JavaScript': 'fab fa-js',
        'TypeScript': 'fab fa-js',
        'HTML': 'fab fa-html5',
        'CSS': 'fab fa-css3',
    }
    return icons.get(language, 'fas fa-code')

def get_tech_icon(tech):
    icons = {
        'React': 'fab fa-react',
        'Vue.js': 'fab fa-vuejs',
        'Node.js': 'fab fa-node-js',
        'Angular': 'fab fa-angular',
        'Docker': 'fab fa-docker',
        'AWS': 'fab fa-aws',
        'Streamlit': 'fas fa-chart-line',
    }
    return icons.get(tech, 'fas fa-laptop-code')

def get_tool_icon(tool):
    icons = {
        'Git': 'fab fa-git-alt',
        'Docker': 'fab fa-docker',
        'AWS': 'fab fa-aws',
        'GCP': 'fab fa-google',
        'Kubernetes': 'fas fa-dharmachakra',
        'Jenkins': 'fab fa-jenkins',
        'Kafka': 'fas fa-stream',
        'Airflow': 'fas fa-wind',
    }
    return icons.get(tool.lower(), 'fas fa-tools')

def get_cert_icon(cert):
    if 'google' in cert.lower():
        return 'fab fa-google'
    elif 'aws' in cert.lower():
        return 'fab fa-aws'
    elif 'azure' in cert.lower():
        return 'fab fa-microsoft'
    return 'fas fa-certificate'

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
        # parsed_data = parse_resume(temp_path)
        
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
    # personal_info = resume_data.get('personal_info', {})
    # education = resume_data.get('education', [])
    return render_template('about.html', 
                          title='About')

@app.route('/experience')
def experience():
    # experience = resume_data.get('experience', [])
    return render_template('experience.html', 
                          title='Experience')

@app.route('/projects')
def projects():
    # projects = resume_data.get('projects', [])
    return render_template('projects.html', 
                          title='Projects')

@app.route('/skills')
def skills():
    # skills = resume_data.get('skills', {})
    return render_template('skills.html', 
                          title='Skills') 