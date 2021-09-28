from numpy.core.fromnumeric import std
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
from pandas.core.accessor import CachedAccessor
import scipy.stats as st
from scipy.stats.stats import tstd
import statsmodels.stats.proportion as stm
import statsmodels.stats.weightstats as stm
import math


#read csv file into dataframe
df = pd.read_csv("last 6 months.csv")
print (df.info())


###1  coloumn_NSW
#taking only NSW column
sample1 = df["NSW"]

#Calculating the central Tendency of Data 


#descriptive statistics: mean,mode,median
median_of_NSW =stats.median(sample1)
mean_of_NSW = stats.mean(sample1)
mode_of_NSW = stats.mode(sample1)

#Variance and deviation
variance= stats.variance(sample1)
deviation= sample1.std(ddof=1)

#print the mean, mode and median of the NSW
#Print the varience and deviation for the sample
print("\nThe median value of NSW is: %.2f"%median_of_NSW)
print("\nThe mean value of NSW is: %.2f"%mean_of_NSW)
print("\nThe mode value of NSW is: %.2f"%mode_of_NSW)
print("\nThe variance in NSW is: %.2f"%variance)
print("\nThe deviation of NSW is %.2f"%deviation)

#range
max_ = max(sample1)
min_ = min(sample1)
range = max_ - min_
print("The range is",range)


# Q1 Quartile 1 of NSW,VIC,ACT,WA,TAS,SA,QLD and NT
print(df.quantile(q=(0.25,0.50,0.75)))

#Data Visualization


#histogram of NSW, median as central tendency
df1= df["NSW"].between(200,1603)
bin_width= 0.5
bin_count = int(median_of_NSW/bin_width)

#plot the histogram: median as central tendency
plt.hist(sample1,color="green",edgecolor= "black", bins = bin_count)
plt.title("Histogram of Number of Cases in NSW")
plt.xlabel("Number of cases")
plt.ylabel("NSW")
plt.show()


#inferential statistics
#total cases in a day in NSW state

#1: confidence interval
#taking sample of total cases of 26 random days in NSW

list_dates= ["13/04/2021","17/04/2021","22/04/2021","02/05/2021","10/05/2021","20/05/20212","29/05/2021"
             ,"5/06/2021","16/06/2021", "21/06/2021", "27/06/2021", "8/07/2021","16/07/2021","25/07/2021","31/07/2021",
             "4/08/2021","10/08/2021","15/08/2021","18/08/2021","19/08/2021" "22/08/2021",
             "25/08/2021","1/09/2021","9/09/2021","15/09/2021","26/09/2021"]

#taking the number of cases of 26 random days in NSW
sample2= np.array([5,7,7,3,6,2,1,0,3,7,32,38,98,234,360,417,634,684,830,921,1118,1471,1261,964])
                  

#compute the sample statistics
print("computing the basic statistics ...")
x_bar= st.tmean(sample2)
s=st.tstd(sample2)
n=len(sample2)
print(x_bar, s , n)


#z-score(assuming 95% confidence level)
z_score =st.norm.ppf(q=0.975)
print("z-statistic: %.2f" %z_score)

#compute standard error
std_err=s/math.sqrt(n)
print("std_err: %.2f" %std_err)

#compute the margin of error
mrg_err=z_score * std_err
print("mrg_err:%.2f"%mrg_err)


#confidence level
conf_lvl=0.95
    

#also'alpha'
sig_1v1= 1-conf_lvl

#degree of freedom
deg_free= 1-n


#calculating confidence interval of Total cases in a day in NSW
ci_low, ci_upp= stm._zconfint_generic(x_bar, std_err, alpha=0.05, alternative="two-sided")
print("The lower C.I is" , ci_low, "\nThe upper class C.I is:", ci_upp)


#perform one-sample t-test
#null hypothesis: population mean=379.29
#alternative hypothesis: population mean>379.29 (in the function below,note the argument 'greater')
t_stats, p_val = st.ttest_1samp(sample2, 379.29, alternative='greater')
print("\n computing t* ...")
print("\t t-statistic (t*): %.2f" % t_stats)

print("n computing p_valve ....")
print("\t p-value: %.4f" % p_val)


print("\n conclusion:")
if p_val<0.05:
    print ("\t we reject the null hypothesis.")
else:
    print("\t we accept the null hypothesis")



              
    
