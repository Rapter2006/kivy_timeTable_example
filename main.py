# -*- coding: utf-8 -*-
# Author: RapteR
# Website: rapter2006.blogspot.com
# email: rapter2006@ya.ru

import kivy
kivy.require('1.0.7')

from kivy.core.window import Window
from kivy.animation import Animation
from kivy.core.image import Image
from kivy.graphics import *
from kivy.app import App
from kivy.core.audio import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch
from kivy.uix.scatter import Scatter

import os
import random

#global
size_d = 30.0
switch_random = Switch(active=False)
switch_logo = Switch(active=True)
switch_sound = Switch(active=True)
switch_party = Switch(active=False)
switch_move = Switch(active=False)

buttonMonday = Button(background_normal='data/1.png')
buttonTuesday = Button(background_normal='data/2.png')
buttonWednesday = Button(background_normal='data/3.png')
buttonThursday = Button(background_normal='data/4.png')
buttonFriday = Button(background_normal='data/5.png')
buttonSaturday = Button(background_normal='data/6.png')
#set default background-color and fullscreen
Window.clearcolor = (0.5, 0.73, 0.96, 0.5) #TouchLay Blue

class PointoutWidget(Widget):
    def on_touch_down(self, touch):
            if switch_sound.active == True:
		#load random sounds from data/sound
		path = 'data/sound/'
		count_sound = 0
		dirList=os.listdir(path)
		for fname in dirList:
		    count_sound += 1
		sound = SoundLoader.load(filename='data/sound/'+ str(dirList[random.randrange(0, count_sound, 1)]))
		if not sound:
		    print 'Sound: can\'t load sound!'
		else:
		    # play the sound
	   	    sound.play()

            with self.canvas:
		#party mode
                if switch_party.active == True:
                        rand1 = (float)(random.randrange(1, 100))/100
                        rand2 = (float)(random.randrange(1, 100))/100
                        rand3 = (float)(random.randrange(1, 100))/100
                        print 'Color(%f, %f, %f, 1.0)' % (rand1, rand2, rand3)
                        color = Color(rand1, rand2, rand3, 1.0)
                else:
                        color = Color(1, 1, 1, 1.0)
	        if switch_random.active == True:
	    	        size_d_rand = size_d + random.randrange(0, 101, 2)
	                ellipse = Ellipse(pos=(touch.x - size_d_rand/2, touch.y - size_d_rand/2), size=(size_d_rand, size_d_rand))
	 	        # animate the alpha color over random secounds
		        size_d_animate = size_d_rand+random.randrange(10, 200, 1)
		        animation_time = random.randrange(1.0, 10.0, 1)
	                Animation(a=0.0, d=animation_time).start(color)
 	       	        Animation(pos=(touch.x - (size_d_rand+size_d_animate)/2, touch.y - (size_d_rand+size_d_animate )/2),   				      size=(size_d_animate ,size_d_animate), d=animation_time).start(ellipse)
                else: 
	                ellipse = Ellipse(pos=(touch.x - size_d/2, touch.y - size_d/2), size=(size_d, size_d ))		    
       		        # animate the alpha color over 3 seconds
       		        Animation(a=0.0, d=1.0).start(color)
 	       	        Animation(pos=(touch.x - (size_d+100)/2, touch.y - (size_d+100)/2), size=(size_d+100, size_d+100), d=3.0).start(ellipse)
                touch.ud.my_graphics = (color, ellipse)

    def on_touch_move(self, touch):
        if switch_move.active == True:
            self.touching(touch)

    def on_touch_up(self, touch):
        # check if my_graphics exist for that touch
        if 'my_graphics' not in touch.ud:
            return
        # get the color and rect attached to the touch
        color, ellipse = touch.ud.my_graphics


class PointoutApp(App):
    icon = 'data/icon.png'
    def build(self):
        parent = Widget()
        painter = PointoutWidget()
        settingButton = Button(background_normal='data/task.png')
	sliderSize = Slider(min=1.0, max=100, value=30)	
        parent.add_widget(painter)
	parent.add_widget(settingButton)
	#TODO: create a hover animation
	#load the welcome image
	welcomeTexture = Image.load('data/welcome.png', keep_data=True).texture
	welcomeImg = Rectangle(size=(500,200), pos=((Window.width/2)-250, (Window.height/2)-100), texture= welcomeTexture)
	#set on startup
	painter.canvas.add(welcomeImg)

	layout = GridLayout(cols=2)
	layout_row1 = GridLayout(cols=2)
	layout_row2 = GridLayout(cols=2)
	layout_row3 = GridLayout(cols=2)
	layout_row4 = GridLayout(cols=2)
	layout_row5 = GridLayout(cols=2)
        layout_row6 = GridLayout(cols=2)
        layout_row7 = GridLayout(cols=2)
	

	layout.add_widget(layout_row1)
	layout_row1.add_widget(Label(text=u'Понедельник:', font_size=15))
	layout_row1.add_widget(buttonMonday)
     
	##########################
	layout.add_widget(layout_row2)
	layout_row2.add_widget(Label(text=u'Вторник:', font_size=15))
	layout_row2.add_widget(buttonTuesday)
	##########################
	layout.add_widget(layout_row3)
	layout_row3.add_widget(Label(text=u'Среда:', font_size=15))
	layout_row3.add_widget(buttonWednesday)
	##########################
	layout.add_widget(layout_row4)
	layout_row4.add_widget(Label(text=u'Четверг:', font_size=15))
	layout_row4.add_widget(buttonThursday)
	##########################
	layout.add_widget(layout_row5)
	layout_row5.add_widget(Label(text=u'Пятница:', font_size=15))
	layout_row5.add_widget(buttonFriday)
	##########################
	layout.add_widget(layout_row6)
        layout_row6.add_widget(Label(text=u'Суббота:', font_size=15))
        layout_row6.add_widget(buttonSaturday)
    ##########################

	popup = Popup(title=u'Расписание П-92', content=layout, size_hint=(None, None), size=(500, 500))
    


        def setting_popup(obj):
	     popup.open()
        settingButton.bind(on_release=setting_popup)

        def setting_popup_Monday(obj):
            content_Monday = Label(text=u'08.00 ауд.202 Мифология(л)\n\n09.50 ауд.425 Функ.прог.(п)\n\n11.40 ауд.211 ТРПО(л)\n\n13.45 ауд.211 ТРПО(л)(ВЕРХ)', font_size=20)
            popup_Monday = Popup(title=u'Понедельник', content=content_Monday, size_hint=(None, None), size=(500, 500))
            popup_Monday.open()
        buttonMonday.bind(on_release=setting_popup_Monday)
		
        def setting_popup_Tuesday(obj):
            content_Tuesday = Label(text=u'08.00 ауд.407 ТЯПиМТ(л)\n\n09.50 ауд.419 ТЯПиМТ(п)\n\n11.40 ауд.218 Комп. графика(л)\n\n13.45 ауд.219 или 432а МСЗКИ(п)', font_size=20)
            popup_Tuesday = Popup(title=u'Вторник', content=content_Tuesday, size_hint=(None, None), size=(500, 500))
            popup_Tuesday.open()
        buttonTuesday.bind(on_release=setting_popup_Tuesday)

        def setting_popup_Wednesday(obj):
            content_Wednesday = Label(text=u'08.00 ауд.402 ТРПО(п)\n\n09.50 ауд.302 Комп. графика(п)\n\n11.40 ауд.210 МСЗКИ(л)', font_size=20)
            popup_Wednesday = Popup(title=u'Среда', content=content_Wednesday, size_hint=(None, None), size=(500, 500))
            popup_Wednesday.open()
        buttonWednesday.bind(on_release=setting_popup_Wednesday)

        def setting_popup_Thursday(obj):
            content_Thursday = Label(text=u'ВОЕНКА!!!', font_size=20)
            popup_Thursday = Popup(title=u'Четверг', content=content_Thursday, size_hint=(None, None), size=(500, 500))
            popup_Thursday.open()
        buttonThursday.bind(on_release=setting_popup_Thursday)

        def setting_popup_Friday(obj):
            content_Friday = Label(text=u'08.00 ауд.418 Функ.прог.(л)\n\n09.50 ауд.409 Мифология(п)\n\n11.40 ОКНО(НИЗ)\n\n13.45 ауд.418 ТЯПиМТ(л)(НИЗ)', font_size=20)
            popup_Friday = Popup(title=u'Пятница', content=content_Friday, size_hint=(None, None), size=(500, 500))
            popup_Friday.open()
        buttonFriday.bind(on_release=setting_popup_Friday)

        def setting_popup_Saturday(obj):
            content_Saturday = Label(text=u'СВОБОДА!!!', font_size=20)
            popup_Saturday = Popup(title=u'Суббота', content=content_Saturday, size_hint=(None, None), size=(500, 500))
            popup_Saturday.open()
        buttonSaturday.bind(on_release=setting_popup_Saturday)
		 
        return parent

if __name__ in ('__main__', '__android__'):
    PointoutApp().run()
