# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Lab_2"
# Set the dimensions
arcade.open_window(600, 600, "Lab 2")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.color.BITTER_LIME)

# Draw the clouds
arcade.draw_ellipse_filled(100, 500, 60, 150, arcade.color.LIGHT_GRAY)
arcade.draw_ellipse_filled(100, 500, 60, 150, arcade.color.LIGHT_GRAY, 50, 150)
arcade.draw_ellipse_filled(100, 500, 60, 150, arcade.color.LIGHT_GRAY, 270)
arcade.draw_ellipse_filled(100, 500, 60, 150, arcade.color.LIGHT_GRAY, 310)

# Draw the clouds
arcade.draw_ellipse_filled(500, 400, 60, 150, arcade.color.LIGHT_GRAY)
arcade.draw_ellipse_filled(500, 400, 60, 150, arcade.color.LIGHT_GRAY, 50, 150)
arcade.draw_ellipse_filled(500, 400, 60, 150, arcade.color.LIGHT_GRAY, 270)
arcade.draw_ellipse_filled(500, 400, 60, 150, arcade.color.LIGHT_GRAY, 310)

# Draw the jet body
arcade.draw_triangle_filled(300, 300, 350, 450, 250, 450, (84, 88, 81))

# Draw the jet window
arcade.draw_arc_filled(300, 335, 20, 40, (255, 255, 255), 0, 180)

# Draw the left jet wing
arcade.draw_triangle_filled(215, 425, 290, 425, 290, 375, (84, 88, 81))

# Draw the right jet wing
arcade.draw_triangle_filled(310, 375, 310, 425, 375, 425, (84, 88, 81))

# Draw the left tail wing
arcade.draw_line(275, 440, 270, 470, (84, 88, 81), 6)

# Draw the right tail wing
arcade.draw_line(325, 440, 330, 470, (84, 88, 81), 6)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
