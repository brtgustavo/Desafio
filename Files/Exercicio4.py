velocidade_carro = 110
velocidade_caminhao = 80
distancia_total = 100 
tempo_pedagio = 10 # tempo em minutos

distancia_carro = ((velocidade_carro * ((distancia_total/2))) / (velocidade_carro + velocidade_caminhao)) + ((velocidade_carro * (tempo_pedagio/60)))

distancia_restante_carro = distancia_total - distancia_carro

distancia_caminhao = (velocidade_caminhao * ((distancia_total/2)-(tempo_pedagio/60))) / (velocidade_caminhao + velocidade_carro) + ((velocidade_caminhao * (tempo_pedagio/60)))

distancia_restante_caminhao = distancia_total - distancia_caminhao

print("O carro estará a", distancia_restante_carro, "km de Ribeirão Preto quando os veículos se cruzarem.")

print("O caminhão estará a", distancia_restante_caminhao, "km de Ribeirão Preto quando os veículos se cruzarem.")

if (distancia_restante_caminhao < distancia_restante_carro):
    print("Caminhão está mais perto")
else:
    print("Carro está mais perto")
