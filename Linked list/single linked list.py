class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class N:
    def __init__(self,data,p):
        self.data=data
        self.next=p

class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
        
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head 
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
            
    def display(self):
        current =self.head
        print('the linked list:',end="")
        while current is not None:
            print (current.data,end=' ')
            current=current.next
        print("\n head:",self.head.data,"\n last node:",self.last_node.data)
        
    def count(self):
        p=self.head
        n=0
        while p is not None:
            n=n+1
            p=p.next
        print("number of nodes=",n)
        
    def search(self):
        x=int(input("enter the item you want to find"))
        position=1
        p=self.head
        while p is not None:
            if p.data==x:
                print(x,"is at position",position)
                return True
            position+=1
            p=p.next
        else:
            print(x,"is not found in the list")
            return False 
        
    def insert_start(self):
        data=int(input("enter data item to insert at start:"))
        self.head=N(data,self.head)
        self.display()
        
    def insert_end(self):
        data=int(input("enter data item to insert at end:"))
        self.last_node.next=Node(data)
        self.last_node=self.last_node.next
        self.display()
    
    def insert_at(self):
        data=int(input("enter data item to insert  :"))
        d=int(input("enter position at which you want to add element:"))
        i=1
        if d==1:
            m=self.head
            self.head=N(data,m)
        else:
            current =self.head
            while i<d-1 and current is not None:
                current=current.next
                i=i+1
            if current is None:
                print("out of range")
            else:
                m=current.next
                current.next=N(data,m)
        self.display()
        
    def delete_start(self):
        print("delete starting node;")
        self.head=self.head.next
        self.display()
        
    def delete_end(self):
        print("delete last node")
        current=self.head
        while current.next!=self.last_node:
            current=current.next
        self.last_node=current
        current.next=None
        self.display()
        
    def delete_at(self):
        print("delete at node;")
        d=int(input("enter position of which you want to delete element:"))
        i=1
        if d==1:
            self.delete_start()
        else:
            current =self.head
            while i<d-1 and current is not None:
                current=current.next
                i=i+1
            if current is None:
                print("out of range")
            else:
                
                if current.next==self.last_node:
                    self.last_node=current
                current.next=current.next.next
        self.display()
        
    def reverse(self):
        temp=None
        current=self.head
        last=self.head
        while current is not None:   
            q=current.next
            current.next=temp
            temp=current 
            current=q
        self.head=temp
        self.last_node=last 
        self.display()
        

     
#to create a linked list        
a_list =LinkedList()
n=int(input("how many elemens would you like to add?")) 
for i in range(n):
     data =int(input('enter data item:'))
     a_list.append(data)
print('the linked list:',end="")
a_list.display()

#to count number of nodes
a_list.count()
#to search the item in list       
a_list.search()
#to insert item at start
a_list.insert_start()
#To insert item at end       
a_list.insert_end()
#to insert item at position      
a_list.insert_at()
#to delete start node    
a_list.delete_start()
#to delete end node        
a_list.delete_end()
#to delete node at position       
a_list.delete_at()
#To reverse the list       
a_list.reverse()
        
    
    
        
