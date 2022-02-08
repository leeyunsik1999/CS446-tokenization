from stopper import Stopper
from tokenizer import Tokenizer

# stopper = Stopper()

# print(stopper.check('myar'))
# print(stopper.check('i'))

text = open("./textfiles/tokenization-input-part-A.txt", 'r')
for x in text:
    print(len(x))
    print(Tokenizer.tokenize(x))