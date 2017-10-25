from librip.gens import gen_random, field
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 100)
data3 = ['a', 'A', 'b', 'B']

print(*list(i for i in Unique(field(data2), ignore_case=True)), sep=", ")
