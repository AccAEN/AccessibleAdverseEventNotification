import sys

SearchPattern = 'error'
SearchColumn = 4

SearchPattern = 'Cardiac disorders'
SearchColumn = 3


yp = ''
mp = ''
dp = ''
c1 = 0
c2 = 0
c3 = 0

fi = open( 'DAEN_webscrape_medsummary.txt', 'r' )
line = fi.readline()
fo = open( 'DAEN_webscrape_medsummary_' + SearchPattern + '_' + str( SearchColumn ) + '.txt', 'w' )
fo.write( 'Year\tMonth\tDay\tSearchColumn\tSearchPattern\tNumber of cases\tNumber of cases with a single suspected medicine\tNumber of cases where death was a reported outcome\n' )
fo2 = open( 'DAEN_webscrape_medsummary_' + SearchPattern + '_' + str( SearchColumn ) + '_each.txt', 'w' )
fo2.write( 'Year\tMonth\tDay\tMedDRA system organ class\tMedDRA reaction term\tNumber of cases\tNumber of cases with a single suspected medicine\tNumber of cases where death was a reported outcome\n' )
while( 1 ):
    line = fi.readline().strip()
    if( line == '' ):
        break
    linesp = line.split( '\t' )
    if( ( yp != linesp[ 0 ] ) or ( mp != linesp[ 1 ] ) or ( dp != linesp[ 2 ] ) ):
        if( yp != '' ):
            # save it
            fo.write( yp + '\t' +\
                      mp + '\t' +\
                      dp + '\t' +\
                      str( SearchColumn ) + '\t' +\
                      SearchPattern + '\t' +\
                      str( c1 ) + '\t' +\
                      str( c2 ) + '\t' +\
                      str( c3 ) + '\n' )
        # put new values in yp, mp, dp
        yp = linesp[ 0 ]
        mp = linesp[ 1 ]
        dp = linesp[ 2 ]
        c1 = 0
        c2 = 0
        c3 = 0
        
    if( linesp[ SearchColumn ].find( SearchPattern ) >= 0 ):
        fo2.write( line + '\n' )
        c1 += int( linesp[ 5 ] )
        c2 += int( linesp[ 6 ] )
        c3 += int( linesp[ 7 ] )
        
fo.write( yp + '\t' +\
          mp + '\t' +\
          dp + '\t' +\
          str( SearchColumn ) + '\t' +\
          SearchPattern + '\t' +\
          str( c1 ) + '\t' +\
          str( c2 ) + '\t' +\
          str( c3 ) + '\n' )

fi.close()
fo.close()
fo2.close()
                                
