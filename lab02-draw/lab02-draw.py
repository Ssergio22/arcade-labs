import arcade
#from arcade import draw_rectangle_filled

arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()


def planeta(center_x:float, center_y:float, radius:float):
    arcade.draw_circle_filled(center_x, center_y, radius+3, arcade.color.GAINSBORO,0)
    arcade.draw_circle_filled(center_x, center_y, radius, arcade.color.JADE,0)
def hamaca(center_x:float, center_y:float, width:float, height:float, start_angle:float, end_angle:float):
    arcade.draw_arc_filled(center_x, center_y, width, height, arcade.color.ARSENIC,start_angle,end_angle)
    arcade.draw_arc_filled(center_x, center_y+20, width, height, arcade.color.GO_GREEN,start_angle,end_angle)
def estrellas():
    arcade.draw_circle_filled(750, 40, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(200, 100, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(100, 400, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(500, 550, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(640, 200, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(300, 600, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(450, 70, 4, arcade.color.ANTI_FLASH_WHITE,0)
    arcade.draw_circle_filled(700, 300, 4, arcade.color.ANTI_FLASH_WHITE,0)
def gab():
    arcade.draw_circle_filled(280, 300, 19, arcade.color.ARSENIC,0)
    arcade.draw_ellipse_filled(385,284,200,20,arcade.color.ARSENIC,5)

    arcade.draw_ellipse_filled(515,285,90,10,arcade.color.ARSENIC,-10)
    arcade.draw_ellipse_filled(480,295,60,10,arcade.color.ARSENIC,-38)
    arcade.draw_ellipse_filled(518,310,40,10,arcade.color.ARSENIC,7)

    arcade.draw_ellipse_filled(350,295,50,10,arcade.color.ARSENIC,-38)
    arcade.draw_ellipse_filled(353,317,40,10,arcade.color.ARSENIC,30)
    arcade.draw_ellipse_filled(330,305,50,10,arcade.color.ARSENIC,-60)

    arcade.draw_triangle_filled(390,340,384,350,290,300,arcade.color.ARSENIC)

planeta(400,300,177)
hamaca(400,260,350,80,180,360)
gab()
estrellas()


arcade.finish_render()
arcade.run()