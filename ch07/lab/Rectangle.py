class Rectangle:
    def __init__(self, x, y, h, w):
        """
        __init__
        Initializes the Rectangle object with the given dimensions.

        Args:
        x (int): The x coordinate of the upper left corner of the rectangle.
        y (int): The y coordinate of the upper left corner of the rectangle.
        h (int): The height of the rectangle.
        w (int): The width of the rectangle.

        Returns:
        None
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

    def __str__(self):
        """
        Returns a string representation of the rectangle object.

        Returns:
        str: A string representation of the rectangle object.
        """
        return f"(x: {self.x}, y: {self.y}) width: {self.width}, height: {self.height}"