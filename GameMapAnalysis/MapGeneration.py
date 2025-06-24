import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import sys



LoadPath='/Users/yirangong/Projects/RoadConstruction/MapGeneration/DataPool/'
LoadSection='/Exp1'

dataName = '/rc-collab'
#datafileLocation=LoadPath+LoadSection+'/rc-collab.json'
datafileLocation=LoadPath+LoadSection+'/2023-03-08T03_25_43Z_rc-collab-default-rtdb_data.json.gz'
mapfileLocation=LoadPath+LoadSection+'/basic_summary_1'
data_dir =LoadPath+LoadSection+'/Preprocessed'
fig_save_dir=LoadPath+LoadSection+'/Figures'




# load map from json
import json
with open(LoadPath+LoadSection+'/basic_map_1','r') as file: 
    basic_all = json.load(file)

# You have to replace the following piece with the new variables
with open(mapfileLocation,'r') as file: 
    summary = json.load(file)
    diff_list = summary[0] 
    optimal_list = summary[1] 
    greedy1_list = summary[2]
    greedy2_list = summary[3]
    optimal_number = summary[4] 
    optimalTurn_list = summary[7] 
    # ALL THE MAPS
    
    # list of optimal move lists within a game
    OptPathAll=summary[13] 
    # list of all the optimal turn lists
    OptTurnsAll=summary[14]  
    
    
    delta_contribution=summary[15]
    
    contribution_p1=summary[16] # average of the contrubution (the number of moves people contribute) in all of possible optimal solutions 
    contribution_p2=summary[17]

basic_map = []
optimal = []
optimal_n = []




#%%

ind = 1

optimal_path1=[optimal_list[ind][i] for i, item in enumerate(optimalTurn_list[ind]) if item==1]
optimal_path2=[optimal_list[ind][i] for i, item in enumerate(optimalTurn_list[ind]) if item==2]

print(f'optimal_list {optimal_list[ind]}')
print(f'optimal turn list {optimalTurn_list[ind]}')
print(optimal_path1)
print(optimal_path2)

plt.scatter(basic_all[ind].get("x"), basic_all[ind].get("y"))
plt.title(f"Optimal {ind}")

# Plotting and marking optimal_path1
optimalx = [(basic_all[ind].get("x"))[point] for point in optimal_path1]
optimaly = [(basic_all[ind].get("y"))[point] for point in optimal_path1]
plt.plot(optimalx, optimaly, 'bo', linestyle="--")

# Mark the first point of optimal_path1
if optimal_path1:
    first_point_x = optimalx[0]
    first_point_y = optimaly[0]
    plt.text(first_point_x, first_point_y, '**', color='blue', fontsize=12, ha='right')

# Plotting and marking optimal_path2
optimalx = [(basic_all[ind].get("x"))[point] for point in optimal_path2]
optimaly = [(basic_all[ind].get("y"))[point] for point in optimal_path2]
plt.plot(optimalx, optimaly, 'ro', linestyle="--")

# Mark the first point of optimal_path2
if optimal_path2:
    first_point_x = optimalx[0]
    first_point_y = optimaly[0]
    plt.text(first_point_x, first_point_y, '**', color='red', fontsize=12, ha='right')

plt.show()

#%%


plt.scatter(basic_all[ind].get("x"), basic_all[ind].get("y"))
plt.title(f"Greedy {ind}")
greedy1x_list=[]
greedy1y_list=[]
greedy2x_list=[]
greedy2y_list=[]

for counter in range(len(greedy1_list[ind])):
    greedy1x_list.append((basic_all[ind].get("x"))[greedy1_list[ind][counter]] )
    greedy1y_list.append((basic_all[ind].get("y"))[greedy1_list[ind][counter]] )
    counter=counter+1
    
plt.plot(greedy1x_list, greedy1y_list, 'ro', linestyle="--")

# Mark the first point of greedy1_list
if greedy1_list[ind]:
    first_point_x = greedy1x_list[0]
    first_point_y = greedy1y_list[0]
    plt.text(first_point_x, first_point_y, '**', color='red', fontsize=12, ha='right')

for counter in range(len(greedy2_list[ind])):
    greedy2x_list.append((basic_all[ind].get("x"))[greedy2_list[ind][counter]] )
    greedy2y_list.append((basic_all[ind].get("y"))[greedy2_list[ind][counter]])
    counter=counter+1

plt.plot(greedy2x_list, greedy2y_list, 'bo', linestyle="--")

# Mark the first point of greedy2_list
if greedy2_list[ind]:
    first_point_x = greedy2x_list[0]
    first_point_y = greedy2y_list[0]
    plt.text(first_point_x, first_point_y, '**', color='blue', fontsize=12, ha='right')

plt.show()





# %%
