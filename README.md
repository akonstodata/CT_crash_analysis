Crash Analysis for Connecticut I-84: 2015-2019
------------


Introduction
------------
Interstate 84 runs from eastern to western Connecticut, covering approximately one hundred miles en-route.  It acts as a main thoroughfare into and out of the larger Connecticut towns of Hartford and Waterbury, and is often the source of contention regarding expansion and construction projects [1-2].  

The Connecticut Crash Data Repository (CTCDR) is a rich resource of crash data in Connecticut, with data available dating from 1995 to the present for all accidents on Connecticut's roadways [3].  The CTCDR provides an interactive method to visualize certain features of the data.  As we show below, visualizations with additional overlays of local information can serve to augment and complement the information provided by CTCDR.

In this analysis, we create visualizations of crash statistics for I-84 from 2015-2019, overlaid with exit markers and town delineations, and separated into 
*Eastbound* and *Westbound* categories.  Using these visualizations, it is easy to observe where and when accident peaks occur, and therefore make more informed decisions regarding route planning.  We hope that this analysis can help drivers and decision-makers make objective assessments for traffic and crash data on I-84.  We provide all code for the visualizations in a public repository, for those interested in replicating and further exploring the data.  We will continue to update this page with additional analyses of the data.

Furthermore, we expect that this analysis can be used to compare against the expected marked change in traffic behavior in 2020 due to the COVID-19 epidemic.

The Jupyter notebook for all updated analyses is found [[here]](https://github.com/akonstodata/CT_crash_analysis/blob/master/code/CT84_Analysis_2015_2019_v2.ipynb)

Contact: Anna Konstorum (konstorum.anna@gmail.com)

Last updated: 04-05-2020

Results
------------

We consider crash data recorded from January, 2015 - December, 2019, which includes information from the Model Minimum Uniform Crash Criteria (MMUCC) guidelines dataset that houses crash data captured by a revised Connecticut Uniform Police Crash Report (PR-1).


Frequency of accidents by week and month in 2015-2019
------------

We plot total crash frequency as a function of week and month, and observe patterns of cyclical peaks (Fig 1, see Jupyter code for interactive version).

![](https://github.com/akonstodata/CT_crash_analysis/blob/master/results/Fig_1_totalfreq.png)

Frequency of accidents by town
------------

In order to get a general sense of which towns most accidents occur, we plot a histogram of the total number of crashes on I-84 by town, in descending order of crash number (Fig 2).

![](https://github.com/akonstodata/CT_crash_analysis/blob/master/results/Fig2_bytown.png)


Visualization of accident frequency by location and direction
------------

We visualize accident information overlaid on exit, mile, and town markers (Fig 3).

![](https://github.com/akonstodata/CT_crash_analysis/blob/master/results/Fig3_vis.png)

We now compare accidents during morning vs. evening rush hours.  We observe a high level of eastbound accidents in West Hartford and westbound accidents in East Hartford, not surprising as these accidents follow expected traffic commute patterns in Hartford (Fig 4a).  The reverse trend is evident in the evening rush hour (Fig 4b).

![](https://github.com/akonstodata/CT_crash_analysis/blob/master/results/Fig4a_vis_rush_morn.png)
------------
![](https://github.com/akonstodata/CT_crash_analysis/blob/master/results/Fig4b_vis_rush_eve.png)


Close look at one town: Southington
------------

By focusing our analysis on Southington, we observe a major increase in accidents surrounding exits, especially exits 30-32 (Fig 5).

![](https://github.com/akonstodata/CT_crash_analysis/blob/master/results/Fig5_vis_southington.png)

Conclusions
------------
A visual analysis of accident frequency on I-84 reveals easy-to-observe patterns that trend to traffic volume and seasonal accident peaks.  It reveals higher crash frequency surrounding on- and off-ramps (e.g. Southington), which may be useful for allocation of monitoring resources.  Further planned analyses include adding severity and DUI information to the time- and location-specific visualizations.

References
------------

[[1]](https://www.newstimes.com/local/article/Report-I-84-expansion-among-nation-s-biggest-11083090.php)  I-84 expansion among nation's biggest boondoggles.  News-Times (April 17, 2017) 

[[2]](https://www.newstimes.com/local/article/No-end-in-sight-for-traffic-problems-on-7870279.php) No end in sight for traffic problems on overburdened I-84.  News-Times (May 23, 2016)


Source Data
------------
[[3]](https://ctcrash.uconn.edu/) Connecticut Crash Data Repository

[[4]](https://portal.ct.gov/dot) Connecticut Department of Transportation


