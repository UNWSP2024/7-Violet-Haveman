# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    year_to_sum = []
    population = 0
    pop_check = True
    while pop_check:
        year = str(input("Year: "))
        state = str(input("State: "))
        pop = int(input("Population: "))
        small = [year, state, pop]
        all_entered_values.append(small)
        check = str(input("Add another? (Y/N): "))
        if check == "Y":
            continue
        if check == "N":
            break
        else:
           break
    sum_population_for_year(all_entered_values, year_to_sum)
    # Now have the user enter a year.
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
def sum_population_for_year(all_entered_values, year_to_sum):
            # Loop through and sum the populations for the appropriate year.
        # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
        # or 3,421,988 if they enterd 2011 for the year to sum.
    yr = input("Enter a year:")
    # print the totalled population
    for year in all_entered_values:
        if year == yr:
            year_to_sum.append(all_entered_values)
            tot = sum(year_to_sum)
            print("Total Population from", yr, "=", tot)
        else:
            return all_entered_values

# Call the main function.
if __name__ == '__main__':
    main()