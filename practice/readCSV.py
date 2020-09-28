import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff

#data_csv = pd.read_csv('ble_packet.csv')
wifi_csv = pd.read_csv('wifi_packet.csv')
zbee_csv = pd.read_csv('zbee.csv')

lis = []



colors = {'Wi-Fi': 'rgb(220, 0, 0)',
          'ZB': (1, 0.9, 0.16),
          'BLE': 'rgb(0, 255, 100)'}

#src_li = data_csv['Source']
#dst_li = data_csv['Destination']
#time_li = data_csv['Time']

#for i in range(len(time_li)):
#    di = dict(Task=str(time_li[i]), Start = str(src_li[i]), Finish=str(dst_li[i]), Resource='BLE')
#    lis.append(di)

src_li = wifi_csv['Source']
dst_li = wifi_csv['Destination']
time_li = wifi_csv['Time']

for i in range(len(time_li)):
    di = dict(Task=str(time_li[i]), Start = str(src_li[i]), Finish=str(dst_li[i]), Resource='Wi-Fi')
    lis.append(di)

src_li = zbee_csv['Source']
dst_li = zbee_csv['Destination']
time_li = zbee_csv['Time']

for i in range(len(time_li)):
    di = dict(Task=str(time_li[i]), Start = str(src_li[i]), Finish=str(dst_li[i]), Resource='ZB')
    lis.append(di)
    
df = pd.DataFrame(lis)


fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)


fig.update_layout(title='Sniffer', xaxis_title='Device', yaxis_title='Time', legend_title='Type')
fig.update_layout(autosize=False, width=1200, height=1200)

fig['layout']['xaxis'].update({'type':None})

fig.show()
