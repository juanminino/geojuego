#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

geo = {"Albania": ["Tirana", "Europa"],
"Alemania": ["Berlín", "Europa"],
"Andorra": ["Andorra la bella", "Europa"],
"Austria": ["Viena", "Europa"],
"Bielorrusia": ["Minsk", "Europa"],
"Bélgica": ["Bruselas", "Europa"],
"Bosnia-herzegovina": ["Sarajevo", "Europa"],
"Bulgaria": ["Sofía", "Europa"],
"Croacia": ["Zagreb", "Europa"],
"Dinamarca": ["Copenhague", "Europa"],
"Eslovaquia": ["Bratislava", "Europa"],
"Eslovenia": ["Liubliana", "Europa"],
"España": ["Madrid", "Europa"],
"Estonia": ["Tallin", "Europa"],
"Federación Rusa": ["Moscú", "Europa"],
"Finlandia": ["Helsinki", "Europa"],
"Francia": ["Paris", "Europa"],
"Grecia": ["Atenas", "Europa"],
"Hungría": ["Budapest", "Europa"],
"Irlanda": ["Dublin", "Europa"],
"Islandia": ["Reikiavik", "Europa"],
"Italia": ["Roma", "Europa"],
"Letonia": ["Riga", "Europa"],
"Liechtenstein": ["Vaduz", "Europa"],
"Lituania": ["Vilna", "Europa"],
"Luxemburgo": ["Luxemburgo", "Europa"],
"Macedonia": ["Skopje", "Europa"],
"Malta": ["La Valetta", "Europa"],
"Moldova": ["Chisinau", "Europa"],
"Mónaco": ["Mónaco-ville", "Europa"],
"Noruega": ["Oslo", "Europa"],
"Países Bajos (Holanda)": ["Amsterdam", "Europa"],
"Polonia": ["Varsovia", "Europa"],
"Afganistán": ["Kabul", "Asia"],
"Angola": ["Luanda", "África"],
"Argelia": ["Argel", "África"],
"Antigua y Barbuda": ["Saint John", "América"],
"Argentina": ["Buenos Aires", "América"],
"Barbados": ["Bridgetown", "América"],
"Bahamas": ["Nasau", "América"],
"Armenia": ["Erevan", "Asia"],
"Arabia saudita": ["Riad", "Asia"],
"Azerbaiyan": ["Baku", "Asia"],
"Bangladés": ["Daca", "Asia"],
"Baréin":["Manama", "Asia"],
"Australia": ["Canberra", "Oceanía"], 
"Belice": ["Belmopan", "América"],
"Benin": ["Porto-novo",	"África"],
"Birmania": ["Naipyido", "Asia"],
"Bolivia": ["Sucre", "América"],
"Botsuana":	["Gaborone", "África"],
"Brasil": ["Brasilia",	"América"],
"Brunéi": ["Bandar Seri Begawan", "Asia"],
"Burkina faso":	["Uagadugu", "África"],
"Burundi": ["Buyumbura", "África"],
"Butan": ["Thimphu", "Asia"],
"Cabo Verde": ["Praia", "África"],
"Camboya": ["Nom pen", "Asia"],
"Camerun": ["yaundé", "África"],
"Canada": ["Ottawa", "América"],
"Catar": ["Doha", "Asia"],
"Chad": ["yamena", "África"],
"Chile": ["Santiago", "América"],
"China": ["Pekín", "Asia"],
"Colombia": ["Bogotá", "América"],
"Comoras": ["Moroni", "África"],
"Congo": ["Brazzaville", "África"],
"Corea del Norte": ["Pionyang", "Asia"],
"Corea del Sur": ["Seul", "Asia"],
"Costa de Marfil": ["Yamusukro", "África"],
"Costa rica": ["San José", "América"],
"Cuba": ["La Habana",	"América"],
"Dominica": ["Roseau", "América"],
"Ecuador": ["Quito", "América"],
"Egipto": ["El Cairo", "África"],
"El salvador": ["San Salvador",	"América"],
"Emiratos Árabes Unidos": ["Abu Dabi", "Asia"],
"Eritrea": ["Asmara", "África"],
"Estados unidos": ["Washington D.C.", "América"],
"Estonia": ["Tallin", "Europa"],
"Etiopia": ["Adis Abeba", "África"],
"Filipinas": ["Manila",	"Asia"],
"Fiyi":	["Suva", "Oceanía"],
"Gabon": ["Libreville", "África"],
"Gambia": ["Banjul", "África"],
"Georgia": ["Tiflis", "Asia"],
"Ghana": ["Accra", "África"],
"Granada": ["Saint George", "América"],
"Guatemala": ["Guatemala", "América"],
"Guinea	": ["Conakri", "África"],
"Guinea ecuatorial": ["Malabo",	"África"],
"Guinea-bisau": ["Bisau", "África"],
"Guyana": ["Georgetown", "América"],
"Haiti": ["Puerto principe",	"América"],
"Honduras": ["Tegucigalpa", "América"],
"India": ["Nueva delhi", "Asia"],
"Indonesia": ["yakarta", "Asia"],
"Irak":	["Bagdad",	"Asia"],
"Iran":	["Teheran",	"Asia"],
"Islas marshall": ["Majuro", "Oceanía"],
"Islas salomon": ["Honiara", "Oceanía"],
"Israel": ["Jerusalén",	"Asia"],
"Jamaica": ["Kingston", "América"],
"Japon": ["Tokio", "Asia"],
"Jordania": ["Aman", "Asia"],
"Kazajistan": ["Astana", "Asia"],
"Kenia": ["Nairobi", "África"],
"Kirguistan": ["Biskek", "Asia"],
"Kiribati": ["Tarawa", "Oceanía"],
"Kuwait": ["Kuwait city", "Asia"],
"Laos": ["Vientian", "Asia"],
"Lesoto": ["Maseru", "África"],
"Libano": ["Beirut", "Asia"],
"Liberia": ["Monrovia", "África"],
"Libia": ["Tripoli", "África"],
"Madagascar": ["Antananarivo", "África"],
"Malasia": ["Kuala lumpur", "Asia"],
"Malaui": ["Lilongüe", "África"], #lilongüe
"Maldivas": ["Malé", "Asia"],
"Mali":	["Bamako", "África"],
"Marruecos": ["Rabat", "África"],
"Mauricio": ["Port louis", "África"],
"Mauritania": ["Nuakchot", "África"],
"México": ["México", "América"],
"Micronesia": ["Palikir", "Oceanía"],
"Mongolia": ["Ulan bator", "Asia"],
"Mozambique": ["Maputo", "África"],
"Namibia": ["Windhoek", "África"],
"Nauru": ["yaren", "Oceanía"],
"Nepal": ["Katmandu", "Asia"],
"Nicaragua": ["Managua", "América"],
"Niger": ["Niamey", "África"],
"Nigeria": ["Abuya", "África"],
"Nueva zelanda": ["Wellington", "Oceanía"],
"Oman": ["Mascate", "Asia"],
"Pakistan": ["Islamabad", "Asia"],
"Palaos": ["Melekeok", "Oceanía"],
"Palestina": ["Jerusalén Este", "Asia"],
"Panama": ["Panama", "América"],
"Papua nueva guinea": ["Puerto Moresby", "Oceanía"],
"Paraguay": ["Asuncion", "América"],
"Peru": ["Lima", "América"],
"República Centroafricana": ["Bangui", "África"],
"República Checa": ["Praga", "Europa"],
"República Democratica del Congo": ["Kinsasa", "África"],
"República Dominicana": ["Santo Domingo", "América"],
"Ruanda": ["Kigali", "África"],
"Samoa": ["Apia", "Oceanía"],
"San cristobal y nieves": ["Basseterre", "América"],
"San marino": ["San marino", "Europa"],
"San Vicente y las granadinas": ["Kingstown", "América"],
"Santa lucia": ["Castries", "América"],
"Santo tomé y principe": ["Santo tomé", "África"],
"Senegal": ["Dakar", "África"],
"Seychelles": ["Victoria", "África"],
"Sierra leona": ["Freetown", "África"],
"Singapur": ["Singapur", "Asia"],
"Siria": ["Damasco", "Asia"],
"Somalia": ["Mogadiscio", "África"],
"Sri lanka": ["Sri Jayawardenapura Kotte", "Asia"],
"Suazilandia": ["Mbabane", "África"],
"SudÁfrica": ["Pretoria", "África"],
"Sudan": ["Jartum", "África"],
"Sudan del sur": ["Yuba", "África"],
"Surinam": ["Paramaribo", "América"],
"Tailandia": ["Bangkok", "Asia"],
"Taiwan": ["Taipéi", "Asia"],
"Tanzania": ["Dodoma", "África"],
"Tayikistan": ["Dusambé", "Asia"],
"Timor oriental": ["Dili", "Oceanía"],
"Togo": ["Lomé", "África"],
"Tonga": ["Nukualofa", "Oceanía"],
"Trinidad y tobago": ["Puerto España", "América"],
"Tunez": ["Tunez", "África"],
"Turkmenistan": ["Asjabad", "Asia"],
"Turquia": ["Ankara", "Asia"],
"Tuvalu": ["Funafuti", "Oceanía"],
"Uganda": ["Kampala", "África"],
"Uruguay": ["Montevideo", "América"],
"Uzbekistan": ["Taskent", "Asia"],
"Vanuatu": ["Port Vila", "Oceanía"],
"Vaticano": ["Vaticano", "Europa"],
"Venezuela":["Caracas",	"América"],
"Vietnam": ["Hanoi", "Asia"],
"Yemen": ["Sana", "Asia"],
"Yibuti": ["yibuti", "África"],
"Zambia": ["Lusaka", "África"],
"Zimbabue": ["Harare", "África"],
}



#igualar paises bajos a holanda con algun if
#contemplar con if cuando pais y capital es igual si se hace seleccion inteligente
#que el usuario solo ponga pais o capital y elp rograma deba detectar cual de los dos es,
#para en ese caso preguntar a cual de las dos hace referencia

"""Print(geo["Albania"][0])
print(" ")"""
#capital = (geo["Andorra"][0])

#x = raw_input("Dale : ")
#x = x.lower()



#print("La capital de")
#"Federacion rusa"
#"Hungria"
#"Monaco"



#capital = geo[x][0]
#continente = geo[x][1]

#def capital_azar():
#    country, capital_continente = random.choice(list(geo.items()))
#    return capital_continente[0]
#.title()

#memo = capital_azar()
#print("viene memooo")
#print(memo)

#print(country)
#print(capital_continente)

#print("La capital de: " + country + " es: a) Madrid b) " + capital_continente[0] + " c) Kirigali")



#print("La capital de " + x.capitalize() + " es: " + capital.title() + ". " + x.title() + " pertenece al continente: " + continente.title())



#tonta_lista = ["a", "b", "c"]
#print(tonta_lista)
#random.shuffle(tonta_lista)
#print(tonta_lista)

#mas_tonta = ["2", "3", "4", "5"]

#print(azar)

#print(list(geo.keys())[list(geo.values()).index("damasco")])
#print(geo["damasco"])
#print (geo["Siria"][0])

#for element in geo:
#    if geo[element][0] == "Damasco": #en "Damasco" poner variable de capital random elegida                             #por el programa
#        pais_ganador = element
#        print(pais_ganador)

def juego_continente():
    def adivina_continente():
        continente_secreto = ""
        continente_secreto =  random.choice(list(geo.items()))
        return continente_secreto

    continente = adivina_continente()
    print("pais para adivinar continente: " + continente[0])
    #print("continente secreto: " + continente[1][1])
    respuesta_usuario= input("a)América, b)Europa, c)Asia, d)África, e)Oceanía, Su respuesta es: ")


    if(respuesta_usuario == "a"):
        respuesta_usuario = "América"
    if(respuesta_usuario == "b"):
        respuesta_usuario = "Europa"
    if(respuesta_usuario == "c"):
        respuesta_usuario = "Asia"
    if(respuesta_usuario == "d"):
        respuesta_usuario = "África"
    if(respuesta_usuario == "e"):
        respuesta_usuario = "Oceanía"
    if(respuesta_usuario == continente[1][1]):
        print("¡Respuesta correcta, Muy bien hecho!")
    else:
        print("¡No caballo!, " + continente[1][1] + " es el continente al que pertenece " + continente[0])    
    repetir = input("Desear seguir jugando? [s = si, n = no] ")
    if(repetir == "s"):
        juego_continente()
    else:
        print("¡Adiós!, espero te hayas divertido")
    

juego_continente()

