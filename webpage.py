import avl
import re

class WebPageIndex:
    
    def __init__(self, file):
        self.file = file
        self.avlweb = avl.AVLTreeMap()
        f = open(self.file, "r")
        self.words = f.read().lower()
        self.words = re.split("\W", self.words)
        self.priority = 0
    

    def getCount(self, s):
        counter = 0
        for i in self.words:
            if i == s:
                counter+=1
        return counter
    
    def getOccurences(self, s):
        occurences = []
        for i in range(len(self.words)):
            if self.words[i] == s:
                occurences.append(i)
        return occurences

    def createTree(self):
        for i in self.words:
            if self.avlweb.get(i):
                continue
            else:
                self.avlweb.put(i, self.getOccurences(i))
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
    print(root.value,"-", root.key)  
  
    # Process left child  
    print2DUtil(root.left, space)


class WebPagePriorityQueue():

    def __init__(self, query, container):
        self.query = query
        self.container = container
        self.heap = []
        querySplit = re.split("\W", query) #Splits the query in case the query is a sentence
        for i in self.container:
            priority = 0
            for w in querySplit: #Adds up all the occurences of each word in the query
                priority+=i.getCount(w)
            i.priority = priority
            self.heap.append(i)
        self.heap.sort(reverse=True, key=self.getPriority) #Creates Max Heap Structure


    def getPriority(self, index):
        return index.priority

    #Returns highest value in heap
    def peek(self):
        return self.heap[0]

    #Deletes highest value in heap
    def poll(self):
        self.heap.pop(0)

    #toString function
    #Prints out the file name and priorities of the indexes
    def getHeapName(self):
        print("---------------------------------")
        for i in self.heap:
            print(i.file," || Priority: ",i.priority) 

    #Same code as for loop in constructor
    def reheap(self, query):
        self.heap = []
        self.priorities = avl.AVLTreeMap()
        querySplit = re.split("\W", query)
        for i in self.container:
            priority = 0
            for w in querySplit: #Adds up all the occurences of each word in the query
                priority+=i.getCount(w)
            i.priority = priority
            self.heap.append(i)
        self.heap.sort(reverse=True, key=self.getPriority)
 

    









if __name__ == "__main__":
    web = WebPageIndex("C:\\Users\Tom\Desktop\CISC235A2\data\doc1-arraylist.txt")
    print(web.getCount("array"))
    web.createTree()
    print2DUtil(web.avlweb.root, 10)
    #webq = WebPagePriorityQueue("meme","C:\\Users\Tom\Desktop\CISC235A2\data\doc1-arraylist.txt")
    #webq.instance.createTree()
    #print2DUtil(webq.instance.avlweb.root, 0)