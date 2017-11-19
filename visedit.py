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

def heatmap(arr):
    fig, ax = plt.subplots()
    ax.imshow(arr)
    return fig, ax

def table_for_figure(data, fig):
    df = pd.DataFrame(data)
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
        qgrid_widget.df = df_stacked.reindex([(y, x)])
    fig.canvas.mpl_connect('button_press_event', onclick)
    return qgrid_widget
      
def heatmap_with_table(arr):
    fig, ax = heatmap(arr)
    qgrid_widget = table_for_figure(arr, fig)
    return qgrid_widget, fig, ax
