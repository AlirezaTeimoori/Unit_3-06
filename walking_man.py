# Created by: Alireza Teimoori
# Created on: 17 Oct 2017
# Created for: ICS3UR-1
# Lesson: Unit_3-06
# This program shows a man walking across the screen


import ui
import time 
@ui.in_background

def animate_touch_up_inside(sender):
    count = 1
    
    
    while count <= 10:
        walking_man = "Resources/walk"+ str(count)+".bmp"
        
        view['man_imageview'].image = ui.Image(walking_man)
        count = count +1
        
        view['man_imageview'].x = view['man_imageview'].x - 6 
        time.sleep(0.05)
        if count >= 10 :
            count = 1
        if view['man_imageview'].x <= -140 :
            view['man_imageview'].x = 480
        
view = ui.load_view()
view.present('sheet')
