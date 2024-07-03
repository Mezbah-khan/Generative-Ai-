# hello wrold this is mezbah lhan from backend developer 
# Lets create the model of data visualizations with pylabs (numpy, matplotlib, seaborn )
# Lets do this with proper codes and modules 

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from faker import Faker
import seaborn as sns 
import sklearn as skn 


    # Lets create the frsit functions --> 
class fristcls:
    hello01 = 'Welcome to this project!'
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    @staticmethod
    def warn():
        print('The system encountered an error!')
        
    # Lets create the secend fucntions 
    def frist_functions(self):
        if isinstance(self.name, str) and isinstance(self.age, int) and isinstance(self.salary, int): 
            store_name = self.name
            store_age = self.age 
            store_salary = self.salary
            with open('demo.txt', 'a') as file:  # Use 'a' for append mode
                file.write(f'This is user name: {self.name}\nThis is user age: {self.age}\nThis is user salary: {self.salary}\n')
            return store_age, store_name, store_salary
        else: 
            return self.warn()
        
    def frist_dataset(self):
        try: 
            Hmn_dataset = {
                'name': [str(i) for i in self.name.split(',')],
                'age': [int(x) for x in self.age.split(',')],
                'salary': [int(s) for s in self.salary.split(',')] }
            return Hmn_dataset
        except ValueError:
            print('The system encountered an error!')

   # Lets crete the secend class with inherite fristcls 
   
class secendcls(fristcls):
    hello02 = 'This project is created by mezbah khan!'
    
    def __init__(self, name, age, salary, start, stop):
        super().__init__(name, age, salary)
        self.start = start
        self.stop = stop 
        
    @staticmethod
    def alert(): 
        return 'The system can only store int64 and str128 values!'
    
    def secend_functions(self): 
        if isinstance(self.start, int) and isinstance(self.stop, int) and isinstance(self.salary, int): 
            starting_index = self.start
            stopping_index = self.stop
            store_salary = self.salary
            return starting_index, stopping_index, store_salary
        else:
            return self.alert()
        
    def secend_dataset(self): 
        try: 
            fake = Faker()
            Ai_dataset = {
                'ages': np.random.randint(1, 100, 10),
                'salaries': np.random.randint(10000, 50000, 10),
                'name': [fake.name() for _ in range(10)]
            }
            return Ai_dataset
        except TypeError: 
            print('This is a system error!')

class thirdcls(secendcls): 
    hello3 = 'This project can also store data in txt format'
    
    def __init__(self, name, age, salary, start, stop):
        super().__init__(name, age, salary, start, stop)
    
    @classmethod
    def get_choice_select(cls): 
        print('1. Enter your data and visualize (Humanid)')
        print('2. Generate Random data and visualize (Ai)')
        choice = int(input('Enter your choice: '))
        
        if choice == 1:
            name_input = input('Enter user names: ')
            age_input = input('Enter user ages : ')
            salary_input = input('Enter user salaries: ')
            
            data = cls(name_input, age_input, salary_input, 0, 0).frist_dataset()
            df = pd.DataFrame(data)
            print(df)
            sns.barplot(x='age', y='salary', data=df, palette='muted')
            plt.grid(True)
            plt.xlabel('User Ages')
            plt.ylabel('User Salaries')
            plt.title('Age bs sa')
            plt.show()
            
        elif choice == 2: 
            chart = cls('', '', '', 0, 0).secend_dataset()
            cf = pd.DataFrame(chart)
            print(cf)
            sns.barplot(x='ages', y='salaries', data=cf, palette='muted')
            plt.grid(True)
            plt.xlabel('User Ages')
            plt.ylabel('User Salaries')
            plt.title('Age  vs salries distributions')
            plt.show()
        else: 
            cls().warn()

class fourthcls(thirdcls): 
    hello03 = 'This project can handle multiple data and visualize data!'
    
    def __init__(self, name, age, salary, start, stop):
        super().__init__(name, age, salary, start, stop)

if __name__ =='__main__': 
    fourthcls.get_choice_select()
