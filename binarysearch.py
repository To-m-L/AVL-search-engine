class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 0
class BST:
    def __init__(self):
        self.root = None
    
    #Checks if the tree's root is null
    #returns True if it is, returns False if it is not
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    #Gets the height of a particular node
    def getHeight(self, node):
        if node is None:
            return 0
 
        return max(self.getHeight(node.left), self.getHeight(node.right)) +1

    #Goes through the whole tree and applies getHeight to all the nodes
    def fixHeight(self, root):
        if root:
            root.height = self.getHeight(root)
            self.fixHeight(root.left)
            self.fixHeight(root.right)

    #Insert function
    #In: data
    #Will traverse the binary search tree and insert a node when it has hit a leaf node. The node will contain data
    #After insertion, the function will call fixHeight to get the correct height value on each node
    def insert(self, data):
        if self.isEmpty():
            self.root = Node(data)
        else:
            current = self.root
            while True:
                parent = current
                if current.data == None:
                    parent.left = Node(data)
                    break
                elif data < current.data:
                    current = current.left
                    if current == None:
                        parent.left = Node(data)
                        break
                else:
                    current = current.right
                    if current == None:
                        parent.right = Node(data)
                        break

        self.fixHeight(self.root)

    #Fixes the values from getAllHeights (-1 to each value) and then returns the sum of all the values
    def getTotalHeight(self, root):
        heights = self.getAllHeights(root)
        for i in range(len(heights)): 
            heights[i] = heights[i] - 1 
        return sum(heights)

    #In: root
    #root is a Node object
    #getAllHeights will use Preorder Traversal in order to get the height value of all the nodes into an array
    #Out: heights
    #heights is an array containing all the height values
    def getAllHeights(self, root):
        heights = []
        if root:
            heights.append(root.height)
            heights = heights + self.getAllHeights(root.left)
            heights = heights + self.getAllHeights(root.right)
        return heights
    
    #Gets the weight balance of a node
    #The weight balance is | # left nodes - # right nodes |
    def getWeightBalance(self, root):
        leftnodes = self.getTreeVals(root.left)
        rightnodes = self.getTreeVals(root.right)
        return abs(len(leftnodes) - len(rightnodes))

    #Gets all the weight balances of the tree
    def getWeightBalances(self, root):
        weights = []
        if root:
            weights.append(self.getWeightBalance(root))
            weights = weights + self.getWeightBalances(root.left)
            weights = weights + self.getWeightBalances(root.right)
        return weights

    #Gets the weight balance factor of the tree (highest value of all the weight balances)
    def getWeightBalanceFactor(self):
        weights = self.getWeightBalances(self.root)
        return max(weights)

    #Gets all the tree values using Preorder Traversal
    #Used in weight balance calculation
    def getTreeVals(self, root):
        vals = []
        if root:
            vals.append(root.data)
            vals = vals + self.getTreeVals(root.left)
            vals = vals + self.getTreeVals(root.right)
        return vals
        
    

#G4G code Professor Tian linked to print the tree
#https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/ 
COUNT = [10]
def print2DUtil(root, space) : 
  
    # Base case  
    if (root == None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    print2DUtil(root.right, space)  
  
    # Print current node after space  
    # count  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.data)  
  
    # Process left child  
    print2DUtil(root.left, space)  

if __name__ == "__main__":
    bst = BST()
    bst.insert(6)
    bst.insert(4)
    bst.insert(9)
    bst.insert(5)
    bst.insert(8)
    bst.insert(7)
    print2DUtil(bst.root, 10)
    print(bst.getAllHeights(bst.root))
    print(bst.getTotalHeight(bst.root))
    print(bst.getWeightBalance(bst.root))
    print(bst.getWeightBalances(bst.root))
    print(bst.getWeightBalanceFactor())
