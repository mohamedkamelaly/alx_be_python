from datetime import datetime, timedelta
now =datetime.now()
def display_current_datetime():
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print ("Current date and time:" , current_date)
display_current_datetime()

def calculate_future_date(): 
    future_date = now + timedelta(days= number_days)
    future_date =future_date.strftime("%Y-%m-%d")
    print(future_date)
number_days= int(input("Enter the number of days to add to the current date: "))
calculate_future_date()