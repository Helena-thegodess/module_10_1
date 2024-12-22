import threading
import time
from datetime import datetime

time_st1 = datetime.now()

def wite_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf=8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1} \n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')


time_end1 = datetime.now()
time_result = time_end1 - time_st1
print(f'Работа потоков {time_result}')

time_st2 = datetime.now()

thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time_end2 = datetime.now()
time_result2 = time_end2 - time_st2
print(f'Работа потоков {time_result2}')