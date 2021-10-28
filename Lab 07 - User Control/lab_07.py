import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 5


class Jet:
    def __init__(self, position_x, position_y, change_x, change_y, radius):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        x = self.position_x
        y = self.position_y
        arcade.draw_triangle_filled(x, y, x + 50, y + 150, x - 50, y + 150, (84, 88, 81))
        arcade.draw_arc_filled(x, y + 35, 20, 40, (255, 255, 255), 0, 180)
        arcade.draw_triangle_filled(x - 75, y + 125, x - 10, y + 125, x - 10, y + 75, (84, 88, 81))
        arcade.draw_triangle_filled(x + 10, y + 75, x + 10, y + 125, x + 75, y + 125, (84, 88, 81))
        arcade.draw_line(x - 25, y + 140, x - 30, y + 170, (84, 88, 81), 6)
        arcade.draw_line(x + 25, y + 140, x + 30, y + 170, (84, 88, 81), 6)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.

        # So we just see our object, not the pointer.

        self.set_mouse_visible(False)

        # Create our ball
        self.jet = Jet(10, 10, 0, 0, 75)

        self.laser_sound = arcade.load_sound("arcade_resources_sounds_laser2.wav")

        self.explosion_sound = arcade.load_sound("arcade_resources_sounds_explosion2.wav")
        self.explosion_sound_jet = None

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        arcade.draw_ellipse_filled(100, 500, 60, 150, arcade.color.LIGHT_GRAY)
        arcade.draw_ellipse_filled(100, 500, 60, 150, arcade.color.LIGHT_GRAY, 50, 150)
        arcade.draw_ellipse_filled(100, 500, 60, 150, arcade.color.LIGHT_GRAY, 270)
        arcade.draw_ellipse_filled(100, 500, 60, 150, arcade.color.LIGHT_GRAY, 310)

        arcade.draw_ellipse_filled(400, 500, 60, 150, arcade.color.LIGHT_GRAY)
        arcade.draw_ellipse_filled(400, 500, 60, 150, arcade.color.LIGHT_GRAY, 50, 150)
        arcade.draw_ellipse_filled(400, 500, 60, 150, arcade.color.LIGHT_GRAY, 270)
        arcade.draw_ellipse_filled(400, 500, 60, 150, arcade.color.LIGHT_GRAY, 310)
        self.jet.draw()

    def update(self, delta_time):
        self.jet.update()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.

        Happens approximately 60 times per second."""

        self.jet.position_x = x

        self.jet.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.jet.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.jet.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.jet.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.jet.change_y = -MOVEMENT_SPEED
        if not self.explosion_sound_jet or not self.explosion_sound_jet.playing:
            self.explosion_sound_jet = arcade.play_sound(self.explosion_sound)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.jet.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.jet.change_y = 0

        self.jet.draw()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7")
    arcade.run()


main()
