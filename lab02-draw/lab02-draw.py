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
def gab(center_x:float, center_y:float):
    arcade.draw_circle_filled(center_x, center_y+16, 19, arcade.color.ARSENIC,0)  #cabesa
    arcade.draw_ellipse_filled(center_x+105,center_y,200,20,arcade.color.ARSENIC,5)  #torso

    arcade.draw_ellipse_filled(center_x+235,center_y+1,90,10,arcade.color.ARSENIC,-10)   #pata_recta
    arcade.draw_ellipse_filled(center_x+200,center_y+11,60,10,arcade.color.ARSENIC,-38)   #pata_curva_1
    arcade.draw_ellipse_filled(center_x+238,center_y+26,40,10,arcade.color.ARSENIC,7)   #pata_curva_2

    arcade.draw_ellipse_filled(center_x+70,center_y+11,50,10,arcade.color.ARSENIC,-38)  #brazo_curvo_1
    arcade.draw_ellipse_filled(center_x+73,center_y+33,40,10,arcade.color.ARSENIC,30)  #brazo_curvo_2
    arcade.draw_ellipse_filled(center_x+50,center_y+21,50,10,arcade.color.ARSENIC,-60) #brazo_recto

    arcade.draw_triangle_filled(center_x+110,center_y+56,center_x+104,center_y+66,center_x+10,center_y+16,arcade.color.ARSENIC) #flauta

planeta(400,300,177)
hamaca(400,260,350,80,180,360)
gab(280,284)
estrellas()


arcade.finish_render()
arcade.run()