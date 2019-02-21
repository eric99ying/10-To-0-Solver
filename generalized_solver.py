"""
generalized_solver
~~~
Solves 10 to 0 with 1,2,-1. 
"""
# Some important constants
STARTING_NUM = 10
WIN = 0
LOSS = 1
DRAW = 2

# Keep track of the state of each position. 0 == WIN, 1 == LOSE, 2 == DRAW
cache = [-1] * (STARTING_NUM + 1)

# Assumes STARTING_NUM is at least larger than 3
def generate_moves(p: int):

	if p == 0:
		return []
	elif p == 1:
		return [0, 2]
	elif p == STARTING_NUM:
		return [STARTING_NUM - 1, STARTING_NUM - 2]
	else:
		return [p - 1, p - 2, p + 1]


def solve(p: int):

	# Traverse the game tree and assign back pointers and children numbers
	children_number = [0] * (STARTING_NUM + 1)
	back_pointers = [[] for i in range(STARTING_NUM + 1)]
	visited = [False for i in range(STARTING_NUM + 1)]
	dfs_fringe = [STARTING_NUM]

	while len(dfs_fringe) != 0:
		element = dfs_fringe.pop(0)
		visited[element] = True
		succesors = generate_moves(element)
		for suc in succesors:
			back_pointers[suc].append(element)
			children_number[element] += 1
			if not visited(suc):
				dfs_fringe.append(suc)


	# Solve the game
	fringe = [(p, LOSS)]
	visited = [False for i in range(STARTING_NUM + 1)]

`   # Continue until the fringe is empty, pop out the first element and set visited to True
	while len(fringe) != 0:
		element_pair = fringe.pop(0)
		element = element_pair[0]
		status = element_pair[1]
		visited[element] = True

		# If that element was a losing position, set any parent to a winning position.
		if status == LOSS:
			parents = back_pointers[element]
			for par in parents:
				cache[par] = WIN
				if not visited(par):
					fringe.append((par, WIN))
		elif status == WIN:
			parents = back_pointers[element]
			for par in parents:
				children_number[par] -= 1
				if children_number[par] == 0:
					cache[par] = LOSS
					if not visited(par):
						fringe.append((par, LOSS))



	# Any node not visited is a draw
	for i in range(len(cache)):
		if cache[i] == -1:
			cache[i] = DRAW


# Script that solves and prints out the status of each move
if __name__ == "__main__":
	
	solve(STARTING_NUM)
	print("Position, Win/Lose, Remoteness")
	for i in range(len(cache)):
		if cache[i] == WIN:
			print(i, ": ", "WIN")
		elif cache[i] == LOSS:
			print(i, ": ", "LOSS")
		else:
			print(i, ": ", "DRAW")




