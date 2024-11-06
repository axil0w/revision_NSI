class User(object): #Classe pour les users
"""
Classe des users
"""
	def __init__(self, name, grades):
		self.name = name #nom de lutilisateur
		self.grades = grades #notes
		self.login = False
		
	def get_name(self):
		return self.name 
	
	def get_grades(self):
	"""
	Permet d avoir les notes de l utilisateur
	"""
		if len(self.grades) == 0: #si n a psa de notes
			return 0
		return self.grades
	
	def log(self, sen):
		if sen: #si se connecte
			self.login = True #est connecte
		else:
			self.login = False
		return self.login

	def get_avg(self):
	"""
	Permet de retourner la moyenne des notes de l utilisateur
	"""
		sm = 0
		for grade in self.grades: #fait la moyenne des notes
			sm+=grade
		sm/=len(self.grades)
		return sm
	
	def add_grade(self, grade):
	"""
	Permet d ajouter une note
	"""
		self.grades.append(grade) #ajoute une note
	
	def rename(self, name):
	"""
	Permet de renommer un utilisateur
	"""
		self.name = name #change de nome
		
class UserManager(object): 
"""
Permet de gerer les utilisateurs
"""
	def __init__(self, user_list):
		self.user_list = user_list #liste de users
		self.max_user = 5 #nombre max d utilisateurs
	
	def get_user_list(self):
		return self.user_list
	
	def add_user(self, name):
	"""
	ajoute un utiliateur a la liste
	"""
		if len(self.user_list) <= self.max_user: #si assez de place
			user = User(name, []) #ajoute un utilisateur
			self.user_list[name] = user
		else: #si plus de place
			m = "Déjà", self.max_user, " utilisateurs enregistrés, maximum atteint." 
			r = name, " non pris en compte."
			return m, r
	
	def del_user(self, name):
	"""
	supprime un utliateur de la liste
	"""
		del(self.user_list[name]) #supprime un utilisateur
		
	def rename_user(self, user_name, name):
	"""
	Renomme un utilisateur
	"""
		self.user_list[user_name].rename(name) #renome l instance User
		self.user_list[name] = self.user_list.pop(user_name) #change la cle
	
	def connecting(self, name, sen):
		return self.user_list[name].log(sen)
