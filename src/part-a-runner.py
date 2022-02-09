from processor import Processor

data = Processor().getData()

output = open('../tokenized.txt', 'w')

for str in data:
    output.write(str + '\n')