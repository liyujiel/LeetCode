# Python zip function? 

def rotate1(self,matrix):
    matrix[:] = zip(*matrix[::-1])


# map solution
def rotate2(self,matrix):
    matrix[:] = map(list,*matrix[::-1]) 

# Direct
def rotate3(self,matrix):
    n = len(matrix)
    for i in range(n/2):
        # n-n/2 I guess is for chop left
        for j in range(n-n/2):
            matrix[i][j],matrix[~j][i],matrix[~i][~j],matrix[j][~i] = matrix[~j][i],matrix[~i][~j],matrix[j][~i],matrix[i][j]