month_list = [    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
def main():
    while True:
        try:
            input_date = input("Date: ")
            month , date , year = map(int,input_date.split("/"))
            #Checking that month and date are totally in the range 
            if(check_date(date) and check_month(month)):
                index = check_month(month)
                print(f"{year}-{index}-{date}")
                break
            else:
                continue
                
        except(ValueError):
            date_month , year = input_date.split(", ")
            month , date = date_month.split(" ")
            #Changed date into int as it has been compared with the number in check_date func
            date = int(date)
            year = int(year)

            if(check_date(date) and check_month(month)):
                month_index = check_month(month)
                print(f"{year}-{month_index}-{date}")
                break
            else:
                continue

def check_date(date):
    if(date > 31 ):
        return False
    else:
        return True

def check_month(month):
    if(month in month_list):
            index = month_list.index(month) + 1
            return index
    elif(month > 12):
        return False
    else:
        return month
        
main()

