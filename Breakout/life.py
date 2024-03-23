import arcade

class Life(arcade.Sprite):
    def __init__(self, x):
        super().__init__('D:\Assignment_16\Breakout\heart.png')
        self.center_x = x + 33
        self.center_y = 11
        self.width = 40
        self.height = 30
        self.angle = 360
        self.lose_life_sound = arcade.load_sound(':resources:sounds/lose2.wav',False)
    
    def lose_life(self):
        arcade.play_sound(self.lose_life_sound)
        
