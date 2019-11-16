import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np
# imaginary Sales data. 

data  =  [['A', 'B', 'C', 'D', 'E'],
        [16, 3, 28, 0, 18],
        [18, 0, 12, 5, 29],
        [9, 11, 17, 27, 0],
        [19, 0, 31, 11, 12],
        [23, 17, 10, 0, 34]]


matrix = np.array([[16,  3, 28,  0, 18],
                 [18,  0, 12,  5, 29],
                 [ 9, 11, 17, 27,  0],
                 [19,  0, 31, 11, 12],
                 [23, 17, 10,  0, 34]], dtype = int)
L,M =  matrix.shape
table  =  ff.create_table(data, index = True)
#table.write_html('Data-Table.html', auto_open = True)

'''
Create ideograms which are arcs defined by the column total
'''
PI = np.pi

def moduloAB(x, a, b): #maps a real number onto the unit circle identified with
                       #the interval [a,b), b-a = 2*PI
        if a>=b:
            raise ValueError('Incorrect interval ends')
        y = (x-a)%(b-a)
        return y+b if y<0 else y+a

def test_2PI(x):
    return 0<=x <2*PI

row_sum = [np.sum(matrix[k,:]) for k in range(L)]

#set the gap between two consecutive ideograms
gap = 2*PI*0.005
ideogram_length = 2*PI*np.asarray(row_sum)/sum(row_sum)-gap*np.ones(L) # length of the arcs based on row sum


# generate coordinates of the ideogram arcs
def get_ideogram_ends(ideogram_len, gap):
    ideo_ends = []
    left = 0
    for k in range(len(ideogram_len)):
        right = left+ideogram_len[k]
        ideo_ends.append([left, right])
        left = right+gap
    return ideo_ends

ideo_ends  =  get_ideogram_ends(ideogram_length, gap)
print(f'The coordinates of the ideogram ends {ideo_ends}')