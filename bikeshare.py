import time
import pandas as pd
import numpy as np

#Dictionaries and lists to be used
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS_LISTED = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

MONTHS_NO_DATA = ['july', 'august', 'september', 'october', 'november', 'december']

DOW_LISTED = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
'saturday', 'sunday']

#Line to use between inputs/outputs
line = '/'*40

#This ascii art belongs to Chritopher Jhonsons
art_bike = """
                                           $"   *.
               d$$$$$$$P"                  $    J
                   ^$.                     4r  "
                   d"b                    .db
                  P   $                  e" $
         ..ec.. ."     *.              zP   $.zec..
     .^        3*b.     *.           .P" .@"4F      "4
   ."         d"  ^b.    *c        .$"  d"   $         %
  /          P      $.    "c      d"   @     3r         3
 4        .eE........$r===e$$$$eeP    J       *..        b
 $       $$$$$       $   4$$$$$$$     F       d$$$.      4
 $       $$$$$       $   4$$$$$$$     L       *$$$"      4
 4         "      ""3P ===$$$$$$"     3                  P
  *                 $       ¨"¨        b                J
   ".             .P                    %.             @
     %.         z*"                      ^%.        .r"
        "*==*""                             ^"*==*""

"""

#This ascii art belongs to josera@obelix.cica.es
bike = """
               __o
             _ |/<_
            (_)| (_)

        """

clock = """
        
            +====+
            |(::)|
            | )( |
            |(..)|
            +====+

        """

parked = """
                
              ___V
             _\  /_
            (_)  (_)

        """

calendar = """
            +------+
            +------+
            |      |
            |  27  |
            +------+

"""

error = '\nOpps! Sorry, something went wrong   :( \n'

#Function to filter through the user's input
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n'*2 + '*'*50 + '\n   Hello! Let\'s explore some US bikeshare data!\n' + '*'*50 + '\n'*2)
    print(art_bike)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input(">> Please select New York City, Chicago or Washington: ").lower()

    while city not in CITY_DATA:
        city = input(
        ">> Seems like that city is not on the list or was misspelled. Please try again: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(">> All months or an specific one?: ").lower()

    #Tell the user wether there's information or not for the month selected
    while month not in MONTHS_LISTED:
        if month in MONTHS_NO_DATA:
            month = input("There is no data for that month. Please select another one: ").lower()
        else:
            month = input(">> That doesn't seem to be a valid month. Please try again: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(">> All days of the weeks or an specific one?: ").lower()

    while day not in DOW_LISTED:
        day = input(">> That doesn't seem like a valid day of the week. Please try again: ").lower()

    return city, month, day
    print(line)


#Function to load the data from the CSV
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


#Function for date and time statistics
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('   TIME STATISTICS')

    #Visual breaker
    print(calendar)

    # TO DO: display the most common month
    try:
        print("   Most common month for rides is: {}".format(str(df['month'].mode().loc[0])) + '\n')
    except:
        print(error)

    # TO DO: display the most common day of week
    try:
        print("   Most common day of week: {}".format(str(df['day_of_week'].mode().loc[0]))+ '\n')
    except:
        print(error)


    # TO DO: display the most common start hour
    try:
        print("   Most common starting hour is: {}".format(str(df['hour'].mode().loc[0]))+ '\n')
    except:
        print(error)

    #Visual breaker
    print("\nThis took %s seconds." % (time.time() - start_time))
    print(line)


#Function for Stations statistics
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('   STATION STATISTICS')

    #Visual breaker
    print(parked)

    # TO DO: display most commonly used start station
    try:
        print('   Most common Start Station: {}'.format(str(df['Start Station'].mode().loc[0]))+ '\n')
    except:
        print(error)

    # TO DO: display most commonly used end station
    try:
        print('   Most common End Station: {}'.format(str(df['End Station'].mode().loc[0]))+ '\n')
    except:
        print(error)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']

    try:
        print('   Most common combination: {}'.format(str(df['combination'].mode().loc[0]))+ '\n')
    except:
        print(error)

    #Visual breaker
    print("\nThis took %s seconds." % (time.time() - start_time))
    print(line)


#Function for trip duration statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('   TRIP DURATION STATISTICS')

    #Visual breaker
    print(clock)

    #Travel's time deltas
    df['Time Delta'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # TO DO: display total travel time
    total_delta = df['Time Delta'].sum()

    try:
        print('   The total time traveled was: ', total_delta)
    except:
        print(error)

    # TO DO: display mean travel time
    mean_delta = df['Time Delta'].mean()

    try:
        print('   The mean time traveled was: ', mean_delta)
    except:
        print(error)

    #Visual breaker
    print("\nThis took %s seconds." % (time.time() - start_time))
    print(line)


#Function for user statistics
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('   USER STATISTICS')

    #Visual breaker
    print(bike)

    # TO DO: Display counts of user types
    try:
        print('The users types are:' + '\n' + '{}'.format(str(df['User Type'].value_counts())) + '\n' * 2 )
    except:
        print(error)

    # TO DO: Display counts of gender
    try:
        print('Gender distribution:' + '\n' + '{}'.format(str(df['Gender'].value_counts())) + '\n' * 2 )
    except:
        print(error)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The youngest rider was born in: {}'.format(int(df['Birth Year'].max())))
        print('The oldest rider was born in: {}'.format(int(df['Birth Year'].min())))
        print('Most riders have been born in: {}'.format(int(df['Birth Year'].mode())))
    except:
        print(error)

    #Visual breaker
    print("\nThis took %s seconds." % (time.time() - start_time))
    print(line)

#Function to display raw data
def raw_data(df):
    """Displays raw data in 5 lines chunks per the user request"""

    try:
        count = 5
        start = 0
        end = start + count
        row_count = len(df)

        print('   RAW DATA')
        print('\n' * 2, 'Total rows from the data base: ', row_count, '\n' * 2)
        
        print(format(str(df[start: end])))


        while end < row_count:

            continue_raw_data = input('>> Would you like to see more raw data? Answer Yes to continue: \n')

            if continue_raw_data.lower() == 'yes':

                start = end
                count = start + 5
                end = count

                print(format(str(df[start: end])))
            else:
                break
        else:    
            print('\n No more data to show \n')
    except:
        print(error)
            

#Main part of the code that condences all of the functions
def main():
    while True:

        
        city, month, day = get_filters()
        df = load_data(city, month, day)

        question_time_stats = input('\n>> Would you like to know about time statistics? Enter Yes to continue or No to skip to the following statistic: \n')
        if question_time_stats.lower() == 'yes':
            time_stats(df)

        question_stations_stats = input('\n>> Would you like to know about station statistics? Enter Yes to continue or No to skip to the following statistic: \n')
        if question_stations_stats.lower() == 'yes':
            station_stats(df)

        question_travel_stats = input('\n>> Would you like to know about travel statistics? Enter Yes to continue or No to skip to the following statistic: \n')
        if question_travel_stats.lower() == 'yes':
            trip_duration_stats(df)

        question_user_stats = input('\n>> Would you like to know about user statistics? Enter Yes to continue or No to skip to the following statistic: \n')
        if question_user_stats.lower() == 'yes':
            user_stats(df)

        question_raw_data = input('\n>> Would you like to see the raw data? Enter Yes to continue or No to skip: \n')
        if question_raw_data.lower() == 'yes':
            raw_data(df)

        restart = input('\n>> Would you like to restart? Enter yes or no: \n')
        if restart.lower() != 'yes':
            break

#Conditional on which it's printed on the terminal
if __name__ == "__main__":
    main()