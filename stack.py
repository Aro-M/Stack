
class Stack(object):
    def __init__(self):
        self.item = []
    def push(self,it):
        self.item.append(it)
    def pop(self):
        if len(self.item) == 0:
            return  print("Stack is empty")
        else:
            return self.item.pop()
    def peek(self):
        return self.item[-1]
    def size(self):
        return len(self.item)
    def isEmpty(self):
        if len(self.item) == 0:
            print(True)
        print(False)
    def clear(self):
        self.item = []
        print(self.item)
    def top(self):
        return  self.item[0]
    def show(self):
        for x in self.item:
            print(x,end=" ||  \n" )
        if len(self.item) == 0:
            print(self.item)

st = Stack()
st.push(14)
st.push("this is stack")
st.push(56.5)
st.push(15845)
st.push("ads")
st.show()
st.pop()
st.pop()
st.pop()
st.show()
print(st.size())
st.isEmpty()
print(st.top())
print(st.peek())
st.clear()
st.show()




