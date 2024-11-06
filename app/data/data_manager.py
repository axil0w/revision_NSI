import json
from app.models.question import Question, TextQuestion, LinkQuestion

class JsonFile(object): #Pour les fichiers json
    def __init__(self, path):
        self.path = path #emplacment du fichier
        self.data = self.extract_data() #extrait les donnees du fichier

    def extract_data(self):
        with open(self.path) as file: #selon le module json
            data = json.load(file)
            return data

class QuestionFile(JsonFile): #Pour les fichiers json contenant les questions
    def __init__(self, path):
        super().__init__(path) #heritage de la classe des fichiers json
        self.sorted_questions = self.sort_data() #ressort l'ensemble des questions

    def sort_data(self):
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

                elif q_obj[1]["type"] == "link":
                    questions.append(LinkQuestion(question, proposition, answer, subject, category))

                else: #ici question type qcm dites classiques
                    questions.append(Question(question, proposition, answer, subject, category))

                data[obj[0]] = questions #dico contenant les questions triees suivant le theme
        return data #sous forme {"theme":[q1, q2, ...]} avec les Q sous forme d objets

class UserFile(JsonFile): #Pour les fichiers contenant les donnees des utilisateurs
    def __init__(self, path):
        super().__init__(path) #heritage de la classe des fichier json

print(QuestionFile("/questions.json").sorted_questions)