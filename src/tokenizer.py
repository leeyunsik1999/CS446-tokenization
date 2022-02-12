class Tokenizer():
    def abbreviate(word):
        """
        takes in a word and returns if it's an abbreviation or not.
        """
        if len(word) < 3 or len(word)%2 == 1:
            return False
        expect_period = False
        for letter in word:
            if letter.isnumeric():
                return False
            if expect_period:
                if letter != '.':
                    return False
                expect_period = False
            else:
                if letter == '.':
                    return False
                expect_period = True
        return True