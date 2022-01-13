class Node:
    def __init__(self, key, value):
        self.right = None
        self.left = None
        self.key = key
        self.value = value
        self.height = 0

class AVLTreeMap:

    def __init__(self):
        self.root = None
    
    #Checks if the tree's root is null
    #returns True if it is, returns False if it is not
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    
    #gets the height of a particular node
    def getHeight(self, node):
        if node is None:
            return 0
 
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1 
    
    #gets the balance factor of a node
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)

    #Rotates the tree to the left
    def leftRotate(self, root):
        newRoot = root.right
        carry = newRoot.left
        newRoot.left = root
        root.right = carry
        root.height = self.getHeight(root)
        newRoot.height = self.getHeight(newRoot)
        return newRoot

    #Rotates the tree to the right
    def rightRotate(self, root):
        newRoot = root.left
        carry = newRoot.right
        newRoot.right = root
        root.left = carry
        root.height = self.getHeight(root)
        newRoot.height = self.getHeight(newRoot)
        return newRoot
    
    #Goes through the whole tree and applies getHeight to all the nodes
    def fixHeight(self, root):
        if root:
            root.height = self.getHeight(root)
            self.fixHeight(root.left)
            self.fixHeight(root.right)

    #In: key, value
    #put will insert a node into the AVL tree. The node will have 'key' and 'value'
    #After insertion, the function will call fixHeight to fix the height value of all the nodes
    #After fixHeight, the function will rotate if the balance factor is > 1 or < -1
    def put(self, key, value):
        if self.isEmpty():
            self.root = Node(key, value)
        else:
            current = self.root
            done = False
            while not done:
                if key > current.key:
                    if current.right == None: 
                        current.right = Node(key, value)
                        done = True
                    else:
                        current = current.right

                else:
                    if current.left == None:
                        current.left = Node(key, value)
                        done = True
                    else:
                        current = current.left
        

        self.fixHeight(self.root)
        balance = self.getBalance(self.root)
        
        #Left Left
        if balance > 1 and key < self.root.left.key:
            self.root = self.rightRotate(self.root)
        #Right Right
        if balance < -1 and key > self.root.right.key:
            self.root = self.leftRotate(self.root)
        #Left Right
        if balance > 1 and key > self.root.left.key:
            self.root.left = self.leftRotate(self.root.left)
            self.root = self.rightRotate(self.root)
        #Right Left
        if balance < -1 and key < self.root.right.key:
            self.root.right = self.rightRotate(self.root.right)
            self.root = self.leftRotate(self.root)
    
    #Returns the value associated with the key if the key is found, otherwise returns null
    def get(self, key):
        if self.root == key:
            return self.root.value
        else:
            current = self.root
            while True:
                if current == None:
                    return None
                if key == current.key:
                    return current.value
                elif key < current.key:
                    current = current.left
                else:
                    current = current.right
        
            

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
    print(root.key)  
  
    # Process left child  
    print2DUtil(root.left, space)




if __name__ == "__main__":
    avl = AVLTreeMap()
    root = avl.root
    
    avl.put(15, "bob")
    avl.put(20, "anna")
    avl.put(24, "tom")
    avl.put(13, "david")
    avl.put(10, "david")
    avl.put(7, "ben")
    avl.put(30, "karen")
    avl.put(36, "erin")
    avl.put(25, "david")
    print2DUtil(avl.root, 10)
    print(avl.get(15))
    print(avl.get(20))
    
    