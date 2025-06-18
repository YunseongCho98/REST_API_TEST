from PIL import Image

def predict(image: Image.Image) -> Image.Image:
    # 여기에서 실제 ESRGAN 등 업스케일링 처리
    # 예시로 그냥 크기만 2배로 늘림
    return image.resize((image.width * 2, image.height * 2))