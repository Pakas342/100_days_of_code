import pandas
import random as r

# ---------------------------- CONSTANTS ------------------------------- #
FIRST_FILEPATH = "data/french_words.csv"
SECOND_FILEPATH = "data/french_words_yet_to_know.csv"

# ---------------------------- Functions SETUP ------------------------------- #


class Brain:
    def __init__(self):
        try:
            self.data = pandas.read_csv(SECOND_FILEPATH).to_dict(orient="records")
        except FileNotFoundError:
            self.data = pandas.read_csv(FIRST_FILEPATH).to_dict(orient="records")

        self.already_know = []
        self.words_to_choose = self.data

    def random_word(self):
        if len(self.words_to_choose) > 0:
            return self.words_to_choose[r.randint(0, (len(self.words_to_choose) - 1))]
        else:
            pass

    def right_answer(self, word_dict):
        if len(self.words_to_choose) > 0:
            self.words_to_choose.remove(word_dict)
            new_data = pandas.DataFrame(self.words_to_choose)
            new_data.to_csv(SECOND_FILEPATH, index=False)
        else:
            pass

    def not_all_know(self):
        if len(self.words_to_choose) > 1:
            return True
        else:
            return False
