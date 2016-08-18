from __future__ import unicode_literals, division
import panda as pd
from models import AttackAim

exampledata = {'Countries': ['India', 'US', 'China', 'UK', 'Australia'],
        'AttackOriginCountry': [42, 52, 36, 24, 73],
        'AttackTargetCountry': [4, 24, 31, 2, 3],
        'Attack_Dummy': [25, 94, 57, 62, 70]}

examplecolumns  = ['Countries', 'AttackOriginCountry', 'AttackTargetCountry', 'Attack_Dummy']
AttackAimValues = [42, 52, 36, 24, 73]


AttackAim_df = {'NamesofCountries': AttackAim,
        'AttackOriginCountryValues': AttackAimValues}


def collect_stats(df, column_names):
    mean = {}
    for column_name in column_names:
        mean[column_name] = computeMean(df, column_name)
    return {'average': mean}

def computeDescriptive(df, column_name):
    return df[column_name].describe()

def computeMean(df, column_name):
    if all(isinstance(item, int) for item in df[column_name]):
        mean = df[column_name].mean()
    else:
        mean = 0
    return mean

def computeSum(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].sum()
    return des


def computeCumSum(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].cumsum()
    return des

def computeCount(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].cumsum()
    return des


def computeMinimum(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].min()
    return des


def computeMaximum(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].max()
    return des

def computeMedian(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].median()
    return des


def computeVaraince(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].var()
    return des



def computeSkew(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].skew()
    return des


def computeKurt(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df[whichone].kurt()
    return des


def computeCorrelation(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df.corr();
    return des

def computeCorrelation(data,columns,whichone):
    df =  pd.DataFrame(data,columns)
    des = df.var();
    return des


'''
df = pd.DataFrame(data, columns = ['Countries', 'AttackOriginCountry', 'AttackTargetCountry', 'Attack_Dummy'])
df['age'].sum()
df['AttackOriginCountry'].mean()
df['AttackTargetCountry'].cumsum()
df['AttackTargetCountry'].describe()
df['preTestScore'].count()
df['preTestScore'].min()
df['preTestScore'].max()
df['preTestScore'].median()
df['preTestScore'].var()
df['preTestScore'].skew()
df['preTestScore'].kurt()
df.corr()
df.cov()
'''