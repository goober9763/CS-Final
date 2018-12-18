import pygame
from noteClass2 import NoteInteractionStaffOne
from noteClass2 import NoteInteractionStaffTwo
from pygame.locals import *
import sys
import time
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
		self.listOfNotesStaffTwo = [(-1) for i in range(10)]
		self.listOfLineNotesStaffOne = [(-1) for i in range(10)]
		self.listOfLineNotesStaffTwo = [(-1) for i in range(10)]
		self.listOfDrawBoxesStaffOne = [(-1) for i in range(10)]
		self.listOfDrawBoxesStaffTwo = [(-1) for i in range(10)]

		a3 = pygame.mixer.Sound("./audio/A3.wav")
		b3 = pygame.mixer.Sound("./audio/B3.wav")
		c3 = pygame.mixer.Sound("./audio/C3.wav")
		d2 = pygame.mixer.Sound("./audio/D2.wav")
		d3 = pygame.mixer.Sound("./audio/D3.wav")
		e2 = pygame.mixer.Sound("./audio/E2.wav")
		e3 = pygame.mixer.Sound("./audio/E3.wav")
		f2 = pygame.mixer.Sound("./audio/F2.wav")
		f3 = pygame.mixer.Sound("./audio/F3.wav")
		g2 = pygame.mixer.Sound("./audio/G2.wav")
		g3 = pygame.mixer.Sound("./audio/G3.wav")
		self.error = pygame.mixer.Sound("./audio/Error.wav")
		self.soundList = [g3,f3,e3,d3,c3,b3,a3,g2,f2,e2,d2]

	#def whenThereIsAClick(self):

	def createScreen(self):

		self.clef = pygame.image.load("trebleClef.png")
		self.clef = pygame.transform.scale(self.clef, (int(132 * self.screenWidth/1280), int(176 * self.screenHeight/720)))
		self.play = pygame.image.load("play.png")
		self.play = pygame.transform.scale(self.play, (int(50 * self.screenWidth/1280), int(50 * self.screenHeight/720)))
		self.playRect = self.play.get_rect()
		screenInfo = pygame.display.Info()

		self.verticleLineNumber = 0
		self.horizontalLineNumberStaffOne = 0
		self.horizontalLineNumberStaffTwo = 0
		self.screenWidth = screenInfo.current_w
		self.screenHeight = screenInfo.current_h
		# noteStaffOne = NoteInteractionStaffOne()
		# noteStaffTwo = NoteInteractionStaffTwo()

		self.clef = pygame.image.load("trebleClef.png")
		self.clef = pygame.transform.scale(self.clef, (int(132 * self.screenWidth/1280), int(176 * self.screenHeight/720)))

		self.matrixOfNotesStaffOne = [["empty" for boxes in range(6)] for collumns in range(10)]
		self.matrixOfNotesStaffTwo = [["empty" for boxes in range(6)] for collumns in range(10)]
		self.matrixOfNotesOnLineStaffOne = [["empty" for lines in range(5)] for collumns in range(10)]
		self.matrixOfNotesOnLineStaffTwo = [["empty" for lines in range(5)] for collumns in range(10)]
		self.matrixOfDrawBoxesStaffOne = [["empty" for drawBoxes in range(5)] for collumns in range(10)]
		self.matrixOfDrawBoxesStaffTwo = [["empty" for drawBoxes in range(5)] for collumns in range(10)]

		for nextVerticleLine in range(10):
			pygame.draw.line(self.screen, self.black, (4/15 * self.screenWidth + self.verticleLineNumber * 1/15 * self.screenWidth, self.screenHeight * 4/25), (4/15 * self.screenWidth + self.verticleLineNumber * 1/15 * self.screenWidth, self.screenHeight - self.screenHeight/5), 3)
			self.verticleLineNumber += 1
			self.verticleBoxLineNumberStaffOne = 0
			self.verticleBoxLineNumberStaffTwo = 0
			self.verticleLineLineNumberStaffOne = 0
			self.verticleLineLineNumberStaffTwo = 0
			self.verticleDrawBoxLineNumberStaffOne = 0
			self.verticleDrawBoxLineNumberStaffTwo = 0

			for nextBoxDown in range(6):
				self.matrixOfNotesStaffOne[nextVerticleLine][nextBoxDown] = NoteInteractionStaffOne((nextVerticleLine, nextBoxDown), self.screenWidth, self.screenHeight)
				self.matrixOfNotesStaffOne[nextVerticleLine][nextBoxDown].clickBoxStaffOne(self.screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleBoxLineNumberStaffOne)
				self.verticleBoxLineNumberStaffOne += 1

			for nextBoxDownStaffTwo in range(6):
				self.matrixOfNotesStaffTwo[nextVerticleLine][nextBoxDownStaffTwo] = NoteInteractionStaffTwo((nextVerticleLine, nextBoxDownStaffTwo), self.screenWidth, self.screenHeight)
				self.matrixOfNotesStaffTwo[nextVerticleLine][nextBoxDownStaffTwo].clickBoxStaffTwo(self.screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleBoxLineNumberStaffTwo)
				self.verticleBoxLineNumberStaffTwo += 1

			for nextLineDown in range(5):
				self.matrixOfNotesOnLineStaffOne[nextVerticleLine][nextLineDown] = NoteInteractionStaffOne((nextVerticleLine, nextLineDown), self.screenWidth, self.screenHeight)
				self.matrixOfNotesOnLineStaffOne[nextVerticleLine][nextLineDown].clickLineStaffOne(self.screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleLineLineNumberStaffOne)
				self.verticleLineLineNumberStaffOne += 1

			for nextLineDownStaffTwo in range(5):
				self.matrixOfNotesOnLineStaffTwo[nextVerticleLine][nextLineDownStaffTwo] = NoteInteractionStaffTwo((nextVerticleLine, nextLineDownStaffTwo), self.screenWidth, self.screenHeight)
				self.matrixOfNotesOnLineStaffTwo[nextVerticleLine][nextLineDownStaffTwo].clickLineStaffTwo(self.screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleLineLineNumberStaffTwo)
				self.verticleLineLineNumberStaffTwo += 1

			for nextDrawBoxDown in range(5):
				self.matrixOfDrawBoxesStaffOne[nextVerticleLine][nextDrawBoxDown] = NoteInteractionStaffOne((nextVerticleLine, nextDrawBoxDown), self.screenWidth, self.screenHeight)
				self.matrixOfDrawBoxesStaffOne[nextVerticleLine][nextDrawBoxDown].drawBoxStaffOne(self.screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleDrawBoxLineNumberStaffOne)
				self.verticleDrawBoxLineNumberStaffOne += 1

			for nextDrawBoxDownStaffTwo in range(5):
				self.matrixOfDrawBoxesStaffTwo[nextVerticleLine][nextDrawBoxDownStaffTwo] = NoteInteractionStaffTwo((nextVerticleLine, nextDrawBoxDownStaffTwo), self.screenWidth, self.screenHeight)
				self.matrixOfDrawBoxesStaffTwo[nextVerticleLine][nextDrawBoxDownStaffTwo].drawBoxStaffTwo(self.screen, self.screenWidth, self.screenHeight, self.verticleLineNumber, self.verticleDrawBoxLineNumberStaffTwo)
				self.verticleDrawBoxLineNumberStaffTwo += 1

		for nextLineInStaffOne in range(5):
			pygame.draw.line(self.screen, self.black, (2/15 * self.screenWidth, 1/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffOne), (self.screenWidth - 11/90 * self.screenWidth, 1/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffOne), 3)
			self.horizontalLineNumberStaffOne = self.horizontalLineNumberStaffOne + 1

		for nextLineInStaffTwo in range(5):
			pygame.draw.line(self.screen, self.black, (2/15 * self.screenWidth, 3/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffTwo), (self.screenWidth - 11/90 * self.screenWidth, 3/5 * self.screenHeight + 1/25 * self.screenHeight * self.horizontalLineNumberStaffTwo), 3)
			self.horizontalLineNumberStaffTwo = self.horizontalLineNumberStaffTwo + 1
		pygame.draw.line(self.screen, self.black, (13/15 * self.screenWidth + 1/90 * self.screenWidth, self.screenHeight * 4/25), (13/15 * self.screenWidth + 1/90 * self.screenWidth, self.screenHeight - self.screenHeight/5), 5)
		pygame.Surface.blit(self.screen, self.clef, (7/60 * self.screenWidth, 11/60 * self.screenHeight))
		pygame.Surface.blit(self.screen, self.clef, (7/60 * self.screenWidth, 35/60 * self.screenHeight))
		pygame.Surface.blit(self.screen, self.play, (1/60 * self.screenWidth, 1/60 * self.screenHeight))
		pygame.display.flip()

	def	WhenABoxIsClickedInStaffOne(self, clickPositionStaffOne):
		for list in self.matrixOfNotesStaffOne:
			for currentNote in list:
				if currentNote.boxStaffOne.collidepoint(clickPositionStaffOne):
					if (self.listOfNotesStaffOne[currentNote.position[0]] != (-1)):
						pygame.draw.rect(self.screen, self.white, self.matrixOfNotesStaffOne[currentNote.position[0]][self.listOfNotesStaffOne[currentNote.position[0]]].boxStaffOne)
					if (self.listOfLineNotesStaffOne[currentNote.position[0]] != (-1)):
						pygame.draw.rect(self.screen, self.white, self.matrixOfDrawBoxesStaffOne[currentNote.position[0]][self.listOfDrawBoxesStaffOne[currentNote.position[0]]].blitDrawBoxStaffOne)
						pygame.draw.rect(self.screen, self.black, self.matrixOfNotesOnLineStaffOne[currentNote.position[0]][self.listOfLineNotesStaffOne[currentNote.position[0]]].lineStaffOne)
					pygame.Surface.blit(self.screen, currentNote.note, (currentNote.boxStaffOne.x, currentNote.boxStaffOne.y))
					self.listOfNotesStaffOne[currentNote.position[0]] = currentNote.position[1]
					self.listOfLineNotesStaffOne[currentNote.position[0]] = -1
					print(self.listOfNotesStaffOne)

	def	WhenABoxIsClickedInStaffTwo(self, clickPositionStaffTwo):
			for list in self.matrixOfNotesStaffTwo:
				for currentNote in list:
					if currentNote.boxStaffTwo.collidepoint(clickPositionStaffTwo):
						if (self.listOfNotesStaffTwo[currentNote.position[0]] != (-1)):
							pygame.draw.rect(self.screen, self.white, self.matrixOfNotesStaffTwo[currentNote.position[0]][self.listOfNotesStaffTwo[currentNote.position[0]]].boxStaffTwo)
						if (self.listOfLineNotesStaffTwo[currentNote.position[0]] != (-1)):
							pygame.draw.rect(self.screen, self.white, self.matrixOfDrawBoxesStaffTwo[currentNote.position[0]][self.listOfDrawBoxesStaffTwo[currentNote.position[0]]].blitDrawBoxStaffTwo)
							pygame.draw.rect(self.screen, self.black, self.matrixOfNotesOnLineStaffTwo[currentNote.position[0]][self.listOfLineNotesStaffTwo[currentNote.position[0]]].lineStaffTwo)
						pygame.Surface.blit(self.screen, currentNote.note, (currentNote.boxStaffTwo.x, currentNote.boxStaffTwo.y))
						self.listOfNotesStaffTwo[currentNote.position[0]] = currentNote.position[1]
						self.listOfLineNotesStaffTwo[currentNote.position[0]] = -1

						print(self.listOfNotesStaffTwo)

	def	WhenALineIsClickedInStaffOne(self, clickPositionStaffOne):
		for list in self.matrixOfNotesOnLineStaffOne:
			for currentNote in list:
				if currentNote.lineStaffOne.collidepoint(clickPositionStaffOne):
					if (self.listOfLineNotesStaffOne[currentNote.position[0]] != (-1)):
						pygame.draw.rect(self.screen, self.white, self.matrixOfDrawBoxesStaffOne[currentNote.position[0]][self.listOfDrawBoxesStaffOne[currentNote.position[0]]].blitDrawBoxStaffOne)
						pygame.draw.rect(self.screen, self.black, self.matrixOfNotesOnLineStaffOne[currentNote.position[0]][self.listOfLineNotesStaffOne[currentNote.position[0]]].lineStaffOne)
					if (self.listOfNotesStaffOne[currentNote.position[0]] != (-1)):
						pygame.draw.rect(self.screen, self.white, self.matrixOfNotesStaffOne[currentNote.position[0]][self.listOfNotesStaffOne[currentNote.position[0]]].boxStaffOne)
					currentBox = self.matrixOfDrawBoxesStaffOne[self.matrixOfNotesOnLineStaffOne.index(list)][list.index(currentNote)]

					pygame.Surface.blit(self.screen, currentBox.note, (currentBox.blitDrawBoxStaffOne.x, currentBox.blitDrawBoxStaffOne.y))
					self.listOfLineNotesStaffOne[currentNote.position[0]] = currentNote.position[1]
					self.listOfDrawBoxesStaffOne[currentBox.position[0]] = currentBox.position[1]
					self.listOfNotesStaffOne[currentNote.position[0]] = -1

					print(self.listOfLineNotesStaffOne)

	def	WhenALineIsClickedInStaffTwo(self, clickPositionStaffTwo):
		for list in self.matrixOfNotesOnLineStaffTwo:
			for currentNote in list:
				if currentNote.lineStaffTwo.collidepoint(clickPositionStaffTwo):
					if (self.listOfLineNotesStaffTwo[currentNote.position[0]] != (-1)):
						pygame.draw.rect(self.screen, self.white, self.matrixOfDrawBoxesStaffTwo[currentNote.position[0]][self.listOfDrawBoxesStaffTwo[currentNote.position[0]]].blitDrawBoxStaffTwo)
						pygame.draw.rect(self.screen, self.black, self.matrixOfNotesOnLineStaffOne[currentNote.position[0]][self.listOfLineNotesStaffTwo[currentNote.position[0]]].lineStaffTwo)
					if (self.listOfNotesStaffTwo[currentNote.position[0]] != (-1)):
						pygame.draw.rect(self.screen, self.white, self.matrixOfNotesStaffTwo[currentNote.position[0]][self.listOfNotesStaffTwo[currentNote.position[0]]].boxStaffTwo)
					currentBox = self.matrixOfDrawBoxesStaffTwo[self.matrixOfNotesOnLineStaffTwo.index(list)][list.index(currentNote)]
					pygame.Surface.blit(self.screen, currentBox.note, (currentBox.blitDrawBoxStaffTwo.x, currentBox.blitDrawBoxStaffTwo.y))
					self.listOfLineNotesStaffTwo[currentNote.position[0]] = currentNote.position[1]
					self.listOfDrawBoxesStaffTwo[currentBox.position[0]] = currentBox.position[1]
					self.listOfNotesStaffTwo[currentNote.position[0]] = -1

					print(self.listOfLineNotesStaffTwo)
	def CheckSequence(self):
		for i in range(10):
			if self.listOfNotesStaffOne[i] != -1:
				staffOneSound = self.soundList[self.listOfNotesStaffOne[i]]
			elif self.listOfLineNotesStaffOne[i] != -1:
				staffOneSound = self.soundList[self.listOfLineNotesStaffOne[i]]
			else:
				self.error.play()
				return False
			if self.listOfNotesStaffTwo[i] != -1:
				staffTwoSound = self.soundList[self.listOfNotesStaffTwo[i]]
			elif self.listOfLineNotesStaffTwo[i] != -1:
				staffTwoSound = self.soundList[self.listOfLineNotesStaffTwo[i]]
			else:
				self.error.play()
				return False
		return True


	def PlaySequence(self,mousePosition):

		if self.playRect.collidepoint(mousePosition) and self.CheckSequence():
			staffOneSound = self.error
			staffTwoSound = self.error
			for i in range(10):
				if self.listOfNotesStaffOne[i] != -1:
					staffOneSound = self.soundList[self.listOfNotesStaffOne[i]]
				elif self.listOfLineNotesStaffOne[i] != -1:
					staffOneSound = self.soundList[self.listOfLineNotesStaffOne[i]]
				if self.listOfNotesStaffTwo[i] != -1:
					staffTwoSound = self.soundList[self.listOfNotesStaffTwo[i]]
				elif self.listOfLineNotesStaffTwo[i] != -1:
					staffTwoSound = self.soundList[self.listOfLineNotesStaffTwo[i]]

				pygame.mixer.Channel(0).play(staffOneSound)
				pygame.mixer.Channel(1).play(staffTwoSound)
				time.sleep(0.8)





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
		screen.fill(GUI.white)
		GUI.matrixOfNotesStaffOne = [["empty" for boxes in range(6)] for collumns in range(10)]
		GUI.matrixOfNotesStaffTwo = [["empty" for boxes in range(6)] for collumns in range(10)]
		GUI.matrixOfNotesOnLineStaffOne = [["empty" for lines in range(5)] for collumns in range(10)]
		GUI.matrixOfNotesOnLineStaffTwo = [["empty" for lines in range(5)] for collumns in range(10)]
		GUI.matrixOfDrawBoxesStaffOne = [["empty" for drawBoxes in range(5)] for collumns in range(10)]
		GUI.matrixOfDrawBoxesStaffTwo = [["empty" for drawBoxes in range(5)] for collumns in range(10)]
		GUI.listOfNotesStaffOne = [(-1) for i in range(10)]
		GUI.listOfNotesStaffTwo = [(-1) for i in range(10)]
		GUI.listOfLineNotesStaffOne = [(-1) for i in range(10)]
		GUI.listOfLineNotesStaffTwo = [(-1) for i in range(10)]
		GUI.listOfDrawBoxesStaffOne = [(-1) for i in range(10)]
		GUI.listOfDrawBoxesStaffTwo = [(-1) for i in range(10)]
		GUI.createScreen()

	if event.type == pygame.MOUSEBUTTONUP:
		positionOfTheMouse = pygame.mouse.get_pos()
		GUI.WhenABoxIsClickedInStaffOne(positionOfTheMouse)
		GUI.WhenABoxIsClickedInStaffTwo(positionOfTheMouse)
		GUI.WhenALineIsClickedInStaffOne(positionOfTheMouse)
		GUI.WhenALineIsClickedInStaffTwo(positionOfTheMouse)
		GUI.PlaySequence(positionOfTheMouse)

		pygame.display.flip()
