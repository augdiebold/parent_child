'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple families and generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

1   2    4           30
 \ /   /  \           \
  3   5    9  15      16
   \ / \    \ /
    6   7   12


Sample input/output (pseudodata):

parentChildPairs = [
    (5, 6), (1, 3), (2, 3), (3, 6), (15, 12),
    (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
]


Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.


Output may be in any order:

findNodesWithZeroAndOneParents(parentChildPairs) => [
  [1, 2, 4, 15, 30],   // Individuals with zero parents
  [5, 7, 9, 16]        // Individuals with exactly one parent
]

'''

parent_child_pairs = [
    (5, 6), (1, 3), (2, 3), (3, 6), (15, 12),
    (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
]


def findNodesWithZeroAndOneParents(data):

    parents = [pair[0] for pair in data]
    children = [pair[1] for pair in data]

    zero_parents = [parent for parent in parents if parent not in children]
    zero_parents = list(set(zero_parents))

    one_parent = sorted([child for child in children if children.count(child)==1])

    return [zero_parents, one_parent]


if __name__ == '__main__':
    assert findNodesWithZeroAndOneParents(parent_child_pairs) == [
        [1, 2, 4, 15, 30],
        [5, 7, 9, 16]
    ]