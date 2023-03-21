import view
import database

def main() :
    while True :
        request = view.choice()
        if request == 1:
            user = view.get_person()
            database.write_data(user)
        if request == 2:
            users = database.read_data()
            name = view.ask_person()
            database.find_person(users, name )
        if request == 3:
            database.print_all()
        else:
            break
            


if __name__ == "__main__" :
    main()  