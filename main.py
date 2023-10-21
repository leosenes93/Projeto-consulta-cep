from consulta_cep import ConsultaCep

cep = "88107387"
mostracep = ConsultaCep(cep)

#print(mostracep)

obj = mostracep.ConsultaApi()
bairro, cidade, uf = mostracep.ConsultaApi()
print(bairro, cidade, uf)
