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
These files can be easily opened in excel by going file, open, browse, All Files (\*.\*), [find the relevant .tsv file], Open. It is a tab delimited file. In the filenames, phasen refers to the value stored in the PHASEN field, control refers to the placebo group and treatment is the group that got the mRNA injection. I had to split it up like this to be able to fit it in excel.

Josh Guetzkow [@joshg99](https://twitter.com/joshg99/status/1524128806008766464) provided a file with an explanation of all the terms used: 

adva.tsv
```
studyid         Study Identifier
usubjid         Unique Subject Identifier
subjid          Subject Identifier for the Study
siteid          Study Site Identifier
trtp            Planned Treatment
trtpn           Planned Treatment (N)
trta            Actual Treatment
trtan           Actual Treatment (N)
isdtc           Date/Time of Collection
adt             Analysis Date
ady             Analysis Relative Day
avisit          Analysis Visit
avisitn         Analysis Visit (N)
visit           Visit Name
visitnum        Visit Number
parcat1         Parameter Category 1
parcat1n        Parameter Category 1 (N)
param           Parameter
paramn          Parameter (N)
paramcd         Parameter Code
aval            Analysis Value
avalc           Analysis Value (C)
base            Baseline Value
basec           Baseline Value (C)
basetype        Baseline Type
ablfl           Baseline Record Flag
apsblfl         Post Baseline Record Flag
ablpblfl        Baseline and post-baseline flag
dtype           Derivation Type
r2base          Ratio to Baseline
srcdom          Source Data
srcvar          Source Variable
srcseq          Source Sequence Number
anl01fl         Analysis Record Flag 01:Window Record
anl03fl         Analysis Flag 03:valid value
anl04fl         Analysis Flag 04:ge LLoQ
islloq          Lower Limit of Quantitation
isstresc        Result or Finding in Standard Format
evimmfl         Evaluable Immunogenicity Record Flag
aaimmfl         All-available Immunogenicity Record Flag
bsseron         Baseline serostatus (N)
bsseroc         Baseline serostatus
aperiod         Period
aperiodc        Period (C)
apersdtm        Period Start Datetime
aperedtm        Period End Datetime
base4f          Baseline Value for 4 Fold Rise
r2base4f        Ratio to baseline for 4 Fold Rise
fold4fl         Achieve 4-Fold Rise Flag
iststdtl        Measurement, Test or Examination Detail
age             Age
ageu            Age Units
sex             Sex
sexn            Sex (N)
race            Race
racen           Race (N)
randfl          Randomized Population Flag
saffl           Safety Population Flag
arm             Description of Planned Arm
armcd           Planned Arm Code
actarm          Description of Actual Arm
actarmcd        Actual Arm Code
trtsdt          Date of First Exposure to Treatment
trtedt          Date of Last Exposure to Treatment
trtstm          Time of First Exposure to Treatment
trtetm          Time of Last Exposure to Treatment
trt01a          Actual Treatment for Period 01
trt01an         Actual Treatment for Period 01 (N)
trt02a          Actual Treatment for Period 02
trt02an         Actual Treatment for Period 02 (N)
trt01p          Planned Treatment for Period 01
trt01pn         Planned Treatment for Period 01 (N)
trt02p          Planned Treatment for Period 02
trt02pn         Planned Treatment for Period 02 (N)
tr01sdt         Date of First Exposure in Period 01
tr01stm         Time of First Exposure in Period 01
tr01sdtm        Datetime of First Exposure in Period 01
tr01edt         Date of Last Exposure in Period 01
tr01etm         Time of Last Exposure in Period 01
tr01edtm        Datetime of Last Exposure in Period 01
tr02sdt         Date of First Exposure in Period 02
tr02stm         Time of First Exposure in Period 02
tr02sdtm        Datetime of First Exposure in Period 02
tr02edt         Date of Last Exposure in Period 02
tr02etm         Time of Last Exposure in Period 02
tr02edtm        Datetime of Last Exposure in Period 02
cohortn         Cohort Group (N)
cohort          Cohort Group
vax101dt        Vaccination Date 01
vax102dt        Vaccination Date 02
vax10udt        Vaccination Date Unplanned
vax201dt        Vaccination Date 03
vax202dt        Vaccination Date 04
aai01fl         Dose 1 all-available Immun Popu Flag
eval02fl        Dose 2 evaluable Immun Popu Flag
aai02fl         Dose 2 all-available Immun Popu Flag
eval01fl        Dose 1 evaluable Immun Popu Flag
dosalvl         Actual Dosing Level
dosalvln        Actual Dosing Level (N)
dosplvl         Planned Dosing Level
dosplvln        Planned Dosing Level (N)
agegr1          Pooled Age Group 1
agegr1n         Pooled Age Group 1 (N)
agegr2          Pooled Age Group 2
agegr2n         Pooled Age Group 2 (N)
agegr4          Pooled Age Group 4
agegr4n         Pooled Age Group 4 (N)
phase           Study Phase
phasen          Study Phase (N)
covblst         Baseline SARS-CoV-2 Status
hivfl           HIV Positive Subjects Flag
pedimmfl        Pop for Non-inferiority Assessement
ev1md2fl        Subject without Evidence 1MPD2
agetr01         Age at Vaccination 01
vax101          Vaccination 01
vax102          Vaccination 02
vax10u          Vaccination Unplanned
vax201          Vaccination 03
vax202          Vaccination 04
vax20u          Vaccination Unplanned in Period 02
vax20udt        Vaccination Date Unplanned in Period 02
unblnddt        Treatment Unblinded Date
mulenrfl        Multiply Enrolled Subjects
rand1fl         Random - exclude Multi-Enrolloer
trtsdtm         Datetime of First Exposure to Treatment
trtedtm         Datetime of Last Exposure to Treatment
```

adfacevd\_\*.tsv
```
studyid         Study Identifier
usubjid         Unique Subject Identifier
subjid          Subject Identifier for the Study
siteid          Study Site Identifier
age             Age
ageu            Age Units
sex             Sex
sexn            Sex (N)
race            Race
racen           Race (N)
arace           Analysis Race
aracen          Analysis Race (N)
ethnic          Ethnicity
ethnicn         Ethnicity (N)
country         Country
saffl           Safety Population Flag
arm             Description of Planned Arm
armcd           Planned Arm Code
actarm          Description of Actual Arm
actarmcd        Actual Arm Code
trtsdt          Date of First Exposure to Treatment
trtstm          Time of First Exposure to Treatment
trtsdtm         Datetime of First Exposure to Treatment
trtedt          Date of Last Exposure to Treatment
trtetm          Time of Last Exposure to Treatment
trtedtm         Datetime of Last Exposure to Treatment
trt01a          Actual Treatment for Period 01
trt02a          Actual Treatment for Period 02
trt02an         Actual Treatment for Period 02 (N)
trt01an         Actual Treatment for Period 01 (N)
trt01p          Planned Treatment for Period 01
trt01pn         Planned Treatment for Period 01 (N)
trt02p          Planned Treatment for Period 02
trt02pn         Planned Treatment for Period 02 (N)
tr01sdt         Date of First Exposure in Period 01
tr01stm         Time of First Exposure in Period 01
tr01sdtm        Datetime of First Exposure in Period 01
tr01edt         Date of Last Exposure in Period 01
tr01etm         Time of Last Exposure in Period 01
tr01edtm        Datetime of Last Exposure in Period 01
tr02sdt         Date of First Exposure in Period 02
tr02stm         Time of First Exposure in Period 02
tr02sdtm        Datetime of First Exposure in Period 02
tr02edt         Date of Last Exposure in Period 02
tr02etm         Time of Last Exposure in Period 02
tr02edtm        Datetime of Last Exposure in Period 02
vax101dt        Vaccination Date 01
vax102dt        Vaccination Date 02
cohort          Cohort Group
cohortn         Cohort Group (N)
phase           Study Phase
phasen          Study Phase (N)
dosplvl         Planned Dosing Level
dosplvln        Planned Dosing Level (N)
dosalvl         Actual Dosing Level
dosalvln        Actual Dosing Level (N)
agegr1          Pooled Age Group 1
agegr1n         Pooled Age Group 1 (N)
agegr2          Pooled Age Group 2
agegr2n         Pooled Age Group 2 (N)
agegr4          Pooled Age Group 4
agegr4n         Pooled Age Group 4 (N)
racegr1         Pooled Race Group 1
racegr1n        Pooled Race Group 1 (N)
vax101          Vaccination 01
vax102          Vaccination 02
ds30kfl         Phase 3 30k Subjects Flag
covblst         Baseline SARS-CoV-2 Status
mulenrfl        Multiply Enrolled Subjects
hivfl           HIV Positive Subjects Flag
pedreafl        Phase 2/3 Pop for 12-25 Reacto Subset
unblnddt        Treatment Unblinded Date
ds3kfl          Phase 3 3000 Subjects Flag
reactofl        Reactogenicity Population Flag
agetr01         Age at Vaccination 01
vax10u          Vaccination Unplanned
vax10udt        Vaccination Date Unplanned
randfl          Randomized Population Flag
rand1fl         Random - exclude Multi-Enrolloer
saf1fl          Safety - excld Multi-Enrolloer&HIV&IND
saf2fl          Safety - exclude Multi-Enrolloer&IND
srcdom          Source Data
srcseq          Source Sequence Number
fagrpid         Group ID
falnkid         Link ID
falnkgrp        Link Group ID
fatest          Findings About Test Name
fatestcd        Findings About Test Short Name
param           Parameter
paramcd         Parameter Code
paramn          Parameter (N)
faobj           Object of the Observation
parcat1         Parameter Category 1
parcat2         Parameter Category 2
avalc           Analysis Value (C)
aval            Analysis Value
avalcat1        Analysis Value Category 1
avalca1n        Analysis Value Category 1 (N)
fastat          Completion Status
fareasnd        Reason Not Performed
faeval          Evaluator
avisitn         Analysis Visit (N)
avisit          Analysis Visit
adt             Analysis Date
adtm            Analysis Datetime
ady             Analysis Relative Day
atpt            Analysis Timepoint
atptn           Analysis Timepoint (N)
atptref         Analysis Timepoint Reference
faevintx        Evaluation Interval Text
dtype           Derivation Type
fastint         Evaluation Interval Start
faenint         Evaluation Interval End
exdose          Dose
extrt           Name of Treatment
exdosu          Dose Units
exstdtc         Start Date/Time of Treatment
exendtc         End Date/Time of Treatment
cltyp           Collection Type
vsorres         Result or Finding in Original Units
vsorresu        Original Units
vsstresn        Numeric Result/Finding in Standard Units
vsstresu        Standard Units
ftemcat         Fever Temperature Category
ftemcatn        Fever Temperature Category (N)
knowvfl         Known Value Flag
eventfl         Event Value Flag
knowvdfl        Day Known Value Flag
eventdfl        Day Event Value Flag
cutunbfl        Cut after Unblinding Date Flag
eventocc        Occurences of Event
trta            Actual Treatment
trtan           Actual Treatment (N)
trtp            Planned Treatment
trtpn           Planned Treatment (N)
```

adcevd.tsv
```
studyid         Study Identifier
usubjid         Unique Subject Identifier
subjid          Subject Identifier for the Study
siteid          Study Site Identifier
age             Age
ageu            Age Units
sex             Sex
sexn            Sex (N)
race            Race
racen           Race (N)
arace           Analysis Race
aracen          Analysis Race (N)
saffl           Safety Population Flag
arm             Description of Planned Arm
armcd           Planned Arm Code
actarm          Description of Actual Arm
actarmcd        Actual Arm Code
trtsdt          Date of First Exposure to Treatment
trtstm          Time of First Exposure to Treatment
trtsdtm         Datetime of First Exposure to Treatment
trtedt          Date of Last Exposure to Treatment
trtetm          Time of Last Exposure to Treatment
trtedtm         Datetime of Last Exposure to Treatment
trt01a          Actual Treatment for Period 01
trt01an         Actual Treatment for Period 01 (N)
trt02a          Actual Treatment for Period 02
trt02an         Actual Treatment for Period 02 (N)
trt01p          Planned Treatment for Period 01
trt01pn         Planned Treatment for Period 01 (N)
trt02p          Planned Treatment for Period 02
trt02pn         Planned Treatment for Period 02 (N)
tr01sdt         Date of First Exposure in Period 01
tr01stm         Time of First Exposure in Period 01
tr01sdtm        Datetime of First Exposure in Period 01
tr01edt         Date of Last Exposure in Period 01
tr01etm         Time of Last Exposure in Period 01
tr01edtm        Datetime of Last Exposure in Period 01
tr02sdt         Date of First Exposure in Period 02
tr02stm         Time of First Exposure in Period 02
tr02sdtm        Datetime of First Exposure in Period 02
tr02edt         Date of Last Exposure in Period 02
tr02etm         Time of Last Exposure in Period 02
tr02edtm        Datetime of Last Exposure in Period 02
vax101dt        Vaccination Date 01
vax102dt        Vaccination Date 02
cohort          Cohort Group
cohortn         Cohort Group (N)
phase           Study Phase
phasen          Study Phase (N)
dosplvl         Planned Dosing Level
dosplvln        Planned Dosing Level (N)
dosalvl         Actual Dosing Level
dosalvln        Actual Dosing Level (N)
agegr1          Pooled Age Group 1
agegr1n         Pooled Age Group 1 (N)
agegr2          Pooled Age Group 2
agegr2n         Pooled Age Group 2 (N)
agegr4          Pooled Age Group 4
agegr4n         Pooled Age Group 4 (N)
vax101          Vaccination 01
vax102          Vaccination 02
ds30kfl         Phase 3 30k Subjects Flag
covblst         Baseline SARS-CoV-2 Status
mulenrfl        Multiply Enrolled Subjects
hivfl           HIV Positive Subjects Flag
pedreafl        Phase 2/3 Pop for 12-25 Reacto Subset
unblnddt        Treatment Unblinded Date
ds3kfl          Phase 3 3000 Subjects Flag
reactofl        Reactogenicity Population Flag
agetr01         Age at Vaccination 01
vax10u          Vaccination Unplanned
vax10udt        Vaccination Date Unplanned
randfl          Randomized Population Flag
rand1fl         Random - exclude Multi-Enrolloer
saf1fl          Safety - excld Multi-Enrolloer&HIV&IND
saf2fl          Safety - exclude Multi-Enrolloer&IND
trta            Actual Treatment
trtan           Actual Treatment (N)
trtp            Planned Treatment
trtpn           Planned Treatment (N)
srcdom          Source Data
srcseq          Source Sequence Number
cegrpid         Group ID
celnkgrp        Link Group ID
ceterm          Reported Term for the Clinical Event
cellt           Lowest Level Term
cedecod         Dictionary-Derived Term
ceptcd          Preferred Term Code
cebodsys        Body System or Organ Class
cebdsycd        Body System or Organ Class Code
cecat           Category for Clinical Event
cescat          Subcategory for Clinical Event
cepresp         Clinical Event Pre-Specified
ceoccur         Clinical Event Occurrence
cestat          Completion Status
cereasnd        Reason Clinical Event Not Collected
asev            Analysis Severity/Intensity
cesev           Severity/Intensity
celoc           Location of Event
celat           Laterality
cestdtc         Start Date/Time of Clinical Event
ceendtc         End Date/Time of Clinical Event
cestdy          Study Day of Start of Observation
ceendy          Study Day of End of Observation
ceenrtpt        End Relative to Reference Time Point
ceentpt         End Reference Time Point
cetpt           Planned Time Point Name
cetptref        Time Point Reference
exdose          Dose
extrt           Name of Treatment
exdosu          Dose Units
exstdtc         Start Date/Time of Treatment
exendtc         End Date/Time of Treatment
astdt           Analysis Start Date
aendt           Analysis End Date
aduru           Analysis Duration Units
adurn           Analysis Duration (N)
knowvfl         Known Value Flag
eventfl         Event Value Flag
```

addv.tsv
```
studyid         Study Identifier
usubjid         Unique Subject Identifier
domain          Domain Abbreviation
subjid          Subject Identifier for the Study
siteid          Study Site Identifier
age             Age
sex             Sex
race            Race
trtsdt          Date of First Exposure to Treatment
trtedt          Date of Last Exposure to Treatment
arm             Description of Planned Arm
armcd           Planned Arm Code
actarm          Description of Actual Arm
actarmcd        Actual Arm Code
trt01p          Planned Treatment for Period 01
trt01a          Actual Treatment for Period 01
trt01pn         Planned Treatment for Period 01 (N)
trt01an         Actual Treatment for Period 01 (N)
agegr1          Pooled Age Group 1
agegr1n         Pooled Age Group 1 (N)
dvseq           Sequence Number
dvspid          Sponsor-Defined Identifier
dvterm          Protocol Deviation Term
dvterm1         Protocol Deviation Term 1
dvdecod         Protocol Deviation Coded Term
epoch           Epoch
actsite         Actual Site of Deviation Occurrence
desgtor         Visit Designator
cape            Confirmed Analysis Population Exclusion
dvcat           Category for Protocol Deviation
dvstdtc         Start Date/Time of Deviation
dvstdy          Study Day of Start of Deviation
astdt           Analysis Start Date
prefl           Pre-treatment Flag
trpfl           On Treatment Flag
randfl          Randomized Population Flag
phase           Study Phase
phasen          Study Phase (N)
cohort          Cohort Group
cohortn         Cohort Group (N)
dosalvl         Actual Dosing Level
dosalvln        Actual Dosing Level (N)
dosplvl         Planned Dosing Level
dosplvln        Planned Dosing Level (N)
ds3kfl          Phase 3 3000 Subjects Flag
agegr3n         Pooled Age Group 3 (N)
agegr3          Pooled Age Group 3
agegr4n         Pooled Age Group 4 (N)
agegr4          Pooled Age Group 4
hivfl           HIV Positive Subjects Flag
agetr01         Age at Vaccination 01
trtsdtm         Datetime of First Exposure to Treatment
trtedtm         Datetime of Last Exposure to Treatment
tr01sdtm        Datetime of First Exposure in Period 01
tr01edtm        Datetime of Last Exposure in Period 01
tr02sdtm        Datetime of First Exposure in Period 02
tr02edtm        Datetime of Last Exposure in Period 02
vax101          Vaccination 01
vax102          Vaccination 02
vax10u          Vaccination Unplanned
vax201          Vaccination 03
vax202          Vaccination 04
vax20u          Vaccination Unplanned in Period 02
vax20udt        Vaccination Date Unplanned in Period 02
unblnddt        Treatment Unblinded Date
mulenrfl        Multiply Enrolled Subjects
rand1fl         Random - exclude Multi-Enrolloer
```

The notes below are unimportant if you just want to view it in excel.

The R code for opening the .xpt files and saving as .tsv files that excel can manage is below:

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
