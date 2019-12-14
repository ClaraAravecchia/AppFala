# -*- coding: cp1252 -*-
# -*- coding: UTF-8 -*-

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.widget import Canvas
from kivy.graphics import Color, Line, Rectangle
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from random import random
import pyttsx3
import kivy.modules.screen

def Speak(x):
	# Converte texto em voz, em portugues
	engine= pyttsx3.init()
	engine.setProperty("voice", "brazil")#b"brazil")
	# configura a velocidade
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-80)
	engine.say(str(x))
	engine.runAndWait()
	engine.stop()


class SampBoxLayout(BoxLayout, Widget):
	# Executa o audio das strings
	def sede(self):     Speak("Estou com sede")
	def fome(self):     Speak("Estou com fome")
	def sono(self):     Speak("Estou com sono")
	def dor(self):      Speak("Estou com dor")
	def brincar(self):  Speak("Quero brincar")
	def banheiro(self): Speak("Quero ir ao banheiro")
	def dormir(self):   Speak("Quero dormir")
	def comer(self):    Speak("Quero comer")
	def esquerda(self): Speak("Esquerda")
	def direita(self):  Speak("Direita")
	def cima(self):     Speak("Pra cima")
	def baixo (self):   Speak("Pra baixo")
	def feliz(self):    Speak("Estou Feliz!")
	def triste(self):   Speak("Estou triste")
	def sim(self):      Speak("Sim")
	def nao(self):      Speak("Nao")
	def porfavor(self): Speak("Por favor")
	def obg(self):		Speak("Obrigado!")
	def licenca(self):	Speak("Com licensa") 
	def ajuda(self):	Speak("Preciso de ajuda")
	def dia(self):		Speak("Bom Dia")
	def tarde(self):  	Speak("Boa Tarde")
	def noite(self):	Speak("Boa Noite")
	def oi(self):		Speak("Oi!")
	def tchau(self):	Speak("Tchau!")

	
	#def on_keyboard(self,entry):print ("Usando o teclado")

	def strSpeak(self, string):

		try:
			Speak(string)

		except:
			pass

	#def show_keyboard(self, event):
		#entry.focus = True
		#Clock.schedule_once(show_keyboard)

	# def show_keyboard(self, **kwargs):
		
	# 	if self._keyboard.widget:
	# 		keyboard = Window.request_keyboard(self._keyboard_closed, input_type ='text')
	# 	else:
	# 		keyboard = self._keyboard.widget

	# def _keyboard_closed(self):
	# 	print('My keyboard have been closed!')

	# 	keyboard.release()
	# 	return True

	# def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
	# 	print('The key', keycode, 'have been pressed')
	# 	print(' - text is %r' % text)
	# 	print(' - modifiers are %r' % modifiers)

	# 	# Keycode is composed of an integer + a string
	# 	# If we hit escape, release the keyboard
	# 	if keycode[1] == 'escape':
	# 		keyboard.release()

	# 	# Return True to accept the key. Otherwise, it will be used by
	# 	# the system.
	# 	return True

class Bind(Widget):
	# Lida com os binds do painel de desenho
	def __init__(self, **kwargs):
		super(Bind, self).__init__(**kwargs)
		self.touch=[]

	def on_touch_down(self, touch):
		# se botao do mouse apertado
		with self.canvas:
			# cor aleatoria
			Color(random(), random(), random())
			# self.line == posicao do mouse
			self.line=Line(points=(touch.x, touch.y), width=5)
			
	def on_touch_move(self, touch):
		# se botao do mouse + movimento
		# adiciona o proximo ponto do mouse
		self.line.points += [touch.x, touch.y]
		self.draw= ObjectProperty(self.line)
		#print touch.profile


	def on_touch_up(self, touch):
		# se botao do mouse for solto
		# remove self.line
		self.canvas.children.remove(self.line)
	
class SampleApp(App):
	def build(self):
		Window.clearcolor = (0, .8, .8, 1)
	
		return SampBoxLayout()

sample_app = SampleApp()
sample_app.run()
