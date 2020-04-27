from matplotlib.figure import Figure


def create_line_graph(data):
    x_values = data.pop('x_values', [])
    y_values = data.pop('y_values', [])
    if len(x_values) != len(y_values):
        raise Exception('x_values and y_values list must be the same length')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1, **data)
    axis.plot(x_values, y_values)
    return fig
