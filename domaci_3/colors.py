class Color:
    def __init__(self, red, green, blue):
        self._red = self._validate_color(red)
        self._green = self._validate_color(green)
        self._blue = self._validate_color(blue)

    def _validate_color(self, value):
        if 0 <= value <= 255:
            return value
        else:
            print("Invalid color value! Color value should be between 0 and 255.")
            return None

    def get_red(self):
        return self._red

    def set_red(self, value):
        self._red = self._validate_color(value)

    def get_green(self):
        return self._green

    def set_green(self, value):
        self._green = self._validate_color(value)

    def get_blue(self):
        return self._blue

    def set_blue(self, value):
        self._blue = self._validate_color(value)

    def add_red(self, change):
        new_red = self._red + change
        if 0 <= new_red <= 255:
            self._red = new_red
        else:
            print("Invalid color value! Red color value should be between 0 and 255.")

    def add_green(self, change):
        new_green = self._green + change
        if 0 <= new_green <= 255:
            self._green = new_green
        else:
            print("Invalid color value! Green color value should be between 0 and 255.")

    def add_blue(self, change):
        new_blue = self._blue + change
        if 0 <= new_blue <= 255:
            self._blue = new_blue
        else:
            print("Invalid color value! Blue color value should be between 0 and 255.")

    def __lt__(self, other):
        return (self._red, self._green, self._blue) < (other.get_red(), other.get_green(), other.get_blue())

    def __eq__(self, other):
        return (self._red, self._green, self._blue) == (other.get_red(), other.get_green(), other.get_blue())

    def __str__(self):
        return f"\"red\": {self._red}, \"green\": {self._green}, \"blue\": {self._blue}"


# Example usage
color1 = Color(50, 75, 100)
color2 = Color(100, 150, 200)

print("Color 1:", color1)
print("Color 2:", color2)

print("Is color1 less than color2?", color1 < color2)
print("Are color1 and color2 equal?", color1 == color2)

color1.add_red(-120)
color1.add_green(50)
color1.add_blue(100)

print("Modified Color 1:", color1)
