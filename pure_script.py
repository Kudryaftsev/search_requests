#   Скрипт, решающий следующие задачи:
#
#   1) Определить количество поисковых запросов в определенном .txt;
#   2) Определить количество сегментов запросов;
#   3) Определить самый популярный сегмент среди этих запросов.

#   Импортируем библиотеки, с которыми мы будем работать:
import re
from collections import Counter

#   Задаем пустые списки, с которыми мы будем работать
all_results = []    #   Все результаты
all_misses = []     #   Все пропуски

#   Задаем pattern для поиска запросов
pattern = r'\w+'

#   Путь к файлу, в котором находятся запросы
file_way = input( 'Введите путь к файлу: ' )

#   Функция поиска и сортировки
def do_search_n_sort( file_way ):
    with open( file_way, 'r' ) as file:
        for row in file:
            coincidence = re.findall( pattern, row )    #   ищем совпадения построчно
            if len(coincidence) > 0:
                all_results.append( coincidence[0] )
            else:
                all_misses.append( coincidence )
        
    sort_all_results = Counter( all_results ).most_common() #   Сортируем по убыванию

    print( 'Количество поисковых запросов: ', len(all_results) )
    print( 'Количество сегментов поисковых запросов: ', len(sort_all_results) )
    print( 'Самый популярный сегмент: ', sort_all_results[0] )
    print( 'Распределение по сегментам в порядке убывания: ' )
    for i in sort_all_results:
        print( i )

do_search_n_sort( file_way )