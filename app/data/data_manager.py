import json


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



