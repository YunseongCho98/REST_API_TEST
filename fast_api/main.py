from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from PIL import Image, ImageOps
import io
import os
import model

# uvicorn main:app --host 0.0.0.0 --port 5001

app = FastAPI()
templates = Jinja2Templates(directory=".")

UPLOAD_FORM = """
<!doctype html>
<title>Image Upscaler</title>
<h1>Upload an image to upscale (2x)</h1>
<form method=post enctype=multipart/form-data action="/upscale">
  <input type=file name=image>
  <input type=submit value="Upscale">
</form>
"""

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(content=UPLOAD_FORM)

@app.post("/upscale")
async def upscale(image: UploadFile = File(...)):
    try:
        contents = await image.read()
        img = Image.open(io.BytesIO(contents))
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")

        if img.format == 'PDF':
            img = img.convert("RGB")

        result_image = model.predict(img)

        img_io = io.BytesIO()
        result_image.save(img_io, format='JPEG')
        img_io.seek(0)

        orig_filename = os.path.splitext(image.filename)[0]
        download_name = f"{orig_filename}-upscaled.jpg"

        return StreamingResponse(
            img_io,
            media_type="image/jpeg",
            headers={
                "Content-Disposition": f'attachment; filename="{download_name}"'
            }
        )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)