#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This set of functions is used to create a town class
CT Crash data analysis

@author: Anna Konstorum (konstorum.anna@gmail.com)
"""
import plot_results

class town_acc():
    """Analyzing I-84 CT crash data by town"""
    #import numpy as np
    
    def __init__(self,town,full_data,exit_mile,town_mile):
        """Initialize town and full data repository"""
        self.town = town
        self.full_data = full_data
        self.exit_mile = exit_mile
        self.town_mile = town_mile
    
    def get_town_data(self):
        """Subset full data by town if requested"""
        full_data_crash = self.full_data
        if self.town == 'All':
            town_data_subset = full_data_crash
        else:
            town_data_subset = full_data_crash[full_data_crash["Town_Name"]==self.town]
        return(town_data_subset)
    
    def get_weekdays(self,town_data_subset):
        """Subset for just weekdays"""
        town_data_weekday = town_data_subset[(town_data_subset["Day_of_the_Week_Text_Format"]!="Saturday") 
                                    & (town_data_subset["Day_of_the_Week_Text_Format"]!="Sunday")]
        town_data_weekday = town_data_weekday.reset_index()
        return town_data_weekday
    
    def get_rush_hour(self,town_data_subset,morn_eve):
        if morn_eve == "morning":
            start_time="06:00:00"
            end_time="09:00:00"
        else:
            start_time = "16:00:00"
            end_time = "19:00:00"

        town_data_rush_hour = town_data_subset[town_data_subset.final_time.dt.strftime("%H:%M:%S").between(start_time,end_time)] 

        return town_data_rush_hour
    
    def plot_town_data(self,town_data_subset, y_max, y_min,title_out):
        plot_results.plot_accidents_bytown(self.exit_mile, self.town_mile,self.town,town_data_subset, y_max, y_min, title_out)