import arcade
arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.BABY_BLUE)
arcade.start_render()
#-----SUELO-----#
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(390, 1, 220, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(190, 1, 250, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(690, 1, 150, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(590, 1, 150, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(80, 1, 250, arcade.color.BANGLADESH_GREEN)
#-----SOL-----#
arcade.draw_circle_filled(690, 470, 80, arcade.color.YELLOW)
arcade.draw_circle_filled(690, 470, 70, arcade.color.BANANA_YELLOW)
#-----ÁRBOL-----#
#TRONCO
arcade.draw_rectangle_filled(80, 285, 20, 90, arcade.color.DARK_BROWN)
#HOJAS
arcade.draw_rectangle_filled(80, 300, 120, 30, arcade.color.JUNGLE_GREEN)
arcade.draw_rectangle_filled(80, 330, 100, 30, arcade.color.JUNGLE_GREEN)
arcade.draw_rectangle_filled(80, 360, 80, 30, arcade.color.JUNGLE_GREEN)
arcade.draw_rectangle_filled(80, 390, 60, 30, arcade.color.JUNGLE_GREEN)
arcade.draw_rectangle_filled(80, 410, 40, 30, arcade.color.JUNGLE_GREEN)
arcade.draw_rectangle_filled(80, 440, 20, 30, arcade.color.JUNGLE_GREEN)
#-----NUBES-----#
arcade.draw_circle_filled(290, 400, 22, arcade.color.WHITE)
arcade.draw_circle_filled(250, 400, 18, arcade.color.WHITE)
arcade.draw_circle_filled(270, 415, 20, arcade.color.WHITE)
arcade.draw_circle_filled(270, 400, 21, arcade.color.WHITE)

arcade.draw_circle_filled(500, 500, 37, arcade.color.WHITE)
arcade.draw_circle_filled(430, 500, 33, arcade.color.WHITE)
arcade.draw_circle_filled(470, 515, 35, arcade.color.WHITE)
arcade.draw_circle_filled(470, 500, 36, arcade.color.WHITE)

arcade.draw_circle_filled(690, 300, 19, arcade.color.WHITE)
arcade.draw_circle_filled(650, 300, 15, arcade.color.WHITE)
arcade.draw_circle_filled(670, 315, 17, arcade.color.WHITE)
arcade.draw_circle_filled(670, 300, 18, arcade.color.WHITE)

#-----ARBUSTOS-----#
arcade.draw_circle_filled(690, 100, 19, arcade.color.AMAZON)
arcade.draw_circle_filled(650, 100, 15, arcade.color.AMAZON)
arcade.draw_circle_filled(670, 100, 17, arcade.color.AMAZON)
arcade.draw_circle_filled(670, 110, 18, arcade.color.AMAZON)

arcade.draw_circle_filled(390, 150, 19, arcade.color.AMAZON)
arcade.draw_circle_filled(350, 150, 15, arcade.color.AMAZON)
arcade.draw_circle_filled(370, 150, 17, arcade.color.AMAZON)
arcade.draw_circle_filled(370, 160, 18, arcade.color.AMAZON)

arcade.draw_circle_filled(290, 80, 19, arcade.color.AMAZON)
arcade.draw_circle_filled(250, 80, 15, arcade.color.AMAZON)
arcade.draw_circle_filled(270, 80, 17, arcade.color.AMAZON)
arcade.draw_circle_filled(270, 90, 18, arcade.color.AMAZON)

arcade.draw_circle_filled(90, 100, 19, arcade.color.AMAZON)
arcade.draw_circle_filled(50, 100, 15, arcade.color.AMAZON)
arcade.draw_circle_filled(70, 100, 17, arcade.color.AMAZON)
arcade.draw_circle_filled(70, 110, 18, arcade.color.AMAZON)



#-----FIN-----#
arcade.finish_render()
arcade.run()