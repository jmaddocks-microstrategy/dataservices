# dataservices

The dataservices project is designed to simplify the ingestion of public data into MicroStrategy. There are many ways to import data into MicroStrategy, but continuous updates (incremental refresh) require orchestration that this project is designed to address. The project queries the webservice at defined intervals, and will run on a timer until the process is shutdown. 

This data loader designed to update MicroStrategy cubes from Socrata Open Data APIs (https://dev.socrata.com/). Socrata data is available in many state governments, e.g. the city of Chicago: https://data.cityofchicago.org/browse?limitTo=datasets

<h4>Requirements</h4>

Python 3

<h4>Installation</h4>

    pip install dataservices

<h4>Getting started</h4>

The dataservices.cfg configuration file should be updated as follows:

<b>Settings</b>

    queryintervalminutes 
   is the number of minutes between querying the webservices. By default this is set to 1440 minutes (24 hours), to limit the queries that are passed to the webservices.

    checkintervalseconds
   controls the seconds between checking how often queryintervalminutes is checked. By default this is set to 10 seconds (every 10 seconds, the number of elapsed minutes will be re-evaluated)

<b>mstr_library</b>

Replace the following values to match your MicroStrategy environment (do not use single or double quotes):

    __your_server__
    __your_user__
    __your_password__
    __your_project__
