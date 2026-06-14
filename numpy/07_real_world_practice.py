import numpy as np

# Scenario: Analyzing Weekly Temperatures
# Imagine we have temperature data for 4 different cities over 7 days.
np.random.seed(42) # For consistent results
temps = np.random.randint(20, 40, (4, 7))

cities = ["New York", "London", "Tokyo", "Mumbai"]
print("Temperature Matrix (Cities x Days):\n", temps)

# 1. Average temperature per city
avg_temps = temps.mean(axis=1)
for city, avg in zip(cities, avg_temps):
    print(f"{city} Average Temp: {avg:.2f}°C")

# 2. Find the hottest day overall
max_temp = temps.max()
day_idx = np.unravel_index(temps.argmax(), temps.shape)
print(f"\nHottest Temp recorded: {max_temp}°C in {cities[day_idx[0]]} on Day {day_idx[1]+1}")

# 3. Normalizing Data (Feature Scaling)
# Formula: (x - min) / (max - min)
normalized_temps = (temps - temps.min()) / (temps.max() - temps.min())
print("\nNormalized Temperatures (0 to 1 range):\n", normalized_temps)

# 4. Data Cleaning: Handling "Outliers"
# Let's say any temp > 38 is considered a "Heatwave"
heatwave_days = temps[temps > 38]
print("\nHeatwave temperatures recorded:", heatwave_days)

# 5. Transposing for analysis by day
daily_stats = temps.T
print("\nDay 1 temps across all cities:", daily_stats[0])
