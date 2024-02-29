from model.Tree import Tree

def main():
    root = Tree(10)
    root = root.add(root, 15)
    root = root.add(root, 2)
    root = root.add(root, 7)
    root = root.add(root, 18)
    root = root.add(root, 12)
    root = root.add(root, 20)

    print(root.pre_order(root))
    print(root.in_order(root))
    print(root.post_order(root))
    print(root.height(root))
    print(root.weight(root))
    print(root.lessest(root))
    print(root.greatest(root))
    print(root.exists(root, 1))
    print(root.exists(root, 12))
    print(root.exists(root, 18))

if __name__ == "__main__":
    main()