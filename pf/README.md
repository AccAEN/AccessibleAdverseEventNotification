# Pfizer .xpt files

The files in this directory are a spreadsheet readable (tab separated values) version of the .xpt files from the [Pfizer documents released on 2 May 2022](https://www.icandecide.org/pfizer-documents-download-multiple-files/). I have broken up some of the files to be able to fit in excel (excel has a 1,048,576 row limit). Excel isn't the ideal platform to analyse this data set, but there are a lot of clever citizen scientists keen to uncover the truth regarding the Pfizer COVID-19 vaccine trial. I thought it might be useful to convert the data to a format most people could work with. 

Original .xpt files and the .tsv files I generated are:

```
FDA-CBER-2021-5683-0065774 to -0066700_125742_S1_M5_c4591001-A-D-addv.xpt
    addv.tsv
FDA-CBER-2021-5683-0059000 to -0065773_125742_S1_M5_c4591001-A-D-adcevd.xpt
    adcevd.tsv
FDA-CBER-2021-5683-0123168 to -0126026_125742_S1_M5_c4591001-A-D-adva.xpt
    adva.tsv
FDA-CBER-2021-5683-0066701 to -0123167_125742_S1_M5_c4591001-A-D-adfacevd.xpt
    adfacevd_phasen1.tsv
    adfacevd_phasen2.tsv
    adfacevd_phasen4.tsv
    adfacevd_phasen3_control.tsv
    adfacevd_phasen3_treatment.tsv
```
These files can be easily opened in excel by going file, open, browse, All Files (*.*), [find the relevant .tsv file], Open. It is a tab delimited file. In the filenames, phasen refers to the value stored in the PHASEN field, control refers to the placebo group and treatment is the group that got the mRNA injection. I had to split it up like this to be able to fit it in excel.

The notes below are unimportant if you just want to view it in excel.

The R code for opening the .xpt files and saving as .tsv is below:

```
library( foreign )
library( data.table )
addv = read.xport( '<location of xpt files>/FDA-CBER-2021-5683-0065774 to -0066700_125742_S1_M5_c4591001-A-D-addv.xpt' )
adcevd = read.xport( '<location of xpt files>/FDA-CBER-2021-5683-0059000 to -0065773_125742_S1_M5_c4591001-A-D-adcevd.xpt' )
adva = read.xport( '<location of xpt files>/FDA-CBER-2021-5683-0123168 to -0126026_125742_S1_M5_c4591001-A-D-adva.xpt' )
adfacevd = read.xport( '<location of xpt files>/FDA-CBER-2021-5683-0066701 to -0123167_125742_S1_M5_c4591001-A-D-adfacevd.xpt' )
fwrite( addv, file = '<location of xpt files>/addv.tsv', sep = '\t' )
fwrite( adcevd, file = '<location of xpt files>/adcevd.tsv', sep = '\t' )
fwrite( adva, file = '<location of xpt files>/adva.tsv', sep = '\t' )
fwrite( adfacevd[ adfacevd$PHASEN == 1, ], file = '<location of xpt files>/adfacevd_phasen1.tsv', sep = '\t' )
fwrite( adfacevd[ adfacevd$PHASEN == 2, ], file = '<location of xpt files>/adfacevd_phasen2.tsv', sep = '\t' )
fwrite( adfacevd[ adfacevd$PHASEN == 4, ], file = '<location of xpt files>/adfacevd_phasen4.tsv', sep = '\t' )
adfacevd_phasen3 = adfacevd[ adfacevd$PHASEN == 3, ]
levels( as.factor( adfacevd_phasen3$ARM ) )
fwrite( adfacevd_phasen3[ adfacevd_phasen3$ARM == 'Placebo', ], file = '<location of xpt files>/adfacevd_phasen3_control.tsv', sep = '\t' )
fwrite( adfacevd_phasen3[ adfacevd_phasen3$ARM != 'Placebo', ], file = '<location of xpt files>/adfacevd_phasen3_treatment.tsv', sep = '\t' )
```

Opening .xpt files in python:
```
import xport
fo = open( '<location of xpt files>/FDA-CBER-2021-5683-0065774 to -0066700_125742_S1_M5_c4591001-A-D-addv.xpt', 'rb' )
for row in xport.Reader( fo ):
    print( row )
fo.close()
```
