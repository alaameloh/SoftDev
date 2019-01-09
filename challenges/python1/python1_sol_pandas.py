import sys
import pandas as pd
f = open(str(sys.argv[1]))
#f = open("auth.log")

raw_data = f.readlines()

for i in range(len(raw_data)):
    raw_data[i] = raw_data[i].split()
df = pd.DataFrame(raw_data).rename ({5: 'status',8:'user', 10:'IP'}, axis='columns')
df = df[(df.status == 'Accepted' )| (df.status == 'Failed')]
df = df[['IP','user' ,'status']]
df_dummies = pd.get_dummies(df.status)
df_dummies = pd.concat([df[['IP','user']],df_dummies],axis=1)

def f_accepted(row) :
	if row['Accepted']==1 :
		return(row['user'])
	else:
		return None
def f_failed(row) :
	if row['Failed']==1 :
		return(row['user'])
	else:
		return None
df_dummies['accepted_users'] = df_dummies.apply(f_accepted,axis=1)
df_dummies['failed_users'] = df_dummies.apply(f_failed,axis=1)
df_dummies.drop(columns='user',inplace=True)
df_grouped = df_dummies.groupby(['IP']).agg({'Accepted':sum,'Failed':sum,'accepted_users':pd.Series.nunique , 'failed_users':pd.Series.nunique})
df_grouped.reset_index(inplace=True)
print()
for _ ,row in df_grouped.iterrows():
	if row['Accepted'] and (row['Failed'] > row['Accepted']):
		print (row['IP'],'-',row['Failed'],'failed for',row['failed_users'],'users -', row['Accepted'],'accepted for',row['accepted_users'],'users')