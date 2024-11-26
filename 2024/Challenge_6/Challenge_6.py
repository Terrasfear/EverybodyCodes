class Tree:

    num_apples = 0
    tree = {}
    apples = {}

    def __init__(self, tree_description):
        self.generateTree(tree_description)

        self.generateApplePaths()


    def generateTree(self, tree_description):
        self.num_apples = 0
        self.tree = {"RR": None}

        for line in tree_description:
            node, branches = line.removesuffix("\n").split(":")
            if node == "ANT" or node == "BUG":
                continue

            branches = branches.split(",")

            for branch in branches:
                if branch == "@":  # apple
                    self.tree[f"@_{self.num_apples}"] = node
                    self.num_apples += 1
                elif branch == "ANT" or branch == "BUG":
                    continue
                else:
                    self.tree[branch] = node

    def generateApplePaths(self):

        for i in range(self.num_apples):
            apple = f"@_{i}"
            self.apples[apple] = ["@"]

            node = apple
            while self.tree[node]:
                node = self.tree[node]
                self.apples[apple].append(node)


for part in [1, 2, 3]:

    with open(f"Input_{part}", 'r') as _file:
        _lines = _file.readlines()

        tree = Tree(_lines)

    lengths = []

    for apple in tree.apples:
        lengths.append(len(tree.apples[apple]))

    for apple_nr, length in enumerate(lengths):
        if lengths.count(length) == 1:
            break

    apple = tree.apples[f"@_{apple_nr}"]

    if part == 1:
        answer = "".join(apple[::-1])
    elif part == 2 or part == 3:
        answer = "".join([node[0] for node in apple[::-1]])
    else:
        answer = -1

    print(f"Part {part}: {answer}", end="\n\n\n")