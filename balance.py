class stack:
    def __init__(self,size):
        self.size=size
        self.stack=[0]*size
        self.top=-1
    def push(self,data):
        if self.top>=self.size-1:
            print("Overflow")
        else:
            self.top+=1
            self.stack[self.top]=data
    def pop(self):
        if self.top==-1:
            print("Underflow")
        else:
            temp=self.stack[top]
            self.top-=1
        return temp
    def check(self,char):
        print(char)
        for i in char:
            if i=='['or'('or'{':
                self.push(i)
            elif i==']'or')'or'}':
                temp=self.pop(i)
                print(temp,i)
                if self.top==-1:
                    print("right is more")
                elif not(self.match(i,temp)):
                    print("Mismatched")
                    break
        if self.top==-1:
            print("balanced")
    def match(self,left,right):
        if left=='['and right==']':
            return True
        elif left =='(' and right==')':
            return True
        elif left=='{' and right=='}':
            return True
        else:
            return False
size=int(input("enter the size"))
obj=stack(size)
exp=input("enter the expression")
obj.check(exp)

                
            
