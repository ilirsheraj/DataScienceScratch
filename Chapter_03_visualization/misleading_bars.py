import matplotlib.pyplot as plt


mentions = [500, 505]
years = [2017, 2018]
plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times i heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Look at the 'huge' increase")
plt.show()

# Same data without manipulating the y-axis
plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times i heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)
#plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Not such a big difference")
plt.show()
