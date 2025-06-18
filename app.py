from flask import Flask, request, jsonify, render_template_string
from PIL import Image
import io
import model
from PIL import ImageOps
import os

app = Flask(__name__)

UPLOAD_FORM = """
<!doctype html>
<title>Image Upscaler</title>
<h1>Upload an image to upscale (2x)</h1>
<form method=post enctype=multipart/form-data action="/upscale">
  <input type=file name=image>
  <input type=submit value="Upscale">
</form>
"""

@app.route('/')
def index():
    return render_template_string(UPLOAD_FORM)

@app.route('/upscale', methods=['POST'])
def upscale():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    try:
        file = request.files['image']
        image = Image.open(file.stream)
        image = ImageOps.exif_transpose(image) 
        image = image.convert("RGB")

        if image.format == 'PDF':
            image = image.convert("RGB")

        result_image = model.predict(image)

        img_io = io.BytesIO()
        result_image.save(img_io, 'JPEG')
        img_io.seek(0)

        orig_filename = os.path.splitext(file.filename)[0]
        download_name = f"{orig_filename}-upscaled.jpg"

        return (
            img_io.read(),
            200,
            {
                'Content-Type': 'image/jpeg',
                'Content-Disposition': f'attachment; filename="{download_name}"'
            }
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)