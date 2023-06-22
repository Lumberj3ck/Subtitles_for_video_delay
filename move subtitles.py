from time_manager import Timemanager

PATH_TO_FILM = r'D:\Downloads\Guardians.Of.The.Galaxy.Volume.3.2023.1080p.HDTS-C1NEM4[TGx]'
FROM_WHERE = 662
DELAY = 31
file = open('test.txt')
subtitles = file.read()
file.close()
splited = subtitles.split(' --> ')
new_subs = []

for idx, row in enumerate(splited[FROM_WHERE:-1:]):
    if idx == 0:
        previous_row = splited[FROM_WHERE - 1].split('\n')
        previous_row[-1] = Timemanager(previous_row[-1], DELAY, 'sec').result
        splited[FROM_WHERE - 1] = '\n'.join(previous_row)
    lst = row.split('\n')
    start = lst[0]
    end = lst[-1]
    new_start = Timemanager(start, DELAY, 'sec').result
    new_end = Timemanager(end, DELAY, 'sec').result
    lst[0] = new_start
    lst[-1] = new_end
    updated = '\n'.join(lst)
    new_subs.append(updated)

splited = splited[:FROM_WHERE] + new_subs
file = open('test1.txt', 'w')
res = ' --> '.join(splited)
file.write(res)

print('Success')
