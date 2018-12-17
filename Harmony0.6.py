import pygame
from noteClass import Note
from pygame.locals import *
import sys
pygame.init()
pygame.display.set_caption("Harmonise")
class Interface:
	def __init__(self):
		self.white = [255,255,255]
		self.black = [0,0,0]
		self.screenWidth=1280
		self.screenHeight=720

	#def whenThereIsAClick(self):

	def createScreen(self):
		pygame.init()
		screen=pygame.display.set_mode((self.screenWidth,self.screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)
		screen.fill(self.white)
		pygame.display.flip()
		self.verticleLineNumber = 0
		self.horizontalLineNumberStaffOne = 0
		self.horizontalLineNumberStaffTwo = 0
		self.clef = pygame.image.load("trebleClef.png")
		self.clef = pygame.transform.scale(self.clef, (int(132 * self.screenWidth/1280), int(176 * self.screenHeight/720)))
		
		while True:
			event = pygame.event.wait()

			if event.type == QUIT: 
				pygame.display.quit()
				pygame.quit()
				sys.exit()

			elif event.type == VIDEORESIZE:
				screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
				screen.fill(self.white)
				screenInfo = pygame.display.Info()
				self.screenWidth = screenInfo.current_w
				self.screenHeight = screenInfo.current_h
				self.verticleLineNumber = 0
				self.horizontalLineNumberStaffOne = 0
				self.horizontalLineNumberStaffTwo = 0
				self.clef = pygame.image.load("trebleClef.png")
				self.clef = pygame.transform.scale(self.clef, (int(132 * self.screenWidth/1280), int(176 * self.screenHeight/720)))
				for nextVarticleLine in range(10):
					pygame.draw.line(screen, self.black, (4/15 * self.screenWidth + self.verticleLineNumber * 1/15 * self.screenWidth, self.screenHeight * 4/25), (4/15 * self.screenWidth + self.verticleLineNumber * 1/15 * self.screenWidth, self.screenHeight - self.screenHeight/5), 3)
					self.verticleLineNumber += 1
					self.verticleBoxLineNumberStaffOne = 0
					self.verticleBoxLineNumberStaffTwo = 0
					for nextBoxDown in range(6):
						note1 = Note()
						note1.clickBoxStaffOne(screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleBoxLineNumberStaffOne)
						self.verticleBoxLineNumberStaffOne += 1
					for nextBoxDownStaffTwo in range(6):
						note2 = Note()
						note2.clickBoxStaffTwo(screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleBoxLineNumberStaffTwo)
						self.verticleBoxLineNumberStaffTwo += 1
				for nextLineInStaffOne in range(5):
					pygame.draw.line(screen, self.black, (2/15 * self.screenWidth, 1/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffOne), (self.screenWidth - 11/90 * self.screenWidth, 1/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffOne), 3)
					self.horizontalLineNumberStaffOne = self.horizontalLineNumberStaffOne + 1
				for nextLineInStaffTwo in range(5):
					pygame.draw.line(screen, self.black, (2/15 * self.screenWidth, 3/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffTwo), (self.screenWidth - 11/90 * self.screenWidth, 3/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffTwo), 3)
					self.horizontalLineNumberStaffTwo = self.horizontalLineNumberStaffTwo + 1
				pygame.draw.line(screen, self.black, (13/15 * self.screenWidth + 1/90 * self.screenWidth, self.screenHeight * 4/25), (13/15 * self.screenWidth + 1/90 * self.screenWidth, self.screenHeight - self.screenHeight/5), 5)
				pygame.Surface.blit(screen, self.clef, (7/60 * self.screenWidth, 11/60 * self.screenHeight))
				pygame.Surface.blit(screen, self.clef, (7/60 * self.screenWidth, 35/60 * self.screenHeight))
				pygame.display.flip()

			

GUI = Interface()
GUI.createScreen()
print("madecit through")


