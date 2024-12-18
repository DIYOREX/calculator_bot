class Line:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Line with width {self.width} and height {self.height}"

    def __bool__(self):
        return self.width > 0 and self.height > 0

    def __len__(self):
        return self.width + self.height

    def __repr__(self):
        return f"line({self.width}, {self.height})"
