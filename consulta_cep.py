import requests

class ConsultaCep:
    def __init__(self, documento) -> None:
        documento = str(documento)
        if self.validaCep(documento):
            self.cep = documento
        else:
            raise ValueError("CEP Inválido!")

    def validaCep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def formataCep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])
    
    def __str__(self) -> str:
        return self.ConsultaApi
    
    def ConsultaApi(self):
        url = "viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        return r.json()



        