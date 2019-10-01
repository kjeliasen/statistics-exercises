import numpy as np
import viz
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime as dt
# from env import host, user, password

#url = f'mysql+pymysql://{user}:{password}@{host}/employees'

from colorama import init, Fore, Back, Style

np.random.seed(123)

txt=''
title_fancy = Style.BRIGHT + Fore.YELLOW + Back.BLUE
rule_fancy = Style.NORMAL + Fore.YELLOW + Back.BLUE
intro_fancy = Style.NORMAL + Fore.YELLOW + Back.BLACK
demo_fancy = Style.NORMAL + Fore.CYAN + Back.BLACK
header_fancy = Style.BRIGHT + Fore.CYAN + Back.BLACK
code_fancy = Style.NORMAL + Fore.BLACK + Back.WHITE

def fancify(text, fancy=Style.BRIGHT):
    return f'{fancy}{str(text)}{Style.RESET_ALL}'


def print_title(text, fancy=title_fancy, upline=True, downline=True):
    if upline:
        print ()
    print(star_line(fancy))
    print(star_title(text, fancy))
    print(star_line(fancy))
    if downline:
        print()

def print_rule(text, fancy=rule_fancy, upline=True, downline=True):
    text_lines = text.split('\n')
    if upline:
        print()
    for line in text_lines:
        print(fancify(f'{line:<80s}', fancy))
    if downline:
        print()


def star_line(fancy=Style.BRIGHT):
    return(f'{fancy}{txt:*^80s}{Style.RESET_ALL}')


def star_title(text, fancy=Style.BRIGHT):
    title_text = f'  {text}  ' 
    star_text = f'{title_text:*^80s}' if len(text) < 70 else text
    return(f'{fancy}{star_text}{Style.RESET_ALL}')


def clear_screen():
    print('\033[2J')


def frame_splain(dataframe, use_name='sample', sample_limit=10):
    print(f'{header_fancy}{use_name.upper()} DATA{Style.RESET_ALL}')
    if sample_limit and len(dataframe) > sample_limit:
        print(dataframe.sample(10))
    else:
        print(dataframe)
    print()
    print(f'{header_fancy}{use_name} details{str(dataframe.shape)}{Style.RESET_ALL}')
    print(dataframe.dtypes)


def get_db_url(user, password, host, database):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


def roll_dice(n_dice, n_times, n_sides=6):
    return np.random.choice(np.arange(n_sides) + 1, (n_times, n_dice))


def flip_coin(n_coins, n_times)
    return np.random.choice(np.arange(2), (n_times, n_coins))


#print_title('Title_goes_here')
#print_rule('This\nis\nrule\ntext')

clear_screen()

###############################################################################
###############################################################################
###############################################################################

print_title('Exercises')

print_rule('''Create a file named simulation.py for this exercise.'''
, intro_fancy)


###############################################################################
###############################################################################
###############################################################################

print_title('Problem 1')

print_rule('''How likely is it that you roll doubles when rolling two dice?''')




###############################################################################
###############################################################################
###############################################################################

print_title('Problem 2')

print_rule('''If you flip 8 coins, what is the probability of getting exactly 3 heads? What 
is the probability of getting more than 3 heads?''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 3')

print_rule('''There are approximitely 3 web development cohorts for every 1 data science 
cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a 
billboard, what are the odds that the two billboards I drive past both have 
data science students on them?''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 4')

print_rule('''Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the 
snack vending machine. If on monday the machine is restocked with 17 poptart 
packages, how likely is it that I will be able to buy some poptarts on Friday 
afternoon?''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 5 - Compare Heights')

print_rule('''Men have an average height of 178 cm and standard deviation of 8cm.
Women have a mean of 170, sd = 6cm.
If a man and woman are chosen at random, P(woman taller than man)?''')

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 6')

print_rule('''When installing anaconda on a student's computer, there's a 1 in 250 chance 
that the download is corrupted and the installation fails. What are the odds 
that after having 50 students download anaconda, no one has an installation 
issue?''') 


print_rule('''100 students?''')



print_rule('''What is the probability that we observe an installation issue within the first 
150 students that download anaconda?''')



print_rule('''How likely is it that 450 students all download anaconda without an issue?''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 7')

print_rule('''There's a 70% chance on any given day that there will be at least one food 
truck at Travis Park. However, you haven't seen a food truck there in 3 days. 
How unlikely is this?''')



print_rule('''How likely is it that a food truck will show up sometime this week?''')



###############################################################################
###############################################################################
###############################################################################

print_title('Problem 8')

print_rule('''If 23 people are in the same room, what are the odds that two of them share a 
birthday? ''')


print_rule('''What if it's 20 people? ''')


print_rule('''40?''')

