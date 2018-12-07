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