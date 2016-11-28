Readme
------
This document describes the folder structure and how processes are linked across folders.

-nas1 # currently houses sample data for testing. Eventually this should be the holding area for all scripts that will pull data from NAS1
 --singtel
 --m1
 --starhub 

-scrubbers
 --m1 #scripts specific to M1 data (in each do sys.path.append("../common') to look for imported scripts from common folder)
 --starhub #scripts specific to Starhub data
 --singtel #scripts specific to Singtel data
 --common #scripts that will be used by "m1", "starhub" and "singtel" folders 
   --error log scripts etc.
 --requirements.txt #specifies packages needed for all scripts in scrubbers folder. 

library name + version. std format that pip understands. e.g. pytz==2015.2 

-output
 --logs #logs written here
   --m1
   --starhub
   --singtel
 --scrubbed #cleaned and valid data
   --m1
   --starhub
   --singtel
