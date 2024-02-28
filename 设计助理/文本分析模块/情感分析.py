from snownlp import SnowNLP

class SentimentAnalyzer:
    def __init__(self):
        pass

    def analyze_sentiment(self, text):
        # 使用SnowNLP进行情感分析
        s = SnowNLP(text)
        # SnowNLP的sentiments方法返回一个介于0到1之间的值，表示情感倾向
        return s.sentiments

# 示例
analyzer = SentimentAnalyzer()
sentiment = analyzer.analyze_sentiment(sample_text)
print(f"情感倾向: {sentiment} (接近1表示正面情感，接近0表示负面情感)")
