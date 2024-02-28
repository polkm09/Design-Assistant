from PIL import Image
import numpy as np

class ImageProcessor:
    def __init__(self):
        pass

    def load_image(self, path):
        # 加载图像
        return Image.open(path)

    def preprocess_image(self, image):
        # 对图像进行预处理（例如：大小调整、归一化等）
        image = image.resize((224, 224))
        image = np.array(image) / 255.0
        return image

# 示例
processor = ImageProcessor()
image_path = "path/to/room/image.jpg"
image = processor.load_image(image_path)
preprocessed_image = processor.preprocess_image(image)
