#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# # question 01

# In[2]:


import pandas as pd


# In[10]:


df=pd.read_csv('flight_price.csv')


# In[40]:


df


# In[41]:


import pandas as pd

# assuming df is your pandas DataFrame
print(df.columns)


# In[42]:


df.shape


# # question 02

# In[43]:


import matplotlib.pyplot as plt


# In[44]:


varible=df['Price']


# In[45]:


plt.hist(varible,bins=10)
plt.show()


# # question 03

# In[58]:


import pandas as pd

# assuming df is your pandas DataFrame
summary = df.describe()
print("Range of the DataFrame:")
print(summary.loc['min', :] , "to", summary.loc['max', :])


# # question 05

# In[59]:


import pandas as pd
import matplotlib.pyplot as plt

# assuming df is your pandas DataFrame and 'Airline' and 'Price' are the names of the columns you want to analyze
df.boxplot(column='Price', by='Airline', figsize=(10,6))
plt.xlabel('Airline')
plt.ylabel('Price')
plt.title('Price of Flights by Airline')
plt.suptitle('')
plt.show()


# # question 06

# In[60]:


import matplotlib.pyplot as plt

# assuming df is your pandas DataFrame and 'Price' is the name of the column you want to analyze
plt.boxplot(df['Price'])
plt.ylabel('Price')
plt.title('Boxplot of Flight Prices')
plt.show()


# In[ ]:





# In[57]:


import pandas as pd

df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'])
df['Year'] = df['Date_of_Journey'].dt.year
df['Month'] = df['Date_of_Journey'].dt.month
month_year_group = df.groupby(['Year', 'Month'])
mean_price = month_year_group['Price'].mean()
num_flights = month_year_group.size()

Q6. You are working for a travel agency, and your boss has asked you to analyze the Flight Price dataset
to identify the peak travel season. What features would you analyze to identify the peak season, and how
would you present your findings to your boss?
To identify the peak travel season from the Flight Price dataset, I would analyze the following features:

Date of the Flight: I would look at the data for the entire year to see which months have the highest average ticket prices.

Destination: I would analyze the data by destination to see which locations have the highest ticket prices and during which time of the year.

Airlines: I would analyze the data by airline to see which airlines have the highest ticket prices and during which time of the year.

Holidays and Events: I would analyze the data to see which holidays and events have the highest ticket prices.

Flight Route: I would analyze the data to see which flight routes have the highest ticket prices.

After analyzing these features, I would present my findings to my boss in the form of a report, including the following information:

The months with the highest average ticket prices.

The top destinations with the highest ticket prices and the months during which they are the highest.

The top airlines with the highest ticket prices and the months during which they are the highest.

The holidays and events that have the highest ticket prices.

The top flight routes with the highest ticket prices.

Additionally, I would recommend the following to my boss based on my findings:

Increase marketing efforts during the peak season to attract more customers.

Offer discounts during the off-season to attract customers.

Consider adding new destinations or routes during the peak season to increase revenue.
# # question 07

# In[62]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Flight Price dataset into a pandas DataFrame
flight_data = pd.read_csv("flight_prices.csv")

# Identify trends in flight prices based on date of the flight
flight_data['Date_of_Flight'] = pd.to_datetime(flight_data['Date_of_Flight'])
flight_data.set_index('Date_of_Flight', inplace=True)
monthly_avg = flight_data.groupby(pd.Grouper(freq='M')).mean()
plt.plot(monthly_avg['Price'])
plt.xlabel('Date of the Flight')
plt.ylabel('Average Ticket Price')
plt.title('Trends in Flight Prices over Time')
plt.show()

# Identify trends in flight prices based on destination
destination_avg = flight_data.groupby('Destination')['Price'].mean()
destination_avg.plot(kind='bar')
plt.xlabel('Destination')
plt.ylabel('Average Ticket Price')
plt.title('Average Ticket Prices by Destination')
plt.show()

# Identify trends in flight prices based on airline
airline_avg = flight_data.groupby('Airline')['Price'].mean()
airline_avg.plot(kind='bar')
plt.xlabel('Airline')
plt.ylabel('Average Ticket Price')
plt.title('Average Ticket Prices by Airline')
plt.show()

# Identify trends in flight prices based on flight route
flight_route_avg = flight_data.groupby('Flight_Route')['Price'].mean()
flight_route_avg.plot(kind='bar')
plt.xlabel('Flight Route')
plt.ylabel('Average Ticket Price')
plt.title('Average Ticket Prices by Flight Route')
plt.show()

# Identify trends in flight prices based on duration of the flight
flight_data['Duration'] = flight_data['Arrival_Time'] - flight_data['Departure_Time']
duration_avg = flight_data.groupby('Duration')['Price'].mean()
duration_avg.plot(kind='line')
plt.xlabel('Duration of Flight')
plt.ylabel('Average Ticket Price')
plt.title('Average Ticket Prices by Duration of Flight')
plt.show()

# Identify trends in flight prices based on the day of the week
flight_data['Day_of_Week'] = flight_data['Date_of_Flight'].dt.day_name()
day_avg = flight_data.groupby('Day_of_Week')['Price'].mean()
sns.barplot(x=day_avg.index, y=day_avg.values)
plt.xlabel('Day of the Week')
plt.ylabel('Average Ticket Price')
plt.title('Average Ticket Prices by Day of the Week')
plt.show()


# In[63]:


import pandas as pd

# Load the data into a Pandas DataFrame
df = pd.read_csv('flight_price_dataset.csv')

# Explore the data
print(df.head())
print(df.info())
print(df.describe())
import matplotlib.pyplot as plt

# Create a scatter plot of departure time vs. flight price
plt.scatter(df['Departure Time'], df['Flight Price'])
plt.title('Departure Time vs. Flight Price')
plt.xlabel('Departure Time')
plt.ylabel('Flight Price')
plt.show()


# # question 09

# In[64]:


import pandas as pd

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Print the dimensions of the DataFrame
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])


# # question 10
Q10. How does the rating of apps vary by category? Create a boxplot to compare the ratings of different 
app categories.
# In[66]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Create a boxplot to compare the ratings of different app categories
df.boxplot(column=['Rating'], by=['Category'], figsize=(10,8))
plt.title('Rating of Apps by Category')
plt.xlabel('Category')
plt.ylabel('Rating')
plt.xticks(rotation=90)
plt.show()


# # question 11

# In[67]:


import pandas as pd

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Count the number of missing values in each column
print(df.isnull().sum())


# # question 012

# In[68]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Create a scatter plot of the rating vs. size of the app
plt.scatter(df['Size'], df['Rating'], alpha=0.5)
plt.title('Rating vs. Size of App')
plt.xlabel('Size of App (in MB)')
plt.ylabel('Rating')
plt.show()


# # question 13

# In[69]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Compute the mean price for each app type
mean_prices = df.groupby('Type')['Price'].mean()

# Create a bar chart of the mean prices by app type
mean_prices.plot(kind='bar', rot=0)
plt.title('Average Prices by App Type')
plt.xlabel('App Type')
plt.ylabel('Average Price')
plt.show()


# # question 14

# In[ ]:


import pandas as pd

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Convert the 'Installs' column to numeric format
df['Installs'] = pd.to_numeric(df['Installs'].str.replace('[+,]', ''))

# Create a frequency table of the number of installs for each app
freq_table = df[['App', 'Installs']].groupby('App').sum().sort_values(by='Installs', ascending=False)

# Display the top 10 most popular apps
top_10 = freq_table.head(10)
print(top_10)


# # question 15

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Convert the 'Installs' column to numeric format
df['Installs'] = pd.to_numeric(df['Installs'].str.replace('[+,]', ''))

# Group the data by the 'Category' column and compute the sum of the 'Installs' column for each category
category_installs = df.groupby('Category')['Installs'].sum()

# Sort the resulting frequency table in descending order of the number of installs
category_installs_sorted = category_installs.sort_values(ascending=False)

# Create a bar chart of the most popular app categories
category_installs_sorted.plot(kind='bar')
plt.title('Most Popular App Categories')
plt.xlabel('App Category')
plt.ylabel('Total Installs')
plt.show()


# # question 16

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Group the data by the 'Developer' column and count the number of apps published by each developer
apps_per_developer = df.groupby('Developer')['App'].count()

# Sort the resulting frequency table in descending order of the number of apps published
apps_per_developer_sorted = apps_per_developer.sort_values(ascending=False)

# Create a bar chart of the number of apps published by each developer
apps_per_developer_sorted[:10].plot(kind='bar')
plt.title('Top 10 Developers by Number of Apps Published')
plt.xlabel('Developer')
plt.ylabel('Number of Apps')
plt.show()

# Group the data by the 'Developer' column and compute the average rating and total installs for each developer
developer_stats = df.groupby('Developer').agg({'Rating': 'mean', 'Installs': 'sum'})

# Create a scatter plot of the average rating of apps published by each developer against the number of installs
plt.scatter(developer_stats['Rating'], developer_stats['Installs'])
plt.title('Developer Success by App Rating and Installs')
plt.xlabel('Average App Rating')
plt.ylabel('Total Installs')
plt.show()

# Create a box plot of the price of apps published by each developer
df.boxplot(column='Price', by='Developer')
plt.title('App Prices by Developer')
plt.xlabel('Developer')
plt.ylabel('App Price')
plt.show()


# # question 17

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the Google Playstore dataset into a Pandas DataFrame
df = pd.read_csv('googleplaystore.csv')

# Convert the 'Last Updated' column to datetime format
df['Last Updated'] = pd.to_datetime(df['Last Updated'])

# Create a new column with the month of the 'Last Updated' column
df['Month'] = df['Last Updated'].dt.month

# Group the data by the month and compute the total installs and average rating for each month
monthly_stats = df.groupby('Month').agg({'Installs': 'sum', 'Rating': 'mean'})

# Create a line chart of the number of installs by month
monthly_stats['Installs'].plot()
plt.title('App Installs by Month')
plt.xlabel('Month')
plt.ylabel('Total Installs')
plt.show()

# Create a line chart of the average rating by month
monthly_stats['Rating'].plot()
plt.title('App Rating by Month')
plt.xlabel('Month')
plt.ylabel('Average Rating')
plt.show()

# Group the data by the month and app category and compute the total installs for each month and category
category_stats = df.groupby(['Month', 'Category']).agg({'Installs': 'sum'})

# Create a stacked bar chart of the popularity of different app categories by month
category_stats.unstack()['Installs'].plot(kind='bar', stacked=True)
plt.title('App Category Popularity by Month')
plt.xlabel('Month')
plt.ylabel('Total Installs')
plt.show()

