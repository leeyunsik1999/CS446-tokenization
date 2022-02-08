import re   
from stopper import Stopper
from stemmer import Stemmer
from collections import Counter

"""
The main processor for the project.

Contains the logic for the tokenization part, as it made more sense to do stopping and stemming during tokenization.

This is to avoid multiple passthroughs of the array of tokenized strings.

+ This way, I can add some if/else logic within the process to tell if it's part A or B, so I can run both in the same script (here).

Stopper and stemmer is still a separate class/file.

Reason for having this as a class: I wanted to be able to pass in a flag for part a/b, and didn't want to make people require using command line inputs.
+ Also wanted to differentiate what scripts to run (part-a-runner vs part-b-runner) for each part.
"""


class Processor():
    def __init__(self, part_a=True):
        self.part_a = part_a
        self.stopper = Stopper()
        # Obtain text to process
        text = self.getText()

        # Array of indexes to if part A, else counter for part B
        self.data = [] if part_a else Counter()

        for line in text:
            """
            Tokenizing part. Also adds to array / counter, depending on part_a flag.

            Flow: remove apostrophes --> lowercase --> split --> abbreviate --> stop --> stem --> add to array/collection

            I decided to stop during the tokenizer process 

            Reasoning: abbreviate at end so i can simply take the input and .replace all periods from it easily, or split by . and append that to the returning array of strings
            """

            # Lowercasing stage
            line = line.lower()

            # Removing apostrophes. Tried using  re.sub, but much slower than replace
            line = line.replace('\'', '')

            # Splitting string by special characters, return resulting array of strings
            tokens = re.findall("[a-z0-9\.]+", line)

            for token in tokens:
                """
                Part for abbreviating, stopping and stemming individual words. Then, depending on part A or B, simply appends to an array or to counter.
                """
                # Abbreviating. Pairs of letter and period --> strip periods. After abbreviating, run it through stopper and stemmer.
                if re.match('^[a-z]\.(([a-z]\.)+)$', token):
                    token = token.replace('.', '')
                    self.stop_and_stem(token)
                else:
                    for s in token.split("."):
                        self.stop_and_stem(s)


    def getText(self):
        """
        Method that reads the text to process.

        Imports part A text if self.part_a is True. Imports part B if not.
        """
        text = open(
            f"tokenization-input-part-{'A' if self.part_a else 'B'}.txt")
        return text


    def stop_and_stem(self, token):
        """
        Method that takes in a token.

        Checks if it is a stopword. If it is, do nothing.

        If it is not, stem it, and then add to appropriate list / counter depending on part_a flag.
        """
        # Checking if token is a stopword. Stem only if it isn't. If it is, do nothing
        if not self.stopper.check(token):
            #TODO: Stem word

            if (self.part_a):
                self.data.append(token)
            else:
                self.data[token] += 1
