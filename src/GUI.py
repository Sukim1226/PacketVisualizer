import pandas as pd
import plotly.figure_factory as ff
import plotly.subplots as sub
import random

class GUI:
    def __init__(self):
        self.figures = {}

    def match_color(self, color_keys):
        colors = {}
        for key in color_keys:
            r, g, b = random.sample(range(0, 256), 3)
            colors[key] = 'rgb({}, {}, {})'.format(r, g, b)
        return colors

    def add(self, protocol_instance):
        dic = {}
        dic['color_keys'] = self.match_color(protocol_instance.gen_color_keys())
        dic['data'] = protocol_instance.package
        dic['fig'] = self.make_figure(protocol_instance.package, 
            dic['color_keys'], protocol_instance.category)
        self.figures[protocol_instance.category] = dic

    def make_figure(self, datas, color_keys, title):
        df = pd.DataFrame(datas)
        colors = self.match_color(color_keys)
        fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, showgrid_x=True, showgrid_y=True, 
            height=600, width=None, group_tasks=True, show_hover_fill=True)
        fig.update_traces(hoverinfo='text')
        fig.update_layout(title='<b>' + title + ' Packet Visualizer</b>', xaxis_title='<b>Sequence</b>', yaxis_title='<b>Source</b>', legend_title='<b>Command</b>')
        fig.update_layout(xaxis_rangemode='tozero', xaxis_type=None, xaxis_tickmode='linear', xaxis_showticklabels=False)      
        return fig

    def make_subplot(self):
        sub_fig = sub.make_subplots(rows=len(self.figures), cols=1, subplot_titles=list(self.figures.keys()))
        idx = 1
        for protocol in self.figures:
            for trace in self.figures[protocol]['fig'].data:
                sub_fig.add_trace(trace, row=idx, col=1)
            idx += 1
        for i in range(1, len(self.figures) + 1):
            sub_fig.update_xaxes(title_text='<b>Sequence</b>', tickmode='linear', showticklabels=False, rangemode='tozero', row=i, col=1)
            sub_fig.update_yaxes(title_text='<b>Source</b>', showgrid=False, zeroline=False, showticklabels=False, row=i, col=1)
        sub_fig.update_layout(title='<b>Packet Visualizer</b>', legend_title='<b>Command</b>')
        return sub_fig

    def show(self, cmd):
        if cmd == 'ALL' and len(self.figures) > 1:
            self.make_subplot().show()
        else:
            self.figures[cmd]['fig'].show()