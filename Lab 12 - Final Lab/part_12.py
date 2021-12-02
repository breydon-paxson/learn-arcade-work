""" Lab 12 Final """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_SHIP = 0.5
SPRITE_SCALING_BIG_METEOR = 0.3
SPRITE_SCALING_SMALL_METEOR = 0.1
BIG_METEOR_COUNT = 50
SMALL_METEOR_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Small(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class Big(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x

        if self.left < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 12")

        self.ship_list = None
        self.big_meteor_list = None
        self.small_meteor_list = None

        self.coin_sound = arcade.load_sound("arcade_resources_sounds_coin2.wav")
        self.error_sound = arcade.load_sound("arcade_resources_sounds_error1.wav")

        self.ship_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.DARK_RED)

    def setup(self):
        self.ship_list = arcade.SpriteList()
        self.big_meteor_list = arcade.SpriteList()
        self.small_meteor_list = arcade.SpriteList()

        self.score = 0

        self.ship_sprite = arcade.Sprite("playerShip1_orange.png", SPRITE_SCALING_SHIP)
        self.ship_sprite.center_x = 50
        self.ship_sprite.center_y = 50
        self.ship_list.append(self.ship_sprite)

        # Creating small meteor
        for i in range(SMALL_METEOR_COUNT):
            small_meteor = Small("saw.png", SPRITE_SCALING_SMALL_METEOR)

            small_meteor.center_x = random.randrange(SCREEN_WIDTH)
            small_meteor.center_y = random.randrange(SCREEN_HEIGHT)

            self.saw_list.append(small_meteor)

        # Creating big meteor
        for i in range(BIG_METEOR_COUNT):
            big_meteor = Big("big_meteor.png", SPRITE_SCALING_BIG_METEOR)

            big_meteor.center_x = random.randrange(SCREEN_WIDTH)
            big_meteor.center_y = random.randrange(SCREEN_HEIGHT)
            big_meteor.change_x = random.randrange(-3, 4)
            big_meteor.change_y = random.randrange(-3, 4)

            self.person_list.append(big_meteor)

    def on_draw(self):
        arcade.start_render()
        self.big_meteor_list.draw()
        self.ship_list.draw()
        self.small_meteor_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 28)
        if len(self.big_meteor_list) == 0:
            gameover = f"GAME OVER"
            arcade.draw_text(gameover, 300, 300, arcade.color.WHITE, 25)

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.big_meteor_list) > 0:
            self.ship_sprite.center_x = x
            self.ship_sprite.center_y = y

    def update(self, delta_time):
        if len(self.big_meteor_list) > 0:
            self.big_meteor_list.update()
            self.small_meteor_list.update()
        big_meteor_hit_list = arcade.check_for_collision_with_list(self.ship_sprite, self.big_meteor_list)
        for big in big_meteor_hit_list:
            big.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)
        small_meteor_hit_list = arcade.check_for_collision_with_list(self.ship_sprite, self.small_meteor_list)
        for small in small_meteor_hit_list:
            small.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.error_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
