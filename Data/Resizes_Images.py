import cv2
import os

#target_size = (100, 100)
def resize_images(image_directory, target_size, ):
    if not os.path.exists('resized'):
        os.makedirs('resized')

    for filename in os.listdir(image_directory):
        if filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(image_directory, filename))
            resized_img = cv2.resize(img, target_size)
            cv2.imwrite(os.path.join('resized', filename), resized_img)

# print('All images resized.')
