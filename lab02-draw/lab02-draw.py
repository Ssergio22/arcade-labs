import arcade
#from arcade import draw_rectangle_filled

arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()


def planeta():
    arcade.draw_circle_filled(400, 300, 180, arcade.color.GAINSBORO,0)
    arcade.draw_circle_filled(400, 300, 177, arcade.color.JADE,0)
def hamaca():
    arcade.draw_arc_filled(400, 260, 350, 80, arcade.color.ARSENIC,180,360)
    arcade.draw_arc_filled(400, 280, 350, 80, arcade.color.GO_GREEN,180,360)
def estrellas():
    arcade.draw_circle_filled(750, 40, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(200, 100, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(100, 400, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(500, 550, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(640, 200, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(300, 600, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(450, 70, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(700, 300, 4, arcade.color.ANTI_FLASH_WHITE,0)
def G():
    arcade.draw_circle_filled(280, 300, 19, arcade.color.ARSENIC,0)
    arcade.draw_ellipse_filled(385,284,200,20,arcade.color.ARSENIC,5)

    arcade.draw_ellipse_filled(515,285,90,10,arcade.color.ARSENIC,-10)
    arcade.draw_ellipse_filled(480,295,60,10,arcade.color.ARSENIC,-38)
    arcade.draw_ellipse_filled(518,310,40,10,arcade.color.ARSENIC,7)

    arcade.draw_ellipse_filled(350,295,50,10,arcade.color.ARSENIC,-38)
    arcade.draw_ellipse_filled(353,317,40,10,arcade.color.ARSENIC,30)
    arcade.draw_ellipse_filled(330,305,50,10,arcade.color.ARSENIC,-60)

    arcade.draw_triangle_filled(390,340,384,350,290,300,arcade.color.ARSENIC)

planeta()
hamaca()
G()
estrellas()


arcade.finish_render()
arcade.run()