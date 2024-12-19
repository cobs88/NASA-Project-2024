import matplotlib.pyplot as plt
import numpy as np

# Data setup (Input your own data here)
plants = ['Spinach', 'Kale', 'Soybeans', 'Potatoes', 'Strawberries']
growth_rate = [30, 35, 50, 70, 40]  # Growth rate (days to harvest)
yield_per_area = [3.5, 4.0, 6.0, 5.0, 2.5]  # Yield per square meter (kg)
water_usage = [1.2, 1.1, 1.8, 1.5, 1.0]  # Water usage per kg (liters)
nutritional_value = [9, 8.5, 7, 6, 9.5]  # Nutritional value (arbitrary scale)

# ----- Bar Chart: Growth Rate Comparison -----
plt.figure(figsize=(10, 5))
plt.bar(plants, growth_rate, color='purple')
plt.title('Growth Rate Comparison of Plants (Days to Harvest)')
plt.xlabel('Plants')
plt.ylabel('Days to Harvest')
plt.savefig('/home/cobs/Documents/NASA-Project-2024-1/growth_rate_comparison.png')  # Save the figure
plt.close()