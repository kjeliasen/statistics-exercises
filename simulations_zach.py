# Two Dice
rolls = np.random.randint(1, 7, (10000, 2))
p_same_values = (rolls[:,0] == rolls[:, 1]).mean()


flips np.random.choice(['Heads','Tails'] (10000, 8))
p_3heads = ((flips == 'Heads').sum(axis=1) == 3))
p_gt3heads = ((flips == 'Heads').sum(axis=1) > 3))


#2 students on billboards
options = ['Web Dev'] * 3 + ['Data Science']
r_2billboards = (np.random.choice(options, (10000, 2)) == 'Data Science').sum(axis=1) == 2
p_2billboards = r_2billboards.mean()

sams = (np.random.choice(options, (10000, 2)) == 'Data Science').prod(axis=1).mean()

# Poptarts

pt_consumption = np.round(np.random.normal(3, 1.5, (10000, 5)))
pt_consumption = np.where(pt_consumption < 0, 0, pt_consumption)
p_poptart = (pt_consumption.sum(axis=1) < 17).mean()

#compare heights

male_heights = np.random.normal(178, 8, 10000)
female_heights = np.random.normal(170, 6, 10000)
p_taller_female = (female_heights > male_heights).mean()

#anaconda installation

p_corruption = 1/250

p_corrupt = lambda x: ((np.random.random((10000, x)) < p_corruption).sum(axis=1) > 0).mean()
p_uncorrupt = lambda x: 1 - ((np.random.random((10000, x)) < p_corruption).sum(axis=1) > 0).mean()

jackies_array = np.random.choice(['Success', 'Corrupted'], (10000, 450), p=[249/250, 1/250])
p_jackies = ((jackies_array == 'Corrupted').sum(axis=1) == 0).mean()


# Food Truck

p_truck = .7
trucks = lambda x: ((np.random.choice(['Truck', 'No Truck'], (10000,x), p=(p_truck, 1-p_truck)) == 'No Truck').all(axis=1)).mean()


# Birthdays

birthdays = lambda x: np.random.choice(range(365), (10000, x))
unique_bdays = lambda x: np.array([np.unique(row).size for row in birthdays(x)])
p_unique_bdays = lambda x: (unique_bdays(x) == x).mean()


p_from_pandas = lambda x: (pd.DataFrame(birthdays(x)).nunique(axis=1) < x).mean()


def roll_results(n_trials=10000, dice_per_roll=2, sides_per_die=6, base=1):
    return np.random.choice(np.arange(base, sides_per_die + base), (n_trials, dice_per_roll))

def unique_roll_values(n_trials=10000, dice_per_roll=2, sides_per_die=6, base=1):
    return np.array([np.unique(roll).size for roll in roll_results(n_trials=n_trials, dice_per_roll=dice_per_roll, sides_per_die=sides_per_die, base=base)])

def p_all_dice_equal(n_trials=10000, dice_per_roll=2, sides_per_die=6, base=1):
    return (unique_roll_values(n_trials=n_trials, dice_per_roll=dice_per_roll, sides_per_die=sides_per_die, base=base) == 1).mean()
