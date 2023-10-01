import pandas
import random as r

# ---------------------------- CONSTANTS ------------------------------- #
FILEPATH = "data/french_words.csv"


# ---------------------------- Functions SETUP ------------------------------- #


class Brain:
    def __init__(self):
        self.data = pandas.read_csv(FILEPATH).to_dict(orient="records")
        self.already_know = []
        self.words_to_choose = self.data

    def random_word(self):
        if len(self.words_to_choose)  > 0:
            return self.words_to_choose[r.randint(0, (len(self.words_to_choose) - 1))]
        else:
            pass

    def right_answer(self, word_dict):
        if len(self.words_to_choose) > 0:
            self.words_to_choose.remove(word_dict)
        else:
            pass

    def not_all_know(self):
        if len(self.words_to_choose) > 1:
            return True
        else:
            return False
