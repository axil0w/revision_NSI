import json
from app.models.question import Question, TextQuestion
from app.models.user import User, UserManager
from app.models.cours import Cours, CoursManager

class JsonFile(object): #Pour les fichiers json
	"""
	classe mère traitant des objets json
	"""
	def __init__(self, path):
		self.path = path #emplacment du fichier
		self.data = self.extract_data() #extrait les donnees du fichier

	def extract_data(self):
		"""
		Permet d extraire les donnees dun fichier json
		Out : les donnees du fichier en question
		"""
		with open(self.path) as file: #selon le module json
			data = json.load(file)
			return data

class QuestionFile(JsonFile): #Pour les fichiers json contenant les questions
	"""
	Classe pour le fichier json contenant les questions
	"""
	def __init__(self, path):
		super().__init__(path) #heritage de la classe des fichiers json
		self.sorted_questions = self.sort_data() #ressort l'ensemble des questions

	def sort_data(self):
		"""
		Permet de trier les donnees bruts du fichier json
		Out : les donnees triee sous forme de dico avec les questions en objets
		"""
		data = {}
		for obj in self.data.items(): #pour chaque categorie
			questions = []

			for q_obj in obj[1]["questions"].items(): #pour chaque questions contenues dans la categorie
				question = q_obj[0] #differents attributs de la question
				proposition = q_obj[1]["points"] #pas implementation la plus opti mais la plus claire
				answer = q_obj[1]["answer"]
				subject = q_obj[1]["subject"] #fait lien avec le cours
				category = obj[1]["category"] #theme de la question

				if q_obj[1]["type"] == "text": #trie en fonction du type de question
					questions.append(TextQuestion(question, proposition, answer, subject, category))

				else: #ici question type qcm dites classiques
					questions.append(Question(question, proposition, answer, subject, category))

				data[obj[0]] = questions #dico contenant les questions triees suivant le theme
		return data#sous forme {"theme":[q1, q2, ...]} avec les Q sous forme d objets

class UserFile(JsonFile):
	"""
	Pour les fichiers contenant les donnees des utilisateurs
	"""
	def __init__(self, path):
		super().__init__(path) #heritage de la classe des fichier json
		self.sorted_users = self.sort_data() #donnees une fois traitees
	
	def sort_data(self):
		"""
		permet de trier les donnees bruts du json
		Out : un dico contenant les objets utilisateurs instancies
		"""
		users = {}
		for user in self.data.keys(): #recupere les donnees du ficier json et les traite 
			users[user]=User(user, self.data[user]["grades"]) #creer un dico contenant les users
		return users
		
	def get_users(self):
		return self.sorted_users

	def users_dump(self, user_list): 
		"""
		Permet de faire sauvegarde des users et de leurs notes
		dans le fichier json concerne
		"""
		for user in user_list.keys():
			grades = user_list[user].get_grades()
			
			if user in self.data.keys(): # si le user est bien present dans les anciennes data
				
				if grades != self.data[user]["grades"]: #et si les notes ont changees, les actualiser
					self.data[user]["grades"]=grades

			else: #si pas present dans les anciennes data
				self.data[user] = {"grades":grades} #ajouter le user et ses notes obtenus durant la session
		
		name_list = []
		for user in self.data.keys(): 
			if user not in user_list.keys(): #si utilisateur dans les anciennes data plus presents
				name_list.append(user)
		
		for user in name_list:
			del(self.data[user]) #le supp des data sauvegardee
		
		self.dumping_data()	

	def dumping_data(self):
		"""
		Realise l ecriture dans le fichier json
		"""
		with open(self.path, 'w') as file: #reecrit les donnees dans le fichier json
			json.dump(self.data, file)	

class CoursFile(JsonFile):
	"""
	Traite le fichier json concernant le cours
	"""
	def __init__(self, path):
		super().__init__(path) #heritage de la classe des fichier json
		self.sorted_cours = self.sort_data()
		
	def sort_data(self):
		"""
		Permet de traiter les donnees brut du json
		Out :le dico contenant les donnees du cours
		"""
		cours = {}
		for category in self.data.keys(): #recupere les donnees du ficier json et les traite 
			cours[category]=Cours(category, self.data[category]) #creer un dico contenant les cours
		return cours
		
	def get_cours(self):
		return self.sorted_cours
