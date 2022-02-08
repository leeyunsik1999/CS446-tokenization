from processor import Processor

data = Processor().getData()

output = open('../part_a_output.txt', 'w')

for str in data:
    output.write(str + '\n')