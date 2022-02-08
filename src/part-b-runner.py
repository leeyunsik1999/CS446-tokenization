from processor import Processor

data = [x[0] for x in Processor(part_a=False).getData().most_common(300)]

output = open('../part_b_output.txt', 'w')

for str in data:
    output.write(str + '\n')