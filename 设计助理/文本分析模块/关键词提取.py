import jieba.analyse

class KeywordExtractor:
    def __init__(self):
        pass

    def extract_keywords(self, text, topK=5):
        # 使用TF-IDF算法提取关键词
        keywords = jieba.analyse.extract_tags(text, topK=topK)
        return keywords

# 示例
extractor = KeywordExtractor()
keywords = extractor.extract_keywords(processed_text)
print(keywords)
