import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff

wifi = pd.read_csv('wifi_duration.csv', names=['a', 'b', 'c', 'd'])
Hub = [ip, 0x00]
df = pd.DataFrame([dict(Task="2020-12-21:11:00", Start='led', Finish='hub', Resource='Wi-Fi'),
      dict(Task="2020-12-21:11:11", Start='smartphone', Finish='hub', Resource='ZB'),
      dict(Task="2020-12-21:11:13", Start='hub', Finish='smartphone', Resource='Wi-Fi'),
      dict(Task="2020-12-21:11:17", Start='led', Finish='smartphone', Resource='BLE')])


colors = {'Wi-Fi': 'rgb(220, 0, 0)',
          'ZB': (1, 0.9, 0.16),
          'BLE': 'rgb(0, 255, 100)'}


#fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
#fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)

fig.update_layout(title='Sniffer', xaxis_title='Time', yaxis_title='Device', legend_title='Type')

fig['layout']['xaxis'].update({'type':None})

fig.show()

#layout = {'xaxis': {'automargin':True}, 'yaxis': {'automargin': True}},
