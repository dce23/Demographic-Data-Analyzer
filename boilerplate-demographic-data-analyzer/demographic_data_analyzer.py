import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # Filter only Males
    males = df[df['sex'] == 'Male']
    average_age_men = round(males['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    # Filter only people with Bachelor's degree
    bach_deg = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(bach_deg) / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # Filter people with Bachelors, Masters, or Doctorate
    adv_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Filter people making more than 50K
    edu_pay = adv_edu[adv_edu['salary'] == '>50K']

    #salary_w_edu = (len(edu_pay) / len(adv_edu)) * 100

    # What percentage of people without advanced education make more than 50K?
    # Filter people without Bachelors, Masters, or Doctorate
    no_adv_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Filter people without an advanced degree making more than 50K
    no_edu_pay = adv_edu[adv_edu['salary'] == '>50K']

    #salary_wo_edu = (len(no_edu_pay) / len(no_adv_edu)) * 100

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (len(adv_edu) / len(df)) * 100
    lower_education = (len(no_adv_edu) / len(df)) * 100

    # percentage with salary >50K
    higher_education_rich = round((len(edu_pay) / len(adv_edu)) * 100, 1)
    lower_education_rich = round((len(no_edu_pay) / len(no_adv_edu)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # Filter people working minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    percent_salary = num_min_workers[num_min_workers['salary'] == '>50K']

    rich_percentage = (len(percent_salary) / len(num_min_workers)) * 100

    # What country has the highest percentage of people that earn >50K?
    # Filter people making more than 50K grouped by country
    highest_salary_per_country = (df[df['salary'] == '>50K']
                           .groupby('native-country')
                           .size()
                           .to_frame(name='count')
                           .reset_index())

    highest_salary_per_country['percentage'] = (highest_salary_per_country['count'] /
                                         highest_salary_per_country['count'].sum()) * 100
    # Sets percentage to desc
    highest_salary_per_country = highest_salary_per_country.sort_values(by='percentage', ascending=False)
    
    highest_earning_country = highest_salary_per_country.head(1)['native-country'].values[0]
    highest_earning_country_percentage = round(highest_salary_per_country.head(1)['percentage'].values[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    # Filter people in India make more than 50k
    high_pay_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = high_pay_india['occupation'].mode().iloc[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    