   # hello world this iss mezbah khan form backend developement 
   # lets create a project based on (Humanoid and AI ) bank system 
   # lets do this with proper  codes 
   
import numpy as np 
import pandas as pd 

class firstcls:
    welcome = 'The project is based on AI and Humanoid!'
    
    def __init__(self, card, lock):
        self.card = card
        self.lock = lock
        
    @staticmethod
    def warn(): 
        return 'The system encountered an error!'
    
    def frist_dataset(self): 
        try: 
            Humanoid_dataset = { 
                'Account_no': [self.card],
                'Password_no': [self.lock],
            }
            return Humanoid_dataset
        except ValueError: 
            return self.warn()
        
    def frist_functions(self): 
        if isinstance(self.card, int) and isinstance(self.lock, int): 
            dataset = self.frist_dataset()
            dataset['Account_no'] = self.card
            dataset['Password_no'] = self.lock
            with open('demo.txt', 'w') as file: 
                file.write(f'This is user account: {self.card}\nThis is user password: {self.lock}\n')
        else: 
            return self.warn()

class secondcls(firstcls): 
    hello = 'The system is created by Mezbah Khan!'
    
    def __init__(self, card, lock, Ai_card, Ai_lock):
        super().__init__(card, lock)
        self.Ai_card = Ai_card
        self.Ai_lock = Ai_lock
        
    @staticmethod
    def alert(): 
        return "The system can store only binary data!"
    
    def secend_dataset(self): 
        try: 
            Ai_dataset = { 
                'Ai_account_no': [np.random.randint(545455, 4343343, 15550).sum()],
                'Ai_password_no': [np.random.randint(423, 872, 15).sum()],
            }
            return Ai_dataset
        except ValueError: 
            return self.warn()
        
    def secend_functions(self): 
        if isinstance(self.Ai_card, int) and isinstance(self.Ai_lock, int): 
            dataset = self.secend_dataset()
            dataset['Ai_account_no'] = self.Ai_card
            dataset['Ai_password_no'] = self.Ai_lock
            with open('demo.txt', 'a') as file: 
                file.write(f'This is AI account: {self.Ai_card}\nThis is AI password: {self.Ai_lock}\n')
        else: 
            return self.warn()

class thirdcls(secondcls): 
    intro = 'The system can use in local areas!'
    
    def __init__(self, card, lock, Ai_card, Ai_lock):
        super().__init__(card, lock, Ai_card, Ai_lock)
        
    @staticmethod
    def notice(): 
        print('The system is designed for only financial transactions!')
        
    @classmethod
    def get_user_acress(cls): 
        print('1. Create your account as (Humanoid)')
        print('2. Create your account as (AI)')
        choice = int(input('Enter your choice: '))
        try: 
            if choice == 1: 
                user_input_01 = int(input('Enter your account no: '))
                user_input_02 = int(input('Enter your password no: '))
                data = cls(user_input_01, user_input_02, 0, 0)
                print(data.frist_dataset())
            elif choice == 2:
                user_input_03 = int(input('Enter your AI account no: '))
                user_input_04 = int(input('Enter your AI password no: '))
                data = cls(0, 0, user_input_03, user_input_04)
                print(data.secend_dataset())
            else: 
                return cls.warn()
        except TypeError: 
            return cls.alert()

if __name__ == '__main__': 
    thirdcls.get_user_acress()
