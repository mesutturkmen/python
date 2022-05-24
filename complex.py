class complex():
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def show(self):
        return f'{self.r}+{self.i}i'
    def add(self,c1,c2):
        return f'{c1.r+c2.r}+{c1.i+c2.i}i'
    def sub(self,c1,c2):
        if c1.i-c2.i < 0:
            return f'{c1.r-c2.r}{c1.i-c2.i}i'
        return f'{c1.r-c2.r}+{c1.i-c2.i}i'
    def mul(self,c1,c2):
            return f'{c1.r*c2.r-c1.i*c2.i}+{c1.r*c2.i+c1.i*c2.r}i'
    def eq(self,c1,c2):
        if c1.i==c2.i and c1.r==c2.r:
            return True
        return 0

in1=int(input())
in2=int(input())

in3=int(input())
in4=int(input())       
c1=complex(in1,in2)
c2=complex(in3,in4)
print(c1.show())
print(c2.show())
print(c1.add(c1,c2))
print(c1.sub(c1,c2))
print(c1.mul(c1,c2))
print(c1.eq(c1,c2))