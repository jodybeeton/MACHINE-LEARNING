import matplotlib.pyplot as plt
temperature = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
soup_sales = [220.00, 330.00, 190.00, 340.00, 410.00, 445.00, 415.00]
plt.scatter(temperature, soup_sales)
plt.title("Soup sales in relation to temperature.")
plt.xlabel("Temperature")
plt.ylabel("Price in (R)")
plt. plot(temperature + soup_sales)
plt.show()
