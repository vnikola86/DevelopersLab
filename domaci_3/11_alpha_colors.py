from colors import Color

class AlphaColor(Color):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self._alpha = self._validate_alpha(alpha)

    def _validate_alpha(self, value):
        if 0 <= value <= 1:
            return value
        else:
            print("Invalid alpha value! Alpha value should be between 0 and 1.")
            return None

    def get_alpha(self):
        return self._alpha

    def set_alpha(self, value):
        self._alpha = self._validate_alpha(value)

    def update_color_by_alpha(self, alpha):
        self.set_red(self.get_red() * (1 - alpha))
        self.set_green(self.get_green() * (1 - alpha))
        self.set_blue(self.get_blue() * (1 - alpha))

    def __str__(self):
        return f"\"red\": {self.get_red()}, \"green\": {self.get_green()}, \"blue\": {self.get_blue()}, \"alpha\": {self.get_alpha()}"

# Example usage
alpha_color1 = AlphaColor(100, 125, 150, 0.3)
alpha_color2 = AlphaColor(150, 200, 250, 0.5)


print("Alpha Color 1:", alpha_color1)
print("Alpha Color 2:", alpha_color2)

alpha_color1.update_color_by_alpha(0.2)
alpha_color2.update_color_by_alpha(0.1)

print("Updated Alpha Color 1:", alpha_color1)
print("Updated Alpha Color 2:", alpha_color2)
