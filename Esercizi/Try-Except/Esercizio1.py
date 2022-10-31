import time

count = 0
while (True):
    print(f"elaborazione n.: {count}")
    time.sleep(1)
    count += 1
    try: #try = prova, se va male trova una soluzione
        print(n)
    except:
        print("Si è verificato un errore")
