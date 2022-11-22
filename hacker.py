import whois

from past.builtins import raw_input

dominio = raw_input("ALVO: ")
consulta_whois = whois.whois(dominio)

#print consulta whois.name

print(consulta_whois.text)
