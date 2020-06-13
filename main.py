from flask import Flask, render_template, Response
from face_detect import VideoCamera

import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(face_detect):
    while True:
        img = face_detect.get_frame()
        frame1=cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
