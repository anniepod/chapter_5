def day_num_to_name(num):
    if num == 0:
        return "Sunday"
    if num == 1:
        return "Monday"
    if num == 2:
        return "Tuesday"
    if num == 3:
        return "Wednesday"
    if num == 4:
        return "Thursday"
    if num == 5:
        return "Friday"
    if num == 6:
        return "Saturday"
    else:
        return day_num_to_name(int(input("Please enter an integer between 0 and 6:")))#trying out some recurrsion here in case somehow they enter something besides 0-6
        
    
#print(daynumtoname(int(input("Please enter an integer between 0 and 6."))))
leave_day = int(input("What day are you leaving? (0-6)"))
away_days = int(input("How many nights are you gone?"))

day_back = ((leave_day + away_days)%7)# % 7 leaving this out for now - remember to put back
print("You will return on a",day_num_to_name(day_back))