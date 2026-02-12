from flask import Flask, render_template, request, send_from_directory
import cv2
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        grayscale_option = request.form.get("grayscale")

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        img = cv2.imread(filepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.2, 6)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(img, f"Faces: {len(faces)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        if grayscale_option:
            img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        cv2.imwrite(filepath, img)

        return render_template("index.html",
                               image=filepath,
                               face_count=len(faces),
                               filename=file.filename)

    return render_template("index.html", image=None, face_count=None)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
