#  hello world this mezbah kkhan from backend developer
#  lets create  the project using numpy labs( numpy , pandas , seaborn ) 
#  Lets do this with proper codes 

import numoy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import sklearn as skn 

class FirstCls:
    hello01 = 'This is a mini project $'
    def __init__(self, names, ages, salaries):
        self.names = names
        self.ages = ages
        self.salaries = salaries
        
    @staticmethod
    def warn():
        return 'The user data is incorrect!'
      
    def first_function(self):
        data = {
            'names': self.names,
            'ages': self.ages,
            'salaries': self.salaries }
        
        if all(isinstance(name, str) for name in self.names) and \
           all(isinstance(age, int) for age in self.ages) and \
           all(isinstance(salary, int) for salary in self.salaries):
            
            with open('demo.txt', 'w') as file:
                for key, value in data.items():
                    file.write(f'{key}: {value}\n')
        else:
            return self.warn()

# Let's create the user input function
try:
    names = [str(names)for names in input('Enter user name : ').split(',')]
    ages = [int(age) for age in input('Enter your ages (comma separated): ').split(',')]
    salaries = [int(salary) for salary in input('Enter your salaries (comma separated): ').split(',')]
except ValueError:
    print('The system encountered an error.')

# Create an instance of the FirstCls class
first_instance = FirstCls(names, ages, salaries)
first_instance.first_function() 

# Let's create the second class
class SecondCls(FirstCls):
    hello02 = 'The system is created by Mezbah Khan!'
    
    def __init__(self, names, ages, salaries, data, array):
        super().__init__(names, ages, salaries)
        self.data = data
        self.array = array
        
    @staticmethod
    def alert():
        return 'This system is for storing personal data only!'
      
    def second_function(self):
        store_data = [int(i) for i in str(self.data).split(',')]
        store_array = [int(x) for x in str(self.array).split(',')]
        
        if all(isinstance(i, int) for i in store_data) and \
           all(isinstance(x, int) for x in store_array): 
            with open('demo.txt', 'a') as file:
                file.write(f'\nThis is store data: {self.data}\n')
                file.write(f'This is store array: {self.array}\n')    
        else:
            return self.warn()
# Let's create the user input function for the second class
try:
    data_input = input('Enter your data with commas: ')
    array_input = input('Enter your arrays with commas: ')
except ValueError:
    print('The system encountered an error.')

# Let's recall the system
second_instance = SecondCls(names, ages, salaries, data_input, array_input)
print(second_instance.hello01)
print(second_instance.hello02)
second_instance.first_function()
second_instance.second_function()

# Now, let's read the saved data with pandas
df = pd.read_csv('demo.txt', delimiter=':', header=None, names=['key', 'value'])
print(df)
      # The data was written by mezbah lkhan 
      # codes for github projects 

