import tensorflow as tf

class FeatureExtractor:
    def __init__(self, model):
        self.model = model

    def extract_features(self, image):
        # 使用预训练的CNN模型提取特征
        return self.model.predict(np.expand_dims(image, axis=0))

# 示例
# 加载预训练的CNN模型（例如：VGG16）
model = tf.keras.applications.VGG16(weights='imagenet', include_top=False)
extractor = FeatureExtractor(model)
features = extractor.extract_features(preprocessed_image)
