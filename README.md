# AccessibleAdverseEventNotification
Making the DAEN information accessible.

[Have a look at my articles on substack.](https://accaen.substack.com/p/south-australian-ambulance-service)

[I'm also on twitter](https://twitter.com/AccAEN)

*Update on 14/4/2022 - The most recent complete re-scrape resulted in the removal of 275 'Myocarditis' cases (about 19% of cases) from DAEN. Most of these cases were changed to 'Myopericarditis'. As a result I have changed the Myocarditis graphs to include 'Myocarditis' and 'Myopericarditis' cases.*

The purpose of this repository is to make the information on Australian COVID-19 adverse events accessible. The Therapeutics Goods Administration (TGA) keeps a database of adverse reactions to medications including the COVID-19 vaccines. This Database of Adverse Event Notifications (DAEN) is available to the public via [this awful web interface](https://apps.tga.gov.au/PROD/DAEN/daen-entry.aspx). The most recent two weeks is never available.

The DAEN website doesn't provide information in a format that might be useful for analysis. Instead you have to scrape the information by entering each individual day and collecting the results from two tables which might span multiple pages. I've already done that and the code is [here](code/DAEN_scrape.py) (this code isn't great, but it is good enough to get the job done).

Please be aware that the numbers reported in DAEN are probably significantly less than the actual number of adverse events and deaths. [As the DAEN website states](https://www.tga.gov.au/about-daen-medicines):
> Adverse event reports from consumers and health professionals to the TGA are voluntary, so there is under-reporting by these groups of adverse events related to therapeutic goods in Australia. This is the same around the world.

The scraped data is found in the data directory. These files are tab separated files which you can easily import in to a spreadsheet program. All of the files are only for COVID-19 vaccines.
- [DAEN_webscrape_simple.txt](data/DAEN_webscrape_simple.txt) This file shows the date (twice for reasons that made sense at the time, but don't necessarily make sense anymore), the number of cases reported that day, the number of cases with a single suspected medicine for that day, and the number of deaths reported that day.
- [DAEN_webscrape_medsummary.txt](data/DAEN_webscrape_medsummary.txt) This file gives a daily count of each adverse event category. Please note that if one patient had multiple adverse events, then each event would be counted in the appropriate category.
- [DAEN_webscrape_listofreports.txt](data/DAEN_webscrape_listofreports.txt) This file provides the individual reports and includes sex and age (when recorded).

Information about re-scraping can be found [here](https://github.com/AccAEN/AccessibleAdverseEventNotification/tree/main/data)

[Figure 1](graphs/DAEN%20cases.png) shows some of the basic information such as number of adverse events and deaths reported each day for the COVID-19 vaccines, myocarditis/myopericarditis, pericarditis and the more general term cardiac disorder. The most common MedDRA reaction terms in the Cardiac disorders classification are also listed.

![Figure 1](graphs/DAEN%20cases.png)
Figure 1.

[Figure 2](graphs/DAEN%20histogram%20myocarditis%20age.png) shows histograms of reported cases of myocarditis/myopericarditis and pericarditis from the COVID-19 vaccine. The younger age groups have a significantly lower and delayed uptake compared with other age groups. Figure 3 shows how the histograms have progressed over time. The age groupings have been changed to reflect age groupings from [vaccine rollout data](https://www.health.gov.au/resources/collections/covid-19-vaccination-daily-rollout-update).

![Figure 2](graphs/DAEN%20histogram%20myocarditis%20age.png)
Figure 2.

![Figure 3](graphs/DAEN_histogram_xcarditis_age.gif)  
Figure 3.

Figure 4 estimates the number of myocarditis and pericarditis cases reported in DAEN per 100,000 people that received two doses. This used DAEN data to 7/1/2022 and the [vaccination numbers](https://www.health.gov.au/resources/collections/covid-19-vaccination-daily-rollout-update) released by the Australian Government for 30/12/2021. An equal number of males and females receiving the vaccination for each group was assumed, as precise numbers were not available. Please note that records in DAEN for myocarditis/myopericarditis and pericarditis that excluded sex or age information were not used in this calculation (16% of myocarditis and 21% of pericarditis cases excluded age or sex information).

![Figure 4](graphs/DAEN%20myocarditis%20per%20100000.png)
Figure 4.

Figures 5 and 6 plot the reports of myocarditis/myopericarditis by age grouped by sex or manufacturer respectively. Figures 7 and 8 are the same for pericarditis. A '-' is used where an age was not given in the report.

![Figure 5](graphs/DAEN%20myocarditis%20cases%20age.png)
Figure 5.

![Figure 6](graphs/DAEN%20myocarditis%20cases%20manufacturer.png)
Figure 6.

![Figure 7](graphs/DAEN%20pericarditis%20cases%20age.png)
Figure 7.

![Figure 8](graphs/DAEN%20pericarditis%20cases%20manufacturer.png)
Figure 8.


Figure 9 shows the case fatality rate of people in Australia who contracted COVID-19. Data taken from [health.gov](https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-case-numbers-and-statistics#cases-and-deaths-by-age-and-sex) on 30/1/2022. Bottom graph has a logarithmic y-axis to see what is happening with those under the age of 60.

![Figure 9](graphs/Case%20fatality%20rate%20with%20COVID-19.png)  
Figure 9.

### WARNING - It looks like there are some vaccines that don't have the word 'vaccine' in DAEN. This will result in an error in the calculation below. I don't yet know how big this error is and haven't yet worked out how to search for all vaccines.

Figure 10 shows the results from DAEN searches using the term 'vaccine' to look at all adverse event and death records for each year from 2000 to 2021. In 2021 there were 737 deaths suspected to be from the COVID-19 vaccine recorded in DAEN and two from all other vaccines combined. There were 98,876 adverse event cases recorded in DAEN from the COVID-19 vaccines and 1,217 from all other vaccines. Please note, this is not normalised for the number of vaccines administered (which would probably be a more useful comparison).

![Figure 10](graphs/DAEN%202000-2021.png)
Figure 10.

Figure 11 attempts to estimate the number of adverse events and deaths per vaccine. This is a work in progress and the numbers will change as more information is discovered about prior vaccination numbers. To me it looks like the COVID-19 vaccines have a suspected death rate per million vaccinations that is 184 times the average of 2000 to 2020.

![Figure 11](graphs/DAEN%202000-2021%20rate%20per%20million.png)
Figure 11.

There are some significant problems with this comparison. The group of people that received the COVID-19 vaccine is not the same as the group that recevied the other vaccines. This is lumping all adverse events in together which can range from a sore arm to a heart attack. If you want to follow along (and I suggest you check my working, don't believe me, please always check everything), the DAEN data can be collected by going [here](https://apps.tga.gov.au/Prod/daen/daen-entry.aspx). For "Select medicines" type "vaccine" and tick the box "Medicines found for 'vaccine…'"
Then select the desired year and look at the "Number of reports (cases):" and " Number of cases where death was a reported outcome:"
Repeat for each relevant year. For 2021 I only collected results for "COVID" in selected medicines.

Get population information (in one of the spreadsheets) [here](https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/jun-2021)

Get COVID vaccination numbers [here](https://www.health.gov.au/resources/publications/covid-19-vaccine-rollout-update-31-december-2021)

Get childhood vaccination rates and number of vaccinations [here](https://www.health.gov.au/health-topics/immunisation/childhood-immunisation-coverage/current-coverage-data-tables-for-all-children)

I used the estimate of influenza vaccination of 39% of the 18+ population from [here](https://www.health.gov.au/sites/default/files/report-newspoll-flu-vaccinations-survey-jun-2014.pdf)

I decided to only consider the number of 'fully vaccinated' as a single vaccination instance rather than count each dose. I only looked at one, two and five year old children since that data set was easy to find. There are a lot more vaccinations that I didn't count that would make the difference even larger (i.e. even worse for the COVID-19 vaccines). I think the biggest potential error is using the estimate of influenza vaccinations for the population over 18 years of age from 2014, I am not sure how accurate that estimate is and if it is safe to assume the same for other years.

Here is another way to compare the COVID-19 vaccine safety to previous vaccines (webm video opens in new page):

### WARNING - It looks like there are some vaccines that don't have the word 'vaccine' in DAEN. This will result in an error in the calculation below. I don't yet know how big this error is and haven't yet worked out how to search for all vaccines.

[![webm](graphs/playwebm.png)](https://htmlpreview.github.io/?https://github.com/AccAEN/AccessibleAdverseEventNotification/blob/main/graphs/playwebm.html)

Sources:

https://www.servicesaustralia.gov.au/sites/default/files/annual-report-2019-20v2.pdf

https://www.health.gov.au/sites/default/files/documents/2021/12/covid-19-vaccine-rollout-update-31-december-2021.pdf

https://apps.tga.gov.au/Prod/daen/daen-entry.aspx

Figure 12 shows the DAEN entries with 'error' in the terms. There were a whole lot of new errors showing up in the latest full re-scrape that wasn't in the previous one. The most notable are seen on 1/11/2021 where a number of 'Expired product administered' was recorded, and 5/11/2021 where numerous teenagers were incorrectly given AstraZeneca which was recorded as 'Wrong product administered'.

![Figure 12](graphs/DAEN%20error%20reported.png)
Figure 12.

Figure 13 is the age standardised case rate per 100,000 according to Public Health Scotland. While this is an interesting graph, there could be a bias in non-testing of those who are unvaccinated. There could also be a bias where people who have been infected decide not to get the vaccine as they already have natural immunity.

![Figure 13](graphs/Scottish%20age%20standardised%20case%20rate.png)
Figure 13

Figure 14 shows a selection of the concerning adverse events in children 5-11 years old. These children have only received the first dose from 10 January 2022 and the second dose from 7 March 2022. The reference list of adverse events has been changed to the European Medicines Agency (EMA) list of [Important Medical Events](https://www.ema.europa.eu/en/documents/other/meddra-important-medical-event-terms-list-version-250_en.xlsx) with syncope excluded. Including syncope would make the list about twice as big, and I don't think children fainting after a needle is as concerning as the other things on the list. Figure 15 is the same, but for 12 to 17 year old children/teenagers.

![Figure 14](graphs/DAEN%20IMEs%205-11yo.png)
Figure 14

![Figure 15](graphs/DAEN%20IMEs%2012-17yo.png)
Figure 15

Figure 16 shows DAEN reports with myocardial infarction (heart attack) in the MedDRA reaction terms.

![Figure 16](graphs/DAEN%20myocardial%20infarction.png)
Figure 16

An interesting pattern emerges when looking at cardiac arrest reports in DAEN with the 28 day moving average (Figure 16). 

![Figure 17](graphs/DAEN%20cardiac%20arrest.png)
Figure 17

In the latest re-scrape I also scraped by manufacturer. Figure 18 shows the suspected AEs and deaths by COVID-19 vaccine manufacturer.

![Figure 18](graphs/DAEN%20cases%20by%20manufacturer.png)
Figure 18


The shortened URL for this page is http://bit.ly/35oQMZG
