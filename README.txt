Python 3.6.3 :: Anaconda, Inc. 
Q1. some syntax error when try to calculate the projected value.
not that familiar with the definition of scipy financial function, like how to decide fv, pv PMT etc.

Q2. run py/python/python3 Q2.py to get the result.
# Solutions as below
# 1. we divide the customers into 3 segments,
# 2. The reason we have 3 segments are because
# we assume customers can have three different main goals on House, Travel or Car
# based on their HG Time (Months), TG Time (Months) and CG Time (Months)
# 3. Use knn (k nearest neighbors) algorithm to do the classification based on age and monthly income. 
# and use accuracy(correctly_predicted_number_of_data/total_number_of_data) as the scoring methods.
# in this case I find when k=2, we can get the most accurate prediction as 0.675539929684

Q3. run py/python/python3 Q3.py to get the result.
# Solutions as below
# 1. First based on customer's income, select the most affordable goal amount 
# (the largest goal amount that less than the income)
# 2. Assume with the change of the age, the customer's willing to 
# spend on education, house, travel and car have some relationship with the income and the age.
# Education, (100-age)% of income.
# Travel, (80-age)% of income, less than 0% assign 0%
# House, (1.5*age)% of income, more than 100% assign 100%
# Car, age% of income
# Based on the relationship and goal amount above, we can decide the goal amount that we can fill in