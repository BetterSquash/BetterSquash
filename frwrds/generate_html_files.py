import os
import shutil

def generate_html_files():
    # Get the current directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths to the template and filenames list
    template_path = os.path.join(current_dir, "template.html")
    filenames_path = os.path.join(current_dir, "local-links.txt")
    
    # Check if the required files exist
    if not os.path.exists(template_path):
        print(f"Error: template.html not found in {current_dir}")
        return
    
    if not os.path.exists(filenames_path):
        print(f"Error: local-links.txt not found in {current_dir}")
        return
    
    # Read template content
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    
    # Read filenames from local-links.txt
    with open(filenames_path, 'r', encoding='utf-8') as filenames_file:
        filenames = [line.strip() for line in filenames_file if line.strip()]
    
    # Create directory for output files if it doesn't exist
    output_dir = current_dir
    os.makedirs(output_dir, exist_ok=True)
    
    # Count successful and failed file creations
    success_count = 0
    failed_files = []
    
    # Generate HTML files
    for filename in filenames:
        output_path = os.path.join(output_dir, filename)
        try:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(template_content)
            success_count += 1
        except Exception as e:
            failed_files.append((filename, str(e)))
    
    # Print summary
    print(f"HTML file generation complete!")
    print(f"Successfully created {success_count} out of {len(filenames)} files")
    
    if failed_files:
        print(f"Failed to create {len(failed_files)} files:")
        for filename, error in failed_files:
            print(f"  - {filename}: {error}")

if __name__ == "__main__":
    generate_html_files()