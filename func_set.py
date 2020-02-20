import pandas as pd , numpy as np
import matplotlib.pyplot as plt , matplotlib.patches as mpatches


data = pd.read_csv('TC1-SUNPHARMA.csv')
df= pd.DataFrame(data)
date = (df['Date'].apply(lambda x : x.split('-')[2]))
year_wise = df.groupby(date).mean().reset_index()

def show_options():
    list = ['Open Price', 'High Price', 'Low Price', 'Last Traded Price', 'Close Price', 'Total Traded Quantity',
            'Turnover (in Lakhs)']
    dict_list = dict(enumerate(list , 1))
    for key , val in dict_list.items():
        print(key ,val)
    inp = int(input('Enter your choice :'))
    if inp in dict_list.keys():
        return dict_list[inp]
def complete_report ():
    x =  np.arange(len(year_wise['Date']))
    wid =0.15

    plt.title('SUNPHARMA' , fontsize = 20)
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.xticks(x+ wid*1.5 , [ i for i in year_wise['Date']])
    plt.bar(x , [i for i in year_wise['Open Price']] , width = wid , color = 'green' , zorder = 0 )
    plt.bar(x + wid , [i for i in year_wise['Last Traded Price']], width=wid, color='r', zorder=0)
    plt.bar(x+ wid*2 , [i for i in year_wise['High Price']], width=wid, color='yellow', zorder=0)
    plt.bar(x+ wid*3 , [i for i in year_wise['Low Price']], width=wid, color='orange', zorder=0)
    plt.bar(x + wid * 3, [i for i in year_wise['Close Price']], width=wid, color='b', zorder=0)
    p1 = mpatches.Patch(color = 'green' , label = 'Open Price')
    p2 = mpatches.Patch(color='r', label='Last Traded Price')
    p3 = mpatches.Patch(color='yellow', label='High Price')
    p4 = mpatches.Patch(color='orange', label='Low  Price')
    p5 = mpatches.Patch(color='b', label='Close  Price')
    plt.legend(handles =[p1,p2,p3,p4,p5] )
    plt.show()

    return year_wise

def show_data(show):
    fig = plt.figure()
    plt.title(show)
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.bar(year_wise['Date'] , year_wise[show])
    plt.show()
    return (year_wise[show])


def Date_wise():
    data = pd.read_csv('TC1-SUNPHARMA.csv')
    df = pd.DataFrame(data)
    Date = '-'.join(input('Enter a date : ').split( ))
    if df[df['Date']==Date].empty:
        print ('No Record Found...!!!')
    else:
        print(df[df['Date']==Date])

