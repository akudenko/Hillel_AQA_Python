# Занятия проходят по понедельникам и четвергам в 19:15
# Первое занятие произошло 17.10.2022. Всего 32 занятия.
# Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):
#
# Lecture  1: 17 Oct 2022 19:15
# Lecture  2: 20 Oct 2022 19:15
# ...
# Lecture  9: 14 Nov 2022 19:15
# Lecture 10: 17 Nov 2022 19:15
# ...
# Lecture 32: 02 Feb 2023 19:15

from datetime import timedelta, datetime

time_lst = []
first_lecture = datetime(2022, 10, 17, 19, 15, 00)
delta_3_days = timedelta(days=3)
delta_4_days = timedelta(days=4)

for i in range(32):
    strf = first_lecture.strftime('%d %b %Y  %H:%M')
    if i % 2 == 0:
        first_lecture += delta_3_days
        time_lst.append(f'Lecture {i + 1:>3}: {strf}')
    else:
        first_lecture += delta_4_days
        time_lst.append(f'Lecture {i + 1:>3}: {strf}')

for i in time_lst:
    print(i)
