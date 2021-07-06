from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        self.f = open(file_path,"r")
        self.words = self.f.read().split("\n")
        print(f"{len(self.words)} words read")

    def random(self):
        return choice(self.words)
        
        
    
    