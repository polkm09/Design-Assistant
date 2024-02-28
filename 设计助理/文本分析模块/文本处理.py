import jieba
import re

class TextProcessor:
    def __init__(self):
        pass

    def clean_text(self, text):
        # 清洗文本，去除无关字符
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def segment_text(self, text):
        # 使用jieba进行中文分词
        return jieba.lcut(text)

    def process(self, text):
        # 文本处理流程
        cleaned_text = self.clean_text(text)
        segmented_text = self.segment_text(cleaned_text)
        return segmented_text

# 示例
processor = TextProcessor()
sample_text = "我喜欢现代简约风格，但不喜欢太过艳丽的颜色。"
processed_text = processor.process(sample_text)
print(processed_text)
