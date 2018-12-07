input_file = open("songs.csv", "r")
FILES = input_file.readlines()
TOTAL = [0]
REMAINDER = [1]
EXPORT_LIST = []

def main():
    print("Songs To Learn 1.0 - by Tom Nhan")
    first = menu()

def menu():
    print("L - List songs")
    print("A - Add new song")
    print("C - Complete a new song")
    print("Q - Quit")
    option = input("Please select what you would like to do").upper()
    print("-" * 86)
    while option not in ['L', 'A', 'C', 'Q']:
        option = input("Invalid, please re-input appropriate option").upper()
    if option == "L":
        list()
    elif option == "A":
        add()
    elif option == "C":
        complete()
    else:
        confirm = input("Are you sure you want to quit? - (Y) Yes, (N) No ").upper()
        while confirm not in ['Y', 'N']:
            confirm = input("Invalid, please re-input appropriate option").upper()
        if confirm == "Y":
            with open("songs.csv", "w") as input_file:
                for item in FILES:
                    input_file.write("{}".format(item))
            print("=> Updates to your playlist has been saved")
            print("-- Exited playlist --")
            quit()
        else:
            menu()

def list():
    list = []
    count = 0
    count_2 = 0
    for lines in FILES:
        count += 1
        new_lines = lines.split(",")
        song_name = new_lines[0]
        artist_name = new_lines[1]
        year = new_lines[2]
        status = new_lines[3].replace("y", "*").replace("n", "").replace("\n", "")
        list.append(count)
        final_song_list = ("{:>2}. {:<1} {:<35} - {:<35} ({})".format(count, status, song_name, artist_name, year))
        print(final_song_list)
        if "*" in status:
            count_2 += 1
    print("-" * 86)
    print("Total number of songs:", max(list))
    TOTAL.append(max(list))
    print("Number of songs learnt:", max(list) - count_2)
    print("Number of songs left to learn:", count_2)
    REMAINDER.append(count_2)
    print("-" * 86)
    menu()

def add():
    remove_status = "y\n"
    song_name2 = input("Enter title:")
    while song_name2 in [""," ","  ","   "]:
        print("Please enter a song name")
        song_name2 = input("Enter title:")
    artist_name2 = input("Enter artist:")
    while artist_name2 in ["", " ","   ", "   "]:
        print("Please enter artist name")
        artist_name2 = input("Enter artist:")
    flag=True
    while (flag==True):
        try:
            year_2 = int(input("Enter year: "))
            flag=False
        except ValueError:
            print("Invalid input, please enter a number")
    while len(str(year_2)) < 4 or len(str(year_2)) > 4:
        print("Please enter an appropriate year value with 4 numbers")
        year_2 = int(input("Enter year:"))
    if REMAINDER[-1] == 0:
        REMAINDER.remove(REMAINDER[-1])
    result_1 = ("{},{},{},{}".format(song_name2, artist_name2, year_2,remove_status))
    FILES.append(result_1)
    EXPORT_LIST.append(result_1)
    print("{} by {} from ({}) added to song list".format(song_name2, artist_name2, year_2))
    print("-" * 86)
    menu()