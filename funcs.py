# Functions
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import statsmodels.api as sm



def get_avg_scoreb4cut(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            Stats['Player'] = name[1]
            Stats['Avg_scoreB4cut'] = float(row.find('td', class_= 'player-name').find_next('td').get_text())
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_par5_bird(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            Stats['Player'] = name[1]
            Stats['Percent_Par5_Bird'] = float(row.find('td', class_= 'hidden-small hidden-medium').find_next().get_text())
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_par4_bird(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            Stats['Player'] = name[1]
            Stats['Percent_Par4_Bird'] = float(row.find('td', class_= 'hidden-small hidden-medium').find_next().get_text())
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_par3_bird(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            Stats['Player'] = name[1]
            Stats['Percent_Par3_Bird'] = float(row.find('td', class_= 'hidden-small hidden-medium').find_next().get_text())
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_money_rank(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            rank = (row.find('td')).get_text().strip().strip('T')
            rank = rank.split('\n')
            Stats['Player'] = name[1]
            Stats['Money_Rank'] = int(rank[0])
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_avg_score_rank(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            rank = (row.find('td')).get_text().strip().strip('T')
            rank = rank.split('\n')
            Stats['Player'] = name[1]
            Stats['Avg_Score_Rank'] = int(rank[0])
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_break_par_rank(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            rank = (row.find('td')).get_text().strip().strip('T')
            rank = rank.split('\n')
            Stats['Player'] = name[1]
            Stats['Percent_BreakPar_Rank'] = int(rank[0])
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_top10s(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            Stats['Player'] = name[1]
            Stats["Top_10's"] = float(row.find('td', class_= 'hidden-small hidden-medium').find_next().get_text())
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_greens_hit(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            Stats['Player'] = name[1]
            Stats['Percent_Greens_Hit'] = float(row.find('td', class_= 'hidden-small hidden-medium').find_next().get_text())
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_fairway_stats(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            Stats['Player'] = name[1]
            Stats['Percent_Fairway_Hit'] = float(row.find('td', class_= 'hidden-small hidden-medium').find_next().get_text())
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

def get_driving_stats(urls):
    List_stats = []
    for url in urls:
        soup = BS((requests.get(url)).content, 'html.parser')
        page = soup.find('tbody')
        for row in page.find_all('tr'):
            Stats = {}
            name = (row.find('td', class_= 'player-name').get_text())
            name = name.split('\n')
            rank = (row.find('td')).get_text().strip().strip('T')
            rank = rank.split('\n')
            Stats['Player'] = name[1]
            Stats['Driving_Rank'] = int(rank[0])
            Stats['Average_Drive_Distance'] = float(row.find('td', class_= 'hidden-small hidden-medium').find_next().get_text())
            Stats['Year'] = int(url[56:60])
            List_stats.append(Stats)
    return List_stats

Driving_Distance_urls = ['https://www.pgatour.com/content/pgatour/stats/stat.101.y1980.eoff.t013.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1981.eoff.t013.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1982.eoff.t013.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1983.eoff.t013.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1984.eoff.t013.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1985.eoff.t013.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1986.eoff.t054.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1987.eoff.t054.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1988.eoff.t054.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1989.eoff.t054.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1990.eoff.t054.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1991.eoff.t054.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1992.eoff.t054.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1993.eoff.t054.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1994.eoff.t018.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1995.eoff.t018.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1996.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1997.eoff.t018.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1998.eoff.t018.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y1999.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2000.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2001.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2002.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2003.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2004.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2005.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2006.eoff.t022.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2007.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2008.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2009.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2010.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2011.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2012.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2013.eoff.t041.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2014.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2015.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2016.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2017.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2018.eoff.t020.html',
'https://www.pgatour.com/content/pgatour/stats/stat.101.y2019.eoff.t041.html']


def stepwise_selection(X, y, 
                       initial_list=[], 
                       threshold_in=0.01, 
                       threshold_out = 0.05, 
                       verbose=True):
    """ Perform a forward-backward feature selection 
    based on p-value from statsmodels.api.OLS
    Arguments:
        X - pandas.DataFrame with candidate features
        y - list-like with the target
        initial_list - list of features to start with (column names of X)
        threshold_in - include a feature if its p-value < threshold_in
        threshold_out - exclude a feature if its p-value > threshold_out
        verbose - whether to print the sequence of inclusions and exclusions
    Returns: list of selected features 
    Always set threshold_in < threshold_out to avoid infinite looping.
    See https://en.wikipedia.org/wiki/Stepwise_regression for the details
    """
    included = list(initial_list)
    while True:
        changed=False
        # forward step
        excluded = list(set(X.columns)-set(included))
        new_pval = pd.Series(index=excluded)
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.idxmin()
            included.append(best_feature)
            changed=True
            if verbose:
                print('Add  {:30} with p-value {:.6}'.format(best_feature, best_pval))

        # backward step
        model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()
        # use all coefs except intercept
        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max() # null if pvalues is empty
        if worst_pval > threshold_out:
            changed=True
            worst_feature = pvalues.argmax()
            included.remove(worst_feature)
            if verbose:
                print('Drop {:30} with p-value {:.6}'.format(worst_feature, worst_pval))
        if not changed:
            break
    return included
