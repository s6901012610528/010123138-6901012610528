# code run in Thonny Python 3.14.4
# W14 : Pie chart
import matplotlib.pyplot as plt

hobbies = ['Gaming', 'Reading', 'Exercise', 'Gardening']
hours = [10, 6, 5, 3]

plt.pie( hours, labels=hobbies)

plt.title('Weekly Time Spent on Hobbies')

plt.show()