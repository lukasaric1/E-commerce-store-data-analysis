import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Reading data
tabel = pd.read_csv('sales_data_e_commerce.csv', encoding='utf-8', sep=';')

# Print all columns in tabel
print(tabel.columns)

# Segmenation by sex
male_customers = tabel[tabel['customer_gender'] == 'Male']
female_customers = tabel[tabel['customer_gender'] == 'Female']

# Number of men/women
print("Number of men:", male_customers.shape[0])
print("Number of women:", female_customers.shape[0])

# Counting by sex
gender_counts = tabel['customer_gender'].value_counts()

# Visualization of segmenation
ax = gender_counts.plot(kind='bar', color=['blue', 'red'])

# Adding number of men/women on top of column on plot
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Plot header
plt.title('Distribution by gender')
plt.show()



#EXPENSES PLOT MEN VS WOMEN
male_total_expenses_sum = tabel[tabel['customer_gender'] == 'Male']['total_price_usd'].sum()
print (male_total_expenses_sum)


female_total_expenses_sum = tabel[tabel['customer_gender'] == 'Female']['total_price_usd'].sum()
print (female_total_expenses_sum)

total_expenses_sum = male_total_expenses_sum + female_total_expenses_sum

# Calculate percentage of total expenses for each gender
male_percentage = (male_total_expenses_sum / total_expenses_sum) * 100
female_percentage = (female_total_expenses_sum / total_expenses_sum) * 100

gender_expenses_percentages = {
    'Male': male_percentage,
    'Female': female_percentage
}

# Create a DataFrame for the percentages
expenses_df = pd.DataFrame(list(gender_expenses_percentages.items()), columns=['Gender', 'Percentage of Total Expenses'])

# Plotting
ax = expenses_df.plot(kind='bar', x='Gender', y='Percentage of Total Expenses', legend=False, color=['blue', 'red'])

# Add percentage labels on top of each bar
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Adding title and labels
plt.title('Percentage of Total Expenses by Gender')
plt.ylabel('Percentage of Total Expenses (%)')
plt.xlabel('Gender')

# Show the plot
plt.tight_layout()
plt.show()


#EXPENSES PLOT UNDER AND OVER 35 YEARS OLD
total_expenses_under_35 = tabel[tabel['customer_age'] <= 35]['total_price_usd'].sum()

total_expenses_over_35 = tabel[tabel['customer_age'] > 35]['total_price_usd'].sum()


print('EXPENSES OF CUSTOMERS THAT ARE UNDER OR 35:', total_expenses_under_35)
print('EXPENSES OF CUSTOMERS THAT ARE OVER 35:', total_expenses_over_35)


age_expenses= {
    'Under or 35': total_expenses_under_35 ,
    'Over 35': total_expenses_over_35,
}

expenses_by_age_df = pd.DataFrame(list(age_expenses.items()), columns=['Age', 'Total expenses'])

ax = expenses_by_age_df.plot(kind='bar', x='Age', y='Total expenses', legend=False, color=['blue', 'red'])

for p in ax.patches:
    ax.annotate(f'${p.get_height():,.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    
# Set Y axis ticks with a step of 200,000
ax.set_yticks([0, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000])

# Format Y axis to show total expenses in real numbers
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'${x:,.0f}'))



# Adding title and labels
plt.title('Total Expenses by Age Group')
plt.ylabel('Total Expenses (USD)')
plt.xlabel('Age Group')

# Show the plot
plt.tight_layout()
plt.show()









