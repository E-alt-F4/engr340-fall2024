import sys
import pandas
import numpy

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state,str(fips), int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    Rockingham_County_first_case = None #Set variable for first case to be empty string value
    Harrisonburg_first_case = None #Set variable for first case to be empty string value
    for (date, county, state, fips, cases, deaths) in data: #iterate through the list with the different values already split and established
        if Rockingham_County_first_case == None and county == 'Rockingham' and state == 'Virginia' and cases > 0: #find first date by only searching for a value if the variable is empty which would only be the first value
            #Also searches for the county Rockingham because Virginia districts are dumb, only in the state of Virginia, when cases raise above 0
            Rockingham_County_first_case = date #Set the variable equal to the date of which it happens
            print('First COVID case in Rockingham County happened on', Rockingham_County_first_case) #Print when the first COVID case in Rockingham County happened

        if Harrisonburg_first_case == None and county == 'Harrisonburg city' and cases > 0: #find first date by searching for a value if the variable is empty which would only be the first COVID case date
            #Also searches for cases in Harrisonburg city, no need for any other identifier because there is no other Harrisonburg City(I hope), when cases raise above 0
            Harrisonburg_first_case = date #Set the variable equal to the date of which it happens
            print('First COVID Case in Harrisonburg happened on', Harrisonburg_first_case) #Print when the first COVID case in Harrisonburg city happened

        if Rockingham_County_first_case and Harrisonburg_first_case: #once a date is found for both variables break the loop
            break
    return Rockingham_County_first_case, Harrisonburg_first_case #return dates

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    greatest_number_cases_Harrisonburg = 0 #value for the highest number of cases in Harrisonburg
    greatest_number_cases_Rockingham_County = 0 #value for the highest number of cases in Rockingham County

    Harrisonburg_date = None #date with the greatest number of cases in Harrisonburg
    Rockingham_County_date = None #date with the greatest number of cases in Rockingham County

    cases_harrisonburg = None #incrementing case number across entire data set for Harrisonburg, used to compare number of cases
    cases_rockingham = None #incrementing case number across entire data set for rockingham county

    for (date, county, state, fips, cases, deaths) in data: #iterate through list
        if county == 'Harrisonburg city':  #Searching for only Harrisonburg cases
            if cases_harrisonburg != None: #Starts going through the data set, this line prevents the code from getting stuck
                # using cases_harrisonburg=None did not work because it would never break out of the first comparison
                newcase_harrisonburg = cases - cases_harrisonburg #new value created that is the difference in cases between two days
                if newcase_harrisonburg > greatest_number_cases_Harrisonburg: #compare new value to previous greatest number of cases
                    greatest_number_cases_Harrisonburg = newcase_harrisonburg #store new greatest value until final greatest value is found
                    Harrisonburg_date = date #also attach the date for which that greatest increase in cases occurred
            cases_harrisonburg = cases  #store the first value to be compared against next value in list and repeat through entire list
        #repeating same process but for Rockingham county, dates end up being similar which makes sense as that must be peak COVID in the same area
        if county == 'Rockingham' and state =='Virginia': #searching for only Rockingham county, virginia
            if cases_rockingham != None:
                newcase_rockingham = cases - cases_rockingham
                if newcase_rockingham > greatest_number_cases_Rockingham_County:
                    greatest_number_cases_Rockingham_County = newcase_rockingham
                    Rockingham_County_date = date
            cases_rockingham = cases #similar process to the pi assignment, where the variable is used to continue the comparison and repeat the iteration

    print('The greatest number of cases in a singular day in Harrisonburg was', greatest_number_cases_Harrisonburg,'on', Harrisonburg_date)
    print('The greatest number of cases in a singular day in Rockingham County was', greatest_number_cases_Rockingham_County,'on', Rockingham_County_date)
    return greatest_number_cases_Rockingham_County, Harrisonburg_date, greatest_number_cases_Rockingham_County, Rockingham_County_date
    #440 and 323 seem like low numbers but perhaps COVID was just blown out of proportion by mainstream media

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    cases_harrisonburg = None #create empty value for cases in harrisonburg, used as reference to iterate through all dates
    harrisonburg_cases = [] #empty array to create an array for all dates and number of cases in harrisonburg
    cases_rockingham = None #create empty value for cases in rockingham, used as reference to iterate through all dates
    rockingham_cases = []  #empty array to create an array for all dates and number of cases in rockingham

    max_harrisonburg_7day = 0 #max number of cases in harrisonburg across any given 7 day window
    max_rockingham_7day = 0 #max number of cases in rockingham across any given 7 day window

    #for loop used to create two arrays consisting of all cases data for every date in both locations
    for (date, county, state, fips, cases, deaths) in data:
        if county == 'Harrisonburg city':  #Searching for only Harrisonburg cases
            if cases_harrisonburg != None: #for any data that exist run through state conditions
                increase_cases_harrisonburg = cases - cases_harrisonburg #create value for difference in cases between each date
                harrisonburg_cases =numpy.array([date,increase_cases_harrisonburg]) #store date and number of cases in new array
            cases_harrisonburg = cases #stores values and reuses them for next comparison throughout entire list
            #print(harrisonburg_cases) #used to just see the array data
        if county == 'Rockingham' and state == 'Virginia':
            if cases_rockingham != None:
                increase_cases_rockingham = cases - cases_rockingham
                rockingham_cases =numpy.array([date, increase_cases_rockingham])
            cases_rockingham =cases
            #print(rockingham_cases) #used to see the array data

    for i in range(len(harrisonburg_cases)): #iterate over the entire length of the array
        harrisonburg_7day = 1 #sum(harrisonburg_cases(some function) #function that creates a sum of all possible 7-day windows that will run through entire list
        #also needs to split up array data and reference date and case number separately
        if harrisonburg_7day > max_harrisonburg_7day: #compare previous maximum to next week until max week is found in list
            max_harrisonburg_7day = harrisonburg_7day #store new max as the maximum 7-day case sum
            start_week_harrisonburg = harrisonburg_cases#(function to reference first value in attached data set) #start of week using the first value of 7-day week index created in for loop
            end_week_harrisonburg = harrisonburg_cases#(function to reference first value in attached data set) #end of week using last value of 7-day week index created in for loop

    for i in range(len(rockingham_cases)):
        rockingham_7day = 1 #sum(rockingham_cases(some function) #sum function across 7 day range
        if rockingham_7day > max_rockingham_7day:
            max_rockingham_7day = rockingham_7day
            start_week_rockingham = rockingham_cases#(function to reference first value in attached data set) #cases value at the first index of the 7-day week
            end_week_rockingham = rockingham_cases#(function to reference first value in attached data set) #cases value at the last index of the 7-day week


    print('The worst seven-day period in Harrisonburg was between',start_week_harrisonburg,'and',end_week_harrisonburg)
    print('The worst seven-day period in Rockingham county was between', start_week_rockingham,'and',end_week_rockingham)
    return harrisonburg_cases, rockingham_cases, max_harrisonburg_7day, max_rockingham_7day, start_week_harrisonburg, start_week_rockingham, end_week_harrisonburg, end_week_rockingham

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

   # for (date, county, state, fips, cases, deaths) in data:
       # print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


