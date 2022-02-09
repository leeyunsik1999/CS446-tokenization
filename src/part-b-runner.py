from processor import Processor
import matplotlib.pyplot as plt

processor = Processor(part_a=False)

data = processor.getData().most_common(300)
graph_data = processor.getGraphData()

output = open('../terms.txt', 'w')

plt.plot(graph_data[0], graph_data[1], '.-b', markersize=1)
plt.xlabel("Words in Collection")
plt.ylabel("Words in Vocabulary")
plt.show()
for tup in data:
    output.write(f"{tup[0]} {tup[1]}\n")