""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_ZOMBIE = 0.5
SPRITE_SCALING_PERSON = 0.3
SPRITE_SCALING_SAW = 0.1
PERSON_COUNT = 50
SAW_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Saw(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class Person(arcade.Sprite):

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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        self.zombie_list = None
        self.person_list = None
        self.saw_list = None

        self.coin_sound = arcade.load_sound("arcade_resources_sounds_coin2.wav")
        self.error_sound = arcade.load_sound("arcade_resources_sounds_error1.wav")

        self.zombie_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.DARK_RED)

    def setup(self):
        self.zombie_list = arcade.SpriteList()
        self.person_list = arcade.SpriteList()
        self.saw_list = arcade.SpriteList()

        self.score = 0

        self.zombie_sprite = arcade.Sprite("zombie_idle.png", SPRITE_SCALING_ZOMBIE)
        self.zombie_sprite.center_x = 50
        self.zombie_sprite.center_y = 50
        self.zombie_list.append(self.zombie_sprite)

        # Creating saws
        for i in range(SAW_COUNT):
            saw = Saw("saw.png", SPRITE_SCALING_SAW)

            saw.center_x = random.randrange(SCREEN_WIDTH)
            saw.center_y = random.randrange(SCREEN_HEIGHT)

            self.saw_list.append(saw)

        # Creating people
        for i in range(PERSON_COUNT):
            person = Person("malePerson_idle.png", SPRITE_SCALING_PERSON)

            person.center_x = random.randrange(SCREEN_WIDTH)
            person.center_y = random.randrange(SCREEN_HEIGHT)
            person.change_x = random.randrange(-3, 4)
            person.change_y = random.randrange(-3, 4)

            self.person_list.append(person)

    def on_draw(self):
        arcade.start_render()
        self.person_list.draw()
        self.zombie_list.draw()
        self.saw_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 28)
        if len(self.person_list) == 0:
            gameover = f"GAME OVER"
            arcade.draw_text(gameover, 300, 300, arcade.color.WHITE, 25)

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.person_list) > 0:
            self.zombie_sprite.center_x = x
            self.zombie_sprite.center_y = y

    def update(self, delta_time):
        if len(self.person_list) > 0:
            self.person_list.update()
            self.saw_list.update()
        person_hit_list = arcade.check_for_collision_with_list(self.zombie_sprite, self.person_list)
        for person in person_hit_list:
            person.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)
        saw_hit_list = arcade.check_for_collision_with_list(self.zombie_sprite, self.saw_list)
        for saw in saw_hit_list:
            saw.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.error_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
