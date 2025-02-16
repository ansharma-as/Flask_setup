from flask import Flask , render_template ,  Response
import cv2

app = Flask(__name__)
camera=cv2.VideoCapture(0)


def gen_frames():
    while True:
        ## read the frame continously in while loop
        success,frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            #yeild keyword is used to return the frame continously in the form of bytes
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ =="__main__":
    app.run(debug=True)