"""
solver_10_to_0.py
~~~
Solves a game of 10 to 0. The goal of the game is to be the first person to say 0. The starting current number is set to 10. 
The player alternates turns. Each turn, a player can choose to either say a number one less or two less than the 
current number. 
"""
STARTING_NUM = 50

# keep track of the game over state of each position
cache = [-1] * (STARTING_NUM + 1)
# keep track of remoteness
remote_cache = [-1] * (STARTING_NUM + 1)


def game_over(p: int):
	"""
	A bool value if a position is a game over state.

	Args:
		p (int): Position 
	Returns:
		bool: Game over or not
	"""
	return p == 0


def generate_moves(p: int):
	"""
	Generate a list of possible moves from a position.

	Args:
		p (int): Position
	Returns:
		list<int>: List of possible moves, either -1 or -2
	"""
	if p == 0:
		return []
	elif p == 1:
		return [-1]
	else:
		return [-1, -2]


def do_move(p: int, m: int):
	"""
	Perform a given move. Assumes move given is valid.

	Args:
		p (int): Position 
		m (int): Move (either -1 or -2)
	Returns:
		int: The new position
	"""
	return p + m;

def solve(p: int):
	"""
	Solves a given game instance at position p.

	Args:
		p (int): Position
	Returns:
		tuple:
			int: 1 for loss, 0 for win
			int: remoteness
	"""
	# already exists in cache
	if cache[p] != -1:
		return (cache[p], remote_cache[p])

	# if current position is game over state
	if game_over(p):
		cache[p] = 1
		remote_cache[p] = 0
		return (1, 0)

	# figure out outcomes of next possible moves
	possible_moves = generate_moves(p)
	new_p = [do_move(p, m) for m in possible_moves]
	outcomes = [solve(np) for np in new_p]
	outcomes_w = [x for x in outcomes if x[0] == 0]
	outcomes_l = [x for x in outcomes if x[0] == 1]

	# if losing state exists
	if outcomes_l:
		cache[p] = 0
		remote_cache[p] = 1 + min(outcomes_l, key=lambda x: x[1])[1]
		return (cache[p], remote_cache[p])

	cache[p] = 1
	remote_cache[p] = 1 + max(outcomes_w, key=lambda x: x[1])[1]
	return (cache[p], remote_cache[p])


if __name__ == "__main__":
	#print(solve(1))
	
	solve(STARTING_NUM)
	print("Position, Win/Lose, Remoteness")
	for i in range(len(cache)):
		if cache[i]:
			print(i, ": ", "LOSS", ": ", remote_cache[i])
		else:
			print(i, ": ", "WIN", ": ", remote_cache[i])




