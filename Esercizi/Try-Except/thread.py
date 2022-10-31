import threading
import time

def mythread(name, wait):
    print(f"Io sono {name}, sto partendo")
    time.sleep(int(wait))
    print(f"Io sono {name}, ho finito")

if __name__ == "__main__":
    #target fa eseguire la funzione e args da i parametri daemon questo thread è un demone
    x = threading.Thread(target=mythread, args=('esecutore1',2, daemon=True))
    print("MAIN: avvio")
    x.start()
    print("MAIN: attendo il thread")
    x.join()
    print("MAIN: fine")