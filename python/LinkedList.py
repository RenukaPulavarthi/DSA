class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def TraveseAndPrint(node):
    while node!=None:
        print(node.data)
        node=node.next


a=Node(1)
b=Node(2)
c=Node(3)
a.next=b 
b.next=c 
TraveseAndPrint(a)

lst=[1,2,3,4,5]
root=None
temp=root
for i in lst:
    if root==None:
        root=Node(i)
        temp=root
    else:
        temp.next=Node(i)
        temp=temp.next
TraveseAndPrint(root)