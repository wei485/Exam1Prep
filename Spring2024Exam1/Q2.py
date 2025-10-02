#PartA
ideas_1 = ('robot arm', 'calculator', 'engine')
ideas_2 = ('toaster', 'toaster oven', 'robot arm')
ideas_3 = ('engine', 'car', 'toaster')

set1 = set(ideas_1)
set2 = set(ideas_2)
set3 = set(ideas_3)

set1 = set1.union(set2)
set1 = set1.union(set3)

unique_ideas = tuple(set1)

#Test
print(unique_ideas)

#PartB
votes = [1, 5, 2, 4]
ideas = ['clock', 'toaster', 'calculator', 'robot arm']

ordered_list = []

voteIdeaDict = {}

for i in range(len(votes)):
    voteIdeaDict[votes[i]] = ideas[i]

sort = sorted(voteIdeaDict)

for o in sort:
    ordered_list.append(voteIdeaDict[o])

#test
print(ordered_list)

#PartC
supplies_dict = {'wire': 50, 'wheels': 4, 'breadboard': 6}

supplies_set = set()

for x,y in supplies_dict.items():
    if y < 5 or y > 10:
        supplies_set.add(x)

#test
print(supplies_set)
