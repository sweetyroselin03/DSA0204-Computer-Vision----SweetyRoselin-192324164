import cv2
import matplotlib.pyplot as plt

# Load the image
image_path =r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\parrot.webp"
image = cv2.imread(image_path)

# Check if the image is loaded
if image is None:
    print("Error: Image not found.")
else:
    # Copy image to avoid modifying original
    watermarked = image.copy()

    # Define watermark properties
    watermark_text = 'Parrot'
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale =10 # Larger scale for visibility
    thickness = 20  # Thicker text
    color = (255, 255, 255)  # White
    shadow = (0, 0, 0)  # Black shadow for contrast

    # Compute position for bottom-left corner
    text_size = cv2.getTextSize(watermark_text, font, font_scale, thickness)[0]
    x = 10
    y = image.shape[0] - 10

    # Optional: Add shadow for better visibility
    cv2.putText(watermarked, watermark_text, (x + 2, y + 2), font, font_scale, shadow, thickness, cv2.LINE_AA)
    cv2.putText(watermarked, watermark_text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

    # Display the result
    plt.figure(figsize=(10, 6))
    plt.title("Image with Watermark")
    plt.imshow(cv2.cvtColor(watermarked, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
