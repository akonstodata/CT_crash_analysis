#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This set of functions is used for plotting the results from 
CT Crash data analysis

@author: Anna Konstorum (konstorum.anna@gmail.com)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def myround(x, base=5):
    return int(base * round(float(x)/base))

def plot_accidents_bytown(exit_mile,town_mile,town_name,town_data, y_max, y_min, title_out):
        """Plot accidents by milemarker"""
        exit_mile_E = exit_mile[exit_mile["Direction"]=='E']
        exit_mile_W = exit_mile[exit_mile["Direction"]=='W']
        town_data_east = town_data[town_data["Direction"]=='E']
        town_data_west = town_data[town_data["Direction"]=='W']
        if town_name=="All":
            town_min_ind = 0.00
            town_max_ind = 98.25
        else:
            town_ind = town_mile[town_mile["Town_Name"]==town_name]
            town_min_ind= town_ind["Mile"].values[0]
            town_max_ind = town_min_ind + town_ind["Town_Miles"].values[0]
        
        x_index = np.arange(town_min_ind,town_max_ind,0.25)
        
        town_data_east_loc = town_data_east["Milemarker"]
        town_data_west_loc = town_data_west["Milemarker"]
        
        town_data_east_bin = pd.cut(town_data_east_loc, x_index, include_lowest = 1)
        town_data_west_bin = pd.cut(town_data_west_loc, x_index, include_lowest = 1)

        town_data_east_bin_count = town_data_east_loc.groupby(town_data_east_bin).size()
        town_data_west_bin_count = town_data_west_loc.groupby(town_data_west_bin).size()
        
        max_acc = max(town_data_east_bin_count.max(),town_data_west_bin_count.max())
        
        exit_mile_town_E = exit_mile_E[exit_mile_E["Mile"]>=town_min_ind]
        exit_mile_town_E = exit_mile_town_E[exit_mile_town_E["Mile"]<town_max_ind]
        
        exit_mile_town_W = exit_mile_W[exit_mile_W["Mile"]>=town_min_ind]
        exit_mile_town_W = exit_mile_town_W[exit_mile_town_W["Mile"]<town_max_ind]
        
        if max_acc > 250:
            steps = 100
        elif max_acc <=250 and max_acc > 100:
            steps = 50
        elif max_acc<= 100 and max_acc > 50:
            steps = 25
        elif max_acc<=50 and max_acc > 25:
            steps = 5
        else:
            steps = 2
        if y_max == 'not_set' and y_min == 'not_set':    
            y_max = myround(town_data_east_bin_count.max(),steps)+steps/2
            y_min = -1*myround(town_data_west_bin_count.max(),steps)-steps/2

        fig, ax = plt.subplots(figsize=[15,10])
        plt.rcParams['figure.figsize'] = [15, 10]
        plt.bar(x_index[:-1],town_data_east_bin_count,align='edge', width = 0.25,color='darksalmon')
        plt.bar(x_index[:-1],-town_data_west_bin_count,align='edge', width=0.25, color='cornflowerblue')
        plt.ylim(y_min,y_max)
        plt.yticks(np.arange(y_min,y_max,step=steps),abs(np.arange(y_min,y_max,step=steps)))
        plt.ylabel('Number of accidents',fontsize=14)
        plt.xlabel('I-84 Milemarker',fontsize=14)
        plt.title(title_out,fontsize=15)
        # create custom legend
        leg_elements = [Line2D([0], [0], color='coral', lw=3, label='East'),
                           Line2D([0], [0], color='cornflowerblue', lw=3, label='West')]
        ax.legend(handles=leg_elements, loc='upper right')


        # Add exit ramp delineations and names 
        max_height_mile = int(max(steps/4,2))            
        plt.vlines(exit_mile_town_E["Mile"],ymin = 0, ymax = max_height_mile, color = 'red', linewidth = 0.4, linestyle='-')
        for i, row in enumerate(exit_mile_town_E.values):
            go=0
            if (town_name=="All") and ((i)%5==0):
                go=1
            elif (town_name!="All"):
                go=1
            if go==1:
                Direction, Mile, Exit, Town_Number, Town_name = row
                loc_print = Mile
                plt.text(loc_print,max_height_mile + min(max_height_mile,5),Exit,rotation = 90,color='black',
                    fontsize = 9,verticalalignment='center',horizontalalignment='center' )
                
        plt.vlines(exit_mile_town_W["Mile"],ymin = -1*max_height_mile, ymax =0, color = 'red', linewidth = 0.4, linestyle='-')
        for i, row in enumerate(exit_mile_town_W.values):
            go=0
            if (town_name=="All") and ((i)%5==0):
                go=1
            elif (town_name!='All'):
                go=1
            if go==1:
                Direction, Mile, Exit, Town_Number, Town_name = row
                loc_print = Mile
                plt.text(loc_print,-1*(max_height_mile+min(max_height_mile,5)),Exit,rotation = 90,color='black',
                         fontsize = 9,verticalalignment='center',horizontalalignment='center' )
        # Add town names
        if town_name=="All":
            loc_town_names = town_data_west_bin_count.max()
            plt.vlines(town_mile["Mile"], ymin=-int(max_acc/3), ymax=int(max_acc/3),color='dimgrey', linewidth=0.5,linestyle='-.')
            for i, row in enumerate(town_mile.values):
                Mile, Town_Number, Town_Name, Town_Miles = row
                loc_print = Mile + Town_Miles/2
                if (i!=2 or i!=3):
                    plt.text(loc_print,y_min+5,Town_Name,rotation=-90,
                    fontsize=8,verticalalignment='bottom',horizontalalignment='right')
                elif i==2:
                    plt.text(loc_print+5,-(max(loc_town_names,10)+10),Town_Name,rotation=-90,
                    fontsize=8,verticalalignment='bottom',horizontalalignment='right')
                elif i==3:
                    plt.text(loc_print+8,-(max(loc_town_names,10)+10),Town_Name,rotation=-90,
                    fontsize=8,verticalalignment='bottom',horizontalalignment='right')