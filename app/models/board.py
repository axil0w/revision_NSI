class Leaderboard(object): #classe de la leaderboard
	"""
	Classe de la leaderboard soit 
	le classement entre les utilisateurs
	base sur leurs moyennes
	"""
	def __init__(self, user_list):
		self.user_list = user_list #liste d utilisateurs sous forme de dico
		self.board = user_list.values() #tous les users, arvitraire car ecrase
	
	def get_ordered_board(self):
		"""
		Permet de trier la liste des utilisateurs en fonction de leurs moyennes
		Tri selection
		"""
		new_board = []
		user_list = list(self.user_list.values())
		for u in range(len(self.user_list)): #tri insertion
			r=0
			while r<u and user_list[u].get_avg()<new_board[r].get_avg():
				r+=1
			new_board.insert(r, user_list [u]) #tri dans la nouvelle liste les users en fct de leur moyenne
		self.board = new_board #assigne le nouveau tableau
		
	def refresh_board(self):
		"""
		Permet d actualiser le tableau des infos de la leaderboard
		(nom, notes, moyenne)
		Out : le tableau trie
		"""
		self.get_ordered_board()
		board = []
		for user in self.board: #effectue un nouveau tableau trie par la moy contenant nom, notes en moy 
			board.append((user.get_name(), user.get_grades(), round(user.get_avg(), 2)))
		self.board = board #assigne ce nouveau tableau
		return self.board
		
	def show(self):
		pass
		
	
		
		
