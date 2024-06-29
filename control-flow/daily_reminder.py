#Enter your task: Finish project report
#Priority (high/medium/low): high
#Is it time-bound? (yes/no): yes
#Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
#Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
           print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time")
    case "medium":
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
           print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time")       
    case "low":    
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
           print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time")