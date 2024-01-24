
def saudacao(**kwargs):
    print(kwargs)

#chamar a funçao
    
saudacao(manha= 'bom dia', tarde = 'boa tarde', noite= 'boa noite')

def saudacao_dia(**kwargs):
    for turno,saudacao in kwargs.items():
        print(f'Durante a {turno} dizemos {saudacao}')

saudacao_dia(manha = 'bom dia',tarde = 'boa tarde')

