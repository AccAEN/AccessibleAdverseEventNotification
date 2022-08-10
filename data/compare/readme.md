linux command used:
diff DAEN_2022_07_25_scraped_2022_08_08.txt DAEN_2022_07_25_scraped_2022_08_11.txt > DAEN_2022_07_25_difference.txt

&lt; means a row that was deleted

&gt; means a row that was added

This explains the other terms
https://linuxopsys.com/topics/linux-diff-command

In this case 63 rows were deleted and 15 added.

Example of a change, row 22 was deleted because the MedDRA reaction term 'Vaccine breakthrough infection' was deleted and the MedDRA reaction term 'SARS-CoV-2 test positive' was added, adding row 22 back with that change.```
