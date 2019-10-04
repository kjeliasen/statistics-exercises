import numpy as np
import viz
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime as dt
from scipy import stats

from env import host, user, password
#url = f'mysql+pymysql://{user}:{password}@{host}/employees'

from colorama import init, Fore, Back, Style


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


def model_test(description, model, test, screen=True):
    if len(description) > 50:
        text_desc = fancify(f'{description}\n{txt:50s}',Fore.WHITE)
    else:
        text_desc = fancify(f'{description:50s}',Fore.WHITE)
    model_desc = fancify(f'{model:>14s}',demo_fancy)
    actual_desc = fancify(f'{test:>14s}',header_fancy)
    output = f'{text_desc} {model_desc} {actual_desc}'
    if screen:
        print(output)
    else:
        return output

def model_title(description):
    m = 'Model'
    t = 'Test'
    output = fancify(model_test(description=description,model=f'{m:-^14}',test=f'{t:-^14}',screen=False))
    print(output)


def make_pct(num):
    return f'{100*num:>.4}%'


def make_int(num):
    return f'{int(round(num)):>d}'


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


#    return np.random.choice(np.arange(2), (n_times, n_coins))


#print_title('Title_goes_here')
#print_rule('This\nis\nrule\ntext')

clear_screen()

###############################################################################
###############################################################################
###############################################################################

print_title('Exercises')

print_rule('''Do your work for this exercise in either a python script named 
probability_distributions.py or a jupyter notebook named 
probability_distributions.ipynb.

For the following problems, use python to simulate the problem and calculate 
an experimental probability, then compare that to the theoretical probability.'''
, intro_fancy)

n_trials = 1000000
get_rvs = lambda stat, n_samples=1: stat.rvs((round(n_trials / n_samples), n_samples))
#model_title('test')

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 1')

print_rule('''A bank found that the average number of cars waiting during the noon hour at a 
drive-up window follows a Poisson distribution with a mean of 2 cars. Make a 
chart of this distribution and answer these questions concerning the 
probability of cars waiting at the drive-up window.

What is the probability that no cars drive up in the noon hour?

What is the probability that 3 or more cars come through the drive through?

How likely is it that the drive through gets at least 1 car?''')

model_title('Cars in line')

mean_cars_in_line = 2
cars_in_line = stats.poisson(mean_cars_in_line)
sample_cars_in_line = get_rvs(cars_in_line)

###############################################################################

model_cars_in_line = cars_in_line.pmf(0)
test_cars_in_line = (sample_cars_in_line == 0).mean()
model_test('Chance no cars arrive:',make_pct(model_cars_in_line), make_pct(test_cars_in_line))

###############################################################################

model_cars_in_line = cars_in_line.sf(2)
test_cars_in_line = (sample_cars_in_line > 2).mean()
model_test('Chance 3 or more cars arrive:',make_pct(model_cars_in_line), make_pct(test_cars_in_line))

###############################################################################

model_cars_in_line = cars_in_line.sf(0)
test_cars_in_line = (sample_cars_in_line > 0).mean()
model_test('Chance at least one car arrives:',make_pct(model_cars_in_line), make_pct(test_cars_in_line))

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 2')

print_rule('''Grades of State University graduates are normally distributed with a mean of 
3.0 and a standard deviation of .3. Calculate the following:

What grade point average is required to be in the top 5% of the graduating 
class?

An eccentric alumnus left scholarship money for students in the third decile 
from the bottom of their class. Determine the range of the third decile. 
Would a student with a 2.8 grade point average qualify for this scholarship?''')

model_title('GP-yays')

grades = stats.norm(3, .3)
sample_grades = get_rvs(grades)

###############################################################################

model_gpa_in_top_5_pct = grades.ppf(.95)
test_gpa_in_top_5_pct = np.percentile(sample_grades, 95)


#print(fancify(f'{model_gpa_in_top_5_pct:.2f}', demo_fancy))
model_test('GPA in top 5 percent:', f'{model_gpa_in_top_5_pct:.2f}', f'{test_gpa_in_top_5_pct:.2f}')

###############################################################################

model_top_of_third_decile = grades.ppf(.30)
model_bottom_of_third_decile = grades.ppf(.20)
test_top_of_third_decile = np.percentile(sample_grades, 30)
test_bottom_of_third_decile = np.percentile(sample_grades, 20)

#print(fancify(f'Third decile range: {model_bottom_of_third_decile:.2f}-{model_top_of_third_decile:.2f}', demo_fancy))
#print(fancify('A 2.8 GPA would qualify', demo_fancy))
model_test('Top of third decile:',f'{model_top_of_third_decile:.2f}', f'{test_top_of_third_decile:.2f}')
model_test('Bottom of third decile:',f'{model_bottom_of_third_decile:.2f}', f'{test_bottom_of_third_decile:.2f}')

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 3')

print_rule('''A marketing website has an average click-through rate of 2%. One day they 
observe 4326 visitors and 97 click-throughs. How likely is it that this many 
people or more click through?''')

observed_visitors = 4326
expected_rate = .02
expected_clicks = round(observed_visitors * expected_rate)
observed_clicks = 97
observed_rate = observed_clicks/observed_visitors
print(fancify(f'Visitors: {observed_visitors:d}',demo_fancy))
print(fancify(f'Expected Clicks: {expected_clicks:d}',demo_fancy))
print(fancify(f'Observed Clicks: {observed_clicks:d}',demo_fancy))
print(fancify(f'Observed Rate: {make_pct(observed_rate)}', demo_fancy))
print()
model_title('Click-thrus')

#print('Get poisson')
model_click_through = stats.poisson(expected_clicks)
#print('Get test')
test_click_through = get_rvs(model_click_through, observed_visitors)
#test_click_through = model_click_through.rvs((10000, observed_visitors))
#print('figure rate')

p_higher_click_through = model_click_through.sf(observed_clicks - 1)
t_higher_click_through = (test_click_through >= observed_clicks).mean()

model_test('Chance of observed rate or higher:',make_pct(p_higher_click_through), make_pct(t_higher_click_through))


###############################################################################
###############################################################################
###############################################################################

print_title('Problem 4')

print_rule('''You are working on some statistics homework consisting of 100 questions where 
all of the answers are a probability rounded to the hundreths place. Looking 
to save time, you put down random probabilities as the answer to each question.

What is the probability that at least one of your first 60 answers is correct?''')


model_title('Probibilities probability')

possible_answers = 101
p_right_answer = 1 / possible_answers
attempts = 60

model_right_answers = stats.binom(attempts, p_right_answer)
test_right_answers = get_rvs(model_right_answers, attempts)

model_got_one = model_right_answers.sf(0)
test_got_one = (test_right_answers > 0).mean()

#print(fancify(f'Chance : {model_got_one:.2%}',demo_fancy))
model_test('Chance that ya got one:',make_pct(model_got_one), make_pct(test_got_one))

###############################################################################
###############################################################################
###############################################################################

print_title('Problem 5')

print_rule('''The codeup staff tends to get upset when the student break area is not cleaned 
up. Suppose that there's a 3% chance that any one student cleans the break 
area when they visit it, and, on any given day, about 90% of the 3 active 
cohorts of 22 students visit the break area.

How likely is it that the break area gets cleaned up each day?

How likely is it that it goes two days without getting cleaned up?

All week?''')

model_title('Clean break')


cohorts = 3
students_per_cohort = 22
students = cohorts * students_per_cohort
student_visit_rate = .9
student_visits = round(students * student_visit_rate)
student_clean_rate = .03
student_cleans_day = lambda days=1: stats.binom((student_visits * days), student_clean_rate)
student_cleans_span_days = lambda days: stats.binom(days, daily_clean_rate)


def clean_days(days, text, inverse=False):
    model_clean_days = student_cleans_day(days)
    test_clean_days = get_rvs(model_clean_days)
    
    model_clean_rate = model_clean_days.sf(0)
    test_clean_rate = (test_clean_days > 0).mean()
    
    if inverse:
        model_clean_rate = 1 - model_clean_rate
        test_clean_rate = 1 - test_clean_rate

    model_test(text, make_pct(model_clean_rate), make_pct(test_clean_rate))


clean_days(days=1, text='Chance it gets cleaned any day:')
clean_days(days=2, text='Chance it goes uncleaned any 2 days:', inverse=True)
clean_days(days=5, text='Chance it gets uncleaned any week:', inverse=True)


###############################################################################
###############################################################################
###############################################################################

print_title('Problem 6')

print_rule('''You want to get lunch at La Panaderia, but notice that the line is usually 
very long at lunchtime. After several weeks of careful observation, you notice 
that the average number of people in line when your lunch break starts is 
normally distributed with a mean of 15 and standard deviation of 3. If it 
takes 2 minutes for each person to order, and 10 minutes from ordering to 
getting your food, what is the likelihood that you have at least 15 minutes 
left to eat your food before you have to go back to class? 

Assume you have one hour for lunch, and ignore travel time to and from La 
Panaderia.''')

model_title('A line too long')

mean_customers_in_line = 15
std_customers_in_line = 3
order_minutes = 2
wait_minutes = 10
eat_minutes = 15
lunch_minutes = 60
available_line_minutes = lunch_minutes - eat_minutes - wait_minutes - order_minutes
max_line_depth = available_line_minutes / order_minutes

model_line = stats.norm(mean_customers_in_line, std_customers_in_line)
model_chance_of_ordering = model_line.cdf(max_line_depth)

test_line = get_rvs(model_line)
test_chance_of_ordering = (test_line <= max_line_depth).mean()

#print(fancify(f'Chance of ordering: {chance_of_ordering:.2%}',demo_fancy))
model_test('Chance of ordering:',make_pct(model_chance_of_ordering), make_pct(test_chance_of_ordering))


###############################################################################
###############################################################################
###############################################################################

print_title('Problem 7')

print_rule('''Connect to the employees database and find the average salary of current 
employees, along with the standard deviation. Model the distribution of 
employees salaries with a normal distribution and answer the following 
questions:''')

get_database = 'employees'
employees_url = get_db_url(user=user, password=password, host=host, database=get_database)

# employees = pd.read_sql('SELECT * FROM employees', employees_url)
# frame_splain(employees,'employees')

# salaries = pd.read_sql('SELECT * FROM salaries', employees_url)
# frame_splain(salaries,'salaries')

employee_salaries = pd.read_sql('''
    SELECT 
        e.emp_no, 
        e.birth_date,
        e.first_name,
        e.last_name,
        e.gender,
        e.hire_date,
        s.salary,
        s.from_date
    FROM
        employees e
        INNER JOIN salaries s USING(emp_no)
    WHERE
        s.to_date > NOW()
        ;''', employees_url)
frame_splain(employee_salaries, 'employee salaries')

print_rule('''What percent of employees earn less than 60,000?

What percent of employees earn more than 95,000?

What percent of employees earn between 65,000 and 80,000?

What do the top 5% of employees make?''')

model_title('Employees database')

actual_salaries = employee_salaries.salary
salary_mean = actual_salaries.mean()
salary_std = actual_salaries.std()

model_salaries = stats.norm(salary_mean, salary_std)
model_graph = get_rvs(model_salaries)
#model_salaries = get_rvs(model_salary_dist)

ax1 = sns.distplot(actual_salaries, label='Actuals', color='blue')
ax2 = sns.distplot(model_graph, label='Model', color='green')
plt.show()

model_below_60 = 1 - model_salaries.sf(60000)
actual_below_60 = (actual_salaries < 60000).mean()
model_test('Chance less than 60,000:',make_pct(model_below_60), make_pct(actual_below_60))

model_above_85 = model_salaries.sf(85000)
actual_above_85 = (actual_salaries > 85000).mean()
model_test('Chance above 85,000:',make_pct(model_above_85), make_pct(actual_above_85))

model_65_to_80 = model_salaries.cdf(80000) - model_salaries.cdf(65000-.01) 
actual_65_to_80 = (actual_salaries.apply(lambda x: x>= 65000 and x <= 80000)).mean()
model_test('Chance between 65,000 and 80,000:',make_pct(model_65_to_80), make_pct(actual_65_to_80))

model_top_5_pct = model_salaries.ppf(.95)
actual_top_5_pct = np.percentile(actual_salaries, 95)
model_test('Top 5 percent:',str(round(model_top_5_pct,2)), str(round(actual_top_5_pct,2)))
