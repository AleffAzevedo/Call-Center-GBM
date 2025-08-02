
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_call_center_data(num_rows=1000):
    np.random.seed(42)
    
    # Datas
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(num_rows)]
    
    # Indicadores
    indicadores = ['CSAT', 'Nota de Qualidade', 'TMA']
    nome_indicado = np.random.choice(indicadores, num_rows)
    
    # Grupos de Agentes
    grupos_agente = [f'Grupo_{i}' for i in range(5)]
    grupo_agente = np.random.choice(grupos_agente, num_rows)
    
    # Logins (IDs de Agentes)
    logins = [f'Agente_{i}' for i in range(50)]
    login = np.random.choice(logins, num_rows)
    
    # Numerador e Denominador
    numerador = np.random.randint(0, 1000, num_rows)
    denominador = numerador + np.random.randint(1, 500, num_rows)
    
    # Ajustar para TMA (tempo médio de atendimento) - numerador é tempo, denominador é número de chamadas
    for i in range(num_rows):
        if nome_indicado[i] == 'TMA':
            numerador[i] = np.random.randint(60, 1200) # Tempo em segundos
            denominador[i] = np.random.randint(10, 200) # Número de chamadas
        elif nome_indicado[i] == 'CSAT':
            numerador[i] = np.random.randint(0, 100) # Pontuação
            denominador[i] = np.random.randint(1, 100) # Total de pesquisas
        elif nome_indicado[i] == 'Nota de Qualidade':
            numerador[i] = np.random.randint(0, 10) # Pontuação
            denominador[i] = np.random.randint(1, 10) # Total de avaliações

    df = pd.DataFrame({
        'DATA': dates,
        'LOGIN': login,
        'NOME_INDICADO': nome_indicado,
        'NUMERADOR': numerador,
        'DENOMINADOR': denominador,
        'GRUPO_AGENTE': grupo_agente
    })
    
    return df

if __name__ == '__main__':
    df_ficticio = generate_call_center_data(num_rows=5000) # Gerar 5000 linhas de dados
    df_ficticio.to_csv('call_center_data.csv', index=False)
    print('Dados fictícios gerados e salvos em call_center_data.csv')


