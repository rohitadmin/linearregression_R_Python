#simple linear regression

#importing salary dataset
library(readr)
salarydata = read.csv("D:/datascience/r practice/linear regression/salarydata.csv")
View(salarydata)


#splitting the salary dataset into a training set and test set
#install.packages('caTools')

library(caTools)
set.seed(123)
split = sample.split(salarydata$Salary,SplitRatio=2/3)
training_set=subset(salarydata, split==TRUE)
test_set=subset(salarydata, split==FALSE)

#pointing the simple linear regression of  training data set
regressor =lm(formula = Salary ~ YearsExperience, data = training_set)

summary(regressor)

#predicted the test data set 
Y_predicted = predict(regressor, newdata = test_set)

summary(Y_predicted)

#visualization of Employee salary Training set data
#install.packages('ggplot2')

library(ggplot2)

ggplot() + 
  geom_point(aes(x=training_set$YearsExperience, y= training_set$Salary),
                 colour = 'red') +
  geom_line(aes(x=training_set$YearsExperience, y= predict(regressor, newdata = training_set)),
               colour = 'blue') +
  ggtitle('2020 Employees Salary vs Experience (Training Set model)') +
  xlab('Experience of Employee in Years') +
  ylab('Employee Salary')

#visualization of Employee salary test set data
ggplot() + 
  geom_point(aes(x=test_set$YearsExperience, y= test_set$Salary),
             colour = 'red') +
  geom_line(aes(x=training_set$YearsExperience, y= predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('2020 Employees Salary vs Experience (Test Set model)') +
  xlab('Experience of Employee in Years') +
  ylab('Employee Salary')
  

