from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
     return "Hola a todos, quieres saberl 11 inicial del PSG"

@app.get("/PlantillaPSG/{num}")
def PSG(num):
    Plantilla={
    "1":"Donnarumma",
    "2":"Ramos",
    "3":"Marquinhos",
    "4":"Kimpembe",
    "5":"Hakimi",
    "6":"Verratti",
    “7”:”Paredes”,
    “8”:”Bernart”,
    “9”:”Mbappe”,
    “10”:”Messi”,
    “11”:”Neymar”
         
    }
    return (PSG[num])
@app.get("/Conversor_CaF/{C}")
def conversorCaF(C):
    try:
            C=float(C)
            TF=C*(9/5) + 32
            return f"La temperatura es de {TF} grados Farenheit"
    except:
            return "Entrada invalida"
@app.get("/RevisarEdad/{E1}/{E2}")
def revisar_edades(E1,E2):
    E1=int(E1)
    E2=int(E2)
    if E1>E2+30:
     return "Podria ser su abuelo"
    elif E1>E2+15:
     return "Podrias ser su padre"
    elif E1>E2:
     return "Eres mayor"
    elif E2>E1+30:
     return "Podria ser tu abuelo"
    elif E2>E1+15:
     return "Podria ser tu padre"
    elif E2>E1:
     return "Es mayor que tu"
    else:
     return "Tienen la misma edad"