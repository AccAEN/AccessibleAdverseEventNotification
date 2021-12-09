# AccessibleAdverseEventNotification
Making the DAEN information accessible.

**NOTE - I have recently discovered that the most recent numbers scraped can change significantly. It looks like the data set I uploaded for today (9/12/2021) are missing 3.6% of cases and 0.3% of deaths. It seems like there are such a huge number of adverse events that they can't all be processed in the two weeks before release to the public.**

The purpose of this repository is to make the information on Australian COVID-19 adverse events accessible. The Therapeutics Goods Administration (TGA) keeps a database of adverse reactions to medications including the COVID-19 vaccines. This Database of Adverse Event Notifications (DAEN) is available to the public via [this awful web interface](https://apps.tga.gov.au/PROD/DAEN/daen-entry.aspx). The most recent two weeks is never available.

The DAEN website doesn't provide information in a format that might be useful for analysis. Instead you have to scrape the information by entering each individual day and collecting the results from two tables which might span multiple pages. I've already done that and the code is [here](code/DAEN_scrape.py) (this code isn't great, but it is good enough to get the job done).

Please be aware that the numbers reported in DAEN are probably significantly less than the actual number of adverse events and deaths. [As the DAEN website states](https://www.tga.gov.au/about-daen-medicines):
> Adverse event reports from consumers and health professionals to the TGA are voluntary, so there is under-reporting by these groups of adverse events related to therapeutic goods in Australia. This is the same around the world.

The scraped data is found in the data directory. These files are tab separated files which you can easily import in to a spreadsheet program. All of the files are only for COVID-19 vaccines.
- [DAEN_webscrape_simple.txt](data/DAEN_webscrape_simple.txt) This file shows the date (twice for reasons that made sense at the time, but don't necessarily make sense anymore), the number of cases reported that day, the number of cases with a single suspected medicine for that day, and the number of deaths reported that day.
- [DAEN_webscrape_medsummary.txt](data/DAEN_webscrape_medsummary.txt) This file gives a daily count of each adverse event category. Please note that if one patient had multiple adverse events, then each event would be counted in the appropriate category.
- [DAEN_webscrape_listofreports.txt](data/DAEN_webscrape_listofreports.txt) This file provides the individual reports and includes sex and age (when recorded).

[Figure 1](graphs/DAEN%20cases.png) shows some of the basic information such as number of adverse events and deaths reported each day for the COVID-19 vaccines, myocarditis, pericarditis and the more general term cardiac disorder. The most common MedDRA reaction terms in the Cardiac disorders classification are also listed.

![Figure 1](graphs/DAEN%20cases.png)
Figure 1.

[Figure 2](graphs/DAEN%20histogram%20myocarditis%20age.png) shows a histogram of reported cases of myocarditis and pericarditis from the COVID-19 vaccine. Please note that the age group 10-19 is somewhat distorted as the age 10-11 should not receive the vaccine (although there are cases of [8 year olds getting the vaccine](graphs/DAEN%20young%20vaccinated.png) when that should not have occurred). This age group also has a significantly lower uptake than other age groups. Figure 3 shows how the histogram for myocarditis has progressed over time.

![Figure 2](graphs/DAEN%20histogram%20myocarditis%20age.png)
Figure 2.

![Figure 3](graphs/DAEN_histogram_myocarditis_age.gif)  
Figure 3.

Figure 4 estimates the number of myocarditis and pericarditis cases reported in DAEN per 100,000 people that received two doses. This used DAEN data to 22/11/2021 and the [vaccination numbers](https://www.health.gov.au/resources/collections/covid-19-vaccination-daily-rollout-update) released by the Australian Government for 21/11/2021. An equal number of males and females receiving the vaccination for each group was assumed, as precise numbers were not available.

![Figure 4](graphs/DAEN%20myocarditis%20per%20100000.png)
Figure 4.

Figures 5 and 6 plot the reports of myocarditis by age grouped by sex or manufacturer respectively. Figures 7 and 8 are the same for pericarditis. A '-' is used where an age was not given in the report.

![Figure 5](graphs/DAEN%20myocarditis%20cases%20age.png)
Figure 5.

![Figure 6](graphs/DAEN%20myocarditis%20cases%20manufacturer.png)
Figure 6.

![Figure 7](graphs/DAEN%20pericarditis%20cases%20age.png)
Figure 7.

![Figure 8](graphs/DAEN%20pericarditis%20cases%20manufacturer.png)
Figure 8.


Figure 9 shows the case fatality rate of people in Australia who contracted COVID-19. Data taken from [health.gov](https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-case-numbers-and-statistics#cases-and-deaths-by-age-and-sex) on 1/12/2021. Bottom graph has a logarithmic y-axis to see what is happening with those under the age of 60.

![Figure 9](graphs/Case%20fatality%20rate%20with%20COVID-19.png)  
Figure 9.

It might be useful to work out how many years of life Australians have lost due to COVID-19 and the COVID-19 vaccine. According to the [ABS](https://www.abs.gov.au/statistics/people/population/life-tables/latest-release) (accessed 2/12/2021), the life expectancy at birth for Australians was 81.2 and 85.3 years for males and females respectively in 2018-20. This is the life expectancy of a child born now, this a much higher life expectancy than a child born in the 1930's. The people most likely to die have existing health issues and would have a shorter life expectancy than the ABS figures above, but for simplicity the ABS values will be used. The mean age of any 10 year group is going to be higher than the average of the limits of the group, for simplicity the assumption is that the average age is 7 higher than the minimum for that group. From table 1 below, the human-years lost in Australia of people who had COVID-19 is 6,894 in males and 4,860 in females, and 11,754 in total.

Table 1
![Table 1](graphs/Years%20lost%20to%20COVID-19%20vaccine%20-%20table.png)

The mortality rate of myocarditis has been estimated as 56% at 4.3 years ([Mason et al. 1995](https://pubmed.ncbi.nlm.nih.gov/7596370/)). For simplicity, assume that on average 50% die within 3 years and the other 50% survive (there are a lot of assumptions here for simplification, there isn't a huge amount of data on myocarditis in children, so the survival rate could be different). 

When this calculation was done (DAEN records to 18/11/2021) there were nine records in DAEN with myocarditis that did not include the sex and 104 records that did not include the age, so these are omitted from the calculation. The assumed death age needs to account for the heavy weighting of younger ages and add 3 years. For simplicity assume 6 years over the minimum age for the group. This gives a loss of human-years of 10,528 in males and 5,250 in females for a total of 15,778.

This does not account for the issue of under-reporting. This number is quite difficult to estimate, and will probably be heavily related to prior assumptions of the people that might submit a record. It is possible that under-reporting could be as low as [1 in 200](https://www.bmj.com/rapid-response/2011/11/02/underreporting-vaccine-adverse-events) <if you are aware of better references, please make a note in the discussion section>. For now, assume the under-reporting is 1 in 10. If these assumptions are correct then Australia has lost 158,000 human-years for a disease that has been blamed for the loss of 12,000 human-years. This calculation does not even include the 668 deaths attributed to the COVID-19 vaccine because the age and sex of the deaths suspected to be from the vaccine is not available on the publicly accessible part of DAEN. Also note that the DAEN information (COVID-19 vaccine adverse events) is 2 weeks older than the COVID-19 deaths.

![Figure 10](graphs/Years%20lost%20to%20COVID-19%20vaccine%20-%20graph%2001.png)
Figure 10.

Figure 11 uses an estimated based on research from Israel which had a heavily vaccinated population early. They suggested that [between one in 3000 and one in 6000 men ages 16 to 24](https://www.science.org/content/article/israel-reports-link-between-rare-cases-heart-inflammation-and-covid-19-vaccination). So the DAEN myocarditis data can be scaled up by 1.59 to get 1 in 4,500 for 16-24 year olds.

![Figure 11](graphs/Years%20lost%20to%20COVID-19%20vaccine%20-%20graph%2002.png)
Figure 11.

Figure 12 shows the results from DAEN searches using the term 'vaccine' to look at all adverse event and death records for each year from 2000 to 2021 (although 2021 only included 1/1/2021 to 22/11/2021 at the time this graph was generated). Please note, this is not normalised for the number of vaccines administered (which would probably be a more useful comparison).

![Figure 12](graphs/DAEN%202000-2021.png)
Figure 12.
