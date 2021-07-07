from random import choice

class WordFinder:
    """Word Finder: creates list of words from reference file."""

    def __init__(self, file_path):
        """ initiates word finder with file path """
        file = open(file_path,"r")
        self.words = self.read_file(file)
        print(f"{len(self.words)} words read")

    def random(self):
        """ returns a random word from word list """
        return choice(self.words)

    def read_file(self, file):
        """ returns list of words from reference file """
        return file.read().splitlines()




class RandomWordFinder(WordFinder): 
    """RandomWordFinder: filters out empty entires and comments"""

    def read_file(self, file):
        """ returns list of words from file without empty entries or comments """
        #replace ele with word
        return [ele for ele in file.read().splitlines()
            if ele != "" and "#" not in ele]
