"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 9"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """
    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None
        self.score = 0

        # Sound
        self.coin_sound = arcade.load_sound("arcade_resources_sounds_coin2.wav")

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0
        # Set up the player
        self.player_sprite = arcade.Sprite("robot_idle.png", scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        # Bottom wall
        for x in range(0, 1216, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 400
            self.wall_list.append(wall)
        # Left wall
        for y in range(464, 1216, 64):
            wall = arcade.Sprite("boxCrate.png", SPRITE_SCALING)
            wall.center_y = y
            wall.center_x = 0
            self.wall_list.append(wall)
        # Top wall
        for x in range(0, 1216, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1232
            self.wall_list.append(wall)
        # Right wall
        for y in range(464, 1216, 64):
            wall = arcade.Sprite("boxCrate.png", SPRITE_SCALING)
            wall.center_y = y
            wall.center_x = 1152
            self.wall_list.append(wall)
        for y in range(784, 1136, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_y = y
            wall.center_x = 128
            self.wall_list.append(wall)
        for y in range(528, 848, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_y = y
            wall.center_x = 1026
            self.wall_list.append(wall)
        for x in range(192, 965, 64):
            wall = arcade.Sprite("stoneMid.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1104
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[256, 528],
                           [192, 528],
                           [128, 528],
                           [128, 656],
                           [64, 656],
                           [256, 592],
                           [192, 784],
                           [256, 720],
                           [256, 784],
                           [320, 528],
                           [448, 528],
                           [320, 592],
                           [384, 656],
                           [448, 720],
                           [512, 784],
                           [512, 592],
                           [578, 464],
                           [642, 464],
                           [706, 464],
                           [642, 528],
                           [642, 592],
                           [642, 656],
                           [642, 720],
                           [706, 720],
                           [770, 656],
                           [770, 528],
                           [898, 528],
                           [834, 656],
                           [898, 592],
                           [1026, 528],
                           [1090, 912],
                           [962, 720],
                           [898, 784],
                           [834, 784],
                           [706, 784],
                           [770, 784],
                           [962, 784],
                           [962, 848],
                           [962, 976],
                           [962, 1040],
                           [1026, 1040],
                           [1026, 1104],
                           [320, 784],
                           [642, 784]]
        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("stoneCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Creating the coins
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
            coin_placed_successfully = False
            while not coin_placed_successfully:
                coin.center_x = random.randrange(0, 1152)
                coin.center_y = random.randrange(464, 1152)
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)
                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 28)
        if len(self.coin_list) == 0:
            gameover = f"GAME OVER"
            arcade.draw_text(gameover, 300, 300, arcade.color.WHITE, 25)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        if len(self.coin_list) > 0:
            self.coin_list.update()
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """
        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()