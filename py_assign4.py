# Working with Lists in Python

myUniqueList=[]
myLeftovers=[]

def search(x,index):          # Function to check duplicacy
  
  for i in range(index):

    if x==myUniqueList[i]:
      return True             # If duplicacy found it returns True


def AddToList(x,index):
  
  a=search(x,index)	

  if a==True:
    myLeftovers.append(x)     # Duplicate elements added to myLeftovers
    return False

  else:
    myUniqueList.append(x)    # Unique elements added to myUniqueList
    return True


AddToList(1,0)    
AddToList(2,1)
AddToList(3,2)
AddToList(5,3)
AddToList(1,4)
AddToList(2,5)
AddToList(3,6)

print(myUniqueList)
print(myLeftovers)




