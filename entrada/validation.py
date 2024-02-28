'''
Dados genericos para teste de entrada e validação da etapa ENTRADA
'''

class Partida_Vasco:
    '''Classe temporaria para testar a entrada sem o coletor de dados'''
    Nome: str = 'Vasco'
    Ataque: int = 50
    AtaqueP: int = 50
    Chute: int = 50
    Posse: int = 50

    def return_dict(self):
        return {'Nome': self.Nome, 
                'Ataque': self.Ataque, 
                'AtaqueP': self.AtaqueP, 
                'Chute': self.Chute, 
                'Posse': self.Posse}

def check_url(Url: str):
    '''Função temporaria para testar a partida acontecendo'''
    return True


if __name__ == '__main__':
    
    print(Partida_Vasco().return_dict())

