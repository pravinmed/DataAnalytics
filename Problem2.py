import pandas
import pandasql


def num_rainy_days(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return one column and
    one row - a count of the number of days in the dataframe where
    the rain column is equal to 1 (i.e., the number of days it
    rained).  The dataframe will be titled 'weather_data'. You'll
    need to provide the SQL query.  You might find SQL's count function
    useful for this exercise.  You can read more about it here:
    
    https://dev.mysql.com/doc/refman/5.1/en/counting-rows.html
    
    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply 
    where maxtempi = 76.
    
    You can see the weather data that we are passing in below:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)

    q = "select count(*) from weather_data where rain == 1"

    #The SQL query should return two columns and
    #two rows - whether it was foggy or not (0 or 1) and the max
    #maxtempi for that fog value (i.e., the maximum max temperature
    #for both foggy and non-foggy days).

    q2= "select fog,max(maxtempi) from weather_data group by fog "


##    The SQL query should return one column and
##    one row - the average meantempi on days that are a Saturday
##    or Sunday (i.e., the the average mean temperature on weekends).
##    The dataframe will be titled 'weather_data' and you can access
##    the date in the dataframe via the 'date' column.
    
    q3 = "select avg(meantempi) as avg from weather_data where cast(strftime('%w',date) as integer) == 0 or cast(strftime('%w',date) as integer) == 6"


##    This function should run a SQL query on a dataframe of
##    weather data. More specifically you want to find the average
##    minimum temperature (mintempi column of the weather dataframe) on 
##    rainy days where the minimum temperature is greater than 55 degrees.
    
    q4 = "select avg(mintempi) as average from weather_data where cast(mintempi as integer) >55 and rain ==1"

    
    #your query here
    
    print q
    #Execute your SQL command against the pandas frame
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days
