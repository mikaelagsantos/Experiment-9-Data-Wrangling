import pandas as pd

data1 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80, 95, 79]}
data2 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics': [85, 81, 83]}
data3 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90, 79, 93]}
data4 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93, 89, 88]}

data11 = pd.DataFrame(data1, columns = ['Student', 'Math'])
data22 = pd.DataFrame(data2, columns = ['Student', 'Electronics'])
data33 = pd.DataFrame(data3, columns = ['Student', 'GEAS'])
data44 = pd.DataFrame(data4, columns = ['Student', 'ESAT'])


merge = pd.merge(data11, data22, how='right', on='Student')
merge2 = pd.merge(merge, data33, how='right', on='Student')
merge3 = pd.merge(merge2, data44, how='right', on='Student')

subject = pd.melt(merge3, id_vars = 'Student', value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'])
final = subject.rename(columns = {'variable': 'Subject', 'value': 'Grades'})
final2 = final.sort_values('Student').reset_index().drop(columns = ['index'])
