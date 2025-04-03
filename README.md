# Portfolio Website

A modern, responsive portfolio website built with Flask and Bootstrap.

## Features

- Single-page design with smooth scrolling
- Responsive layout that works on all devices
- Sections for About, Experience, Projects, Skills, and Contact
- Modern UI with animations and transitions
- Contact form for easy communication

## Project Structure

```
portfolio/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── utils/
│   │   └── resume_parser.py
│   ├── __init__.py
│   └── routes.py
├── run.py
├── requirements.txt
└── README.md
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python run.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000/`

## Customization

- Update the dummy data in `app/routes.py` with your personal information
- Add your profile picture to `app/static/images/`
- Modify the styles in `app/static/css/style.css`
- Add your own projects and experiences

## Future Enhancements

- Resume parser integration to automatically populate data
- Blog section
- Portfolio gallery
- Dark mode toggle
- Multi-language support

## License

This project is licensed under the MIT License - see the LICENSE file for details. 