import PyPDF2
import os
import re
from datetime import datetime

def parse_resume(pdf_path):
    """
    Parse the resume PDF and extract relevant information
    """
    try:
        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extract text from all pages
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            # Parse the extracted text
            parsed_data = {
                'raw_text': text,
                'personal_info': extract_personal_info(text),
                'education': extract_education(text),
                'experience': extract_experience(text),
                'skills': extract_skills(text),
                'projects': extract_projects(text),
                'status': 'success'
            }
            
            return parsed_data
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

def extract_personal_info(text):
    personal_info = {
        'name': None,
        'email': None,
        'phone': None,
        'location': None,
        'github': None,
        'linkedin': None
    }
    
    # Split text into lines
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Name is usually in the first few lines, all caps
        if i < 5 and not personal_info['name'] and line and line.isupper() and len(line) > 5:
            personal_info['name'] = line
        elif '@' in line and '.com' in line.lower():
            personal_info['email'] = line.strip()
        elif any(x in line.lower() for x in ['phone', 'tel', 'mobile']) or ('+' in line and any(c.isdigit() for c in line)):
            # Extract just the phone number
            phone = re.search(r'[+]?[\d\s()-]{10,}', line)
            if phone:
                personal_info['phone'] = phone.group(0).strip()
        elif any(x in line.lower() for x in ['location', 'address', 'city']):
            location = line.split(':')[-1].strip() if ':' in line else line
            personal_info['location'] = location
        elif 'github.com' in line.lower():
            personal_info['github'] = extract_url(line)
        elif 'linkedin.com' in line.lower():
            personal_info['linkedin'] = extract_url(line)
    
    return personal_info

def extract_url(text):
    """Extract URL from text."""
    import re
    url_pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*'
    match = re.search(url_pattern, text)
    return match.group(0) if match else None

def clean_text(text):
    """Clean and normalize text."""
    import re
    # Remove extra spaces and normalize hyphens
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(?<=[a-zA-Z])\s*-\s*(?=[a-zA-Z])', '-', text)
    return text.strip()

def extract_education(text):
    """Extract education information from resume text"""
    education = []
    
    # Find the education section
    education_section = None
    sections = text.split('\n\n')
    for i, section in enumerate(sections):
        if 'EDUCATION' in section.upper():
            education_section = section
            # Include next few sections to capture all education info
            for j in range(1, 3):
                if i + j < len(sections):
                    education_section += '\n\n' + sections[i + j]
            break
    
    if education_section:
        # Look for degree patterns
        degree_patterns = [
            r'Master of [\w\s]+|M\.S\.',
            r'Bachelor of [\w\s]+|B\.Tech\.',
            r'Ph\.D\.',
        ]
        
        lines = education_section.split('\n')
        current_entry = {}
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Look for institution and date
            if 'Institute' in line or 'University' in line:
                if current_entry:
                    education.append(current_entry)
                current_entry = {'institution': line}
                # Extract date from the same line
                date_match = re.search(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*\d{4}\s*[–-]\s*(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?\s*\d{4}', line)
                if date_match:
                    current_entry['date'] = date_match.group(0)
                
            # Look for degree and GPA
            for pattern in degree_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    current_entry['degree'] = line
                    gpa_match = re.search(r'GPA:\s*([\d.]+)', line)
                    if gpa_match:
                        current_entry['gpa'] = gpa_match.group(1)
                    break
        
        if current_entry:
            education.append(current_entry)
    
    return education

def extract_experience(text):
    """Extract work experience from resume text"""
    experience = []
    
    # Find the experience section
    experience_section = None
    sections = text.split('\n\n')
    for i, section in enumerate(sections):
        if 'PROFESSIONAL EXPERIENCE' in section.upper():
            experience_section = section
            # Include next few sections to capture all experience info
            for j in range(1, 4):
                if i + j < len(sections):
                    experience_section += '\n\n' + sections[i + j]
            break
    
    if experience_section:
        lines = experience_section.split('\n')
        current_entry = {}
        in_experience = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Look for company and position
            if '|' in line and not line.startswith('•'):
                # Skip project-like entries (containing GitHub or specific tech stacks)
                if 'GitHub' in line or 'Github' in line or any(tech in line for tech in ['Python', 'Docker', 'MLFlow', 'Streamlit', 'PyTorch', 'LLM']):
                    in_experience = False
                    continue
                    
                in_experience = True
                if current_entry:
                    experience.append(current_entry)
                current_entry = {}
                parts = line.split('|')
                current_entry['company'] = parts[0].strip()
                if len(parts) > 1:
                    current_entry['position'] = parts[1].strip()
                
                # Extract date from the same line
                date_match = re.search(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*\d{4}\s*[–-]\s*(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?\s*\d{4}', line)
                if date_match:
                    current_entry['date'] = date_match.group(0)
            
            # Look for achievements
            elif line.startswith('•') and in_experience:
                if current_entry and 'achievements' not in current_entry:
                    current_entry['achievements'] = []
                if current_entry:
                    current_entry['achievements'].append(line[1:].strip())
        
        if current_entry and in_experience:
            experience.append(current_entry)
    
    return experience

def extract_skills(text):
    """Extract skills from resume text"""
    skills = {
        'programming_languages': [],
        'web_technologies': [],
        'databases': [],
        'tools': [],
        'certifications': []
    }
    
    # Find the skills section
    skills_section = None
    sections = text.split('\n\n')
    for section in sections:
        if 'TECHNICAL SKILLS' in section.upper():
            skills_section = section
            break
    
    if skills_section:
        # Common skill keywords
        programming_languages = ['python', 'java', 'javascript', 'c++', 'c#', 'go', 'rust']
        web_technologies = ['html', 'css', 'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'streamlit']
        databases = ['sql', 'mysql', 'postgresql', 'mongodb', 'bigquery']
        tools = ['git', 'docker', 'kubernetes', 'aws', 'gcp', 'linux', 'unix', 'jenkins', 'kafka', 'airflow']
        
        # Extract skills based on keywords
        text_lower = skills_section.lower()
        
        # Extract programming languages
        for lang in programming_languages:
            if lang in text_lower:
                skills['programming_languages'].append(lang.capitalize())
        
        # Extract web technologies
        for tech in web_technologies:
            if tech.lower() in text_lower:
                skills['web_technologies'].append(tech.capitalize())
        
        # Extract databases
        for db in databases:
            if db in text_lower:
                skills['databases'].append(db.capitalize())
        
        # Extract tools
        for tool in tools:
            if tool in text_lower:
                skills['tools'].append(tool.capitalize())
        
        # Extract certifications
        cert_pattern = r'(?:AWS|Google Cloud|Azure)[^,\.]*(?:Engineer|Architect|Developer|Associate|Professional)[^,\.]*'
        certs = re.finditer(cert_pattern, skills_section, re.IGNORECASE)
        for cert in certs:
            skills['certifications'].append(cert.group(0).strip())
    
    return skills

def extract_projects(text_lines):
    projects = []
    seen_projects = set()
    current_project = None
    in_projects_section = False
    
    tech_keywords = {'python', 'java', 'javascript', 'react', 'node', 'aws', 'gcp', 'azure', 'docker', 
                    'kubernetes', 'ml', 'ai', 'pytorch', 'tensorflow', 'llm', 'langchain', 'streamlit',
                    'github', 'git', 'airflow', 'databricks', 'sql', 'mysql', 'mongodb', 'redis'}
    
    for i, line in enumerate(text_lines):
        line = clean_text(line)
        
        if not line:
            continue
            
        if 'PROJECTS' in line.upper() or 'SELECTED PROJECTS' in line.upper():
            in_projects_section = True
            continue
            
        if in_projects_section:
            # Check if this is a project title line
            lower_line = line.lower()
            
            # Skip if line looks like contact info
            if any(x in lower_line for x in ['@', 'phone', 'email', 'address']):
                continue
                
            # Check if line contains GitHub link
            github_url = None
            if 'github' in lower_line:
                github_url = extract_url(line)
                if github_url and current_project:
                    current_project['github'] = github_url
                    continue
            
            # Detect if this is a project title line
            if any(keyword in lower_line for keyword in tech_keywords):
                # Try to split by common separators
                parts = None
                for sep in [':', '|', '-']:
                    if sep in line:
                        parts = [p.strip() for p in line.split(sep)]
                        break
                
                if not parts:
                    # Try to split based on tech keywords
                    parts = line.split()
                    name_parts = []
                    tech_parts = []
                    found_tech = False
                    for part in parts:
                        if not found_tech and part.lower() in tech_keywords:
                            found_tech = True
                        if found_tech:
                            tech_parts.append(part)
                        else:
                            name_parts.append(part)
                    name = ' '.join(name_parts)
                    tech = ' '.join(tech_parts)
                else:
                    name = parts[0]
                    tech = parts[1] if len(parts) > 1 else ''
                
                name = clean_text(name)
                if name and name not in seen_projects and not any(x in name.lower() for x in ['experience', 'education', 'skills']):
                    seen_projects.add(name)
                    current_project = {
                        'name': name,
                        'technologies': clean_text(tech),
                        'github': github_url,
                        'description': []
                    }
                    projects.append(current_project)
            elif current_project and line:
                # Add description if line starts with bullet or if previous line was a description
                if line.startswith('•') or (i > 0 and text_lines[i-1].strip().startswith('•')):
                    desc = line.lstrip('•').strip()
                    if desc and not any(x in desc.lower() for x in ['experience', 'education', 'skills']):
                        current_project['description'].append(clean_text(desc))
    
    return projects 