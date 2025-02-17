import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self, game_width, game_height):
        super().__init__()
        self.center_x = game_width // 2
        self.center_y = game_height // 2
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.color = arcade.color.YELLOW
        self.speed = 5
        self.radius = 15
        self.width = self.radius * 2
        self.height = self.radius * 2

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
