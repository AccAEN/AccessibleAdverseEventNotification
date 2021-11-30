# This code scrapes information from the Australian DAEN
# (Database of Adverse Event Notifications). A shitty website
# That is slow and does not provide data in a user-friendly
# format.
# This requires selenium, chrome and chromedriver.
# This code is shit, but it works well enough for now.
# Change the values in StartDate and EndDate to scrape a day.
# It appends new values to existing files (or creates then if
# they don't exist).
# DAEN witholds access to the most recent data, you can only
# see stuff that is more than 14 days old.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
from datetime import timedelta
import sys
import re
from time import sleep


StartDate = datetime.strptime( '22/02/2021', '%d/%m/%Y' )
StartDate = datetime.strptime( '16/11/2021', '%d/%m/%Y' )
EndDate = datetime.strptime( '16/11/2021', '%d/%m/%Y' )
QueryDate = StartDate








def write_to_log( logtext ):
    with open( 'DAEN_webscrape_log.txt', 'a') as logfile:
        logfile.write( datetime.now().strftime( '%Y-%m-%d %H:%M:%S' ) + '\t' + logtext + '\n' )
        print( logtext )
    return

def write_to_simple( text ):
    with open( 'DAEN_webscrape_simple.txt', 'a') as txtfile:
        txtfile.write( text + '\n' )
        #print( text )
    return

def get_simple_info( StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay ):
    ps = driver.page_source
    i1 = ps.find( '(cases):' )
    i2 = ps.find( '<strong>', i1 ) + 8
    i3 = ps.find( '</strong', i2 )
    cases = ps[ i2:i3 ]
    i1 = ps.find( 'medicine:' )
    i2 = ps.find( '<strong>', i1 ) + 8
    i3 = ps.find( '</strong', i2 )
    singlemedicine = ps[ i2:i3 ]
    i1 = ps.find( 'outcome:' )
    i2 = ps.find( '<strong>', i1 ) + 8
    i3 = ps.find( '</strong', i2 )
    deaths = ps[ i2:i3 ]
    write_to_simple( str( StartYear ) + '\t' +\
                      str( StartMonth ) + '\t' +\
                      str( StartDay ) + '\t' +\
                      str( EndYear ) + '\t' +\
                      str( EndMonth ) + '\t' +\
                      str( EndDay ) + '\t' +\
                      cases + '\t' +\
                      singlemedicine + '\t' +\
                      deaths ) 
    return

def write_to_medsummary( text ):
    with open( 'DAEN_webscrape_medsummary.txt', 'a') as txtfile:
        txtfile.write( text )
        #print( text )
    return

def get_medsummary_info( StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay ):
    table = driver.find_element_by_id( 'ctl00_body_MedicineSummaryControl_MedicineSummaryGrid' )
    body = table.find_element_by_tag_name( 'tbody' )
    body_rows = body.find_elements_by_tag_name( 'tr' )
    text = []
    for row in body_rows:
        txt1 = [ cell.text.encode( 'utf8' ) for cell in row.find_elements_by_tag_name( 'td' ) ]
        txt2 = str( StartYear ) + '\t' +\
               str( StartMonth ) + '\t' +\
               str( StartDay ) + '\t' +\
               '\t'.join( txt1 ).replace( '\n', ' ' ).strip() + '\n'
        text.append( txt2 )
    write_to_medsummary( ''.join( text ) )
    return

def check_medsummary_next():
    try:
        #print( 'finding next' )
        btn_next = driver.find_element_by_id( 'ctl00_body_MedicineSummaryControl_PageNext' )
        #sleep( 1 )
        #print( 'about to click next' )
        btn_next.click()
        #print( 'clicked next' )
        #sleep( 1 )
        return 1
    except:
        return 0

def write_to_listofreports( text ):
    with open( 'DAEN_webscrape_listofreports.txt', 'a') as txtfile:
        txtfile.write( text )
        #print( text )
    return

def get_listofreports_info( StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay ):
    table = driver.find_element_by_id( 'ctl00_body_CaseListingControl_CaseListingGrid' )
    body = table.find_element_by_tag_name( 'tbody' )
    body_rows = body.find_elements_by_tag_name( 'tr' )
    text = []
    for row in body_rows:
        txt1 = [ cell.text.encode( 'utf8' ) for cell in row.find_elements_by_tag_name( 'td' ) ]
        txt2 = str( StartYear ) + '\t' +\
               str( StartMonth ) + '\t' +\
               str( StartDay ) + '\t' +\
               '\t'.join( txt1 ).replace( '\n', ' ' ).strip() + '\n'
        text.append( txt2 )
    write_to_listofreports( ''.join( text ) )
    return

def check_listofreports_next():
    try:
        btn_next = driver.find_element_by_id( 'ctl00_body_CaseListingControl_PageNext' )
        btn_next.click()
        return 1
    except:
        return 0


def search_terms( term, StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay ):
    StartYear = str( StartYear )
    EndYear = str( EndYear )
    Months = [ '','January','February','March','April','May','June','July','August','September','October','November','December' ]
    StartMonth = Months[ StartMonth ]
    EndMonth = Months[ EndMonth ]
    
    write_to_log( term + ' ' + StartYear + ' ' + StartMonth + ' ' + str( StartDay ) + ' ' + EndYear + ' ' + EndMonth + ' ' + str( EndDay ) )
    medicine_box = driver.find_element_by_id( 'medicine-name' )
    medicine_box.send_keys( 'COVID' )
    sleep( 2 )

    #Need to wait until it appears
    while( 1 ):
        try:
            all_medicines = driver.find_element_by_class_name( 'medicines-check-all' )
            all_medicines.click()
            break
        except:
            sleep( 2 )
            pass

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'start-year' )
    txt_el.click()
    txt_el.send_keys( Keys.CONTROL, 'a' )
    txt_el.send_keys( StartYear )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'start-month' )
    txt_el.click()
    #txt_el.send_keys( Keys.CONTROL, 'a' )
    txt_el.send_keys( StartMonth )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'start-day' )
    txt_el.click()
    txt_el.send_keys( Keys.UP * 31 )
    txt_el.send_keys( Keys.DOWN * ( StartDay - 1 ) )
    txt_el.send_keys( Keys.ENTER )

    #menu_sel = Select( txt_el )
    #menu_sel.select_by_visible_text( StartDay )
    #menu_sel.select_by_value( StartDay )
    #sleep( 1 )
    #menu_sel.select_by_index( StartDay - 1 )
    #txt_el.send_keys( Keys.ENTER )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'end-year' )
    txt_el.click()
    txt_el.send_keys( Keys.CONTROL, 'a' )
    txt_el.send_keys( EndYear )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'end-month' )
    txt_el.click()
    #txt_el.send_keys( Keys.CONTROL, 'a' )
    txt_el.send_keys( EndMonth )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'end-day' )
    txt_el.click()
    txt_el.send_keys( Keys.UP * 31 )
    txt_el.send_keys( Keys.DOWN * ( EndDay - 1 ) )
    txt_el.send_keys( Keys.ENTER )

    return


def mod_search_terms( term, StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay ):
    StartYear = str( StartYear )
    EndYear = str( EndYear )
    Months = [ '','January','February','March','April','May','June','July','August','September','October','November','December' ]
    StartMonth = Months[ StartMonth ]
    EndMonth = Months[ EndMonth ]
    
    write_to_log( term + ' ' + StartYear + ' ' + StartMonth + ' ' + str( StartDay ) + ' ' + EndYear + ' ' + EndMonth + ' ' + str( EndDay ) )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'start-year' )
    txt_el.click()
    txt_el.send_keys( Keys.CONTROL, 'a' )
    txt_el.send_keys( StartYear )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'start-month' )
    txt_el.click()
    #txt_el.send_keys( Keys.CONTROL, 'a' )
    txt_el.send_keys( StartMonth )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'start-day' )
    txt_el.click()
    txt_el.send_keys( Keys.UP * 31 )
    txt_el.send_keys( Keys.DOWN * ( StartDay - 1 ) )
    txt_el.send_keys( Keys.ENTER )

    #menu_sel = Select( txt_el )
    #menu_sel.select_by_visible_text( StartDay )
    #menu_sel.select_by_value( StartDay )
    #sleep( 1 )
    #menu_sel.select_by_index( StartDay - 1 )
    #txt_el.send_keys( Keys.ENTER )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'end-year' )
    txt_el.click()
    txt_el.send_keys( Keys.CONTROL, 'a' )
    txt_el.send_keys( EndYear )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'end-month' )
    txt_el.click()
    #txt_el.send_keys( Keys.CONTROL, 'a' )
    txt_el.send_keys( EndMonth )

    sleep( 1 )

    txt_el = driver.find_element_by_id( 'end-day' )
    txt_el.click()
    txt_el.send_keys( Keys.UP * 31 )
    txt_el.send_keys( Keys.DOWN * ( EndDay - 1 ) )
    txt_el.send_keys( Keys.ENTER )

    return





#Check the website
website  = 'http://apps.tga.gov.au/PROD/DAEN/daen-entry.aspx'

user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument( 'user-agent={' + user_agent + '}' )
options.add_argument( "--window-size=1500,800" )
options.add_argument( '--ignore-certificate-errors' )
options.add_argument( '--allow-running-insecure-content' )
options.add_argument( "--disable-extensions" )
options.add_argument( "--proxy-server='direct://'" )
options.add_argument( "--proxy-bypass-list=*" )
options.add_argument( "--start-maximized" )
options.add_argument( '--disable-gpu' )
options.add_argument( '--disable-dev-shm-usage' )
options.add_argument( '--no-sandbox' )
driver = webdriver.Chrome(
    executable_path = "C:\\Install Files\chromedriver.exe",
    options = options ) 

driver.get( website )


try:
    agree_btn = driver.find_element_by_id( 'disclaimer-accept' )
    agree_btn.click()
    #print( 'Clicking on accept' )
except: # selenium.common.exceptions.NoSuchElementException:
    pass


#FirstTime = 1


while( 1 ):
    StartYear = QueryDate.year
    StartMonth = QueryDate.month
    StartDay = QueryDate.day

    EndYear = StartYear
    EndMonth = StartMonth
    EndDay = StartDay

    #if( FirstTime ):
    search_terms( 'COVID', StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay )
        #FirstTime = 0
    #else:
        #mod_search_terms( 'COVID', StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay )



    #menu_sel = Select( txt_el )
    #menu_sel.select_by_visible_text( EndDay )
    #menu_sel.select_by_value( EndDay )
    #sleep( 1 )
    #menu_sel.select_by_index( EndDay - 1 )
    #txt_el.send_keys( Keys.ENTER )


    sleep( 1 )

    #write_to_log( 'testing' )

    #sys.exit()


    submit = driver.find_element_by_id( 'submit-button' )
    submit.click()


    menu_sel = Select( driver.find_element_by_id( 'ctl00_body_MedicineSummaryControl_cmbPageSelection' ) )
    menu_sel.select_by_visible_text( '500' )


    get_simple_info( StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay )

    get_medsummary_info( StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay )
    while( check_medsummary_next() ):
        get_medsummary_info( StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay )



    lor = driver.find_element_by_id( 'ctl00_body_TabPCL' )
    lor.click()

    menu_sel = Select( driver.find_element_by_id( 'ctl00_body_CaseListingControl_cmbPageSelection' ) )
    menu_sel.select_by_visible_text( '500' )

    get_listofreports_info( StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay )
    while( check_listofreports_next() ):
        get_listofreports_info( StartYear, StartMonth, StartDay, EndYear, EndMonth, EndDay )

    write_to_log( str( StartYear ) + ' ' + str( StartMonth ) + ' ' + str( StartDay ) + ' complete' )



    QueryDate = QueryDate + timedelta( days = 1 )
    if( QueryDate > EndDate ):
        break
    btn_newsearch = driver.find_element_by_class_name( 'new-search-button' )
    btn_newsearch.click()
    sleep( 1 )



driver.close()

