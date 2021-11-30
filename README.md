# AccessibleAdverseEventNotification
Making the DAEN information accessible.

The purpose of this repository is to make the information on Australian COVID-19 adverse events accessible. The Therapeutics Goods Administration (TGA) keeps a database of adverse reactions to medications including the COVID-19 vaccines. This Database of Adverse Event Notifications (DAEN) is available to the public via [this awful web interface](https://apps.tga.gov.au/PROD/DAEN/daen-entry.aspx). The most recent two weeks is never available.

The DAEN website doesn't provide information in a format that might be useful for analysis. Instead you have to scrape the information by entering each individual day and collecting the results from two tables which might span multiple pages. I've already done that and the code is [here](code/DAEN_scrape.py) (this code isn't great, but it is good enough to get the job done).

Please be aware that the numbers reported in DAEN are probably significantly less than the actual number of adverse events and deaths. [As the DAEN website states](https://www.tga.gov.au/about-daen-medicines):
> Adverse event reports from consumers and health professionals to the TGA are voluntary, so there is under-reporting by these groups of adverse events related to therapeutic goods in Australia. This is the same around the world.

[Figure 1](graphs/DAEN%20cases.png) shows some of the basic information such as number of adverse events and deaths reported each day for the COVID-19 vaccines, myocarditis, pericarditis and the more general term cardiac disorder. 

![Figure 1](graphs/DAEN%20cases.png)
Figure 1.

[Figure 2](graphs/DAEN%20histogram%20myocarditis%20age.png) shows a histogram of reported cases of myocarditis and pericarditis from the COVID-19 vaccine. Please note that the age group 10-19 is somewhat distorted as the age 10-11 should not receive the vaccine (although there are cases of [8 year olds getting the vaccine](graphs/DAEN%20young%20vaccinated.png) when that should not have occurred). This age group also has a significantly lower uptake than other age groups.

![Figure 2](graphs/DAEN%20histogram%20myocarditis%20age.png)
Figure 2.

Figures 3 and 4 plot the reports of myocarditis by age grouped by sex or manufacturer respectively. Figures 5 and 6 are the same for pericarditis. A '-' is used where an age was not given in the report.

![Figure 3](graphs/DAEN%20myocarditis%20cases%20age.png)
Figure 3.

![Figure 4](graphs/DAEN%20myocarditis%20cases%20manufacturer.png)
Figure 4.

![Figure 5](graphs/DAEN%20pericarditis%20cases%20age.png)
Figure 5.

![Figure 6](graphs/DAEN%20pericarditis%20cases%20manufacturer.png)
Figure 6.

The scraped data is found in the data directory. These files are tab separated files which you can easily import in to a spreadsheet program. All of the files are only for COVID-19 vaccines.
- [DAEN_webscrape_simple.txt](data/DAEN_webscrape_simple.txt) This file shows the date (twice for reasons that made sense at the time, but don't necessarily make sense anymore), the number of cases reported that day, the number of cases with a single suspected medicine for that day, and the number of deaths reported that day.
- [DAEN_webscrape_medsummary.txt](data/DAEN_webscrape_medsummary.txt) This file gives a daily count of each adverse event category. Please note that if one patient had multiple adverse events, then each event would be counted in the appropriate category.
- [DAEN_webscrape_listofreports.txt](data/DAEN_webscrape_listofreports.txt) This file provides the individual reports and includes sex and age (when recorded).

