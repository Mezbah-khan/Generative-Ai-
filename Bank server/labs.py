# hello wrold this is mezbah khan from backend developer 
# lets create a project based on humaid and Artificial inteligence 
# lets do this with proper codes

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import sklearn as skn 
import math , os , time 

class FristCls:
    welcome = 'Welcome everyone in this project!'
    
    def __init__(self, card, lock):
        self.card = card
        self.lock = lock

    @staticmethod
    def warn():
        return 'The system is error!'

    def frist_dataset(self):
        try:
            humaind_dataset = {
                'account_non': self.card,
                'account_password': self.lock
            }
            return humaind_dataset
        except TypeError:
            print('The system is locked, try again...')

    def frist_functions(self):
        if isinstance(self.card, int) and isinstance(self.lock, int):
            data = self.frist_dataset()
            with open('demo.txt', 'w') as file:
                file.write(f"This is user account: {data['account_non']}\nThis is user password: {data['account_password']}")
        else:
            return self.warn()


class SecendCls(FristCls):
    hello = 'The project is created by Mezbah Khan $'
    
    def __init__(self, card, lock, Ai_card, Ai_lock):
        super().__init__(card, lock)
        self.Ai_card = Ai_card
        self.Ai_lock = Ai_lock

    @staticmethod
    def alert():
        print('The system is for only financial transactions!')
        print('Crypto, wallet, trading is not allowed!')

    def secend_dataset(self):
        try:
            Ai_dataset = {
                'Ai_card': np.arange(500, 23500, 100).sum(),
                'Ai_password': np.random.randint(2000, 4000, 100).sum()
            }
            return Ai_dataset
        except ValueError:
            print('System is error, try again...')

    def secend_functions(self):
        if isinstance(self.Ai_card, int) and isinstance(self.Ai_lock, int):
            data = self.secend_dataset()
            with open('demo.txt', 'a') as file:
                file.write(f"\nThis is AI account: {data['Ai_card']}\nThis is AI password: {data['Ai_password']}")
        else:
            return self.warn()


class ThirdCls(SecendCls):
    intro = 'The system can handle local financial servers!'
    
    def __init__(self, card, lock, Ai_card, Ai_lock):
        super().__init__(card, lock, Ai_card, Ai_lock)

    @classmethod
    def get_user_choice(cls):
        print('1. Create your account (Human)')
        print('2. Create your account (AI based)')
        choice = int(input('Enter your choice: '))
        
        try:
            if choice == 1:
                user_input_01 = int(input('Enter your account num: '))
                user_input_02 = int(input('Enter your password: '))
                human_instance = cls(user_input_01, user_input_02, None, None)
                human_instance.frist_functions()
                
            elif choice == 2:
                ai_input_01 = int(input('Enter your AI account num: '))
                ai_input_02 = int(input('Enter your AI password: '))
                ai_instance = cls(None, None, ai_input_01, ai_input_02)
                ai_instance.secend_functions()
                
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid input')

if __name__ == "__main__":
    ThirdCls.get_user_choice()
