import matplotlib.pyplot as plt

class ColorPaletteDisplay:
    def __init__(self, colors):
        self.colors = colors

    def display_palette(self):
        # 创建一个颜色板
        plt.figure(figsize=(8, 2))
        for i, color in enumerate(self.colors):
            plt.fill_between([i, i+1], 0, 1, color=color)
        plt.gca().set_xlim(0, len(self.colors))
        plt.gca().axis('off')
        plt.show()

# 示例
colors = ["#FF5733", "#33FF57", "#3357FF"]  # 示例颜色
palette = ColorPaletteDisplay(colors)
palette.display_palette()
