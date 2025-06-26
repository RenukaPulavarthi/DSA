class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        if len(self.stack)<=0:
            print("stack is empty")
            return
        return self.stack.pop()
        
    def top(self):
        if len(self.stack)<=0:
            print("stack is empty")
            return -1
        return self.stack[-1]
        
    def isEmpty(self):
        return len(self.stack)==0
        
st=stack()
st.push(1)
st.push(2)
st.push(5)
print(st.top())
st.pop()
print(st.top())
st.pop()
print(st.top())
st.pop()
print(st.top())
