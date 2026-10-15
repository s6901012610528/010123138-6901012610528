# code run in Thonny Python 3.14.4
# W11 : Matplotlib
import matplotlib.pyplot as plt
# 4 weeks × 7 days

temperatures = [
    [30, 31, 32, 30, 30, 31, 33], # Week 1
    [29, 30, 31, 32, 31, 30, 29], # Week 2
    [31, 32, 33, 34, 32, 31, 30], # Week 3
    [30, 29, 30, 30, 29, 30, 32] # Week 4
    ]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for week in temperatures:
    plt.plot(days, week)
    
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.title("Temperature for 4 Weeks")
plt.legend(["Week 1", "Week 2", "Week 3", "Week 4"])

plt.show()