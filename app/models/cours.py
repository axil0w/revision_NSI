class Cours(object):
  """
  Classe des objets de type Cours
  contenant differents sujets, du cours
  et les reponses au questions
  """
  def __init__(self, category, cours):
	  self.category = category #categorie du cours
		self.subject_list = list(cours.keys()) #liste des sujets
		self.cours = cours 
		
	def get_cours(self):
		return self.cours
	
	def get_base(self, subject):
        """
        retourne le cours en focntion du sujet fourni
        """
		return self.cours[subject]["cours"]
	
	def get_answer(self, answer_id):
    """
    retourne la reponse dune question en avec son id et le sujet concerne
    """
		return self.cours[subject[0]]["answer"][answer_id[1]]
		
class CoursManager(object):
  """
  permet de gerer les objets de type cours
  """
	def __init__(self, cours_list):
		self.cours_list = cours_list
		self.category_list = list(cours_list.keys())
		
	def get_cours_list(self):
		return self.cours_list
		
	def get_cours(self, category, subject):
		return self.cours_list[category].get_base(subject[0])
		
	def get_answer(self, category, answer_id):
    """
    permet de recuperer une reponse avec son id et la categorie
    """
		return self.cours_list[category].get_answer(answer_id)
