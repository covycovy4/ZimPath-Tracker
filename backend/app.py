from flask import Flask, request, render_template
import os
from analysis import run_minimap2

app = Flask(__name__)
UPLOAD_FOLDER = '../data'
REFERENCE = '../references/salmonella_typhi_ref.fasta'

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

        # Run minimap2 alignment
        result = run_minimap2(filepath, REFERENCE)

        if result:
            return f"<p>File uploaded and aligned successfully! ✅</p><p>Output: {result}</p>"
        else:
            return "❌ Minimap2 alignment failed."

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
