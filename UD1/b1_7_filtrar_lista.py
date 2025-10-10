lista = ["Ana", "Pedro", "Alba", "Lucía", "Antonio", "Federico"]

for nombres in lista :
    if nombres.startswith(("A", "a")):
        continue
    print(f"Los nombres validos son: {nombres}") # Tiene que estar bien anidados los parametros, porque si se mete en el
                                                # if error y si no esta en el for sale mal.