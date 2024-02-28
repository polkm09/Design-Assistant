class DesignSuggestionGenerator:
    def __init__(self, preferences, dislikes):
        self.preferences = preferences
        self.dislikes = dislikes

    def generate_suggestions(self):
        # 生成设计建议
        suggestions = {
            "style": "选择适合的风格",
            "color": "推荐搭配颜色",
            "layout": "建议布局方案"
        }

        # 根据用户偏好和不喜欢的元素调整建议
        if self.preferences["style"]:
            suggestions["style"] = f"推荐风格：{self.preferences['style']}"
        if "艳丽的颜色" in self.dislikes:
            suggestions["color"] = "避免使用过于艳丽的颜色"

        return suggestions

# 示例
generator = DesignSuggestionGenerator(preferences, dislikes)
design_suggestions = generator.generate_suggestions()
print(design_suggestions)
