def parent():
    print("sono in parent!")

    def first_child():
        print("sono in first child!")

    def second_child():
        print("sono in second parent!")

    second_child()
    first_child()

parent()


def decorator(func):
    def wrapper():
        print(f"prima di func")
        func()
        print(f"dopo func")
    return wrapper
    
def ciao():
    print(f"ciao!")

ciao = decorator(ciao)

ciao()


#decorator che calcola il tempo di esecuzione di una funzione

def decorator(func):
    def wrapper(*args):
        import time

        start = time.time()
        func(*args)
        print(f"time elapsed: {time.time() - start}")
    return wrapper
