# 测试文本和图像分析模块
test_text = "我更偏爱温馨舒适的家居风格，不喜欢过于冷淡的色调。"
test_image_path = "test/room/image.jpg"

# 执行文本分析
test_processed_text = text_processor.process(test_text)
test_text_keywords = keyword_extractor.extract_keywords(test_processed_text)
test_sentiment = sentiment_analyzer.analyze_sentiment(test_text)

# 执行图像分析
test_image = image_processor.load_image(test_image_path)
test_preprocessed_image = image_processor.preprocess_image(test_image)
test_image_features = feature_extractor.extract_features(test_preprocessed_image)

# 输出测试结果
print("文本关键词:", test_text_keywords)
print("情感分析:", test_sentiment)
print("图像特征:", test_image_features)

# 进行更多的测试和验证...
