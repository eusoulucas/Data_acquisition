from aquisicao import LiveGraph

titulo = "Gráfico" #str(input("Digite o titulo do seu gráfico: "))
intervalo = int(input("Digite o intervalo entre as plotagens: "))
canal = "Dev1/ai0" #str(input("Digite o canal de aquisição: "))
taxa_de_aquisicao = float(input("Digite a taxa de aquisição: "))
tempo_ct = float(input("Tempo de C/T [s]: "))
taxa_arm = float(input("Taxa de armazenamento: "))

graph = LiveGraph(titulo, intervalo, canal, taxa_de_aquisicao, tempo_ct, taxa_arm)
graph.plot()