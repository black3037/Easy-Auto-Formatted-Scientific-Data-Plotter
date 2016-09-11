""" 
Copyright Derek Black, 2016

This is a simple python module for plot automation

It easily generates preformatted matplotlib plots for fast scientific publication


"""
# Import the appropriate libraries
import matplotlib.pyplot as plt

def ezplot(*argv):
    """
    
    ezplot is a convient way to plot data fast and easily
    
    It is a pre-formated graph type utilzing the matplotlib pyplot
    
    To use this function a few arguements are needed, namely
    
    x      :  x data
    y      :  y data
    xlabel : this is the x axis label. Set to none if no arguement
    ylabel : this is the y axis label. Set to none if no arguement
    title  : this is the title of the graph. Set to none if no arguement
    
    Ex.    : ezplot(x,y,'time','velocity','Velocity-Time Graph')
    
    """
    if len(argv) == 0:
        raise Exception('No Arguements were passed to the function')
    
    elif len(argv) == 1:
        raise Exception('Not enough arguements')

    elif len(argv) == 2:
        x = argv[0]
        y = argv[1]
        xlabel = ''
        ylabel = ''
        title = ''

    else: 
        x = argv[0]
        y = argv[1]
        xlabel = str(argv[2])
        ylabel = str(argv[3])
        title = str(argv[4])
        
    # Check to make sure x and y are same size
    if len(x) == len(y):
        pass
    else:
        raise Exception('Arguments are not of same length')
        
    plt.plot(x,y,'black',label=ylabel)
    
    # Plot features
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.autoscale(tight=True)
    plt.legend()
    
    return plt.show()


def ezmplot(*argv):
    """
    
    ezmplot is a convient way to plot multiple data sets fast and easily
    
    It is a pre-formated graph type utilzing the matplotlib pyplot
    
    To use this function a few arguements are needed, namely
    
    x1      :  x1 data
    y1      :  y1 data
    x2      :  x2 data
    y2      :  y2 data
    xlabel  : this is the x axis label. Set to none if no arguement
    ylabel  : this is the y axis label. Set to none if no arguement
    title   : this is the title of the graph. Set to none if no arguement
    legend1 : data set 1 label, defaults to "data1"
    legend2 : data set 2 label, defaults to "data2"
    
    Ex.    : ezplot(x,y,x2,y2,'time','velocity','Velocity-Time','data1','data2')
    
    """
    if len(argv) == 0:
        raise Exception('No Arguements were passed to the function')
    
    elif len(argv) == 1:
        raise Exception('Not enough arguements')

    elif len(argv) == 2:
        raise Exception('Use ezplot() if graphing only one data set')
    
    elif len(argv) == 4:
        x1 = argv[0]
        y1 = argv[1]
        x2 = argv[2]
        y2 = argv[3]
        xlabel = ''
        ylabel = ''
        title = ''
        legend1 = 'data1'
        legend2 = 'data2'

    else: 
        x1 = argv[0]
        y1 = argv[1]
        x2 = argv[2]
        y2 = argv[3]
        xlabel = str(argv[4])
        ylabel = str(argv[5])
        title = str(argv[6])
        legend1 = str(argv[7])
        legend2 = str(argv[8])
        
    # Check to make sure x and y are same size
    if len(x1) == len(y1) and len(x2) == len(y2):
        pass
    else:
        raise Exception('Arguments are not of same length')
                
    plt.plot(x1,y1,'k',label=legend1)
    plt.plot(x2,y2,'k--',label=legend2)
    # Plot features
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.autoscale(tight=True)
    plt.legend()
    
    return plt.show()

    
    
    
    
    