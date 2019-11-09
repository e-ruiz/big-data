import pprint, random, datetime

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


class Venda():
    _clientes = [
        {"_id": "5dc58145cfb83d37c2e6d1d8", "nome": "ERIC RUIZ"},
        {"_id": "5dc58145cfb83d37c2e6d1d9", "nome": "ROBERTA DE LIMA"},
        {"_id": "5dc58145cfb83d37c2e6d1da", "nome": "DEIVIDI SCALZAVARA"},
        {"_id": "5dc58145cfb83d37c2e6d1db", "nome": "ADOLFO NETO"},
        {"_id": "5dc58145cfb83d37c2e6d1dc", "nome": "JOSE MONESTEL"},
        {"_id": "5dc58145cfb83d37c2e6d1dd", "nome": "WAGNER CORREIA"},
        {"_id": "5dc58145cfb83d37c2e6d1de", "nome": "JACEGUAY ZUKOSKI"},
        {"_id": "5dc58145cfb83d37c2e6d1df", "nome": "MICHEL SOUZA"},
        {"_id": "5dc58145cfb83d37c2e6d1e0", "nome": "MAYRA RODRIGUES"},
        {"_id": "5dc58145cfb83d37c2e6d1e1", "nome": "MICHEL DUARTE"},
        {"_id": "5dc58145cfb83d37c2e6d1e2", "nome": "MARCIO FOSSA"},
        {"_id": "5dc58145cfb83d37c2e6d1e3", "nome": "MARCEL BORNANCIN"},
        {"_id": "5dc58145cfb83d37c2e6d1e4", "nome": "ELOISA PERIN"},
        {"_id": "5dc58145cfb83d37c2e6d1e5", "nome": "TIAGO WIPPEL"},
        {"_id": "5dc58145cfb83d37c2e6d1e6", "nome": "LUCAS FISCHER"},
        {"_id": "5dc58145cfb83d37c2e6d1e7", "nome": "DIEGO PRANDO"},
        {"_id": "5dc58145cfb83d37c2e6d1e8", "nome": "ADRIANO WEIGUERT NAGASAVA"},
        {"_id": "5dc58145cfb83d37c2e6d1e9", "nome": "FERNANDO MIRANDA"},
        {"_id": "5dc58145cfb83d37c2e6d1ea", "nome": "LUIS MONTES"},
        {"_id": "5dc58145cfb83d37c2e6d1eb", "nome": "MARCELO DE SOUZA"}
    ]

    _produtos = {
        'smartphone': [
            {'nome': 'Galaxy s10', 'valor_unitario': 999.99},
            {'nome': 'Xiaomi Redmi', 'valor_unitario': 768.89},
            {'nome': 'iPhone 11 pro', 'valor_unitario': 6899.0},
            {'nome': 'LG K9', 'valor_unitario': 648.99},
            {'nome': 'Moto G7 Play', 'valor_unitario': 829.90}
        ],
        'notebook': [
            {'nome': 'Lenovo Carbon', 'valor_unitario': 9999.98},
            {'nome': 'Mac Book Air', 'valor_unitario': 4680.0},
            {'nome': 'Dell XPS', 'valor_unitario': 7699.79},
            {'nome': 'Alienware', 'valor_unitario': 12350.0},
            {'nome': 'Positivo Motion', 'valor_unitario': 1450.0},
        ],
        'tablet': [
            {'nome': 'Galaxy Tab A10', 'valor_unitario': 899},
            {'nome': 'Multilaser M7S', 'valor_unitario': 375.5},
            {'nome': 'Amazon Fire7', 'valor_unitario': 359.99},
            {'nome': 'iPad', 'valor_unitario': 2159.89},
            {'nome': 'Acer Iconia', 'valor_unitario': 499.0}
        ],
        'monitor': [
            {'nome': 'LG Led 20-M37', 'valor_unitario': 1289.0},
            {'nome': 'Samsung 32 Curve', 'valor_unitario': 2790.99},
            {'nome': 'Philips LED 185', 'valor_unitario': 269.9},
            {'nome': 'AOC 24 Freesync', 'valor_unitario': 619.29}
        ],
        'câmera digital': [
            {'nome': 'Canon Rebel SL2', 'valor_unitario': 3000},
            {'nome': 'Sony W800', 'valor_unitario':  659},
            {'nome': 'Leica V-lux t114', 'valor_unitario': 12300},
            {'nome': 'Nikon Coolpix S8100', 'valor_unitario': 899},
        ],
        'headset': [
            {'nome': 'Razer Kraken', 'valor_unitario': 328.9},
            {'nome': 'AKG K92', 'valor_unitario': 219.90},
            {'nome': 'Sony MDR-5A', 'valor_unitario': 414.62},
            {'nome': 'Apple Beats Studio', 'valor_unitario': 1599}
        ],
        'carregador': [
            {'nome': 'Qi wireless 10w', 'valor_unitario': 12.99},
            {'nome': 'Universal 3 USB 3A', 'valor_unitario': 27.8},
            {'nome': 'Qualcomm Turbo 3A', 'valor_unitario': 36.5}
        ]
    }
    
    def getRandom():
        classificacao_produto = random.choice(list(Venda._produtos.keys()))
        produto = random.choice(Venda._produtos[classificacao_produto])
        cliente = random.choice(Venda._clientes)
        return {
            'nome_produto': produto['nome'],
            'valor_unitario': produto['valor_unitario'],
            'classificacao_produto': classificacao_produto,
            'quantidade': random.choice([1,1,1,1,1,2,2,2,3,4]),
            'nome_cliente': cliente['nome'],
            'id_cliente': cliente['_id'],
            'data_venda': datetime.date(
                    random.randint(2017,2019), 
                    random.randint(1,12), 
                    random.randint(1,28)
                ).isoformat()
        }
    
    def getRandomss():
        c = random.choice(Venda._clientes)
        for c in Venda._clientes:
            vendas = random.randint(4,7)
            while vendas > 0:
                venda = Venda.getRandom()
                venda['id_cliente'] = c['_id']
                venda['nome_cliente'] = c['nome']
                pp.pprint(venda)

                vendas = vendas - 1
                        


    # def getRandom():

    #     return {
    #         'nome_produto':
    #         'valor_unitario':
    #         'classificacao':
    #         'quantidade':
    #         'nome_cliente':
    #         'id_cliente':
    #         'data_venda':
    #     }




pp = pprint.PrettyPrinter()
# pp.pprint(Cliente.nomes)

