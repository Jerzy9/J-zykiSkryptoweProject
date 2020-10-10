
def set_meeting(dic):
    #słownik musi być posortowany od najwiekszego czasu pracy do najmniejszego
    #get_max_hours jest wywoływane dla każdego pracownika

    all_lawyers = dic.get(0)[0]         #liczba wszystkich pracowników
    needed_lawyers = dic.get(0)[1]      #liczba potrzebnych poracownników na spotkaniu
    dic = dic.pop(0)                    #usuwa pierwszy rekord z informacją, zostają juz tylko pracownicy

    for i in dic:
        get_max_hours(dic, i, needed_lawyers) #dla każdego rekordu szuka najlepszego wyniku
        #TUTAJ wybrać tylko ten "get_max" gdzie będzie największa ilość godzin


def get_max_hours(dic, index, needed_lowyers):
    #dla tego czasu szuka największego możliwego czasu innego prawnika

                #!pytanie czy jak szuka najlepszego czasu dla nie pierwszego pracownika, to czy ma zaczynać od niego i lecieć w dól,
                #!czy może w dół a później od góry?
                #!czy od samej góry do dołu omijając siebie (TAK JEST narazie zaimplementowane)

    dic_copy = dic                      #tworzy kopie słownika z której potem bedzie usuwać wybranych prawników

    this_start_time = dic.get(index)[0]
    this_end_time = dic.get(index)[1]

    min_start = 0                       #godzina rozpoczęcia spotkania
    max_end = 0                         #godzina zakończenia spotkania
    max_time = 0                        #długość spotkania
    indexs = list()                     #indexy prawników ktorzy są na output

    for j in range(1, needed_lowyers+1):

        for i in dic:
            if(i != index): # pętla skipuje czas this_prawnika
                #szuka największego możliwego czasu
                bigger_start = max(this_start_time, dic.get(i)[0])
                smaller_end = min(this_end_time, dic.get(i)[1])
                time = smaller_end - bigger_start

                #jeżeli jest większy od tego wczęsniej posiadanego to zamamienia wszystkie poniższe argumenty
                if max_time < time:
                    max_time = time
                    min_start = bigger_start
                    max_end = smaller_end
                    index_to_drop = i


        dic_copy.pop(index_to_drop)     #usuwa prawnika który został wybrany
        indexs.append(index_to_drop)    #ale również dodaje go do wyniku

    return [max_time, indexs]           #zwraca maksymalny czas spotkania i liste prawników którzy wzieli w niej udział



def init():
    dictionary = {
        0:[6,3],
        1:[3, 8],
        2:[4, 12],
        3:[2, 6],
        4:[1, 10],
        5:[5, 9],
        6:[11, 12]
    }


    set_meeting(dictionary)


init()