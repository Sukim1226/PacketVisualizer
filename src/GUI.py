import pandas as pd
import plotly.figure_factory as ff
import random

class GUI:
    def __init__(self, protocol, datas, color_key):
        self.title = protocol + ' Packet Visualizer'
        self.datas = datas
        self.color_key = color_key

    def match_color(self):
        colors = {}
        for i in self.color_key:
            r, g, b = random.sample(range(0, 256), 3)
            colors[i] = 'rgb({}, {}, {})'.format(r, g, b)
        return colors

    def hover(self):
        pass

    def show(self):
        df = pd.DataFrame(self.datas)
        colors = self.match_color()
        fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, 
            showgrid_x=True, showgrid_y=True, width=1200, group_tasks=True)
        fig.update_layout(title=self.title, xaxis_title='Sequence', yaxis_title='Source', legend_title='Opcode')
        fig['layout']['xaxis'].update({'type':None})
        fig.show()