from urllib import request
import requests
import json
import pandas as pd
import time
import os

while True:    

    data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

    json_data = json.loads(data.content)

    candidato = []
    partido = []
    votos = []
    porcentagem = []

    for informacoes in json_data['cand']:

        if int(informacoes['seq']) in range(1,12):
            candidato.append(informacoes['nm'])
            votos.append(informacoes['vap'])
            porcentagem.append(informacoes['pvap'])

    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns = [
        'Candidato', 'Nº de Votos', 'Porcentagem'
    ])
    
    print(votos)
    diferenca1 = []
    diferenca1.append(str(int(votos[0])-int(votos[1])))
    diferenca1 = ''.join(diferenca1)
    contador = 0
    print(diferenca1)
    
    diferenca = []
    
    for c in diferenca1:
        print(c)
        diferenca.append(c)

        contador +=1
        if contador == 3:
            contador = 0
            diferenca.append('.')
            print('.')


    #print(''.join(diferenca))
    ultimo = len(diferenca)-1
    print(ultimo)
    print(diferenca)
    
    
    diferenca[ultimo] = ''
    diferenca = ''.join(diferenca)
    print(diferenca)


    if os.name == "posix":
        os.system("clear")
        print(df_eleicao)
        print(" ")
        print("Porcentagem das Urnas Apuradas: " + json_data['pst'] + "%")
        
        
        print("Diferenca: ", diferenca )
        time.sleep(30)

    elif os.name == "nt":
        os.system("cls")
        print(df_eleicao)
        print(" ")
        print("Porcentagem das Urnas Apuradas: " + json_data['pst'] + "%")
        time.sleep(30)


