nenhuma_infracao = "Nenhuma infração"
infracao_leve = "Infração leve"
infracao_grave = "Infração grave"
infracao_gravissima = "Infração gravíssima"
valor_desconto = 0.20
vermelho ="\033[31m"
verde =  "\033[32m"
fim_cor = "\033[m"
def main()-> None:
    """
    Função Principal responsável pela execução do projeto\n
    Args: Nenhum\n
    Out: None
    """
    banner()
    placa_veiculo, velocidade_registrada, velocidade_maxima_permitida, reincidenca_motorista = cadastro_infracao()
    tipo_infracao = classificacao_infracao(velocidade_registrada,velocidade_maxima_permitida)
    if tipo_infracao == nenhuma_infracao:
        print(f"O motorista {verde}não cometeu nenhum tipo de infração{fim_cor}, neste caso ele não vai receber multa ou pontos.")
        return
    multa_vai_dobrar = reincidenca_motorista and ((tipo_infracao == infracao_grave) or (tipo_infracao == infracao_gravissima))
    multa, pontos = calculo_penalidade(tipo_infracao)
    if multa_vai_dobrar:
        multa *=2
    
    vai_pagar = vai_pagar_agora()
    if vai_pagar:
        multa = desconto(multa)
    reciclagem = "Não Vai Precisar do curso de reciclagem"
    if vai_precisar_curso_reciclagem(tipo_infracao):
        reciclagem = "Vai Precisar do curso de reciclagem"
    print(f"O motorista recebeu uma infração {vermelho}{tipo_infracao}{fim_cor}, vai receber uma multa no valor de {vermelho}R${multa}{fim_cor}, e vai receber {vermelho}{pontos}{fim_cor} pontos , e ele {reciclagem}")


def desconto(multa:float)->float:
    return multa *(1-valor_desconto)

def vai_precisar_curso_reciclagem(tipo_infracao)->bool:
    return tipo_infracao == infracao_gravissima

def vai_pagar_agora()->bool:
    """
    Caso o motorista opte por pagar ele ira receber um desconto na multa
    """
    vai_pagar = input(f"Esse motorista vai pagar agora?[Default: {vermelho}Não{fim_cor}] ")
    if vai_pagar:
        return True
    return False

def calculo_penalidade(tipo_infracao:str)->float:
    """
    Função responsável por validar qual sera a multa e a quantidade de pontos com base no tipo de infração\n
    Args: tipo_infracao\n
    Out: multa, pontos
    """
    if tipo_infracao == infracao_leve:
        multa = 130.16
        pontos = 0
    elif tipo_infracao == infracao_grave:
        multa = 195.23
        pontos = 5
    elif tipo_infracao == infracao_gravissima:
        multa = 880.41
        pontos = 7
    return multa, pontos

    
def cadastro_infracao()->str:
    """"
    Função responsável por receber as informações do motorista\n

    out: placa_veiculo, velocidade_registrada, velocidade_maxima_permitida, reincidenca_motorista
    """
    placa_veiculo = input("Placa do veiculo: ")
    velocidade_registrada = input("Digite a velocidade registrada: ")
    velocidade_maxima_permitida = input("digite a velocidade máxima permitida no local: ")
    reincidenca_motorista = input(f"Esse motorista já foi multado antes?[Default: {vermelho}Não{fim_cor}]:  ")
    return placa_veiculo, velocidade_registrada, velocidade_maxima_permitida, reincidenca_motorista

def classificacao_infracao(velocidade_registrada:str,velocidade_maxima_permitida:str)-> str:
    """"
    Função responsável por classificar o tipo de infração\n
    Args: velocidade_registrada, velocidade_maxima_permitida\n
    out: tipo_infração
    """
    velocidade_maxima_permitida,velocidade_registrada = int(velocidade_maxima_permitida), int(velocidade_registrada)
    if velocidade_registrada <= velocidade_maxima_permitida:
        return nenhuma_infracao
    
    porcentagem_da_velocidade_ultrapassada = ((velocidade_registrada - velocidade_maxima_permitida) / velocidade_maxima_permitida) * 100
    if porcentagem_da_velocidade_ultrapassada <= 20:
        return infracao_leve
    elif porcentagem_da_velocidade_ultrapassada <= 50:
        return infracao_grave
    else:
        return infracao_gravissima



def banner()->None:
    """
    Função responsável por gerar o banner do programa.
    """
    print("""
 █████████   ███           █████                                              █████             ██████   ██████            ████   █████                     
 ███░░░░░███ ░░░           ░░███                                              ░░███             ░░██████ ██████            ░░███  ░░███                      
░███    ░░░  ████   █████  ███████    ██████  █████████████    ██████       ███████   ██████     ░███░█████░███  █████ ████ ░███  ███████    ██████    █████ 
░░█████████ ░░███  ███░░  ░░░███░    ███░░███░░███░░███░░███  ░░░░░███     ███░░███  ███░░███    ░███░░███ ░███ ░░███ ░███  ░███ ░░░███░    ░░░░░███  ███░░  
 ░░░░░░░░███ ░███ ░░█████   ░███    ░███████  ░███ ░███ ░███   ███████    ░███ ░███ ░███████     ░███ ░░░  ░███  ░███ ░███  ░███   ░███      ███████ ░░█████ 
 ███    ░███ ░███  ░░░░███  ░███ ███░███░░░   ░███ ░███ ░███  ███░░███    ░███ ░███ ░███░░░      ░███      ░███  ░███ ░███  ░███   ░███ ███ ███░░███  ░░░░███
░░█████████  █████ ██████   ░░█████ ░░██████  █████░███ █████░░████████   ░░████████░░██████     █████     █████ ░░████████ █████  ░░█████ ░░████████ ██████ 
 ░░░░░░░░░  ░░░░░ ░░░░░░     ░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░░░     ░░░░░░░░  ░░░░░░     ░░░░░     ░░░░░   ░░░░░░░░ ░░░░░    ░░░░░   ░░░░░░░░ ░░░░░░  
""")
main()