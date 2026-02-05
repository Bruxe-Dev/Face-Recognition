import cv2
import os
from datetime import datetime
import time

# Create a folder to store captured images
output_folder = "captured_faces"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created folder: {output_folder}")

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Webcam started successfully!")
print(f"Images will be saved to: {os.path.abspath(output_folder)}")

# Counter for images
image_count = 0
last_capture_time = time.time()

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture image")
        break
    
    # Display the live feed
    cv2.imshow('Webcam Feed - Press Q to quit', frame)
    
    # Check if 5 seconds have passed
    current_time = time.time()
    if current_time - last_capture_time >= 5:
        # Generate timestamp for filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"face_{timestamp}.jpg"
        filepath = os.path.join(output_folder, filename)
        
        # Save the image
        cv2.imwrite(filepath, frame)
        image_count += 1
        print(f"Captured image {image_count}: {filename}")
        
        # Update last capture time
        last_capture_time = current_time
    
    # Check if 'q' key is pressed to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\nQuitting...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print(f"\nTotal images captured: {image_count}")
print(f"Images saved in: {os.path.abspath(output_folder)}")