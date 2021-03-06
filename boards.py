import logic_components


def change(color) -> int:
	if color == 0:
		return 1
	return 0

def boardA() -> logic_components.Board:

	r = 14
	c = 17
	rinstr = [[4,4],[6,6],[2,3,2],[2,4,1,4,2],[2,5,5,2],[2,11,2],
		[2,9,2],[2,7,2],[2,5,2],[2,3,2],[2,1,2],[2,2],[3],[1]]
	cinstr = [[3],[5],[2,2],[2,3,2],[2,4,2],[2,5,2],[2,6,2],[2,6,2],
	[2,6,2],[2,6,2],[2,6,2],[2,5,2],[2,4,2],[2,3,2],[2,2],[5],[3]]
	intsol = [[0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0],
	[0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0],
	[0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0],
	[1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1],
	[1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
	[1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
	[0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0],
	[0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0],
	[0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,0],
	[0,0,0,0,1,1,0,1,1,1,0,1,1,0,0,0,0],
	[0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0],
	[0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]]

	bsol = []
	for row in range(r):
		bsol.append([])
		for col in range(c):
			bsol[row].append(True if intsol[row][col]==1 else False)
	return logic_components.Board(r, c, rinstr, cinstr, bsol)

def boardB() -> logic_components.Board:
	bsol2 = []
	r2 = 20
	c2 = 20

	r2instr = [[12],[14],[4,4],[3,2,2,3],[4,1,1,4],[2,2,2,2,2,2],
	[1,1,1,2,2,1,1,1],[1,1,1,1,1,3,1],[1,1,2,4,1],[1,5,1,1,5,1],
	[1,2,2,1],[4,1,1,4],[2,4,2],[3,1,1,2],[2,2,3],[4,6],[3,4,6],
	[3,5],[3,5],[3,6]]
	c2instr = [[5],[2,1,2],[1,4,1,3],[5,3,4],[14,3],[4,2,6],[3,1,1,3],
	[2,1,2,1,1],[2,1,3,2,1],[2,1,1,1,1],[2,1,1,1],[2,1,2,1,2,1],
	[2,1,3,1,1],[3,1,1,2],[4,2,6,1],[20],[5,5,5],[1,4,1,5],[2,1,4],
	[5,4]]
	intsol2 = [[0,[4,12,4]],
	[0,[3,14,3]],
	[0,[3,4,6,4,3]],
	[0,[3,3,1,2,2,2,1,3,3]],
	[0,[1,4,1,1,6,1,1,4,1]],
	[1,[2,1,2,2,2,2,2,2,2,1,2]],
	[1,[1,1,1,1,1,2,2,2,2,2,1,1,1,1,1]],
	[1,[1,1,1,1,1,3,1,3,1,2,3,1,1]],
	[1,[1,1,1,1,2,8,4,1,1]],
	[1,[1,1,5,2,1,1,1,1,5,1,1]],
	[0,[1,1,1,2,10,2,1,1,1]],
	[0,[2,4,1,1,4,1,1,4,2]],
	[0,[4,2,2,4,2,2,4]],
	[0,[4,3,1,1,2,1,2,2,4]],
	[0,[5,2,2,2,2,3,4]],
	[0,[4,4,4,6,2]],
	[0,[3,3,2,4,2,6]],
	[0,[2,3,10,5]],
	[0,[1,3,11,5]],
	[0,[1,3,10,6]]]

	for row in range(r2):
		bsol2.append([])
		color = intsol2[row][0]
		changes = intsol2[row][1]
		index = 0
		for streak in changes:
			for i in range(index, index+streak):
				if color == 1:
					bsol2[row].append(True)
				if color == 0:
					bsol2[row].append(False)
			color = change(color)
			index += streak
	return logic_components.Board(r2, c2, r2instr, c2instr, bsol2)

def boardC():
	bsol = []
	r = 15
	c = 15

	rinstr = [[6], [1,1],[1,1],[6],[4,6],[1,1,1,2],[15],[6,6],[5,3,5],[4,1,1,4],[4,1,1,4],[4,1,1,4],[5,3,5],[6,6],[15]]
	cinstr = [[9],[10],[9],[11],[1,3,3],[1,2,3,2],[3,1,1,1],[1,1,1,1],[1,1,1,1],[5,2,3,2],[1,2,3,3],[1,12],[1,12],[1,2,9],[5,9]]

	intsol = [[0,[9,6]],
	[0,[9,1,4,1]],
	[0,[9,1,4,1]],
	[0,[9,6]],
	[0,[3,4,2,6]],
	[0,[1,1,1,1,2,1,4,2,2]],
	[1,[15]],
	[1,[6,3,6]],
	[1,[5,1,3,1,5]],
	[1,[4,1,1,3,1,1,4]],
	[1,[4,1,1,3,1,1,4]],
	[1,[4,1,1,3,1,1,4]],
	[1,[5,1,3,1,5]],
	[1,[6,3,6]],
	[1,[15]]]

	for row in range(r):
		bsol.append([])
		color = intsol[row][0]
		changes = intsol[row][1]
		index = 0
		for streak in changes:
			for i in range(index, index+streak):
				if color == 1:
					bsol[row].append(True)
				if color == 0:
					bsol[row].append(False)
			color = change(color)
			index += streak
	return logic_components.Board(r, c, rinstr, cinstr, bsol)

def boardD():
	bsol = []
	r = 15
	c = 15

	rinstr = [[3], [4,2], [6,6], [6,2,1], [1,4,2,1], [6,3,2], [6,7], [6,8],[1,10], [1,10], [1,10], [1,1,4,4], [3,4,4], [4,4], [4,4]]
	cinstr = [[1], [11], [3,3,1], [7,2], [7], [15], [1,5,7], [2,8], [14], [9], [1,6], [1,9], [1,9], [1,10], [12]]

	intsol = [[0,[5,3,7]],
	[0,[2,4,1,2,6]],
	[0,[1,6,1,6,1]],
	[0,[1,6,1,2,4,1]],
	[0,[1,1,1,4,1,2,4,1]],
	[0,[1,6,1,3,2,2]],
	[0,[1,6,1,7]],
	[1,[6,1,8]],
	[0,[1,1,3,10]],
	[0,[1,1,3,10]],
	[0,[1,1,3,10]],
	[0,[1,1,1,1,1,4,2,4]],
	[0,[1,3,1,4,2,4]],
	[0,[5,4,2,4]],
	[0,[5,4,2,4]]]

	for row in range(r):
		bsol.append([])
		color = intsol[row][0]
		changes = intsol[row][1]
		index = 0
		for streak in changes:
			for i in range(index, index+streak):
				if color == 1:
					bsol[row].append(True)
				if color == 0:
					bsol[row].append(False)
			color = change(color)
			index += streak
	return logic_components.Board(r, c, rinstr, cinstr, bsol)

def boardE():
	bsol = []
	r = 20
	c = 20

	rinstr = [[4,4], [6,6], [4,2,4,2,4], [3,10,3], [20], [7,7], [5,5], [3,2,2,3], [2,2,2,2], [3,1,1,2], [1,2], [1,3,2], [2,3,2], [2,2], [1,2,1],
			[1,1], [2,4,2], [2,2], [2,2], [14]]
	cinstr = [[4], [6], [7], [3,4,1], [2,9,2], [10,2,4], [5,1,2,2,1], [2,1,1], [3,3,1,1], [3,2,2,1,1,1], [3,2,1,1,1], [3,3,2,1,1], [2,2,1,1],
			[5,2,2,1], [14,4], [2,9,2], [3,4,1], [7], [6], [4]]

	intsol = [[0,[2,4,8,4,2]],
	[0,[1,6,6,6,1]],
	[1,[4,1,2,1,4,1,2,1,4]],
	[1,[3,2,10,2,3]],
	[1,[20]],
	[1,[7,6,7]],
	[0,[1,5,8,5,1]],
	[0,[3,3,2,2,1,2,1,3,3]],
	[0,[4,2,2,2,1,2,1,2,4]],
	[0,[4,3,1,1,2,1,2,2,4]],
	[0,[4,1,9,2,4]],
	[0,[4,1,4,3,2,2,4]],
	[0,[4,2,3,3,2,2,4]],
	[0,[5,2,6,2,5]],
	[0,[6,1,2,2,2,1,6]],
	[0,[7,1,4,1,7]],
	[0,[5,2,1,4,1,2,5]],
	[0,[5,2,6,2,5]],
	[0,[4,2,8,2,4]],
	[0,[3,14,3]]]

	for row in range(r):
		bsol.append([])
		color = intsol[row][0]
		changes = intsol[row][1]
		index = 0
		for streak in changes:
			for i in range(index, index+streak):
				if color == 1:
					bsol[row].append(True)
				if color == 0:
					bsol[row].append(False)
			color = change(color)
			index += streak
	return logic_components.Board(r, c, rinstr, cinstr, bsol)




def test():
	A = boardA()
	B = boardB()
	print(A.checkIfSolved(), B.checkIfSolved())
	A.printBoard()

def test2():
	c = boardC()
	print(c.rows(), c.cols())

def test3():
	d = boardD()
	print(d.rows(), d.cols())
	print("this should be 15,15")
	print(len(d.rowinstr()), len(d.colinstr()))
	print("this should be 15,15")
	for i in d.solution():
		print(len(i))
	print("These should all equal 15")

def test4():
	e = boardE()
	print(e.rows() == 20, e.cols() == 20)
	print(len(e.rowinstr()) == 20, len(e.colinstr()) == 20)
	print(len(e.solution()) == 20)
	for i in e.solution():
		print(len(i) == 20)
if __name__ == '__main__':
	test4()
