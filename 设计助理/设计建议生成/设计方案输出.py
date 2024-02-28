def format_suggestions(suggestions):
    # 格式化设计建议输出
    formatted_suggestions = "\n".join([f"{key}: {value}" for key, value in suggestions.items()])
    return formatted_suggestions

# 示例
formatted_suggestions = format_suggestions(design_suggestions)
print(formatted_suggestions)
