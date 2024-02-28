def display_style_elements(style):
    # 展示设计风格的关键元素
    elements = {
        "现代简约": ["简洁线条", "中性色调", "极简布局"],
        # 可以根据需要添加更多风格和对应的元素
    }
    if style in elements:
        print(f"风格：{style}")
        for element in elements[style]:
            print(f"- {element}")

# 示例
style = "现代简约"
display_style_elements(style)
