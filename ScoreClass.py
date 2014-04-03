class Score(object):
	
	def __init__(self):
		self.winScore = 0
		self.score = 0
		self.Tx = 0
		self.Sx = 0
		self.Cx = 0
		self.set = 0

	#Turning over a face down tableau card
	def TurnOver(self):
		maxP = 525
		set = 25 
		if(self.Tx <= maxP - set):
			self.score += set
			self.Tx += set
		if(self.Tx >= maxP):
			pass
		if(self.Tx > (maxP - set) and self.Tx < maxP):
			self.score += maxP - self.Tx
			self.Tx += maxP - self.Tx

	#Playing a card from stock to tableau
	def StockToTabl(self):
		set = 45
		maxS = 1080
		if(self.Sx <= maxS - set):
			self.score += set
			self.Sx += set
		if(self.Sx >= maxS):
			pass
		if(self.Sx > (maxS - set) and self.Sx < maxS):
			self.score += maxS - self.Sx
			self.Sx += maxS - self.Sx

	#Transferring a card to the foundations	
	def CardToFound(self):
		set = 60
		maxC = 3120
		if(self.Cx <= (maxC - set)):
			self.score += set
			self.Cx += set
		if(self.Cx >= maxC):
			pass
		if(self.Cx > (maxC - set) and self.Cx < maxC):
			self.score += maxC - self.Cx
			self.Cx += maxC - self.Cx

	#Every second of elapsed time
	def Seconds(self):
		set = -1
		self.score += set

	#Every time Undo is used
	def Undo(self):
		set = -25
		self.score += set

	#Exposed card of a packed column to another packed column
	def PackecColumn(self):
		set = -25
		self.score += set

	#Moving a foundation card back to the tableau
	def FoundToTabl(self):
		set = -75
		self.score += set

	#Each re-deal after the first pass through the stock (Deal 1)
	def reDeal1(self):
		set = -200
		self.score += set
		
	#Each re-deal after the third pass through the stock (Deal 3)
	def reDeal3(self):
		set = -125
		self.score += set

	#Each re-deal after the first pass through the stock (Unlimited Passes)
	def reDealUL(self):
		set = -175
		self.score += set

	def Win(self,timePassed):
		winScore = (2*self.score)-(10*timePassed)
		return winScore