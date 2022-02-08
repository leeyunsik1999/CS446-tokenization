import re

class Tokenizer():
    def tokenize(input: str):
        """
        input: String to tokenize
        output: Array of strings that the input tokenized to

        Flow: remove apostrophes --> lowercase --> split --> abbreviate each word via regex match

        Reasoning: abbreviate at end so i can simply take the input and .replace all periods from it easily, or split by . and append that to the returning array of strings
        """

        # Array containing words that were tokenized AND stopped to be returned
        output = []

        # Lowercasing stage
        input = input.lower()

        # Removing apostrophes. Tried using  re.sub, but much slower than replace
        input = input.replace('\'', '')

        print(input)

        # Splitting string by special characters, return resulting array of strings
        split = re.findall("[a-z0-9\.]+", input)

        for word in split:
            if re.match('^[a-z]\.(([a-z]\.)+)$', word):
                word = word.replace('.', '')
                print(word)
            else:
                for w in word.split("."):
                    print(w)


Tokenizer.tokenize("one two three four's complement said \"I've got some things to do!\" with N.A.S.A. but not pl.u.ral said \"eh--- don't feel like (doing) this \"")