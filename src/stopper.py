class Stopper():
    def __init__(self):
        self.stopwords = set()
        stopwordText = open("./textfiles/stopwords.txt", 'r')
        for x in stopwordText:
            # Tested this with x[0:(len(x)-1)]-- takes essentially the same time as replace, so i'm just using replace for readability
            self.stopwords.add(x.replace('\n',''))

    def check(self, input):
        return input in self.stopwords
