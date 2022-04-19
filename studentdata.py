import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff

df=pd.read_csv("C:/Users/Hp/Desktop/White HAt Junior/PYTHON/Project 109/StudentsPerformance.csv")
Read_Score=df["readingscore"].to_list()

Reading_Mean= statistics.mean(Read_Score)
Reading_Median=statistics.median(Read_Score)
Reading_Mode=statistics.mode(Read_Score)

print("Mean,Median,Mode of Reading Score is {},{},{}".format(Reading_Mean,Reading_Median,Reading_Mode))

Reading_stddev=statistics.stdev(Read_Score)

First_Start_Reading_stdev,First_End_Reading_stdev=Reading_Mean-Reading_stddev,Reading_Mean+Reading_stddev
Sec_Start_Reading_stdev,Sec_End_Reading_stdev=Reading_Mean-(2*Reading_stddev),Reading_Mean+(2*Reading_stddev)
Third_Start_Reading_stdev,Third_End_Reading_stdev=Reading_Mean-(3*Reading_stddev),Reading_Mean+(3*Reading_stddev)

thin_1_stddev= [result for result in Read_Score if result > First_Start_Reading_stdev and result < First_End_Reading_stdev]
thin_2_stddev= [result for result in Read_Score if result > Sec_Start_Reading_stdev and result < Sec_End_Reading_stdev]
thin_3_stddev= [result for result in Read_Score if result > Third_Start_Reading_stdev and result < Third_End_Reading_stdev]

print("{}% of Data lies Within Read_First_stdev". format(len(thin_1_stddev)*100.0/len(Read_Score)))
print("{}% of Data lies Within Read_Sec_stdev". format(len(thin_2_stddev)*100.0/len(Read_Score)))
print("{}% of Data lies Within Read_Third_stdev". format(len(thin_3_stddev)*100.0/len(Read_Score)))

fig=ff.create_distplot([Read_Score],["readingscore"],show_hist=False)
fig.show()