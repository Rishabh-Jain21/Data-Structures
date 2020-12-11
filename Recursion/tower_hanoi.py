def tower(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print('Move disk 1 from '+from_rod+' to rod '+to_rod)
        return

    tower(n-1, from_rod, aux_rod, to_rod)
    print('Move disk '+str(n)+' from '+from_rod+' to rod '+to_rod)
    tower(n-1, aux_rod, to_rod, from_rod)


n = 4
tower(n, 'A', 'C', 'B')
