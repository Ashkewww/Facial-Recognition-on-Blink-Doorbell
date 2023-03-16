import cv2
import os
import dlib

# This Function resizes all the images in the given directory into a the given size
def resize_images(images, target_size):
    
    if type(images) == str:
        if not os.path.exists('resized'):
            os.makedirs('resized')
        for filename in os.listdir(images):
            if filename.endswith('.jpg'):
                img = cv2.imread(os.path.join(images, filename))
                resized_img = cv2.resize(img, target_size)
                cv2.imwrite(os.path.join('resized', filename), resized_img)
    else:
        resized_images = []
        for image in images:
            res_img = cv2.resize(image, target_size)
            resize_images.append(res_img)
        return resized_images
                


# This function returns a list of all the images present in the 

def extract_images(pathToVideo: str) -> list:
    detector = dlib.get_frontal_face_detector()
    vid = cv2.VideoCapture(pathToVideo)
    success, frame = vid.read()
    images = []
    while vid.isOpened():
        if success:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)
            
            for face in faces:
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()
                face_img = frame[y1:y2,x1:x2]
                images.append(face_img)
                
    return images


imag = extract_images("/home/ayush/Projects/Facial-Recognition-on-Blink-Doorbell/Data/Vids/Usable (4).mp4")
imag = resize_images(imag, (100,100))

