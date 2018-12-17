import pygame
class NoteInteractionStaffOne:
	def __init__(self, position=(-1,-1)):
		self.position = position
		self.status = "empty"
		self.white = [255,255,255]
		self.black = [0,0,0]
		self.noteOnLine = pygame.image.load("noteline.png")
		self.note = pygame.image.load("note.png")
		self.note = pygame.transform.scale(self.note, (int( 1/15 * screenWidth - 3), int(1/25 * screenHeight - 3)))
	
	def clickBoxStaffOne(self, screen, screenWidth, screenHeight, verticleLineNumber,verticleBoxLineNumberStaffOne):
		box = pygame.Rect(2 + 2/15 * screenWidth + verticleLineNumber * 1/15 * screenWidth, 3 + 1/5 * screenHeight - 1/25 * screenHeight + 1/25 * screenHeight * verticleBoxLineNumberStaffOne, 1/15 * screenWidth - 3, 1/25 * screenHeight - 3)
		pygame.draw.rect(screen, self.black, box, 0)

	def	WhenABoxIsRightClickedInStaffOne(self, clickPositionStaffOne):
		for note in self.matrixOfNotesStaffOne[nextVerticleLine][nextBoxDown]:
			note.xmethod

	def WhenABoxIsRightClickedInStaffTwo(self, clickPositionStaffOne):

class NoteInteractionStaffTwo:
	def __init__(self, position=(-1,-1)):
		self.position = position
		self.status = "empty"
		self.white = [255,255,255]
		self.black = [0,0,0]
		self.noteOnLine = pygame.image.load("noteline.png")
		self.note = pygame.image.load("note.png")

	def clickBoxStaffTwo(self, screen, screenWidth, screenHeight, verticleLineNumber,verticleBoxLineNumberStaffTwo):
		boxStaffTwo = pygame.Rect(2 + 2/15 * screenWidth + verticleLineNumber * 1/15 * screenWidth, 3 + 3/5 * screenHeight - 1/25 * screenHeight + 1/25 * screenHeight * verticleBoxLineNumberStaffTwo, 1/15 * screenWidth - 3, 1/25 * screenHeight - 3)
		pygame.draw.rect(screen, self.black, boxStaffTwo, 0)
		pygame.draw.rect(screen, self.black, boxStaffTwo, 0)
	
	def	WhenABoxIsRightClickedInStaffOne(self, clickPositionStaffOne):

	def WhenABoxIsLeftClickedInStaffOne(self, clickPositionStaffOne):
		#if box.collidepoint(pygame.mouse.get_pos()):
		#	if pygame.event.EventType == pygame.MOUSEBUTTONDOWN:
		#		if event.button == 1:
		#			pygame.Surface.blit(self.note, boxStaffTwo)
		#		if event.button == 2:
		#			pygame.draw.rect(screen, self.white, box, 0)
