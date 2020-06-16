import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10.0,5.0)

#reading data
salarydata=pd.read_csv('/content/june2020.csv')
print(salarydata.shape)
salarydata.head()

#collecting x and y
X=salarydata['Confirmed'].values
Y=salarydata['Recovered'].values

#mean of x and y
mean_x=np.mean(X)
mean_y=np.mean(Y)

#total number of values
n=len(X)

#using the formulla calculate m 
numerator_val =0
demonitor_val =0

for i in range(n):
  numerator_val += (X[i] - mean_x) * (Y[i] - mean_y)
  demonitor_val += (X[i] - mean_x) ** 2

m = numerator_val / demonitor_val
c = mean_y - (m * mean_x)

#print cofficient value
print('cofficient value', 'M = ' , m, 'c =', c, 'and X =', mean_x )

#plotting the graph

maximum_x = np.max(X) + 100
minimum_x = np.min(X) - 100

#calculating the lines values x and y

x= np.linspace(minimum_x,maximum_x,1000)
y = c + m*x
#print('linear line', 'Y =', y)

plt.title('COVID-19 India Statwise Data Analysis of Confirmed and Recovered Case' , color = 'white')
plt.plot(x, y, color = 'blue', label ='Regression Line')

#scatter point
plt.scatter(X, Y, c='black', label='Scatter Plot')

plt.xlabel('No of Confirmed cases in India statewise', color = 'white')
plt.ylabel('No of Recovered cases in India statewise', color = 'white')
plt.legend()
plt.show()



ss_t = 0
ss_r =0
for i in range(n):
  y_predict = c + m * X[i]
  ss_t += (Y[i] - mean_y) ** 2
  ss_r += (Y[i] - y_predict) ** 2

r_square = 1 - (ss_r / ss_t)

#print cofficient value
print('cofficient value and R sqaure measure', 'M = ' , m, 'c =', c, 'and X =', 
      mean_x) 
print('R_square=', r_square, 'prediction value=', y_predict)

plt.title('COVID-19 India Statwise Data Analysis of Confirmed and Recovered Case (Bar chart)' , color = 'white')
plt.bar(x, y, color = '#58b970', label ='Regression Line')
plt.plot(x, y, color = '#58b970', label ='Regression Line')
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

plt.xlabel('No of Confirmed cases in India statewise', color='white')
plt.ylabel('No of Recovered cases in India statewise', color='white')
plt.legend()
plt.show()