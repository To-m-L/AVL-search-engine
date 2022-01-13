from os import listdir
from os.path import isfile, join
import webpage
import re
#In: string of directory
#Out: array of WebPageIndex objects
def readFiles(path):
    files = [f for f in listdir(path) if isfile(join(path, f))] #Gets an array of all the file names
    instances = [] 
    #Creates WebPageIndex instances with array of file names
    for i in files:
        instance = webpage.WebPageIndex(path + "\\" + i)
        instances.append(instance)
    return instances


if __name__ == "__main__":
    container = readFiles("C:\\Users\Tom\Desktop\CISC235A2\data")
    f = open("C:\\Users\Tom\Desktop\CISC235A2\queries.txt", "r")
    queries = f.read().splitlines()
    webq = webpage.WebPagePriorityQueue("placeholder", container)
    
    for i in queries:
        webq.reheap(i)
        webq.getHeapName()    
    
    