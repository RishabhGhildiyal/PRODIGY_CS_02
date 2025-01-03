from PIL import Image
import os

def encrypt_image(input_path, output_path):
    """
    Encrypt an image by swapping the red and blue channels for each pixel.
    
    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the encrypted image.
    """
    # Validate input path
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return
    
    try:
        # Open the image and load its pixel data
        img = Image.open(input_path)
        img = img.convert("RGB")  # Ensure the image is in RGB mode
        pixels = img.load()
        width, height = img.size

        # Process each pixel: swap red and blue channels
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (b, g, r)  # Swap red and blue channels

        img.save(output_path)
        print(f"Image encrypted successfully and saved to '{output_path}'!")
    except Exception as e:
        print(f"Error during encryption: {e}")


def decrypt_image(input_path, output_path):
    """
    Decrypt an image by swapping the red and blue channels back to their original positions.
    
    Args:
        input_path (str): Path to the encrypted image.
        output_path (str): Path to save the decrypted image.
    """
    # Validate input path
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return
    
    try:
        # Open the image and load its pixel data
        img = Image.open(input_path)
        img = img.convert("RGB")  # Ensure the image is in RGB mode
        pixels = img.load()
        width, height = img.size

        # Process each pixel: swap red and blue channels back
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (b, g, r)  # Restore original channel order

        img.save(output_path)
        print(f"Image decrypted successfully and saved to '{output_path}'!")
    except Exception as e:
        print(f"Error during decryption: {e}")


if __name__ == "__main__":
    try:
        # Ask the user for input and output paths
        input_image = input("Enter the path to the input image: ").strip()
        encrypted_image = input("Enter the path to save the encrypted image (e.g., encrypted_image.jpg): ").strip()
        decrypted_image = input("Enter the path to save the decrypted image (e.g., decrypted_image.jpg): ").strip()

        # Encrypt the image
        print("\nEncrypting the image...")
        encrypt_image(input_image, encrypted_image)

        # Decrypt the image
        print("\nDecrypting the image...")
        decrypt_image(encrypted_image, decrypted_image)
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        input("\nPress Enter to exit...")
