class DFA:
    def __init__(self, estados, sigma, delta, e_inicial, e_final):
        self.estados = estados
        self.sigma = sigma
        self.delta = delta
        self.e_inicial = e_inicial
        self.e_final = e_final

    def run(self, cadena):
        if len(cadena) != 0 and cadena[0] not in self.sigma: # Por si la cadena empieza con un caracter que no esta en el alfabeto
            return False
        
        q_actual = self.e_inicial # Estado inicial
        visitados = []

        for caracter in cadena: 
            for d in self.delta: # delta es una lista de listas, entonces itera por cada lista
                if (q_actual in d) and (caracter in d): # Si el estado actual y el caracter esta en la lista, se ejecuta la transicion
                    q_actual = d[2] # Se guarda el estado
                    visitados.append(q_actual)
                    break # Se pasa a la siguiente letra
        
        return q_actual in self.e_final, visitados # Check si el estado en donde termino es parte de los finales
