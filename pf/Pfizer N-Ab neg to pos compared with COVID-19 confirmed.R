library( foreign )
library( data.table )

dir_in = <change this to the relevant directory>


file_in = paste0( dir_in, 'FDA-CBER-2021-5683-0149082 to -0158559_125742_S1_M5_c4591001-S-D-ce.xpt' )
df = read.xport( file_in )

df_cov = df[ grep( 'COVID-19 confirmed', df$CETERM ), ]
levels( as.factor( df_cov$CETERM ) )
levels( as.factor( df_cov$CEOCCUR ) ) 
sum( df_cov$CEOCCUR == 'Y' )
sum( df_cov$CEOCCUR == 'N' )

length( df_cov$USUBJID )
length( unique( df_cov$USUBJID ) )


advafilename = paste0( dir_in, 'FDA-CBER-2021-5683-0123168 to -0126026_125742_S1_M5_c4591001-A-D-adva.xpt' )
adva = read.xport( advafilename )

# Select just the N-binding antibody assay
NAb = adva[ adva$PARAMN == 5, ]
# Check just collecting N-binding antibody assay
levels( as.factor( NAb$PARAM ) )

# for the Pfizer evaluation, only records up to 14/11/2020 were included
#NAb = NAb[ NAb$ISDTC < '2020-11-15', ]

# Check the states that the value can take
levels( as.factor( NAb$AVALC ) )
sum( NAb$AVALC == 'NEG' )
sum( NAb$AVALC == 'POS' )

# See what visit names are available
levels( as.factor( NAb$VISIT ) )
NAb_v1 = NAb[ ( NAb$VISIT == 'V1_DAY1_VAX1_S' ) | ( NAb$VISIT == 'V1_DAY1_VAX1_L' ), ]
NAb_v3 = NAb[ ( NAb$VISIT == 'V3_MONTH1_POSTVAX2_L' ), ]



# Count all the instances of NAb going from -ve at visit 1 to +ve at visit 3
# Compare with COVID-19 confirmed Y

# Check that the dates seem right
hist( NAb_v1$ADY, breaks = 100 )
min( na.omit( NAb_v1$ADY ) )
max( na.omit( NAb_v1$ADY ) )
hist( NAb_v3$ADY, breaks = 100 )
min( na.omit( NAb_v3$ADY ) )
max( na.omit( NAb_v3$ADY ) )
# There are some problems with dates
sum( na.omit( NAb_v1$ADY ) == 1 )
sum( na.omit( NAb_v1$ADY ) > 1 )
sum( na.omit( NAb_v1$ADY ) != 1 )
NAb_v1$ADY[ NAb_v1$ADY != 1 ] 
sum( is.na(  NAb_v1$ADY ) )
#sum( na.omit( NAb_v3$ADY ) < 28 )
sum( na.omit( NAb_v3$ADY ) < 25 )
sum( na.omit( NAb_v3$ADY ) > 35 )
sum( is.na(  NAb_v3$ADY ) )

# Remove entries where the ADY is NA
NAb_v1 = NAb_v1[ !( is.na(  NAb_v1$ADY ) ), ]
NAb_v3 = NAb_v3[ !( is.na(  NAb_v3$ADY ) ), ]
# Keep only entries where the ADY is 1 or less for visit 1 and between 20 and 40 for visit 3
#NAb_v1 = NAb_v1[ NAb_v1$ADY <= 1, ]
#NAb_v3 = NAb_v3[ ( NAb_v3$ADY >= 25 ) & ( NAb_v3$ADY <= 35 ), ]

#Need to delete all the entries with NA
sum( is.na( NAb_v1$TRTA ) )
sum( is.na( NAb_v3$TRTA ) )
sum( is.na( NAb_v1$AVALC ) )
sum( is.na( NAb_v3$AVALC ) )
NAb_v3 = NAb_v3[ !is.na( NAb_v3$TRTA ), ]

levels( as.factor( NAb_v1$TRTA ) )
levels( as.factor( NAb_v3$TRTA ) )
#levels( as.factor( NAb_v3$AVALC ) )

nt_v1 = sum( NAb_v1$TRTA == 'BNT162b2 Phase 2/3 (30 mcg)' )
nc_v1 = sum( NAb_v1$TRTA == 'Placebo' )
nt_v3 = sum( NAb_v3$TRTA == 'BNT162b2 Phase 2/3 (30 mcg)' )
nc_v3 = sum( NAb_v3$TRTA == 'Placebo' )

nt_v1_NAbpos = sum( ( NAb_v1$TRTA == 'BNT162b2 Phase 2/3 (30 mcg)' ) & ( NAb_v1$AVALC == 'POS' ) )
nt_v1_NAbneg = sum( ( NAb_v1$TRTA == 'BNT162b2 Phase 2/3 (30 mcg)' ) & ( NAb_v1$AVALC == 'NEG' ) )
nc_v1_NAbpos = sum( ( NAb_v1$TRTA == 'Placebo' ) & ( NAb_v1$AVALC == 'POS' ) )
nc_v1_NAbneg = sum( ( NAb_v1$TRTA == 'Placebo' ) & ( NAb_v1$AVALC == 'NEG' ) )
nt_v3_NAbpos = sum( ( NAb_v3$TRTA == 'BNT162b2 Phase 2/3 (30 mcg)' ) & ( NAb_v3$AVALC == 'POS' ) )
nt_v3_NAbneg = sum( ( NAb_v3$TRTA == 'BNT162b2 Phase 2/3 (30 mcg)' ) & ( NAb_v3$AVALC == 'NEG' ) )
nc_v3_NAbpos = sum( ( NAb_v3$TRTA == 'Placebo' ) & ( NAb_v3$AVALC == 'POS' ) )
nc_v3_NAbneg = sum( ( NAb_v3$TRTA == 'Placebo' ) & ( NAb_v3$AVALC == 'NEG' ) )
nc_v1_NAbpos/nc_v1
nt_v1_NAbpos/nt_v1
nc_v3_NAbpos/nc_v3
nt_v3_NAbpos/nt_v3

tab = matrix( c( nt_v3_NAbpos, nt_v3_NAbneg, nc_v3_NAbpos, nc_v3_NAbneg ), nrow = 2, byrow = TRUE )
res = fisher.test( tab, conf.int = TRUE )
res

#check for Duplicate IDs
t1 = NROW( NAb_v1 )
t2 = NROW( unique( NAb_v1$SUBJID ) )
cat( 'In NAb_v1 there are', t1 - t2, 'duplicates\n' )
t1 = NROW( NAb_v3 )
t2 = NROW( unique( NAb_v3$SUBJID ) )
cat( 'In NAb_v3 there are', t1 - t2, 'duplicates\n' )

rowstodelete = c()
# cycle through each record in NAb_v1
for( i in 1:NROW( NAb_v1 ) )
{
  # first check for any duplicates 
  if( sum( NAb_v1$SUBJID == NAb_v1$SUBJID[ i ] ) > 1 )
  {
    rowstodelete = c( rowstodelete, which( NAb_v1$SUBJID == NAb_v1$SUBJID[ i ] )[ 2 ] )
    #print( NAb_v1[ NAb_v1$SUBJID == NAb_v1$SUBJID[ i ], ]$ADY )
    #print( NAb_v1[ NAb_v1$SUBJID == NAb_v1$SUBJID[ i ], ]$AVALC )
  }
}
rowstodelete = unique( rowstodelete )

# Checked that they all have the same value for ADY and AVALC so I can just remove the duplicate entries
NAb_v1 = NAb_v1[ -rowstodelete, ]

V1pV3p_control = 0
V1pV3p_treatment = 0
V1nV3n_control = 0
V1nV3n_treatment = 0
V1nV3p_control = 0
V1nV3p_treatment = 0
V1pV3n_control = 0
V1pV3n_treatment = 0

NAbNtoP_posPCR_control = 0
NAbNtoP_negPCR_control = 0
NAbNtoP_posPCR_treatment = 0
NAbNtoP_negPCR_treatment = 0

count = 0

# cycle through each record in NAb_v1
for( i in 1:NROW( NAb_v1 ) )
{
  # Check that the entry exists in visit 3
  i_v3 = which( NAb_v3$SUBJID == NAb_v1$SUBJID[ i ] )
  if( length( i_v3 ) > 0 )
  {
    count = count + 1
    #cat( count, '\n' )
    str1 = paste0( count )
    if( NAb_v1$TRTA[ i ] == 'Placebo' )
    {
      str1 = paste0( str1, '\t', 'Control  ' )
      if( NAb_v1$AVALC[ i ] == 'POS' )
      {
        str1 = paste0( str1, '\t', 'v1p' )
        if( NAb_v3$AVALC[ i_v3 ] == 'POS' )
        {
          str1 = paste0( str1, '\t', 'v3p' )
          V1pV3p_control = V1pV3p_control + 1
        } else if( NAb_v3$AVALC[ i_v3 ] == 'NEG' ) {
          str1 = paste0( str1, '\t', 'v3n' )
          V1pV3n_control = V1pV3n_control + 1
        }
      } else if( NAb_v1$AVALC[ i ] == 'NEG' )
      {
        str1 = paste0( str1, '\t', 'v1n' )
        if( NAb_v3$AVALC[ i_v3 ] == 'POS' )
        {
          str1 = paste0( str1, '\t', 'v3p' )
          V1nV3p_control = V1nV3p_control + 1
          ##################################################
          #(check COVID-19 confirmed here)
          if( df_cov[ df_cov$USUBJID == NAb_v1$USUBJID[ i ], ] > 0 )
          {
            if( df_cov[ df_cov$USUBJID == NAb_v1$USUBJID[ i ], ][ 1, ]$CEOCCUR == 'Y' )
            {
              NAbNtoP_posPCR_control = NAbNtoP_posPCR_control + 1
            } else if( df_cov[ df_cov$USUBJID == NAb_v1$USUBJID[ i ], ][ 1, ]$CEOCCUR == 'N' ) {
              NAbNtoP_negPCR_control = NAbNtoP_negPCR_control + 1
            }
          }

        } else if( NAb_v3$AVALC[ i_v3 ] == 'NEG' ) {
          str1 = paste0( str1, '\t', 'v3n' )
          V1nV3n_control = V1nV3n_control + 1
        }
      }
    } else {
      str1 = paste0( str1, '\t', 'Treatment' )
      if( NAb_v1$AVALC[ i ] == 'POS' )
      {
        str1 = paste0( str1, '\t', 'v1p' )
        if( NAb_v3$AVALC[ i_v3 ] == 'POS' )
        {
          str1 = paste0( str1, '\t', 'v3p' )
          V1pV3p_treatment = V1pV3p_treatment + 1
        } else if( NAb_v3$AVALC[ i_v3 ] == 'NEG' ) {
          str1 = paste0( str1, '\t', 'v3n' )
          V1pV3n_treatment = V1pV3n_treatment + 1
        }
      } else if( NAb_v1$AVALC[ i ] == 'NEG' )
      {
        str1 = paste0( str1, '\t', 'v1n' )
        if( NAb_v3$AVALC[ i_v3 ] == 'POS' )
        {
          str1 = paste0( str1, '\t', 'v3p' )
          V1nV3p_treatment = V1nV3p_treatment + 1
          #######################################################
          #(check COVID-19 confirmed here)
          if( df_cov[ df_cov$USUBJID == NAb_v1$USUBJID[ i ], ] > 0 )
          {
            if( df_cov[ df_cov$USUBJID == NAb_v1$USUBJID[ i ], ][ 1, ]$CEOCCUR == 'Y' )
            {
              NAbNtoP_posPCR_treatment = NAbNtoP_posPCR_treatment + 1
            } else if( df_cov[ df_cov$USUBJID == NAb_v1$USUBJID[ i ], ][ 1, ]$CEOCCUR == 'N' ) {
              NAbNtoP_negPCR_treatment = NAbNtoP_negPCR_treatment + 1
            }
          }
          
          
        } else if( NAb_v3$AVALC[ i_v3 ] == 'NEG' ) {
          str1 = paste0( str1, '\t', 'v3n' )
          V1nV3n_treatment = V1nV3n_treatment + 1
        }
      }
    }
    #cat( str1, '\n' )
  }
}
cat( ' N-Ab Visit 1\tN-Ab Visit 3\tBNT162b2\t Placebo\n', 
     'POS        \tPOS        \t', sprintf( '%7d', V1pV3p_treatment ), '\t', sprintf( '%7d', V1pV3p_control ), '\n',
     'NEG        \tNEG        \t', sprintf( '%7d', V1nV3n_treatment ), '\t', sprintf( '%7d', V1nV3n_control ), '\n',
     'NEG        \tPOS        \t', sprintf( '%7d', V1nV3p_treatment ), '\t', sprintf( '%7d', V1nV3p_control ), '\n',
     'POS        \tNEG        \t', sprintf( '%7d', V1pV3n_treatment ), '\t', sprintf( '%7d', V1pV3n_control ), '\n' )


cat( paste0( 'N-Ab negative on visit 1 then positive on visit 3\n',
             'PCR result\tBNT162b2\tPlacebo\n',
             'Positive  \t', NAbNtoP_posPCR_treatment, '         \t', NAbNtoP_posPCR_control, '\n',
             'Negative  \t', NAbNtoP_negPCR_treatment, '         \t', NAbNtoP_negPCR_control, '\n' ) )


