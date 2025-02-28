1. Preorder Traversal
In preorder traversal, you visit nodes in the following order:

Visit the root node.
Traverse the left subtree.
Traverse the right subtree.
The sequence is: Root -> Left -> Right.

Example: For the tree:

    1
   / \
  2   3
 / \
4   5
Preorder traversal would be: 1, 2, 4, 5, 3.

2. Inorder Traversal
In inorder traversal, you visit nodes in the following order:

Traverse the left subtree.
Visit the root node.
Traverse the right subtree.
The sequence is: Left -> Root -> Right.

Example: For the same tree:

    1
   / \
  2   3
 / \
4   5
Inorder traversal would be: 4, 2, 5, 1, 3.

3. Postorder Traversal
In postorder traversal, you visit nodes in the following order:

Traverse the left subtree.
Traverse the right subtree.
Visit the root node.
The sequence is: Left -> Right -> Root.

Example: For the same tree:

    1
   / \
  2   3
 / \
4   5
Postorder traversal would be: 4, 5, 2, 3, 1.

Visualizing Traversals
To help visualize these traversals, imagine walking around the tree:

Preorder: You visit nodes as soon as you encounter them.
Inorder: You visit nodes after exploring their left subtree but before their right subtree.
Postorder: You visit nodes only after exploring both subtrees.



 Let's look at examples of preorder, inorder, and postorder traversals for a larger binary tree. Here's a tree for reference:

        10
       /  \
      5    15
     / \   / \
    3   7 12  18
   / \   \
  1   4   8
Preorder Traversal
Order: Root -> Left -> Right

Traversal: 10, 5, 3, 1, 4, 7, 8, 15, 12, 18

Inorder Traversal
Order: Left -> Root -> Right

Traversal: 1, 3, 4, 5, 7, 8, 10, 12, 15, 18

Postorder Traversal
Order: Left -> Right -> Root

Traversal: 1, 4, 3, 8, 7, 5, 12, 18, 15, 10