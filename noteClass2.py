import pygame
class NoteInteractionStaffOne:
	def __init__(self,position,screenWidth,screenHeight):
		self.position = position
		self.status = "empty"
		self.white = [255,255,255]
		self.black = [0,0,0]
		self.color = [255,0,0]
		self.note = pygame.transform.scale(pygame.image.load("note.png"), (int( 1/15 * screenWidth - 3), int(1/25 * screenHeight - 3)))

	def clickBoxStaffOne(self, screen, screenWidth, screenHeight, verticleLineNumber,verticleBoxLineNumberStaffOne):
		self.boxStaffOne = pygame.Rect(2 + 2/15 * screenWidth + verticleLineNumber * 1/15 * screenWidth, 3 + 1/5 * screenHeight - 1/25 * screenHeight + 1/25 * screenHeight * verticleBoxLineNumberStaffOne, 1/15 * screenWidth - 3, 1/25 * screenHeight - 3)
		# pygame.draw.rect(screen, self.black, self.boxStaffOne, 0)

	def drawBoxStaffOne(self, screen, screenWidth, screenHeight, verticleLineNumber,verticleDrawBoxLineNumberStaffOne):
		self.blitDrawBoxStaffOne = pygame.Rect(2 + 2/15 * screenWidth + verticleLineNumber * 1/15 * screenWidth, 3 + 1/5 * screenHeight - 1/50 * screenHeight + 1/25 * screenHeight * verticleDrawBoxLineNumberStaffOne, 1/15 * screenWidth - 3, 1/25 * screenHeight - 3)
		# pygame.draw.rect(screen, self.black, self.drawBoxStaffOne, 0)
		#pygame.draw.rect(screen, self.black, self.drawBoxStaffOne, 0)


	def clickLineStaffOne(self, screen, screenWidth, screenHeight, verticleLineNumber,verticleLineLineNumberStaffOne):
		self.lineStaffOne = pygame.Rect(2 + 2/15 * screenWidth + verticleLineNumber * 1/15 * screenWidth, -1 + 1/5 * screenHeight + 1/25 * screenHeight * verticleLineLineNumberStaffOne, 1/15 * screenWidth - 3, 3)
		#pygame.draw.rect(screen, self.color, self.lineStaffOne, 0)

class NoteInteractionStaffTwo:
	def __init__(self, position,screenWidth,screenHeight):
		self.position = position
		self.status = "empty"
		self.white = [255,255,255]
		self.black = [0,0,0]
		self.color = [255,0,0]
		self.note = pygame.transform.scale(pygame.image.load("note.png"), (int( 1/15 * screenWidth - 3), int(1/25 * screenHeight - 3)))

	def clickBoxStaffTwo(self, screen, screenWidth, screenHeight, verticleLineNumber,verticleBoxLineNumberStaffTwo):
		self.boxStaffTwo = pygame.Rect(2 + 2/15 * screenWidth + verticleLineNumber * 1/15 * screenWidth, 3 + 3/5 * screenHeight - 1/25 * screenHeight + 1/25 * screenHeight * verticleBoxLineNumberStaffTwo, 1/15 * screenWidth - 3, 1/25 * screenHeight - 3)
		# pygame.draw.rect(screen, self.black, self.boxStaffTwo, 0)

	def drawBoxStaffTwo(self, screen, screenWidth, screenHeight, verticleLineNumber,verticleDrawBoxLineNumberStaffTwo):
		self.blitDrawBoxStaffTwo = pygame.Rect(2 + 2/15 * screenWidth + verticleLineNumber * 1/15 * screenWidth, 3 + 3/5 * screenHeight - 1/50 * screenHeight + 1/25 * screenHeight * verticleDrawBoxLineNumberStaffTwo, 1/15 * screenWidth - 3, 1/25 * screenHeight - 3)
		# pygame.draw.rect(screen, self.black, self.drawBoxStaffTwo, 0)
		#pygame.draw.rect(screen, self.black, self.drawBoxStaffTwo, 0)


	def clickLineStaffTwo(self, screen, screenWidth, screenHeight, verticleLineNumber,verticleLineLineNumberStaffTwo):
		self.lineStaffTwo = pygame.Rect(2 + 2/15 * screenWidth + verticleLineNumber * 1/15 * screenWidth, -1 + 3/5 * screenHeight + 1/25 * screenHeight * verticleLineLineNumberStaffTwo, 1/15 * screenWidth - 3, 3)
		#pygame.draw.rect(screen, self.color, self.lineStaffTwo, 0)
