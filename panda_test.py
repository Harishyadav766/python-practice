import pandas as pd
import numpy as np
data = pd.DataFrame({'contry':['India','paksithan','america','africa'],'rank':[1,4,2,3]})
print(data)
a=data.describe()
data.info()
print(a)

data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print('data is :', data)
b=data.sort_values(by=['ounces'],ascending=True,inplace=False)
print('b is :', b)
c= data.sort_values(by=['ounces'],ascending=False,inplace=False)
print('c is :',c)

b=data.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False)
print('b is :', b)
c= data.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False)
print('c is :',c)

data=pd.DataFrame({'k1':['one']*3 + ['two']*3 + ['three']*3,'k2':[1,96,96,8,91,91,16,1,55]})
print(data)

data=pd.DataFrame({'k1':['one']*3 + ['two']*3 + ['three']*3,'k2':[1,96,96,8,91,91,16,1,55]})
print(data)
a=data.sort_values(by='k2')
print('a is the sorted vales:',a)
b=data.drop_duplicates(subset='k1')
print('b is the duplicate value: \n',b)


data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'Honey ham','nova lox'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print('data table is :\n', data)

meat_to_animal = {'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}

def meat_2_animal(series):
    if series['food'] == 'bacon':
        return 'pig'
    elif series['food'] == 'pulled pork':
        return 'pig'
    elif series['food'] == 'pastrami':
        return 'cow'
    elif series['food'] == 'corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'


#for createing a new variable we use below syntax
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print('data table is: \n', data)

#def animal_of_cost(series):
#    if series['animal']=='pig':
#        return  '10000'
#    #else:
#     #   return  '100'
#data['cost'] = data['animal'].map(str.lower).map(animal_of_cost)
#print('data table is:\n',data)
lower = lambda x: x.lower()
data['food'] = data['food'].apply(lower)
data['animal2'] = data.apply(meat_2_animal, axis='columns')
print('data table is :\n',data)

#data.assign(new_veriable= data['ounces']*10)
a = data.assign(new_variable = data['ounces']*1000)
print('data table is : \n',a)
print()
new_data = a.rename(columns = {"new_variable": "cost of animal"}) 
print('new_data is :\n',new_data)

a.drop('animal2',axis='columns',inplace=True)
print('a data table is:\n',a)


a = pd.Series([1., 22., -99., 85., 11., 777., -99., -99] )
print('table a is :\n', a )
a.replace([-99,777], np.nan,inplace=True)
print('table a is :\n',a)

date1 = pd.DataFrame(np.arange(12).reshape((3,4)),index=['bnglr','mysr','new york'],
columns=['one','two','three','four'])
print('date is :\n ', date1)

#date.rename(index = {'ohio':'hfdhf'}, columns = {'one':'one_p'},inpalce=True)
#print('date is :\n ', date)

#date



#a= date.rename(index = {'ohio':'SanF'}, columns={'one':'one_p','two':'two_p'},inplace=True)
#print('date table a is :\n ',a)

date2 =pd.DataFrame(np.arange(12).reshape((3,4)),index=['bnglr','mysr','new yor',],
columns=['one','two','three','four'])
print('date2 table is : \n', date2)

a = date2.index.intersection(date1.index)
print(a)

#date1.columns()
#date2.columns()

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print('cats is :\n',cats)

pd.cut(ages,bins,right=False)

pd.value_counts(cats)

df = pd.DataFrame({'k1':['one','two','three','four'],'k2':['a','b','c','d'],'data1':np.random.randn(4),'data2':np.random.randn(4)})
print('data table of df is : \n ' ,df)
grouped = df['data1'].groupby(df['k1'])
k1=grouped.mean()
print('k1',k1)

dates = pd.date_range('20190213',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index = dates, columns = list('ABCD'))
print('dates table is : \n ', df)

c= df['20190213':'20190217']
print('c: \n' , c)

A=df.loc[:,['A','B']]
print('A: \n', A)

data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print('data_table is :\n', data)
pivot=data.pivot_table(values='ounces',index='group',aggfunc=np.mean)
print('pivot table is :\n ',pivot)