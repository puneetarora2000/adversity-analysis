from models import *
import stats

#Query is fine
'''
    alldata = tablename.objects.filter(whichcolumn)

'''

modelobjects = [SpearIncidenceDetail,Subjects,Organised_Information,InformationSource];


def get_all_data_ColumnWise(tablename,whichcolumn):
    alldata = tablename.objects.all().filter(whichcolumn)
    return alldata

