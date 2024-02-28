# 假设这是通过API接收到的数据
received_text = "我喜欢现代简约风格，但不喜欢太过艳丽的颜色。"
received_image_path = "path/to/room/image.jpg"

# 文本分析
text_processor = TextProcessor()
processed_text = text_processor.process(received_text)

keyword_extractor = KeywordExtractor()
text_keywords = keyword_extractor.extract_keywords(processed_text)

sentiment_analyzer = SentimentAnalyzer()
sentiment = sentiment_analyzer.analyze_sentiment(received_text)

# 图像分析
image_processor = ImageProcessor()
image = image_processor.load_image(received_image_path)
preprocessed_image = image_processor.preprocess_image(image)

feature_extractor = FeatureExtractor(model)
image_features = feature_extractor.extract_features(preprocessed_image)

# 偏好和不喜欢元素识别
preference_identifier = PreferenceIdentifier(text_keywords, image_features)
preferences = preference_identifier.identify_preferences()

dislike_identifier = DislikeIdentifier(text_keywords)
dislikes = dislike_identifier.identify_dislikes()

# 生成设计建议
design_suggestion_generator = DesignSuggestionGenerator(preferences, dislikes)
design_suggestions = design_suggestion_generator.generate_suggestions()

# 可视化展示
formatted_suggestions = format_suggestions(design_suggestions)
print(formatted_suggestions)

# 示例颜色和风格展示（根据实际情况修改）
colors = ["#FF5733", "#33FF57", "#3357FF"]
palette = ColorPaletteDisplay(colors)
palette.display_palette()

style = "现代简约"
display_style_elements(style)
