class queue:
    def  __init__(self):
        self.queue=[]
        
    def push(self,val):
        self.queue.append(val)
        
    def pop(self):
        if len(self.queue)==0:
            print("queue is empty")
            return -1
        return self.queue.pop(0)
        
    def front(self):
        if len(self.queue)==0:
            print("queue is empty")
            return -1
        return self.queue[0]
        
    def isEmpty(self):
        return len(self.queue)==0
        
lst=[1,2,3,4,5]
que=queue()
for i in lst:
    que.push(i)
for i in range(5):
    print(que.front())
    que.pop()
