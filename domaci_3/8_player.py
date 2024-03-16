class Player:
    def __init__(self, x, y, width, height, health):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._health = health

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_health(self):
        return self._health

    def set_health(self, health):
        if 0 <= health <= 100:
            self._health = health
        else:
            print("Invalid health value! Health should be between 0 and 100.")

    def decrease_health(self, damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0


class Enemy:
    def __init__(self, x, y, width, height, damage):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._damage = damage

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_damage(self):
        return self._damage

    def set_damage(self, damage):
        if 0 <= damage <= 100:
            self._damage = damage
        else:
            print("Invalid damage value! Damage should be between 0 and 100.")


def check_collision(player, enemy):
    # Check if the bounding boxes of player and enemy overlap
    player_left = player.get_x()
    player_right = player.get_x() + player.get_width()
    player_bottom = player.get_y()
    player_top = player.get_y() + player.get_height()

    enemy_left = enemy.get_x()
    enemy_right = enemy.get_x() + enemy.get_width()
    enemy_bottom = enemy.get_y()
    enemy_top = enemy.get_y() + enemy.get_height()

    if (player_left < enemy_right and player_right > enemy_left and
            player_top > enemy_bottom and player_bottom < enemy_top):
        return True
    return False


def decrease_health(player, enemy):
    if check_collision(player, enemy):
        player.decrease_health(enemy.get_damage())


# Example usage
player = Player(x=10, y=10, width=20, height=20, health=100)
enemy1 = Enemy(x=15, y=15, width=10, height=10, damage=20)
enemy2 = Enemy(x=100, y=100, width=15, height=15, damage=30)

print("Initial player health:", player.get_health())

# Test collision with enemy1
print("Collision with enemy1:", check_collision(player, enemy1))
decrease_health(player, enemy1)
print("Player health after collision with enemy1:", player.get_health())

# Test collision with enemy2
print("Collision with enemy2:", check_collision(player, enemy2))
decrease_health(player, enemy2)
print("Player health after collision with enemy2:", player.get_health())
