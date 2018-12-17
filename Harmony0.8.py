import pygame
from noteClass2 import NoteInteractionStaffOne
from noteClass2 import NoteInteractionStaffTwo
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
		pygame.init()
		self.screen=pygame.display.set_mode((self.screenWidth,self.screenHeight), HWSURFACE|DOUBLEBUF|RESIZABLE)
		self.screen.fill(self.white)
		pygame.display.flip()
		self.listOfNotesStaffOne = [(-1) for i in range(10)]

	#def whenThereIsAClick(self):

	def createScreen(self):

		self.clef = pygame.image.load("trebleClef.png")
		self.clef = pygame.transform.scale(self.clef, (int(132 * self.screenWidth/1280), int(176 * self.screenHeight/720)))
		screenInfo = pygame.display.Info()

		self.verticleLineNumber = 0
		self.horizontalLineNumberStaffOne = 0
		self.horizontalLineNumberStaffTwo = 0
		self.screenWidth = screenInfo.current_w
		self.screenHeight = screenInfo.current_h
		noteStaffOne = NoteInteractionStaffOne()
		noteStaffTwo = NoteInteractionStaffTwo()

		self.clef = pygame.image.load("trebleClef.png")
		self.clef = pygame.transform.scale(self.clef, (int(132 * self.screenWidth/1280), int(176 * self.screenHeight/720)))

		self.matrixOfNotesStaffOne = [["empty" for boxes in range(6)] for collumns in range(10)]
		self.matrixOfNotesStaffTwo = [["empty" for boxes in range(6)] for collumns in range(10)]

		for nextVarticleLine in range(10):
			pygame.draw.line(self.screen, self.black, (4/15 * self.screenWidth + self.verticleLineNumber * 1/15 * self.screenWidth, self.screenHeight * 4/25), (4/15 * self.screenWidth + self.verticleLineNumber * 1/15 * self.screenWidth, self.screenHeight - self.screenHeight/5), 3)
			self.verticleLineNumber += 1
			self.verticleBoxLineNumberStaffOne = 0
			self.verticleBoxLineNumberStaffTwo = 0

			for nextBoxDown in range(6):
				noteStaffOne.clickBoxStaffOne(self.screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleBoxLineNumberStaffOne)
				self.verticleBoxLineNumberStaffOne += 1
				self.matrixOfNotesStaffOne[nextVerticleLine][nextBoxDown] = NoteInteractionStaffOne((nextVerticleLine, nextBoxDown))

			for nextBoxDownStaffTwo in range(6):
				noteStaffTwo.clickBoxStaffTwo(self.screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleBoxLineNumberStaffTwo)
				self.verticleBoxLineNumberStaffTwo += 1
				self.matrixOfNotesStaffTwo[nextVerticleLine][nextBoxDown] = NoteInteractionStaffTwo((nextVerticleLine, nextBoxDown))

		for nextLineInStaffOne in range(5):
			pygame.draw.line(self.screen, self.black, (2/15 * self.screenWidth, 1/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffOne), (self.screenWidth - 11/90 * self.screenWidth, 1/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffOne), 3)
			self.horizontalLineNumberStaffOne = self.horizontalLineNumberStaffOne + 1

		for nextLineInStaffTwo in range(5):
			pygame.draw.line(self.screen, self.black, (2/15 * self.screenWidth, 3/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffTwo), (self.screenWidth - 11/90 * self.screenWidth, 3/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffTwo), 3)
			self.horizontalLineNumberStaffTwo = self.horizontalLineNumberStaffTwo + 1
		pygame.draw.line(self.screen, self.black, (13/15 * self.screenWidth + 1/90 * self.screenWidth, self.screenHeight * 4/25), (13/15 * self.screenWidth + 1/90 * self.screenWidth, self.screenHeight - self.screenHeight/5), 5)
		pygame.Surface.blit(self.screen, self.clef, (7/60 * self.screenWidth, 11/60 * self.screenHeight))
		pygame.Surface.blit(self.screen, self.clef, (7/60 * self.screenWidth, 35/60 * self.screenHeight))
		pygame.display.flip()

	def	WhenABoxIsClickedInStaffOne(self, clickPositionStaffOne):
		for currentNote in self.matrixOfNotesStaffOne:
			if currentNote.boxStaffOne.collidepoint(clickPositionStaffOne):
				pygame.Surface.blit(self.screen, currentNote.note, (currentNote.boxStaffOne.x, currentNote.boxStaffOne.y))
				if (listOfNotesStaffOne[currentNote.position[0]] != (-1)):
					pygame.draw.rect(self.screen, self.white, matrixOfNotesStaffOne[currentNote.position[0]][listOfNotesStaffOne[currentNote.position[0]]])

				self.listOfNotesStaffOne[currentNote.position[0]] = currentNote.position[1]

	def	WhenABoxIsClickedInStaffTwo(self, clickPositionStaffOne):
			for currentNote in self.matrixOfNotesStaffTwo:
				if currentNote.boxStaffTwo.collidepoint(clickPositionStaffTwo):
					pygame.Surface.blit(self.screen, currentNote.note, (currentNote.boxStaffTwo.x, currentNote.boxStaffTwo.y))
					if (listOfNotesStaffTwo[currentNote.position[0]] != (-1)):
						pygame.draw.rect(self.screen, self.white, matrixOfNotesStaffTwo[currentNote.position[0]][listOfNotesStaffTwo[currentNote.position[0]]])
					self.listOfNotesStaffTwo[currentNote.position[0]] = currentNote.position[1]




GUI = Interface()
GUI.createScreen()

while True:
	event = pygame.event.wait()

	if event.type == QUIT:
		pygame.display.quit()
		pygame.quit()
		sys.exit()
	elif event.type == VIDEORESIZE:
		screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
		screen.fill(white)
		GUI.createScreen()

	if event.type == pygame.MOUSEBUTTONUP:
		positionOfTheMouse = pygame.mouse.get_pos()
		WhenABoxIsClickedInStaffOne(positionOfTheMouse)
		WhenABoxIsClickedInStaffTwo(positionOfTheMouse)

		pygame.display.flip()


		#print(event.button)
		#if event.button == 1:
		#	print("right click")
		#if event.button == 3:
		#	print("left click")
