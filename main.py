import cv2
import numpy as np
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

ARUCO_REAL_SIZE_MM = 10.0
TARGET_DIST_MIN_MM = 4.0
TARGET_DIST_MAX_MM = 5.0

class MeltTestApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10)
        self.image_widget = Image()
        self.layout.add_widget(self.image_widget)
        self.status_label = Label(text="Ожидание...", size_hint_y=0.2, markup=True)
        self.layout.add_widget(self.status_label)
        
        self.capture = cv2.VideoCapture(0)
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        self.aruco_params = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(self.aruco_dict, self.aruco_params)
        self.px_to_mm = 0.1

        Clock.schedule_interval(self.update, 1.0 / 20.0)
        return self.layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if not ret: return
        h, w, _ = frame.shape
        obj_x, melt_x = None, None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = self.detector.detectMarkers(gray)
        if ids is not None:
            c = corners[0][0]
            obj_x = int((c[0][0] + c[2][0]) / 2)
            marker_width_px = np.linalg.norm(c[0] - c[1])
            if marker_width_px > 1:
                self.px_to_mm = ARUCO_REAL_SIZE_MM / marker_width_px
            cv2.polylines(frame, [c.astype(int)], True, (0, 0, 255), 2)

        _, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            if M["m00"] > 10:
                melt_x = int(M["m10"] / M["m00"])
                cv2.line(frame, (melt_x, 0), (melt_x, h), (255, 0, 0), 2)

        if obj_x is not None and melt_x is not None:
            min_px = int(TARGET_DIST_MIN_MM / self.px_to_mm)
            max_px = int(TARGET_DIST_MAX_MM / self.px_to_mm)
            cv2.rectangle(frame, (melt_x - max_px, 0), (melt_x - min_px, h), (0, 255, 0), 2)
            current_dist_mm = (melt_x - obj_x) * self.px_to_mm
            if current_dist_mm < TARGET_DIST_MIN_MM:
                self.status_label.text = f"Дистанция: {current_dist_mm:.2f} мм\n[color=ff3333]БЛИЗКО[/color]"
            elif current_dist_mm > TARGET_DIST_MAX_MM:
                self.status_label.text = f"Дистанция: {current_dist_mm:.2f} мм\n[color=ffff33]ДАЛЕКО[/color]"
            else:
                self.status_label.text = f"Дистанция: {current_dist_mm:.2f} мм\n[color=33ff33]ОК[/color]"

        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(w, h), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image_widget.texture = texture

if __name__ == '__main__':
    MeltTestApp().run()
