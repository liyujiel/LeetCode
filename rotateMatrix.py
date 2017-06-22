# Python zip function? 

def rotate1(self,matrix):
    matrix[:] = zip(*matrix[::-1])


# map solution
def rotate2(self,matrix):
    matrix[:] = map(list,*matrix[::-1]) 