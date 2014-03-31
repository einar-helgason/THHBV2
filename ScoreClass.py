class ScoreClass():
	
	winScore = 0
	score=0
	Tx = 0
	Sx = 0
	Cx = 0
	set = 0

	#Turning over a face down tableau card
	def TurnOver():
		maxP = 525
		set = 25 
		if(Tx <= maxP - set)
			score += set
			Tx += set
		if(Tx >= maxP)
			break
		if(Tx > maxP - set && Tx < maxP)
			score += maxP - Tx
			Tx += maxP - Tx

	#Playing a card from stock to tableau
	def StockToTab():
		set = 45
		maxS = 1080
		if(Sx <= maxS - set)
			score += set
			Sx += set
		if(Sx >= maxS)
			break
		if(Sx > maxS - set && Sx < maxS)
			score += maxS - Sx
			Sx += maxS - Sx

	#Transferring a card to the foundations	
	def CardToFound():
		set = 60
		maxC = 3120
		if(Cx <= maxC - set)
			score += set
			Cx += set
		if(Cx >= maxC)
			break
		if(Cx > maxC - set && Cx < maxC)
			score += maxC - Cx
			Cx += maxC - Cx

	#Every second of elapsed time
	def Seconds():
		set = -1
		score += set

	#Every time Undo is used
	def Undo():
		set = -25
		score += set

	#Exposed card of a packed column to another packed column
	def PackecColumn():
		set = -25
		score += set

	#Moving a foundation card back to the tableau
	def FoundToTabl():
		set = -75
		score += set

	#Each re-deal after the third pass through the stock (Deal 3)
	def reDeal3():
		set = -125
		score += set

	#Each re-deal after the first pass through the stock (Deal 1)
	def reDeal1():
		set = -200
		score += set

	#Each re-deal after the first pass through the stock (Unlimited Passes)
	def reDealUL():
		set = -175
		score += set

	def Win(score, timePassed):
		winScore = (2*score)-(10*timePassed)
		return winScore