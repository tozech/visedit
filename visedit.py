"""visedit - visual editing data

IPy widget to select data in table from the visualisation

Copyright
Tobias Zech - 2017
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import qgrid

pd.set_option('display.max_rows', 8)

def heatmap(df):
    fig, ax = plt.subplots()
    ax.imshow(df)
    return fig, ax

def sort_by_x_y(df_stacked, x0, y0):
    cols = df_stacked.columns
    df = df_stacked.reset_index()
    if df_stacked.index.names == (None, None):
        level_0 = 'level_0'
        level_1 = 'level_1'
    else:
        raise NotImplementedError('Multiindex with level names is implemented yet.')
    df['diff_0'] = np.abs(df[level_0] - y0)
    df['diff_1'] = np.abs(df[level_1] - x0)
    df['max_diff'] = df[['diff_0', 'diff_1']].max(axis=1)
    df = df.sort_values(['max_diff', 'diff_0', 'diff_1'])
    df = df.set_index(['level_0', 'level_1'])
    df = df[cols]
    return df

def table_for_figure(df, fig):
    df_stacked = df.stack()
    df_stacked = pd.DataFrame({'values': df_stacked,
                               'checked': [False for i in range(len(df_stacked))]})
    df_stacked = df_stacked[['values', 'checked']]

    qgrid_widget = qgrid.QgridWidget(df=df_stacked, show_toolbar=True)
    
    pos = []
    def onclick(event):
        x = int(round(event.xdata))
        y = int(round(event.ydata))
        pos.append([x, y])
        qgrid_widget.df = sort_by_x_y(df_stacked, x, y)
    fig.canvas.mpl_connect('button_press_event', onclick)
    return qgrid_widget
      
def heatmap_with_table(df):
    fig, ax = heatmap(df)
    qgrid_widget = table_for_figure(df, fig)
    return qgrid_widget, fig, ax
