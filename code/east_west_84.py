#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This set of functions is used to determine and encode 
consistently the direction of a crash event

@author: Anna Konstorum (konstorum.anna@gmail.com)
"""
import pandas as pd

def direction_decision(i,acc_dir,west_names,east_names,acc_info_full):
    """
    Check whether an input column (acc_dir) from the full accident
    dataframe (acc_info_full) contains informative information 
    with regard to direction
    
    """
    
    # Replace such inputs as 'I-84' with 'I 84', and split items by space
    # At least one of the items should represent direction
    acc_dir_split = acc_dir.replace('-',' ').split(' ')
    acc_dir_split = [item.lower() for item in acc_dir_split]
    
    #checking whether "EB EXIT TO WB" or "WB EXIT TO EB" (or modification from) in acc_dir
    if ("EB EXIT TO WB" in acc_dir) or ("EB-EXIT FR WB" in acc_dir):
        acc_info_full.loc[i,'Direction']='E'
    elif ("WB EXIT TO EB" in acc_dir) or ("WB ACC FR EB" in acc_dir): 
        acc_info_full.loc[i,'Direction']='W'
    #elif checking that acc_dir doesn't have both directions (mark for further evaluation)
    elif any(j in acc_dir_split for j in west_names) & any(j in acc_dir_split for j in east_names):
        acc_info_full.loc[i,'Direction']= "FLAG"
    elif any(j in acc_dir_split for j in west_names):
        acc_info_full.loc[i,'Direction'] = "W"
    elif any(i in acc_dir_split for i in east_names):
        acc_info_full.loc[i,'Direction'] = "E"
    return acc_info_full

def update_indices(acc_info_to_update):
    """
    Recover indices that still need to be updated
    """
    index_unknown = acc_info_to_update.index[acc_info_to_update["Direction"]=="Not_known"]
    index_flag = acc_info_to_update.index[acc_info_to_update["Direction"]=="FLAG"]
    index_all_unknown = index_unknown.union(index_flag)
    return index_unknown,index_flag,index_all_unknown

def east_west(acc_info):
    """
    determine and encode consistently the direction of a crash event
    """
    # Different ways that directions could be coded
    east_names = ['e','eastbound','east','e/b','eb','84e','eastbound,']
    west_names = ['w','westbound','west','w/b','w/b,','wb','84w','westbound,']

    # Create new dataframe which will include standardized direction
    acc_info_dir = acc_info.copy()
    acc_info_dir['Direction'] = 'Not_known'
    
    # Check if Roadway_Name variable is informative
    for i in acc_info_dir.index:
        acc_dir = acc_info_dir.iloc[i]['Roadway_Name']
        acc_info_dir = direction_decision(i,acc_dir,west_names,east_names,acc_info_dir)
        
    # obtain indices of 'Not_known' and 'FLAG'
    index_unknown,index_flag,index_all_unknown = update_indices(acc_info_dir)
    #print("After checking 'Roadway_Name':")
    #print("There are",len(index_unknown), "remaining unknown dir and", len(index_flag), "flagged directions\n")
    
    # Check if Intersecting_Roadway_Name informative for unknown/FLAG indices
    for i in index_all_unknown:
        acc_dir = acc_info_dir.iloc[i]['Intersecting_Roadway_Name']
        # there exist na in this column
        if pd.notna(acc_dir):
            acc_info_dir = direction_decision(i,acc_dir,west_names,east_names,acc_info_dir)
        
    # obtain indices of 'Not_known' and 'FLAG'
    index_unknown,index_flag,index_all_unknown = update_indices(acc_info_dir)
    #print("After checking 'Intersecting_Roadway_Name':")
    #print("There are",len(index_unknown), "remaining unknown dir and", len(index_flag), "flagged directions\n") 
    
    # Check if Landmark_Description informative for unknown/FLAG indices
    for i in index_all_unknown:
        acc_dir = acc_info_dir.iloc[i]['Landmark_Description']
        # there exist na in this column
        if pd.notna(acc_dir):
            acc_info_dir = direction_decision(i,acc_dir,west_names,east_names,acc_info_dir)
            
    # obtain indices of 'Not_known' and 'FLAG'
    index_unknown,index_flag,index_all_unknown = update_indices(acc_info_dir)
    #print("After checking 'Landmark_Description':")
    #print("There are",len(index_unknown), "remaining unknown dir and", len(index_flag), "flagged directions\n")
    
    print("Finished encoding direction")
    return acc_info_dir, index_unknown, index_flag