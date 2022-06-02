import csv
import numpy as np
import matplotlib.pyplot as plt

from pandas import *

data = open('covid19_cases_demographics.csv', 'r')
file = csv.DictReader(data)

total_deaths_feb_2021 = []
all_dates_feb_2021 = []

total_deaths_feb_2022 = []
all_dates_feb_2022 = []

for col in file:
    if col['demographic_category'] == 'Age Group':
        # if report_date == feb 2020 ->
        if col['report_date'][0:7] == '2021-02' and col['demographic_value'] == 'Total':
            total_deaths_feb_2021.append(int(col['deaths']))
            all_dates_feb_2021.append(int(col['report_date'][8:10]))
        if col['report_date'][0:7] == '2022-02' and col['demographic_value'] == 'Total':
            total_deaths_feb_2022.append(int(col['deaths']))
            all_dates_feb_2022.append(int(col['report_date'][8:10]))

print('Deaths of all Age Groups in Feb 2021:', total_deaths_feb_2021)
print('Feb 2021 Dates', all_dates_feb_2021)

print('Deaths of all Age Groups in Feb 2022:', total_deaths_feb_2022)
print('Feb 2022 Dates:', all_dates_feb_2022)


plot1 = plt.figure(1)

plt.xlabel('Feb. 2021')
plt.ylabel('COVID-19 Deaths')
plt.ticklabel_format(style='plain')
plt.xticks(all_dates_feb_2021)
plt.ylim(total_deaths_feb_2021[0], total_deaths_feb_2021[len(total_deaths_feb_2021) - 1])
plt.plot(all_dates_feb_2021, total_deaths_feb_2021, label="Feb. 2021 COVID 19 Deaths", linestyle='-.')

plot2 = plt.figure(2)
plt.xlabel('Feb. 2022')
plt.ylabel('COVID-19 Deaths')
plt.ticklabel_format(style='plain')
plt.xticks(all_dates_feb_2022)
plt.ylim(total_deaths_feb_2022[0], total_deaths_feb_2022[len(total_deaths_feb_2022) - 1])
plt.plot(all_dates_feb_2022, total_deaths_feb_2022, label="Feb. 2022 COVID 19 Deaths", linestyle='-.')

plt.legend()
plt.show()


