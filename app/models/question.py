class Question(object): #Pour les questions (type qcm par def)
    def __init__(self, question, proposition, answer, subject, category):
        self.question = question #queston en elle meme
        self.proposition = proposition #differentes propositions
        self.answer = answer #reponse
        self.subject = subject #sujet plus precis de la question

class TextQuestion(object): #Pour les questions (type qcm par def)
    def __init__(self, question, proposition, answer, subject, category):
        self.question = question #queston en elle meme
        self.proposition = proposition #differentes propositions
        self.answer = answer #reponse
        self.subject = subject #sujet plus precis de la question

class LinkQuestion(object): #Pour les questions (type qcm par def)
    def __init__(self, question, proposition, answer, subject, category):
        self.question = question #queston en elle meme
        self.proposition = proposition #differentes propositions
        self.answer = answer #reponse
        self.subject = subject #sujet plus precis de la question
