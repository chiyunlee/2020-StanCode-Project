"""
File: my_drawing.py
Name:
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Create a window and lots of objects from GObject.
    Add those objects to the window to make the drawing.
    """


    window = GWindow(width=600, height=470, title='little my')



    r = GRect(600,470 , x=0 ,y=0)
    r.filled = True
    r.color = '#1C3747'
    r.fill_color = '#1C3747'
    window.add(r)

    wood1 = GRect(25, 300, x=360, y=170)
    wood1.filled = True
    wood1.color = '#C29950'
    wood1.fill_color = '#C29950'
    window.add(wood1)


    wood3 = GRect(280, 190, x=230, y=10)
    wood3.filled = True
    wood3.color = '#8F4629'
    wood3.fill_color = '#8F4629'
    window.add(wood3)



    wood2 = GRect(240, 150, x=250, y=30)
    wood2.filled = True
    wood2.color = '#C29950'
    wood2.fill_color = '#C29950'
    window.add(wood2)



    grass = GOval(50, 140, x=-10, y=400)
    grass.filled = True
    grass.color = '#405F3E'
    grass.fill_color = '#405F3E'
    window.add(grass)

    grass = GOval(60, 140, x=10, y=420)
    grass.filled = True
    grass.color = '#5D7160'
    grass.fill_color = '#5D7160'
    window.add(grass)

    grass = GOval(90, 160, x=40, y=420)
    grass.filled = True
    grass.color = '#61806B'
    grass.fill_color = '#61806B'
    window.add(grass)

    grass = GOval(100, 140, x=80, y=430)
    grass.filled = True
    grass.color = '#435646'
    grass.fill_color = '#435646'
    window.add(grass)

    grass = GOval(180, 100, x=90, y=430)
    grass.filled = True
    grass.color = '#435646'
    grass.fill_color = '#435646'
    window.add(grass)

    grass = GOval(100, 150, x=200, y=410)
    grass.filled = True
    grass.color = '#405F3E'
    grass.fill_color = '#405F3E'
    window.add(grass)

    grass = GOval(110, 180, x=230, y=420)
    grass.filled = True
    grass.color = '#435646'
    grass.fill_color = '#435646'
    window.add(grass)

    l_shoe = GPolygon()
    l_shoe.add_vertex((170, 370))
    l_shoe.add_vertex((190, 445))
    l_shoe.add_vertex((190, 445))
    l_shoe.add_vertex((200, 445))
    l_shoe.add_vertex((210, 445))
    l_shoe.add_vertex((220, 440))
    l_shoe.add_vertex((230, 455))
    l_shoe.add_vertex((220, 465))
    l_shoe.add_vertex((200, 465))
    l_shoe.add_vertex((185, 460))
    l_shoe.add_vertex((180, 465))
    l_shoe.add_vertex((168, 465))
    l_shoe.add_vertex((155, 370))
    l_shoe.filled = True
    l_shoe.fill_color = 'black'
    window.add(l_shoe)

    r_shoe = GPolygon()
    r_shoe.add_vertex((130, 370))
    r_shoe.add_vertex((110, 445))
    r_shoe.add_vertex((110, 445))
    r_shoe.add_vertex((100, 445))
    r_shoe.add_vertex((90, 445))
    r_shoe.add_vertex((80, 440))
    r_shoe.add_vertex((70, 455))
    r_shoe.add_vertex((85, 465))
    r_shoe.add_vertex((100, 465))
    r_shoe.add_vertex((115, 460))
    r_shoe.add_vertex((120, 465))
    r_shoe.add_vertex((132, 465))
    r_shoe.add_vertex((145, 370))
    r_shoe.filled = True
    r_shoe.fill_color = 'black'
    window.add(r_shoe)

    dress = GPolygon()
    dress.add_vertex((108,218))
    dress.add_vertex((96,250))
    dress.add_vertex((45,260))
    dress.add_vertex((43,275))
    dress.add_vertex((71,330))
    dress.add_vertex((30,390))
    dress.add_vertex((90,410))
    dress.add_vertex((135,415))
    dress.add_vertex((166,420))
    dress.add_vertex((200,415))
    dress.add_vertex((270,390))
    dress.add_vertex((205,265))
    dress.add_vertex((355,265))
    dress.add_vertex((355,250))
    dress.add_vertex((205,250))
    dress.add_vertex((193,218))
    dress.filled = True
    dress.fill_color = '#B5272D'
    window.add(dress)

    l_hand = GPolygon()
    l_hand.add_vertex((90,268))
    l_hand.add_vertex((60,275))
    l_hand.add_vertex((80,310))
    l_hand.filled = True
    l_hand.fill_color = '#1C3747'
    window.add(l_hand)

    l_tie = GPolygon()
    l_tie.add_vertex((150,238))
    l_tie.add_vertex((105,220))
    l_tie.add_vertex((105,255))
    l_tie.filled = True
    l_tie.fill_color = '#D17989'
    window.add(l_tie)

    r_tie = GPolygon()
    r_tie.add_vertex((150, 238))
    r_tie.add_vertex((195, 220))
    r_tie.add_vertex((195, 255))
    r_tie.filled = True
    r_tie.fill_color = '#D17989'
    window.add(r_tie)

    tie = GOval(20, 26, x=140, y=225)
    tie.filled = True
    tie.fill_color = '#D17989'
    window.add(tie)


    l_ear = GOval(40, 40, x=60, y=150)
    l_ear.filled = True
    l_ear.fill_color = '#FFF1E2'
    window.add(l_ear)

    r_ear = GOval(40, 40, x=200, y=150)
    r_ear.filled = True
    r_ear.fill_color = '#FFF1E2'
    window.add(r_ear)

    face = GOval(160,140,x=70,y=90)
    face.filled = True
    face.fill_color = '#FFF1E2'
    window.add(face)

    l_eye = GArc(40,90,-10,-180,x=90,y=140)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    window.add(l_eye)

    l_eye_b = GArc(20, 60, -10, -178, x=100, y=148)
    l_eye_b.filled = True
    l_eye_b.fill_color = '#4A8165'
    window.add(l_eye_b)

    r_eye = GArc(40, 90, 10, -180, x=170, y=140)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    window.add(r_eye)

    r_eye_b = GArc(20, 60, 10, -178, x=180, y=148)
    r_eye_b.filled = True
    r_eye_b.fill_color = '#4A8165'
    window.add(r_eye_b)

    nose1 = GLine(146, 160, 148, 173)
    nose1.color = 'black'
    window.add(nose1)

    nose2 = GLine(156, 160, 154, 173)
    nose2.color = 'black'
    window.add(nose2)

    nose3 = GLine(149, 175, 140, 199)
    nose3.color = 'black'
    window.add(nose3)

    nose4 = GLine(162, 199, 153, 175)
    nose4.color = 'black'
    window.add(nose4)

    nose5 = GLine(140, 199, 162, 199)
    nose5.color = 'black'
    window.add(nose5)

    mouth = GArc (100, 80 , -30,-120 ,x=110 ,y=190)
    mouth.color = 'black'
    window.add(mouth)

    h_tail1 = GOval(50, 100 ,x=125, y=30)
    h_tail1.filled = True
    h_tail1.fill_color = '#F39401'
    h_tail1.color = '#F39401'
    window.add(h_tail1)

    h_tail1_line1 = GArc(160,110,120,100,x=135,y=30)
    h_tail1_line1.color ='black'
    window.add(h_tail1_line1)

    h_tail1_line2 = GArc(160,110,120,100,x=142,y=30)
    h_tail1_line2.color ='black'
    window.add(h_tail1_line2)

    h_tail1_line3 = GArc(160, 110, 60, -100, x=120, y=30)
    h_tail1_line3.color = 'black'
    window.add(h_tail1_line3)

    h_tail1_line4 = GArc(160, 110, 60, -100, x=127, y=30)
    h_tail1_line4.color = 'black'
    window.add(h_tail1_line4)

    h_tail1_line5 = GLine(150, 50, 150, 86)
    h_tail1_line5.color = 'black'
    window.add(h_tail1_line5)


    hair = GArc(160, 240, 0, 180, x=70, y=90)
    hair.filled = True
    hair.fill_color = '#F39401'
    hair.color = '#F39401'
    window.add(hair)

    hairline1 = GArc(800, 230, 115, 69, x=80 , y=90)
    hairline1.color = 'black'
    window.add(hairline1)

    hairline2 = GArc(820, 230, 120, 66, x=95 , y=89)
    hairline2.fill = 'black'
    window.add(hairline2)

    hairline3 = GArc(840, 240, 130, 58, x=110 , y=88)
    hairline3.fill = 'black'
    window.add(hairline3)

    hairline4 = GArc(860, 240, 135, 56, x=125 , y=87)
    hairline4.fill = 'black'
    window.add(hairline4)

    hairline5 = GArc(920, 250, 140, 53, x=135 , y=85)
    hairline5.fill = 'black'
    window.add(hairline5)

    hairline6 = GLine(150, 110, 153, 150)
    hairline6.fill = 'black'
    window.add(hairline6)

    hairline7 = GArc(300, 400, 90, -75, x=80 , y=96)
    hairline7.fill = 'black'
    window.add(hairline7)

    hairline8 = GArc(300, 425, 85, -70, x=75 , y=93)
    hairline8.fill = 'black'
    window.add(hairline8)

    hairline9 = GArc(320, 475, 70, -55, x=90 , y=90)
    hairline9.fill = 'black'
    window.add(hairline9)

    hairline10 = GArc(280, 500, 65, -50, x=100 , y=90)
    hairline10.fill = 'black'
    window.add(hairline10)

    hairline11 = GArc(280, 530, 60, -45, x=100 , y=90)
    hairline11.fill = 'black'
    window.add(hairline11)



    l_hand = GArc(50,50, 40 ,-180, x=43 ,y=298)
    l_hand.filled = True
    l_hand.fill_color = 'black'
    window.add(l_hand)

    r_hand = GOval(40,40,x=350,y=235)
    r_hand.filled = True
    r_hand.fill_color = 'black'
    window.add(r_hand)


    label = GLabel('Python!', x=263, y=140)
    label.font = 'Verdana-38-italic-bold'
    label.color = 'white'
    window.add(label)

    grass = GOval(120, 180, x=260, y=430)
    grass.filled = True
    grass.color = '#435646'
    grass.fill_color = '#5D7160'
    window.add(grass)

    grass = GOval(120, 180, x=330, y=450)
    grass.filled = True
    grass.color = '#405F3E'
    grass.fill_color = '#405F3E'
    window.add(grass)

    grass = GOval(120, 180, x=370, y=430)
    grass.filled = True
    grass.color = '#435646'
    grass.fill_color = '#435646'
    window.add(grass)

    grass = GOval(120, 150, x=430, y=420)
    grass.filled = True
    grass.color = '#4F5939'
    grass.fill_color = '#4F5939'
    window.add(grass)

    grass = GOval(80, 180, x=470, y=410)
    grass.filled = True
    grass.color = '#405F3E'
    grass.fill_color = '#405F3E'
    window.add(grass)

    grass = GOval(120, 150, x=500, y=440)
    grass.filled = True
    grass.color = '#435646'
    grass.fill_color = '#435646'
    window.add(grass)

    hatti = GRect(50,170, x=420, y= 300)
    hatti.filled = True
    hatti.color = '#DADADA'
    hatti.fill_color = '#DADADA'
    window.add(hatti)

    hatti_h = GOval(50,50,x=420,y=275)
    hatti_h.filled = True
    hatti_h.color = '#DADADA'
    hatti_h.fill_color = '#DADADA'
    window.add(hatti_h)

    hatti_e = GOval(25, 25, x=420, y=300)
    hatti_e.filled = True
    hatti_e.color = 'black'
    hatti_e.fill_color = 'white'
    window.add(hatti_e)

    hatti_ee = GOval(25, 25, x=445, y=300)
    hatti_ee.filled = True
    hatti_ee.color = 'black'
    hatti_ee.fill_color = 'white'
    window.add(hatti_ee)

    hatti_b = GOval(10, 10, x=452.5, y=307.5)
    hatti_b.filled = True
    hatti_b.color = 'black'
    hatti_b.fill_color = 'black'
    window.add(hatti_b)

    hatti_bb = GOval(10, 10, x=427.5, y=307.5)
    hatti_bb.filled = True
    hatti_bb.color = 'black'
    hatti_bb.fill_color = 'black'
    window.add(hatti_bb)

    hatti = GRect(50,210, x=480, y=260)
    hatti.filled = True
    hatti.color = '#DADADA'
    hatti.fill_color = '#DADADA'
    window.add(hatti)

    hatti_h = GOval(50,50,x=480,y=235)
    hatti_h.filled = True
    hatti_h.color = '#DADADA'
    hatti_h.fill_color = '#DADADA'
    window.add(hatti_h)

    hatti_e = GOval(25, 25, x=480, y=260)
    hatti_e.filled = True
    hatti_e.color = 'black'
    hatti_e.fill_color = 'white'
    window.add(hatti_e)

    hatti_ee = GOval(25, 25, x=505, y=260)
    hatti_ee.filled = True
    hatti_ee.color = 'black'
    hatti_ee.fill_color = 'white'
    window.add(hatti_ee)

    hatti_b = GOval(10, 10, x=512.5, y=267.5)
    hatti_b.filled = True
    hatti_b.color = 'black'
    hatti_b.fill_color = 'black'
    window.add(hatti_b)

    hatti_bb = GOval(10, 10, x=487.5, y=267.5)
    hatti_bb.filled = True
    hatti_bb.color = 'black'
    hatti_bb.fill_color = 'black'
    window.add(hatti_bb)

    hatti = GRect(50,150, x=520, y=320)
    hatti.filled = True
    hatti.fill_color = '#DADADA'
    window.add(hatti)

    hatti_h = GOval(50,50,x=520,y=295)
    hatti_h.filled = True
    hatti_h.fill_color = '#DADADA'
    window.add(hatti_h)

    r = GRect(48,25, x=521,y=321)
    r.filled = True
    r.color = '#DADADA'
    r.fill_color ='#DADADA'
    window.add(r)

    hatti_e = GOval(25, 25, x=520, y=320)
    hatti_e.filled = True
    hatti_e.color = 'black'
    hatti_e.fill_color = 'white'
    window.add(hatti_e)

    hatti_ee = GOval(25, 25, x=545, y=320)
    hatti_ee.filled = True
    hatti_ee.color = 'black'
    hatti_ee.fill_color = 'white'
    window.add(hatti_ee)

    hatti_b = GOval(10, 10, x=552.5, y=327.5)
    hatti_b.filled = True
    hatti_b.color = 'black'
    hatti_b.fill_color = 'black'
    window.add(hatti_b)

    hatti_bb = GOval(10, 10, x=527.5, y=327.5)
    hatti_bb.filled = True
    hatti_bb.color = 'black'
    hatti_bb.fill_color = 'black'
    window.add(hatti_bb)

    hatti = GRect(50,150, x=450, y=380)
    hatti.filled = True
    hatti.fill_color = '#DADADA'
    window.add(hatti)

    hatti_h = GOval(50,50,x=450,y=355)
    hatti_h.filled = True
    hatti_h.fill_color = '#DADADA'
    window.add(hatti_h)

    r = GRect(48,25, x=451,y=380)
    r.filled = True
    r.color = '#DADADA'
    r.fill_color ='#DADADA'
    window.add(r)

    hatti_e = GOval(25, 25, x=450, y=380)
    hatti_e.filled = True
    hatti_e.color = 'black'
    hatti_e.fill_color = 'white'
    window.add(hatti_e)

    hatti_ee = GOval(25, 25, x=475, y=380)
    hatti_ee.filled = True
    hatti_ee.color = 'black'
    hatti_ee.fill_color = 'white'
    window.add(hatti_ee)

    hatti_b = GOval(10, 10, x=457.5, y=387.5)
    hatti_b.filled = True
    hatti_b.color = 'black'
    hatti_b.fill_color = 'black'
    window.add(hatti_b)

    hatti_bb = GOval(10, 10, x=482.5, y=387.5)
    hatti_bb.filled = True
    hatti_bb.color = 'black'
    hatti_bb.fill_color = 'black'
    window.add(hatti_bb)

















if __name__ == '__main__':
    main()
