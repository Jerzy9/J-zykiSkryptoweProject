def max(a, b):
    if a > b:
        return a
    return b

def min(a, b):
    if a < b:
        return a
    return b

def get_max_hours(lawyers, this_lawyer, needed_lowyers):
    #dla tego czasu szuka największego możliwego czasu innego prawnika
    lawyers_copy = lawyers.copy()                      #tworzy kopie słownika z której potem bedzie usuwać wybranych prawników

    this_start_time = lawyers_copy.get(this_lawyer)[0]
    this_end_time = lawyers_copy.get(this_lawyer)[1]

    # usuwamy z listy aktulanie wybranego pracownika, żeby nie porównywać go z samym sobą
    lawyers_copy.pop(this_lawyer)

    max_start = 0                               #godzina rozpoczęcia spotkania
    min_end = 0                                 #godzina zakończenia spotkania
    lawyers_at_meeting = list()                 #indexy prawników ktorzy są na output
    lawyers_at_meeting.append(this_lawyer)
    start_meeting = 0
    end_meeting = 100

    for needed_lawyer in range(1, needed_lowyers):
        max_time = 0  # długość spotkania

        for lawyer in lawyers_copy:

            bigger_start = max(this_start_time, lawyers_copy.get(lawyer)[0])
            smaller_end = min(this_end_time, lawyers_copy.get(lawyer)[1])
            time = smaller_end - bigger_start

            # szuka prawnika z największym możliwym czasem do aktulanie porównywanego
            # którego godziny startu i końca wolnego czasu mieszczą się w granicy poprzednich prawników
            if max_time < time and start_meeting <= bigger_start and end_meeting >= smaller_end:
                max_time = time
                max_start = bigger_start
                min_end = smaller_end
                index_to_drop = lawyer

        # uaktualnienie godzin spotkania
        start_meeting = max(max_start, start_meeting)
        end_meeting = min(min_end, end_meeting)

        # jeżeli został znaleziony pasujący prawnik do wcześniej wybranych to:
        if(index_to_drop in lawyers_copy):
            lawyers_copy.pop(index_to_drop)     #usuwa prawnika który został wybrany
            lawyers_at_meeting.append(index_to_drop)    #ale również dodaje go do wyniku
        # jeżeli nie, to zwróć 0
        else:
            return [0]

    return [max_time, lawyers_at_meeting]           #zwraca maksymalny czas spotkania i liste prawników którzy wzieli w niej udział

def set_meeting(dic):
    #get_max_hours jest wywoływane dla każdego prawnika

    all_lawyers = dic.get(0)[0]         #liczba wszystkich pracowników
    needed_lawyers = dic.get(0)[1]      #liczba potrzebnych poracownników na spotkaniu
    lawyers = dic.copy()
    lawyers.pop(0)                      #usuwa pierwszy rekord z informacją, zostają juz tylko prawnicy

    longest_time = [0]
    # get_max_hours jest wywoływane dla każdego prawnika
    for this_lawyer in lawyers:
        result = get_max_hours(lawyers, this_lawyer, needed_lawyers) #dla każdego rekordu szuka najlepszego wyniku
        if longest_time[0] < result[0]:
            longest_time = result

    print(longest_time)

def read_file_and_create_dictionary():
    dictionary = {}
    file = open("pra.txt", "r")

    first_line = file.readline()
    first_numbers = split_numbers_and_delete_enter(first_line)
    all_lawyers = int(first_numbers[0])
    needed_lawyers = first_numbers[1]
    index = 0
    for row in file:
        next_line = split_numbers_and_delete_enter(row)
        dictionary
        index += 1


def split_numbers_and_delete_enter(line):
    numbers = line.split(" ")
    numbers[1] = numbers[1][:1]
    return numbers


def init():
    dictionary1 = {
        0:[6,3],
        1:[3, 8],
        2:[4, 12],
        3:[2, 6],
        4:[1, 10],
        5:[5, 9],
        6:[11, 12]
    }

    dictionary2 = {
        0: [6, 3],
        1: [1, 11],
        2: [2, 9],
        3: [3, 4],
        4: [9, 12],
        5: [9, 12],
        6: [9, 12]
    }

    # set_meeting(dictionary1)
    read_file_and_create_dictionary()
init()
