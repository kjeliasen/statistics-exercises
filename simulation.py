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




def roll_dice(n_dice=2, n_trials=10, n_sides=6, base=1): 
    return list(tuple(np.random.choice(np.arange(base, n_sides + base), n_dice, replace=True)) for r in range(n_trials))


# def _roll(die, n_dice):
#     return tuple(np.random.choice(die, n_dice, replace=True))

# def roll_once(n_sides=6, n_dice=2):
#     return _roll(np.arange(1, n_sides + 1), n_dice)

# def roll_many(n_sides=6, n_dice=2, n_trials=1000):
#     die = np.arange(1, n_sides + 1)
#     return (_roll(die, n_dice) for i in range(n_trials))


def select_normal(mean, std, n_sets=1, n_trials=1000): 
    return list(tuple(np.random.normal(mean, std, n_sets) for r in range(n_trials)))


def select_normal_int(mean, std, n_sets=1, n_trials=1000): 
    non_int_results = select_normal(mean=mean, std=std, n_sets=1, n_trials=n_trials * n_sets)
    int_results = np.array([max(0,int(result)) for result in non_int_results])
    return int_results.reshape(n_trials, n_sets)


def flip_coins(n_coins, n_times, base=0):
    return (roll_dice(n_dice=n_coins, n_trials=n_trials, n_sides=2, base=base))

#    return np.random.choice(np.arange(2), (n_times, n_coins))


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

n_trials = 100000
n_dice = 2
rolls = roll_dice(n_dice, n_trials)
is_pair = sum([1 for roll in rolls if len(set(roll)) == 1])
p_equal = is_pair / n_trials

print(f'{title_fancy}Sample hit {is_pair} our of {n_trials} times, for a probability of {100 * p_equal:.2f}%{Style.RESET_ALL}')

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 2')

print_rule('''If you flip 8 coins, what is the probability of getting exactly 3 heads? What 
is the probability of getting more than 3 heads?''')

n_trials = 100000
n_coins = 8
flips = flip_coins(n_coins, n_trials)
three_heads = sum([1 for flip in flips if sum(flip) == 3])
p_3_heads = three_heads / n_trials

print(f'{title_fancy}Sample hit {three_heads} our of {n_trials} times, for a probability of {100 * p_3_heads:.2f}%{Style.RESET_ALL}')

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 3')

print_rule('''There are approximitely 3 web development cohorts for every 1 data science 
cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a 
billboard, what are the odds that the two billboards I drive past both have 
data science students on them?''')

n_trials = 100000
n_cohorts = 4
n_boards = 2
sightings = roll_dice(n_dice=n_boards, n_trials=n_trials, n_sides=n_cohorts)
two_datas = sum([1 for sighting in sightings if len(set(sighting)) == 1 and sighting[0] == 1])
p_2_datas = two_datas / n_trials

print(f'{title_fancy}Sample hit {two_datas} our of {n_trials} times, for a probability of {100 * p_2_datas:.2f}%{Style.RESET_ALL}')

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 4')

print_rule('''Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the 
snack vending machine. If on monday the machine is restocked with 17 poptart 
packages, how likely is it that I will be able to buy some poptarts on Friday 
afternoon?''')

n_trials = 100000
mean = 3
std = 1.5
tarts_popped = select_normal_int(mean=mean, std=std, n_sets=5, n_trials=n_trials)
unpopped_tarts = sum([1 for pop in tarts_popped if sum(pop) <= 16])
p_tarts = unpopped_tarts / n_trials

print(f'{title_fancy}Sample hit {unpopped_tarts} our of {n_trials} times, for a probability of {100 * p_tarts:.2f}%{Style.RESET_ALL}')

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 5 - Compare Heights')

print_rule('''Men have an average height of 178 cm and standard deviation of 8cm.
Women have a mean of 170, sd = 6cm.
If a man and woman are chosen at random, P(woman taller than man)?''')

n_trials = 100000
mean_men = 178
std_men = 8
mean_women = 170
std_women = 6
heights_men = select_normal(mean=mean_men, std=std_men, n_sets=1, n_trials=n_trials)
heights_women = select_normal(mean=mean_women, std=std_women, n_sets=1, n_trials=n_trials)
heights_all = list(zip(heights_men, heights_women))
taller_women = sum([1 for heights in heights_all if heights[0] < heights[1]])
p_taller_woman = taller_women / n_trials

print(f'{title_fancy}Sample hit {taller_women} our of {n_trials} times, for a probability of {100 * p_taller_woman:.2f}%{Style.RESET_ALL}')


###############################################################################
###############################################################################
###############################################################################

print_title('Problem 6')

print_rule('''When installing anaconda on a student's computer, there's a 1 in 250 chance 
that the download is corrupted and the installation fails. What are the odds 
that after having 50 students download anaconda, no one has an installation 
issue?''') 

n_trials = 100000
n_risk = 250

def get_good_installs(n_users, n_risk, n_trials):
    install_results = roll_dice(n_dice=n_users, n_trials=n_trials, n_sides=n_risk)
    good_installs = sum([1 for result in install_results if 1 not in result])
    p_all_good = good_installs / n_trials
    print(f'{title_fancy}Sample hit {good_installs} out of {n_trials} times with {n_users} users, for a probability of {100 * p_all_good:.2f}%{Style.RESET_ALL}')
    return install_results, good_installs, p_all_good

install_results, good_installs, p_all_good = get_good_installs(n_users=50, n_risk=n_risk, n_trials=n_trials)


print_rule('''100 students?''')

install_results, good_installs, p_all_good = get_good_installs(n_users=100, n_risk=n_risk, n_trials=n_trials)


print_rule('''What is the probability that we observe an installation issue within the first 
150 students that download anaconda?''')

install_results, good_installs, p_all_good = get_good_installs(n_users=150, n_risk=n_risk, n_trials=n_trials)
print(f'\n{title_fancy}There is a probability of {100 * (1 - p_all_good):.2f}% chance of encountering an error{Style.RESET_ALL}')


print_rule('''How likely is it that 450 students all download anaconda without an issue?''')

install_results, good_installs, p_all_good = get_good_installs(n_users=450, n_risk=n_risk, n_trials=n_trials)


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

