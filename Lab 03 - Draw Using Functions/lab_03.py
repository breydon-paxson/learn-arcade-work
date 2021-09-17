# Import the "arcade" library
import arcade


def draw_clouds(x, y):
    arcade.draw_ellipse_filled(x, y, 60, 150, arcade.color.LIGHT_GRAY)
    arcade.draw_ellipse_filled(x, y, 60, 150, arcade.color.LIGHT_GRAY, 50, 150)
    arcade.draw_ellipse_filled(x, y, 60, 150, arcade.color.LIGHT_GRAY, 270)
    arcade.draw_ellipse_filled(x, y, 60, 150, arcade.color.LIGHT_GRAY, 310)


def draw_jet(x, y):
    arcade.draw_triangle_filled(x, y, x + 50, y + 150, x - 50, y + 150, (84, 88, 81))
    arcade.draw_arc_filled(x, y + 35, 20, 40, (255, 255, 255), 0, 180)
    arcade.draw_triangle_filled(x - 75, y + 125, x - 10, y + 125, x - 10, y + 75, (84, 88, 81))
    arcade.draw_triangle_filled(x + 10, y + 75, x + 10, y + 125, x + 75, y + 125, (84, 88, 81))
    arcade.draw_line(x - 25, y + 140, x - 30, y + 170, (84, 88, 81), 6)
    arcade.draw_line(x + 25, y + 140, x + 30, y + 170, (84, 88, 81), 6)


def draw_sun(x, y):
    arcade.draw_circle_filled(x, y, 50, arcade.color.YELLOW, 0, 180)
    arcade.draw_line(x + 100, y, x - 100, y, arcade.color.YELLOW, 3)
    arcade.draw_line(x, y - 100, x, y + 100, arcade.color.YELLOW, 3)


def main():
    arcade.open_window(600, 600, "Lab 2")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.start_render()

    draw_clouds(100, 500)
    draw_clouds(500, 100)
    draw_jet(100, 50)
    draw_jet(300, 225)
    draw_jet(500, 400)
    draw_sun(300, 500)


# --- Finish drawing ---
    arcade.finish_render()
    arcade.run()


main()