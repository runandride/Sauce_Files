# Import Directories
import os
import pandas as pd
import seaborn as sns

# In this code I've collected two batches of csv's in two separate 
# directories. One batch I consider "new" or recent data. The other
# I conside "old" data. In reality, you could compare any directories full of data
# with this code. 

# This code will only work if the directories you're referencing have
# CSV's inside.

# Choose your directory
os.chdir("New Directory")

# Path of the old data directory
c = "New Directory"

# Create an empty list
li = []

# Iterate through a directory, this one is for my "new data"
for filename in os.listdir(c):
    print(filename)
    df = pd.read_csv(filename)
    li.append(df)
# Combine data files to creata a datafile with all "new" data
df_new = pd.concat(li)

#Repeat this
os.chdir("Old Directory")
c = "Old Directory"

li = []

for filename in os.listdir(c):
    print(filename)
    df = pd.read_csv(filename)
    li.append(df)
df_old = pd.concat(li)


#Relabel the dataframes because the columns are oddly labeled
df_new.columns = ['time','distance','pace','gap','altitude']
df_old.columns = ['time','distance','pace','gap','altitude']

# Units - Time is in seconds
# Units - Distance is in meters
# You can prove this by looking taking the distance and time units
# and comparing them to your activity.

# Let's do some analysis. Let's see how my first two-miles pace stacks up
# in the past versus the present using the 4 old / new activities I downloaded

# Subset for first two miles: aka - when its less than 3218.69 meters
df_new = df_new.loc[df_new['distance'] < 3218.69]
df_new['Age'] = 'New'
df_old = df_old.loc[df_old['distance'] < 3218.69]
df_old['Age'] = 'Old'

# Combine old and new data files
df_all = pd.concat([df_new,df_old],axis=0)

# Plot old vs new data
sns.boxplot(data=df_all,x='Age',y='gap',showfliers=False)