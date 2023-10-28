import cv2


class Webcam:

    def __init__(self):

        self.cap = cv2.VideoCapture(0)

    

    def open(self):

        if not self.cap.isOpened():

            self.cap.open(0)

    

    def close(self):

        if self.cap.isOpened():

            self.cap.release()

    

    def change_color_space(self, color_space):

        if color_space == 'bgr':

            return

        elif color_space == 'rgb':

            _, frame = self.cap.read()

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            return frame

    

    def convert_to_binary(self, threshold=127):

        _, frame = self.cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

        return binary

    

    def apply_threshold(self, value):

        _, frame = self.cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        _, binary = cv2.threshold(gray, value, 255, cv2.THRESH_BINARY)

        

       

        result = cv2.bitwise_and(frame, frame, mask=binary)

        

        return result



webcam = Webcam()

webcam.open()



frame_rgb = webcam.change_color_space('rgb')



binary_image = webcam.convert_to_binary()




thresholded_image = webcam.apply_threshold(150)


webcam.close()

