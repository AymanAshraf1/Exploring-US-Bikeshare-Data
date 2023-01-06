
import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_list = ['chicago' , 'new york city' , 'washington']

    city = input("please select City to get a statistics on (chicago , new york city , or washington): ")
    city = city.lower()

    while city not in city_list :
        city = input(" Wrong input please type the correct city (chicago , new york city , or washington): ")
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june','all']

    month = input("please select a month to get a statistics on (ex:january, february, march...  MAX june) or \"all\" for every month: ")
    month = month.lower()

    while month not in month_list :
        month = input(" Wrong input please type the correct month or type \"all\": ")
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ,'all']

    day = input("please select a day to get a statistics on (ex: monday, tuesday, wednesday...) or \"all\" for every day: ")
    day = day.lower()

    while day not in day_list :
        day = input(" Wrong input please type the correct day or type \"all\": ")
        day = day.lower()

    

    print('-'*40)
    return city, month.title(), day.title()



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'All':
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

        
    # get user input to view data
    user_input = input("please type yes to view 5 lines of raw data, otherwise type no: ")
    user_input.lower()

    i = 0
    if user_input == "yes":
        while i in range(5):
            print(df.iloc[[i]])
            i += 1
            user_new_input = input("do you want to continue ? yes/no: ")
            user_new_input.lower()
            if user_new_input != 'yes':
                user_input = 'no'
                break
        



    return df


def time_stats(df,city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is: ' + df['month'].mode()[0] + '\n')

    # display the most common day of week
    print('The most common day of week is: ' + df['day_of_week'].mode()[0] + '\n')

    # display the most common start hour
    print('The most common start hour is: ' + str(df['hour'].mode()[0]) + '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most start station is: ' + df['Start Station'].mode()[0] + '\n')

    # display most commonly used end station
    print('The most end station is: ' + df['End Station'].mode()[0] + '\n')

    # display most frequent combination of start station and end station trip
    print('The most common combination of start station and end station trip: ' + (df['End Station'] + ' and ' + df['Start Station']).mode()[0] + '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum(axis=0)
    print('total travel time in hours is: ' + str(total_travel/3600) + '\n')

    # display mean travel time
    total_travel = df['Trip Duration'].mean(axis=0)
    print('mean travel time in minute is: ' + str(total_travel/60) + '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The counts of user types is: ' + '\n' + df['User Type'].value_counts().to_string() + '\n')     

    # Display counts of gender
    if city != 'washington':
        print('The counts of gender is: ' + '\n' + df['Gender'].value_counts().to_string() + '\n')

     
     
    

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('The earliest year of birth is: ' + str(df['Birth Year'].min(axis=0)) + '\n') 
        print('The most recent year of birth is: ' + str(df['Birth Year'].max(axis=0)) + '\n')
        print('The most common year of birth is: ' + str(df['Birth Year'].mode()[0]) + '\n')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,city)
        station_stats(df,city)
        trip_duration_stats(df,city)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
