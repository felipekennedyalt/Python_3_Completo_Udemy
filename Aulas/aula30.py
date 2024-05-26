"""
CONSTANTE = "Variáveis" que não vao mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está 
RADAR_RANGE = 1 # A distaância onde o radar pega

velocidade_carro_ao_passar_radar1 = velocidade > RADAR_1
carro_passsou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passsou_radar1 and velocidade_carro_ao_passar_radar1

print(velocidade_carro_ao_passar_radar1)
print(carro_passsou_radar1)

if velocidade_carro_ao_passar_radar1:
    print("Você está acima da velocidade permitida no radar 1")

if carro_multado_radar_1:
    print("Carro multado em Radar 1")
    