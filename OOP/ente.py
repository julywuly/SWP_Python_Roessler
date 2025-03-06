def sum_recursive(*args):
    if not args:
        return 0
    else:

        return args[0] + sum_recursive(*args[1:])


result = sum_recursive(1, 2, 3, 4, 5)
print(result)


def beispiel_funktion(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


beispiel_funktion(1, 2, 3, name="Mario", level=5)


def kombi_funktion(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print("Args:", args)
    print("Kwargs:", kwargs)


kombi_funktion(10, 20, "extra", x=100, y=200)


def fehlerhafte_funktion(*args, a, b):
    print(f"a: {a}, b: {b}")
    print("Args:", args)


fehlerhafte_funktion(1, 2, 3)


def inner_funktion(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")


def outer_funktion(*args, **kwargs):
    inner_funktion(*args, **kwargs)


outer_funktion(1, 2, c=3)


def aussere_funktion(a, b):
    print(f"Äußere Funktion: a = {a}, b = {b}")

    def erste_innere_funktion(c):
        print(f"  Erste Innere Funktion: c = {c}")

        def zweite_innere_funktion(d):
            print(f"    Zweite Innere Funktion: d = {d}")
            return a + b + c + d

        return zweite_innere_funktion

    return erste_innere_funktion


aufruf_erste = aussere_funktion(1, 2)
aufruf_zweite = aufruf_erste(3)
ergebnis = aufruf_zweite(4)

print(f"Ergebnis der Berechnung: {ergebnis}")
