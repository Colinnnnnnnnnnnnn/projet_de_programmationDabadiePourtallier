from time import perf_counter
from graph import Graph, graph_from_file


def test_routes_n(n, nombre_essais):

    data_path = "input/"
    file_name = "routes."
    numero = str(n)
    g = graph_from_file("input/network." + numero + ".in")
    
    with open(data_path + file_name + numero + '.in', 'r') as file:
        t1_start = perf_counter()
        s = 0
        for i in range(nombre_essais):
            lignei = file.readline().split()
            if len(lignei) > 1:  # premier élément du fichier routes pose problème donc on l'exclut
                ville1 = int(lignei[0])
                ville2 = int(lignei[1])
                g.min_power(ville1, ville2)
            else:
                s += int(lignei[0])
        t1_stop = perf_counter()

    temps_execution = (t1_stop - t1_start) * s / nombre_essais
    print("Temps d'exécution pour le fichier routes " + numero + " en secondes:", temps_execution)
    return temps_execution

test_routes_n(1, 10)
test_routes_n(2, 10)
test_routes_n(3, 10)