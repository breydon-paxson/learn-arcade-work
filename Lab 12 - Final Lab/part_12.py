""" Lab 12 Final """

# All images and sounds came from Python Arcade Library
# https://api.arcade.academy/en/latest/index.html
import math
import random
import arcade

# --- Constants ---
SPRITE_SCALING_SHIP = 0.5
SPRITE_SCALING_BIG_METEOR = 0.3
SPRITE_SCALING_SMALL_METEOR = 0.5
SPRITE_SCALING_LASER = .3
BIG_METEOR_COUNT = 20
SMALL_METEOR_COUNT = 20
SCALE = .3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 4
MAX_PLAYER_BULLETS = 100

ANGLE_SPEED = 5


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Menu Screen - click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        my_game = MyGame()
        my_game.setup()
        self.window.show_view(my_game)


class GameOverView(arcade.View):
    """ Class to manage the game over view """
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture("stars.png")

    def on_show(self):
        """ Called when switching to this view"""
        arcade.background = arcade.load_texture("stars.png")

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        gameover = f"GAME OVER"
        arcade.draw_text(gameover, 300, 300, arcade.color.RED, 25)

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.ESCAPE:
            menu_view = MenuView()
            self.window.show_view(menu_view)


class TurningSprite(arcade.Sprite):
    def update(self):
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x)) - 90


class Ship(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.speed = 0

    def update(self):
        angle_rad = math.radians(self.angle)

        self.angle += self.change_angle

        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)


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


class MyGame(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        self.ship_list = None
        self.big_meteor_list = None
        self.small_meteor_list = None
        self.bullet_list = None
        self.ship_life_list = None

        self.big_hit_sound = arcade.load_sound("arcade_resources_sounds_error4.wav")
        self.small_hit_sound = arcade.load_sound("arcade_resources_sounds_hit4.wav")
        self.gun_sound = arcade.load_sound("arcade_resources_sounds_laser2.wav")

        self.ship_sprite = None
        self.score = 0
        self.lives = 3

        self.background = None

    def setup(self):
        self.ship_list = arcade.SpriteList()
        self.big_meteor_list = arcade.SpriteList()
        self.small_meteor_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.ship_life_list = arcade.SpriteList()

        self.score = 0
        self.lives = 3

        # lives
        cur_pos = 680
        for i in range(self.lives):
            life = arcade.Sprite("playerShip1_orange.png", SCALE)
            life.center_x = cur_pos + life.width
            life.center_y = life.height
            cur_pos += life.width
            self.ship_life_list.append(life)

        self.ship_sprite = arcade.Sprite("playerShip1_orange.png", SPRITE_SCALING_SHIP)
        self.ship_sprite.center_x = 50
        self.ship_sprite.center_y = 50
        self.ship_list.append(self.ship_sprite)

        self.background = arcade.load_texture("stars.png")

        # Creating small meteor
        for i in range(SMALL_METEOR_COUNT):
            small_meteor = Small("small_meteor.png", SPRITE_SCALING_SMALL_METEOR)

            small_meteor.center_x = random.randrange(SCREEN_WIDTH)
            small_meteor.center_y = random.randrange(SCREEN_HEIGHT)

            self.small_meteor_list.append(small_meteor)

        # Creating big meteor
        for i in range(BIG_METEOR_COUNT):
            big_meteor = Big("big_meteor.png", SPRITE_SCALING_BIG_METEOR)

            big_meteor.center_x = random.randrange(SCREEN_WIDTH)
            big_meteor.center_y = random.randrange(SCREEN_HEIGHT)
            big_meteor.change_x = random.randrange(-3, 4)
            big_meteor.change_y = random.randrange(-3, 4)

            self.big_meteor_list.append(big_meteor)

    def on_draw(self):
        arcade.start_render()
        self.big_meteor_list.draw()
        self.ship_list.draw()
        self.small_meteor_list.draw()
        self.bullet_list.draw()
        self.ship_life_list.draw()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 28)
        if len(self.big_meteor_list) == 0 and len(self.small_meteor_list) == 0 or len(self.ship_life_list) == 0:
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)

    def on_mouse_press(self, x, y, button, modifiers):
        if (len(self.big_meteor_list) > 0 or len(self.small_meteor_list) > 0) and len(self.ship_life_list) > 0:
            if len(self.bullet_list) < MAX_PLAYER_BULLETS:
                arcade.play_sound(self.gun_sound)
                bullet = TurningSprite("laserRed01.png", SPRITE_SCALING_LASER)

                bullet.guid = "Bullet"

                # Bullet speed
                bullet.change_y = math.cos(math.radians(self.ship_sprite.angle)) * BULLET_SPEED
                bullet.change_x = -math.sin(math.radians(self.ship_sprite.angle)) * BULLET_SPEED

                # bullet position
                bullet.center_x = self.ship_sprite.center_x
                bullet.center_y = self.ship_sprite.center_y

                # add the bullet to list
                self.bullet_list.append(bullet)

    def on_key_press(self, key, modifiers):
        # turn left
        if key == arcade.key.A:
            self.ship_sprite.change_angle = ANGLE_SPEED
        # turn right
        elif key == arcade.key.D:
            self.ship_sprite.change_angle = -ANGLE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.ship_sprite.change_angle = 0

    def on_mouse_motion(self, x, y, dx, dy):
        if (len(self.big_meteor_list) > 0 or len(self.small_meteor_list) > 0) and len(self.ship_life_list) > 0:
            self.ship_sprite.center_x = x
            self.ship_sprite.center_y = y

    def process_ship_bullets(self):
        self.bullet_list.update()

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.big_meteor_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            for big_meteor in hit_list:
                big_meteor.remove_from_sprite_lists()
                self.score += 1

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.small_meteor_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            for small_meteor in hit_list:
                small_meteor.remove_from_sprite_lists()
                self.score += 5

    def update(self, delta_time):

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 28)
        if len(self.big_meteor_list) == 0 and len(self.small_meteor_list) == 0 or len(self.ship_life_list) == 0:
            gameover = f"GAME OVER"
            arcade.draw_text(gameover, 300, 300, arcade.color.RED, 25)
            return

        self.ship_sprite.angle += self.ship_sprite.change_angle

        if (len(self.big_meteor_list)) > 0 or (len(self.small_meteor_list)) > 0 and (len(self.ship_life_list)) > 0:
            self.big_meteor_list.update()
            self.small_meteor_list.update()
            self.ship_life_list.update()

        big_meteor_hit_list = arcade.check_for_collision_with_list(self.ship_sprite, self.big_meteor_list)
        for big in big_meteor_hit_list:
            big.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.big_hit_sound)
            if len(self.ship_life_list) > 0:
                self.ship_life_list[0].remove_from_sprite_lists()
                self.lives -= 1

        small_meteor_hit_list = arcade.check_for_collision_with_list(self.ship_sprite, self.small_meteor_list)
        for small in small_meteor_hit_list:
            small.remove_from_sprite_lists()
            self.score -= 5
            arcade.play_sound(self.small_hit_sound)
            if len(self.ship_life_list) > 0:
                self.ship_life_list[0].remove_from_sprite_lists()
                self.lives -= 1

        self.process_ship_bullets()


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 12")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
