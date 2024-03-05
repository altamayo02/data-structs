from model.Tree import Tree

def is_bst(tree):
    inorder = tree.in_order(tree)
    for i in range(len(inorder) - 1):
        if inorder[i] > inorder[i + 1]:
            return False
    return True

def main():
    tree = Tree(10)
    tree = tree.add(tree, 15)
    tree = tree.add(tree, 2)
    tree = tree.add(tree, 7)
    tree = tree.add(tree, 18)
    tree = tree.add(tree, 12)
    tree = tree.add(tree, 20)

    print(tree.pre_order(tree))
    print(tree.in_order(tree))
    print(tree.post_order(tree))
    print(tree.height(tree))
    print(tree.weight(tree))
    print(tree.lessest(tree))
    print(tree.greatest(tree))
    print(tree.exists(tree, 1))
    print(tree.exists(tree, 12))
    print(tree.exists(tree, 18))
    print(is_bst(tree))


if __name__ == "__main__":
    main()