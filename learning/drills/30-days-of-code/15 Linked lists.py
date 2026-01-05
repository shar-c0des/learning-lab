class Node:
  def __init__(self,data):
    self.data = data 
    self.next = None

class Soution:
  def display(self,head):
    current = head
    while current:
      print(current.data,end=''_
      current = current.next 

  def insert(self,head,data):



  mylist = Solution()
  T = int(input())
  head = None
  for i in range(T):
    data = int(input())
    head=mylist.insert(head,data)
  mylist.display(head)
  


