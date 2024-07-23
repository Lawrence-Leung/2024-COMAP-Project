import matplotlib.pyplot as plt

food_Abundance = [14.7, 20.6, 13.2, 10.6, 12.5, 13.6, 5.1, 3, 0.9, 1, 0.65, 0, 9]
months = ['May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May']

plt.bar(months, food_Abundance)
plt.xlabel('Months')
plt.ylabel('Food Abundance')
plt.title('Food Abundance by Month')
plt.xticks(rotation=45)
plt.show()
