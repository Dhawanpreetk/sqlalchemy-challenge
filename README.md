# Sqlalchemy-Challenge

This Challenge is about long holiday vacation in Honolulu, Hawaii. To help with the trip planning, we are to do a climate analysis about the area. The following sections outline the steps that are taken to accomplish this task.

# Precipatation Analaysis
In this section, I have used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, using SQLAlchemy ORM queries, Pandas, and Matplotlib. I have complete the following steps:
Used the SQLAlchemy create_engine() function to connect to your SQLite database.
Used the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
Linked Python to the database by creating a SQLAlchemy session.


Performed the following steps: 

1.Find the most recent date in the dataset.

2.Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

3.Select only the "date" and "prcp" values.

4.Load the query results into a Pandas DataFrame. Explicitly set the column names.

5.Sort the DataFrame values by "date".

6.Plot the results by using the DataFrame plot method, as the following image shows:

<img width="467" alt="image" src="https://github.com/Dhawanpreetk/sqlalchemy-challenge/assets/130263833/a8fe4784-57ff-4aec-b9d5-fc9a6d15a5b7">


# Station Analysis : Instructions 

1.Design a query to calculate the total number of stations in the dataset.

2.Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

3.List the stations and observation counts in descending order.

4.Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

5.Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

6.Filter by the station that has the greatest number of observations.

7.Query the previous 12 months of TOBS data for that station.

8.Plot the results as a histogram with bins=12, as the following image shows:

<img width="482" alt="image" src="https://github.com/Dhawanpreetk/sqlalchemy-challenge/assets/130263833/0d494ea8-89b4-4aac-8b0b-16f0cd7fd104">


# Second part of the challenge is Designing the Climate App

Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

/
1.Start at the homepage.
List all the available routes.

2./api/v1.0/precipitation
Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.

3./api/v1.0/stations
Return a JSON list of stations from the dataset.

4./api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.

5./api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


This concludes the challenge.
