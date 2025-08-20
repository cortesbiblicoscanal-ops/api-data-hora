from fastapi import FastAPI
from datetime import datetime, timezone
import pytz

app = FastAPI()

@app.get("/data-hora")
def get_data_hora():
    # Define o fuso horário de Brasília
    fuso_horario_br = pytz.timezone('America/Sao_Paulo')
    
    # Obtém a data e hora atual no fuso horário de Brasília
    agora = datetime.now(fuso_horario_br)
    
    # Formata a data e hora em uma string
    data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
    
    return {
        "data_e_hora": data_formatada,
        "timestamp": agora.timestamp(),
        "fuso_horario": "America/Sao_Paulo"
    }

# Endpoint para obter apenas a data
@app.get("/data")
def get_data():
    fuso_horario_br = pytz.timezone('America/Sao_Paulo')
    agora = datetime.now(fuso_horario_br)
    data_formatada = agora.strftime("%d/%m/%Y")
    
    return {
        "data": data_formatada
    }

# Endpoint para obter apenas a hora
@app.get("/hora")
def get_hora():
    fuso_horario_br = pytz.timezone('America/Sao_Paulo')
    agora = datetime.now(fuso_horario_br)
    hora_formatada = agora.strftime("%H:%M:%S")
    
    return {
        "hora": hora_formatada
    }
