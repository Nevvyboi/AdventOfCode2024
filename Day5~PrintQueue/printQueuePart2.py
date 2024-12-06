"""
While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?
"""

from collections import defaultdict, deque

with open("pages.txt", "r") as file:
    data = file.readlines()
    data = [data.strip() for data in data if data != "\n"]

pageRules : list[list[int]] =  []
pageNumbersPerUpdate : list[int] = []
canContinueWith : bool = False

lenOfData = len(data)
findNewLinePos = len([d for d in data if "|" in d])
rules = data[:findNewLinePos]
rules = [i for i in [rule.split("|") for rule in rules]]
rules = [[int(num) for num in sublist] for sublist in rules]
updates = data[findNewLinePos:]
updates = [updates.split(",") for updates in updates]
updates = [[int(num) for num in sublist] for sublist in updates]

def checkRules(rulez : list[list[int]]) -> dict:
    graphStructure = {}
    for rule in rulez:
        before = rule[0]
        after = rule[1]
        if before not in graphStructure:
            graphStructure[before] = []
        graphStructure[before].append(after)
    return graphStructure


def isUpdateValid(updater : list[int], graphStructureWithRules : dict) -> bool:
    pageIndex = {page : idx for idx, page in enumerate(updater)}

    for before, afters in graphStructureWithRules.items():
        if before in pageIndex:
            for after in afters:
                if after in pageIndex and pageIndex[before] > pageIndex[after]:
                    return False
    return True

def fixUpdate(update : list[int], rules : list[list[int]]):
    graph = defaultdict(list)
    degree = defaultdict(int)
    for before, after in rules:
        graph[before].append(after)
        degree[after] += 1
        if before not in degree:
            degree[before] = 0

    subgraph = defaultdict(list)
    subsetInDegree = defaultdict(int)
    updateSet = set(update)

    for page in updateSet:
        if page in graph:
            for neighbor in graph[page]:
                if neighbor in updateSet:
                    subgraph[page].append(neighbor)
                    subsetInDegree[neighbor] += 1
        if page not in subsetInDegree:
            subsetInDegree[page] = 0

    queue = deque([node for node in subsetInDegree if subsetInDegree[node] == 0])
    sortedBookOrder = []

    while queue:
        node = queue.popleft()
        sortedBookOrder.append(node)

        for neighbor in subgraph[node]:
            subsetInDegree[neighbor] -= 1
            if subsetInDegree[neighbor] == 0:
                queue.append(neighbor)

    if len(sortedBookOrder) != len(sortedBookOrder):
        return

    return sortedBookOrder

graph = checkRules(rules)
totalValueOfMiddlePageOfCorrectedBooks : int = 0

for i, update in enumerate(updates, start=1):
    if isUpdateValid(update, graph):
        pass
    else:
        correctedBookOrder = fixUpdate(update, rules)
        lengthOfCorrectedBooks = len(correctedBookOrder)
        totalValueOfMiddlePageOfCorrectedBooks += correctedBookOrder[lengthOfCorrectedBooks // 2]

print(totalValueOfMiddlePageOfCorrectedBooks)

