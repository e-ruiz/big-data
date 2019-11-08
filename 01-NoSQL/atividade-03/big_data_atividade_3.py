import pprint, random

class Cliente():
    _nomes = ['ERIC RUIZ', 'ROBERTA DE LIMA', 'DEIVIDI SCALZAVARA', 'ADOLFO NETO', 'JOSE MONESTEL', 'WAGNER CORREIA', 'JACEGUAY ZUKOSKI', 'MICHEL SOUZA', 'MAYRA RODRIGUES', 'MICHEL DUARTE', 'MARCIO FOSSA', 'MARCEL BORNANCIN', 'ELOISA PERIN', 'TIAGO WIPPEL', 'LUCAS FISCHER', 'DIEGO PRANDO', 'ADRIANO WEIGUERT NAGASAVA', 'FERNANDO MIRANDA', 'LUIS MONTES', 'MARCELO DE SOUZA']
    _ruas = ['Av. Brasil', 'Rua Uruguai', 'Rua das Acácias', 'Rua Bulcão Viana', 'Av Marcos Konder']
    _cidades = ['Itajaí', 'Florianópolis', 'Brusque', 'Navegantes']
    _paises = ['Brasil']

    def __init__(self):
        self.nome = random.choice(self._nomes)
        self.email = self.generateEmail()
        self.endereco = {}
        self.endereco['pais'] = random.choice(self._paises)
        self.endereco['cidade'] = random.choice(self._cidades)
        self.endereco['rua'] = random.choice(self._ruas)
        self.endereco['numero'] = random.randint(10,999)
        self.endereco['complemento'] = ''

    def generateEmail(self, domain="fakemail.net"):
        return self.nome.lower().replace(' ', '_') + "@" + domain
    
    def getRandom():
        clientes = []
        for n in Cliente._nomes:
            clientes.append({
                'nome': n,
                'contato': {
                    'email': n.lower().replace(' ', '_') + "@fakemail.net",
                    'telefone': '9' + str(random.randint(80000000, 99999999))
                },
                'endereco': {
                    'cidade': random.choice(Cliente._cidades),
                    'complemento': '',
                    'numero': random.randint(1, 999),
                    'pais': random.choice(Cliente._paises),
                    'rua': random.choice(Cliente._ruas)
                }
            })

        return clientes


pp = pprint.PrettyPrinter()
# pp.pprint(Cliente.nomes)

