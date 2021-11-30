# AccessibleAdverseEventNotification
Making the DAEN information accessible.

The purpose of this repository is to make the information on Australian COVID-19 adverse events accessible. The Therapeutics Goods Administration (TGA) keeps a database of adverse reactions to medications including the COVID-19 vaccines. This Database of Adverse Event Notifications (DAEN) is available to the public via [this awful web interface](https://apps.tga.gov.au/PROD/DAEN/daen-entry.aspx).

The DAEN website doesn't provide information in a format that might be useful for analysis. Instead you have to scrape the information by entering each individual day and collecting the results from two tables which might span multiple pages. I've already done that and the code is [here](code/DAEN_scrape.py) (this code isn't particularly reliable, but it is good enough to get the job done).

Please be aware that the numbers reported in DEAN are probably significantly less than the actual number of adverse events and deaths. [As the website states](https://www.tga.gov.au/about-daen-medicines):
> Adverse event reports from consumers and health professionals to the TGA are voluntary, so there is under-reporting by these groups of adverse events related to therapeutic goods in Australia. This is the same around the world.

Figure 1 [DAEN cases.png](graphs/DAEN%20cases.png) shows some of the basic information such as number of adverse events and deaths reported each day for the COVID-19 vaccines, myocarditis, pericarditis and the more general term cardiac disorder. 

![Figure 1](graphs/DAEN%20cases.png)
Figure 1.

Figure 2 [DAEN histogram myocarditis age.png](graphs/DAEN%20histogram%20myocarditis%20age.png) shows a histogram of reported cases of myocarditis and pericarditis from the COVID-19 vaccine. Please note that the age group 10-19 is somewhat distorted as the age 10-11 should not receive the vaccine (although there are cases of 8 year olds getting the vaccine when that should not have occurred). This age group also has a significantly lower uptake than other age groups.

![Figure 2](graphs/DAEN%20histogram%20myocarditis%20age.png)
Figure 2.







