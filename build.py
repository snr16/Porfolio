from app import app
from flask import url_for
import os
import shutil

def build_static_site():
    # Create build directory
    build_dir = 'build'
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)

    # Copy static files
    static_dir = os.path.join(build_dir, 'static')
    shutil.copytree('app/static', static_dir)

    # Generate HTML files
    routes = ['/', '/about', '/experience', '/projects', '/skills', '/contact']
    
    with app.test_client() as client:
        for route in routes:
            response = client.get(route)
            if response.status_code == 200:
                # Create the file path
                if route == '/':
                    file_path = os.path.join(build_dir, 'index.html')
                else:
                    # Remove leading slash and create directory if needed
                    path = route[1:]
                    dir_path = os.path.join(build_dir, os.path.dirname(path))
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)
                    file_path = os.path.join(build_dir, f"{path}.html")
                
                # Write the HTML content
                with open(file_path, 'wb') as f:
                    f.write(response.data)
                print(f"Generated {file_path}")
            else:
                print(f"Error generating {route}: {response.status_code}")

if __name__ == '__main__':
    with app.app_context():
        build_static_site()
    print("\nStatic site generated in the 'build' directory") 