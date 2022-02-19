# Bike sharing data set
In this task you should check out the bike sharing data set (data/bike_sharing.csv) and answer 
the following questions:

1. Is any data missing or corrupted? How would you deal with this?
2. What is the most popular time to rent out bikes?
3. What is the most popular bike rental station?
4. Your manager wants to get a report of the weekly bike rental numbers over the whole data set.
How do you proceed?

## Data set column description
- datetime: hourly date + timestamp  
- season:  
  - 1 = spring 
  - 2 = summer
  - 3 = fall
  - 4 = winter 
- holiday: whether the day is considered a holiday
- workingday: whether the day is neither a weekend nor holiday
- weather: 
  - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
  - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
  - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
  - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog 
- temp: temperature in Celsius
- atemp: "feels like" temperature in Celsius
- humidity: relative humidity
- windspeed: wind speed
- casual: number of non-registered user rentals initiated
- registered: number of registered user rentals initiated
- count: number of total rentals
- rental_station_id: ID of the station where the bike was rented