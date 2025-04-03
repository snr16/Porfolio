import PyPDF2
import os

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
            
            # TODO: Add more sophisticated parsing logic here
            # For now, we'll just return the raw text
            return {
                'raw_text': text,
                'status': 'success'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        } 