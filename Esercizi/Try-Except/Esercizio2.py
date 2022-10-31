try: #try = prova, se va male trova una soluzione
        print(n)
except NameError:
    print("Si è verificato un errore nella variabile n")
except:
    print("Errore generico")
else: #oppure finally ma porta al termine il suo obbiettivo
    print("Tutto bene")