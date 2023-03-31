from Rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Initializes the Surface object with the given image file name and rectangle dimensions.

        Args:
        filename (str): The name of the image file.
        x (int): The x coordinate of the upper left corner of the surface.
        y (int): The y coordinate of the upper left corner of the surface.
        h (int): The height of the surface.
        w (int): The width of the surface.

        Returns:
        Nothing.
        """
        self.image = filename
        self.rect = Rectangle(x, y, h, w)

    def getRect(self):
        """
        Returns the rectangle object associated with the surface.

        Returns:
        Rectangle
            The rectangle object associated with the surface.
        """
        return self.rect
