from data_manager import QuestionFile, UserFile, CoursFile
from user import UserManager
from question import QuestionManager
from cours import CoursManager
from board import Leaderboard
#differents chemins de fichiers
question_file = "question.json"
user_file = "users.json"
cours_file = "cours.json"
#initialise les différents "manager"s
question_manager = QuestionManager(QuestionFile(question_file).get_question()) 
user_manager = UserManager(UserFile(user_file).get_users())
cours_manager = CoursManager(CoursFile(cours_file).get_cours())
leaderboard = Leaderboard(user_manager.get_user_list())
