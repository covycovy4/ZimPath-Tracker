from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Create upload folder if it doesn't exist
UPLOAD_FOLDER = '../data'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["fastq"]
        if file.filename == "":
            return "No file selected"
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f"File {file.filename} uploaded successfully!"
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
