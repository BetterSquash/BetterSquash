import os
import qrcode
from PIL import Image
from urllib.parse import quote

def generate_qr_codes_with_logo():
    # Get the current directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths to the filenames list and logo
    filenames_path = os.path.join(current_dir, "local-links.txt")
    logo_path = os.path.join(current_dir, "logo.png")  # Your logo file
    
    # Check if the required files exist
    if not os.path.exists(filenames_path):
        print(f"Error: local-links.txt not found in {current_dir}")
        return
        
    if not os.path.exists(logo_path):
        print(f"Error: logo.png not found in {current_dir}")
        print("Please place your logo image named 'logo.png' in the same directory")
        return
    
    # Create a directory for QR codes
    qr_dir = os.path.join(current_dir, "qr_codes")
    os.makedirs(qr_dir, exist_ok=True)
    
    # Read filenames from local-links.txt
    with open(filenames_path, 'r', encoding='utf-8') as filenames_file:
        filenames = [line.strip() for line in filenames_file if line.strip()]
    
    # Base URL - change this to your website's base URL
    base_url = "https://bettersquash.com/frwrds/"  # Replace with your actual domain
    
    # Open the logo image
    logo = Image.open(logo_path)
    
    # Set dimensions preserving aspect ratio
    logo_width = 128
    logo_height = 88
    
    # Resize the logo while preserving aspect ratio
    logo = logo.resize((logo_width, logo_height), Image.LANCZOS)
    
    # QR code size
    qr_size = 600
    
    # Calculate logo position offset for center placement
    logo_pos = ((qr_size - logo_width) // 2, (qr_size - logo_height) // 2)
    
    # Count successful and failed QR code creations
    success_count = 0
    failed_files = []
    
    # Generate QR codes
    for filename in filenames:
        try:
            # Create the full URL (properly encoded)
            full_url = base_url + quote(filename)
            
            # Create QR code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction for logo
                box_size=20,  # Increased box size for higher resolution
                border=4,
            )
            
            # Add data to the QR code
            qr.add_data(full_url)
            qr.make(fit=True)
            
            # Create an image from the QR code
            qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
            
            # Resize to exactly 600x600
            qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)
            
            # Paste the logo in the center of the QR code
            qr_img.paste(logo, logo_pos, logo if logo.mode == 'RGBA' else None)
            
            # Save the image
            qr_filename = os.path.splitext(filename)[0] + ".png"
            qr_path = os.path.join(qr_dir, qr_filename)
            qr_img.save(qr_path)
            
            success_count += 1
            
        except Exception as e:
            failed_files.append((filename, str(e)))
    
    # Print summary
    print(f"QR code generation with logo complete!")
    print(f"Successfully created {success_count} out of {len(filenames)} QR codes")
    print(f"QR codes saved in: {qr_dir}")
    
    if failed_files:
        print(f"Failed to create {len(failed_files)} QR codes:")
        for filename, error in failed_files:
            print(f"  - {filename}: {error}")

if __name__ == "__main__":
    # Check if required libraries are installed
    try:
        import qrcode
        from PIL import Image
    except ImportError as e:
        missing_lib = str(e).split("'")[1]
        print(f"The '{missing_lib}' library is not installed.")
        print("Please install required libraries by running: pip install qrcode pillow")
        exit(1)
        
    generate_qr_codes_with_logo()