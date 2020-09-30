import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

#fig = go.Figure()
'''
hover = pd.DataFrame([
    dict(Task='A', Start='2009-01-01', Finish='2009-02-28', Resource="Alex", hover_name='name', hover_data="Suhyun", text='what'),
    dict(Task='B', Start='2009-01-01', Finish='2009-02-28', Resource="Alex", hover_name='name', hover_data="Yurim", text='what'),
    dict(Task='C', Start='2009-01-01', Finish='2009-02-28', Resource="Alex", hover_name='name', hover_data="Gyuri", text='what')])
'''

hover = ['hover_name', 'text']

hover = pd.DataFrame([dict(Task="Job D", Start='2009-02-01', Resource="Suhyun", hover_name='Kim', text='nani')])


example = 'Source: LED<br>Destination: Phone<br>nCommand: Read Response<br>Handle: 0x00000031'
elist = ['Source: LED', 'Destination: Phone', 'Command: Read Response', 'Handle: 0x00000031']

#custom = ['customdata', 'suhyun', 'kim']

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Complete=50, Resource="Alex", Description='My hover1'),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Complete=20, Resource="Alex", Description=example),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Complete=80, Resource="Max", Description=['I', 'My hover3'])
])

#fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource",
#                  hover_name='hover_name', hover_data=hover, text='text')

fig = ff.create_gantt(df, colors=None, index_col='Resource', show_colorbar=True, show_hover_fill=True, group_tasks=False)

num = 1
for i in fig['data']:
    #i.update(text='hi', hovertemplate="Price: %{}".format('499'), hoverinfo="text")
    i.update(hoverinfo="text+x+y")
    num += 1
fig.show()
