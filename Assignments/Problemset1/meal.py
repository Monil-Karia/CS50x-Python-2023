def main():
    input_time = input("What the time: ")
    converted_time = convert(input_time)
    if(converted_time >= 12.0 and converted_time <= 13.0):
        print("Lunch time")
    elif(converted_time >= 7.0 and converted_time <= 8.0):
        print("Breakfast time")
    elif(converted_time >= 18.0 and converted_time<=19.0):
        print("Dinner time")
    else:
        print("Galat time hai re baba")


def convert(time):
    hours , pm_or_am  = time.split(" ")
    hours , minutes  = hours.split(":")
    minutes = float(minutes)
    hours = int(hours)
    
    if(pm_or_am == "pm" and hours< 12):
        hours = hours + 12
    elif(hours == 12 and pm_or_am == "pm"):
        hours = hours
    else:
        hours = hours
    
    # minutes = minutes/60
    # time = hours + minutes
    return hours + minutes/60


main()
