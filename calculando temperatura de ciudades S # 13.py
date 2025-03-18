inport:requests

def main():
    ciudad = input("ingrese una ciudad")
    url = f"https://es.wttr.in/{city}?format=j1"

    respuesta = requests.get(url)
    weather_dic = respuesta.json ()

    temp_c = weather_dic["estado_actual"][0]["temp_c"]
    desc_temp =weather_dic["estado actual"][0]["lang_es"]
    desc_temp = desc_temp[0]["value"]
    print(f"La temperaturaactual de {city} es {temp_c}°c. {desc_temp}.")

if _name_=="_main":
    main()
