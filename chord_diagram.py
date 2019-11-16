import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
# imaginary Sales data. 

data = [['A', 'B', 'C', 'D', 'E', 'total'],
        [16, 3, 28, 0, 18, 65],
        [18, 0, 12, 5, 29, 64],
        [9, 11, 17, 27, 0, 64],
        [19, 0, 31, 11, 12, 73],
        [23, 17, 10, 0, 34, 84]]

table = ff.create_table(data, index=True)
table.write_html('Data-Table.html', auto_open=True)