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

def set_meeting(dic, all_lawyers, needed_lawyers):
    #get_max_hours jest wywoływane dla każdego prawnika
    lawyers = dic.copy()

    longest_time = [0]
    # get_max_hours jest wywoływane dla każdego prawnika
    for this_lawyer in lawyers:
        result = get_max_hours(lawyers, this_lawyer, needed_lawyers) #dla każdego rekordu szuka najlepszego wyniku
        if longest_time[0] < result[0]:
            longest_time = result

    return  longest_time

def read_file_and_create_dictionary():
    dictionary = {}
    file = open("pra.txt", "r")

    first_line = file.readline()
    first_numbers = split_numbers_and_delete_enter(first_line)
    all_lawyers = int(first_numbers[0])
    needed_lawyers = first_numbers[1]
    index = 1

    for row in range(1, all_lawyers):
        next_line = split_numbers_and_delete_enter(file.readline())
        dictionary[index] = next_line
        index += 1

    next_line = split_numbers(file.readline())
    dictionary[index] = next_line

    return dictionary, all_lawyers, needed_lawyers


def split_numbers_and_delete_enter(line):
    numbers = line.split(" ")
    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1][0:-1])
    return numbers

def split_numbers(line):
    numbers = line.split(" ")
    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1])
    return numbers

def write_result_to_file(result):
    print("output in result.txt file: ", result)
    file = open("result.txt", "w")
    meeting_time = str(result[0]) + "\n"
    file.write(meeting_time)

    second_line = ""
    for number_of_lawyer in result[1]:
        second_line += str(number_of_lawyer) + " "

    file.write(second_line)
    file.close()

def init():

    input = read_file_and_create_dictionary()
    dictionary = input[0]
    all_lawyers = int(input[1])
    needed_lawyers = int(input[2])


    output = set_meeting(dictionary, all_lawyers, needed_lawyers)
    write_result_to_file(output)

init()
