import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_data(data, title='Data Plot', xlabel='X-Axis', ylabel='Y-Axis'):
    fig, ax = plt.subplots()
    ax.plot(data)

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.grid()
    
    plt.show()
