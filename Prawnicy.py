
def set_meeting(dic):
    #słownik musi być posortowany od najwiekszego czasu pracy do najmniejszego
    #get_max_hours jest wywoływane dla każdego pracownika

    all_lawyers = dic.get(0)[0]         #liczba wszystkich pracowników
    needed_lawyers = dic.get(0)[1]      #liczba potrzebnych poracownników na spotkaniu
    dic_cut = dic.copy()
    dic_cut.pop(0)                          #usuwa pierwszy rekord z informacją, zostają juz tylko pracownicy
    # print(dic_cut)

    max_resault = 0
    for i in dic_cut:
        resault = get_max_hours(dic_cut, i, needed_lawyers) #dla każdego rekordu szuka najlepszego wyniku
        max_resault = max(max_resault, resault[0])
        print("RESAULT: ", resault)
    print(max_resault)


def get_max_hours(diction, index, needed_lowyers):
    #dla tego czasu szuka największego możliwego czasu innego prawnika

                #!pytanie czy jak szuka najlepszego czasu dla nie pierwszego pracownika, to czy ma zaczynać od niego i lecieć w dól,
                #!czy może w dół a później od góry?
                #!czy od samej góry do dołu omijając siebie (TAK JEST narazie zaimplementowane)

    dic_copy = diction.copy()                      #tworzy kopie słownika z której potem bedzie usuwać wybranych prawników

    # print(dic)

    this_start_time = dic_copy.get(index)[0]
    this_end_time = dic_copy.get(index)[1]

    min_start = 0                       #godzina rozpoczęcia spotkania
    max_end = 0                         #godzina zakończenia spotkania
    indexs = list()                     #indexy prawników ktorzy są na output
    indexs.append(index)
    start_meeting = 0
    end_meeting = 100

    for j in range(1, needed_lowyers):
        max_time = 0  # długość spotkania


        for i in dic_copy:
            if(i != index): # pętla skipuje czas this_prawnika
                # print("i: ", i)
                #szuka największego możliwego czasu
                # if(min_start):
                bigger_start = max(this_start_time, dic_copy.get(i)[0])
                smaller_end = min(this_end_time, dic_copy.get(i)[1])
                # if(min_start>= bigger_start and max_end<=smaller_end):
                time = smaller_end - bigger_start

                if (index == 1):
                    print("start_meeting: ", start_meeting)
                    print("end meeting: ", end_meeting)

                if max_time < time and start_meeting <= bigger_start and end_meeting >= smaller_end:
                    max_time = time
                    min_start = bigger_start
                    max_end = smaller_end
                    index_to_drop = i
                    # if(index == 4):
                    #     print("bigger start: ", bigger_start)
                    #     print("smaller end: ", smaller_end)
                    #     print("time: ", time)
                    #     print("min start: ", min_start)
                    #     print("max_end: ", max_end)
                    #     print("-----")

        start_meeting = max(min_start, start_meeting)
        end_meeting = min(max_end, end_meeting)


        if(index_to_drop in dic_copy):
            dic_copy.pop(index_to_drop)     #usuwa prawnika który został wybrany
            indexs.append(index_to_drop)    #ale również dodaje go do wyniku
        else:
            return [0]
        # if(index == 4):

            # print("after: ",dic_copy)
            # print("indexs: ", indexs)
            # print("index of ROW: ", index)
            # print("index to drop: ", index_to_drop)
            # print("len: ", len(dic_copy))
            # print("------------------")


    return [max_time, indexs]           #zwraca maksymalny czas spotkania i liste prawników którzy wzieli w niej udział



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
        1: [1, 12 ],
        2: [2, 9],
        3: [3, 4],
        4: [9, 12],
        5: [9, 12],
        6: [9, 12]
    }
    # set_meeting(dictionary1)

    set_meeting(dictionary2)

init()