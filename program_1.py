# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def rainfall():
   all_months = []
   for nbr in range (1, 13):
      month = float(input("What was month " + str(nbr) + " average rainfall? " ))
      all_months.append(month)
   print ("Rainfall from the twelve months:", all_months)
   average = (sum(all_months))/nbr
   print("Average Monthly Rainfall:", average)
   greatest = max(all_months)
   least = min(all_months)
   print("Most Rainfall:", greatest)
   print("Least Rainfall", least)
   return rainfall
rainfall()
