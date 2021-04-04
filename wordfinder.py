"""Word Finder: finds random words from a dictionary."""
# file to read -> words.txt 
# import random to use special methods
import random 

class WordFinder:
    """Finds random words from a dictionary"""

    # dunder init method 
    def __init__(self, file):
        file_contents = open(file)
        self.words = self.get_words(file_contents) 
        print(f'{len(self.words)} words read')

    # .get_words() method 
    def get_words(self, file_contents):
        """get words from file"""
        return file_contents.read().splitlines() 

    # .random() method 
    def random(self):
        """Returns a random word from a list of words""" 
        return random.choice(self.words) 

# Instantiate 
# wf = WordFinder('words.txt') 
# wf.random() 

# subclass SpecialWordFinder
class SpecialWordFinder(WordFinder):
    """Method that returns a random word from a list of words but does not consider blank lines or words that are plain comments""" 

    # dunder init method
    def __init__(self, file):
        super().__init__(file) 

    def get_words(self, file_contents):
        return [
            word.strip()
            for word in file_contents
            if word.strip() and not word.startswith("#")
        ]