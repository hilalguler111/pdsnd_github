import time
import pandas as pd
import numpy as np


CITY_DATA ={ 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_city():
    """
    Asks user to specify a city.

    Returns:
        (str) city - name of the city to analyze
    """
    while True:
        city = input("Let's first select a city! Which city would you like to analyze? "
                     "in: Chicago, New York City, or Washington?\n\n").strip().lower()
        if city in ('new york city', 'chicago', 'washington'):
            return city
        else:
            print("Please enter a valid city.")

def get_month(city):
    """
    Asks user to specify a month.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    while True:
        month = input("You can choose between January, February, March, April, May, June, or type all.\n\n").strip().lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            return month
        else:
            print("Please enter a valid month.")

def get_day():
    """
    Asks user to specify a day.

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while True:
        day = input("You can choose between Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or type all.\n\n").strip().lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            return day
        else:
            print("Please enter a valid day.")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = get_city()
    month = get_month(city)
    day = get_day()
    print('-'*40)
    return city, month, day


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
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday
    
    # Filter by month 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month.lower()) + 1
        # Filter DataFrame by month
        df = df[df['Month'] == month_index]
    
    # Filter by day 
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_index = days.index(day.lower()) 
        # Filter DataFrame by weekday
        df = df[df['Weekday'] == day_index]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    months_map = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June'
    }

    
    weekdays_map = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    # Display the most common month
    common_month = df['Month'].mode()[0]
    print('The most common month is:', months_map.get(common_month, common_month))

    # Display the most common day of week
    common_day_of_week = df['Weekday'].mode()[0]
    print('The most common day of the week is:', weekdays_map[common_day_of_week])

    # Display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start Hour'].mode()[0]
    print('The most common start hour is:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is', 
          df['Start Station'].value_counts().idxmax(), '.\n\n')


    # TO DO: display most commonly used end station
    print('The most common end station is', 
          df['End Station'].value_counts().idxmax(), '.\n\n')


    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' (start) and ' + df['End Station'] + ' (end).'
    
    
    most_common_station_combination = df['Station Combination'].value_counts().idxmax()
    print('The most common station combination for your selection is ', most_common_station_combination, '\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_trip_duration_hours = df['Trip Duration'].sum() / 3600
    print('The total travel time is', total_trip_duration_hours, 'hours.\n\n')

    # Display mean travel time
    mean_trip_duration_seconds = df['Trip Duration'].mean()
    mean_trip_duration_hours = mean_trip_duration_seconds / 3600
    print('The mean travel time is', mean_trip_duration_hours, 'hours.\n\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertypes = df['User Type'].values

    count_subscriber  = (usertypes == 'Subscriber').sum()
    count_customer = (usertypes == 'Customer').sum()

    print('The number of subscribers in', city.title(), 'is:',count_subscriber,'\n')
    print('The number of customers in', city.title(), 'is:',count_customer,'\n')


    # TO DO: Display counts of gender
    if city.title() != 'Washington':
        gender = df['Gender'].values
        count_male  = (gender == 'Male').sum()
        count_female = (gender == 'Female').sum()

        print('The number of male users in', city.title(), 'is:',count_male,'\n')
        print('The number of female users in', city.title(), 'is:',count_female,'\n')


    # TO DO: Display earliest, most recent, and most common year of birth
        birth_years = df['Birth Year'].dropna()
        latest_birthyear = birth_years.max()
        earliest_birthyear = int(birth_years.min())

        print('The most recent birth year of users in', city.title(), 'is:',
              latest_birthyear ,'\n')
        print('The earliest birth year of users in', city.title(), 'is:',
              earliest_birthyear,'\n')
        print('The most common birth year of users in', city.title(), 'is:', 
              df['Birth Year'].value_counts().idxmax(), '\n')
    else:
        # print message if Washington was chosen as city
        print('Sorry. Gender and birth year information are not available for Washington!')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    """Displays 5 lines of row data will added in each press"""
    print('Would you like to see 5 lines of raw data? Press enter, If you want to skip, enter no')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))

def raw_data(df):
    """ Displays 5 lines of raw data at a time when yes is selected."""
    # define index i, start at line 1
    i = 1
    while True:
        rawdata = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        #If user opts for it, this displays next 5 rows of data
    
        if rawdata.lower() == 'yes':
            
            print(df[i:i+5])
            i = i+5
        else:
            
            break





#Main function to call all the previous functions
def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
	main()
