users = [
    {"name": "Alex", "age": 33, "city": "Moscow"},
    {"name": "Ivan", "age": 25, "city": "Moscow"},
    {"name": "Anna", "age": 28, "city": "Berlin"},
    {"name": "Bob", "age": 40, "city": "London"}
]


def get_users_by_city(users, city):

    result = []

    for user in users:
        if user["city"] == city:
            result.append(user)

    return result

def sort_users_by_age(users):

    sorted_users = sorted(users, key=lambda user: user["age"])

    return sorted_users

def format_users_text(users):

    info = []

    for user in users:
        info.append(f'{user["name"]}: {user["age"]}')

    return ', '.join(info)

def get_city_report(users, city):

    city_users = get_users_by_city(users, city)

    if city_users == []:
        return "Users not found"

    sorted_users = sort_users_by_age(city_users)

    text = format_users_text(sorted_users)

    return f'Found {len(sorted_users)} users: {text}'



def get_users_older_than(users, age):

    result = []

    for user in users:

        if user["age"] > age:
            result.append(user)

    return result

def get_age_report(users, age):

    older_users = get_users_older_than(users, age)

    if older_users == []:
        return "Users not found"

    sorted_users = sort_users_by_age(older_users)

    text = format_users_text(sorted_users)

    return f'Found {len(sorted_users)} users: {text}'

def get_users_by_age_range(users, min_age, max_age):

    result = []

    for user in users:
        if user["age"] >= min_age and user["age"] <= max_age:
            result.append(user)

    return result 

def get_age_range_report(users, min_age, max_age):

    range_users = get_users_by_age_range(users, min_age, max_age)

    if range_users == []:
        return "Users not found"

    sorted_users = sort_users_by_age(range_users)

    text = format_users_text(sorted_users)

    return f'Found {len(sorted_users)} users: {text}'

def show_menu():

    print("1 - City report")
    print("2 - Age report")
    print("3 - Age range report")
    print("4 - Show all users")
    print("0 - Exit")
    
def run_app():

    while True:

        show_menu()

        choice = input("Choose report: ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            city = input("Enter city: ")

            city_report = get_city_report(users, city)

            print(city_report)

        elif choice == "2":

            try:
                age = int(input("Enter age: "))

                age_report = get_age_report(users, age)

                print(age_report)

            except ValueError:
                print("Please enter a number")    

        elif choice == "3":

            try:
                min_age = int(input("Enter min age: "))
                max_age = int(input("Enter max age: "))

                range_report = get_age_range_report(users, min_age, max_age)

                print(range_report)
                
            except ValueError:
                print("Please enter numbers") 

        elif choice == "4":
            text = format_users_text(users)

            print(text)      

        else:
            print("Wrong choice")
        print()

if __name__ == "__main__":
    run_app()