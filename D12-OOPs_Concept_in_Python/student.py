def main():
    student = get_student()
    if student["name"] =="Padma":
        student["house"] = "RavenClaw"
    
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House ")
    return student

if __name__ == "__main__":
    main()
 