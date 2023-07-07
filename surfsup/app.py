# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///hawaii.sqlite")

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
#measurement = Base.classes.hawaii_measurements
#station= Base.classes.hawaii_stations

measurements = Base.classes.measurement
Stations = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/trip/<start_date>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
  # Create our session (link) from Python to the D

    """Return a list of """
    # Query all passengers
    results = session.query(measurements.date, measurements.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_prcp_data = []
    for date,prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        
        all_prcp_data.append(prcp_dict)

    return jsonify(all_prcp_data)

@app.route("/api/v1.0/stations")
def stations():

    """Return a list of """
    # Query all stations
    result = session.query(Stations.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(result))

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tobs():

    """Return a list of """
    # Query all stations
    previous_temp_data = session.query(measurements.date, measurements.tobs).\
                    filter(measurements.date >= (dt.date(2017, 8, 23) - dt.timedelta(days=365) )).\
                    filter(measurements.station=='USC00519281').all()

    session.close()

    # Convert list of tuples into normal list
    all_temps = list(np.ravel(previous_temp_data))

    return jsonify(all_temps)

@app.route("/api/v1.0/trip/<start_date>")
def trip(start_date, end_date='2017-08-23'):
    # Calculate minimum, average and maximum temperatures for the range of dates starting with start date.
    # If no end date is provided, this will be the end date 2017-08-23.
    query_result = session.query(func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)).\
        filter(measurements.date >= start_date).filter(measurements.date <= end_date).all()
    session.close()

    stats = []
    for min, avg, max in query_result:
        dict = {}
        dict["Min"] = min
        dict["Average"] = avg
        dict["Max"] = max
        stats.append(dict)

    # If the query returned non-null values return the results,
    # otherwise return an error message
    if dict['Min']: 
        return jsonify(stats)
    else:
        return jsonify({"error": f"Date {start_date} not found or not formatted as YYYY-MM-DD."}), 404
  


if __name__ == "__main__":
    app.run(debug=True)