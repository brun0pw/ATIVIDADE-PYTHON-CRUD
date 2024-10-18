import os
os.system("cls||clear")
#vicio em mim a policia em mim
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

#criando o banco de dados
BANCO = create_engine("sqlite:///RhSystem.db")

#criando conexão com o banco de dados
Session = sessionmaker(bind= BANCO)
session= Session()

#craindo tabela
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id_do_funcionario = Column("id", Integer, primary_key = True, autoincrement = True)
    nome = Column("nome", String)
    cpf =  Column("cpf", Integer)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Integer)   
    telefone = Column("telefone", String)
    def __init__(self, nome: str,  cpf :Integer, setor : str, funcao : str, salario: Integer, telefone: str):
        self.nome = nome
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
    #criando tabela no banco de dados    
    Base.metadata.create_all(bind = BANCO)



def salvar_funcionario(nomee, cpff, setorr, funcaoo, salarioo, telefonee):
    funcionario = Funcionario(nome = nomee, cpf = cpff, setor = setorr, funcao = funcaoo, salario = salarioo, telefone = telefonee)
    session.add(funcionario)
    session.commit()
    print("salvo com sucesso!")

def listar_todos_funcionarios():
    # Listando todos os usuários do banco de dados.
    # Read
    print("\nExibindo todos os usuários do bando de dados.")
    lista_funcionario = session.query(Funcionario).all()

    for funcionarios in lista_funcionario:
        print(f"Nome: {funcionarios.nome}, CPF: {funcionarios.cpf}, Setor: {funcionarios.setor}, Função: {funcionarios.funcao}"))
def pesquisar_um_funcionario(cpf):
    funcionario = session.query(Funcionario).filter_by(cpf = cpf).first()
    if funcionario:
        print(f"Nome: {funcionario.nome}, CPF: {funcionario.cpf}, Setor: {funcionario.setor}, Função: {funcionario.funcao}")
    else:
        print("Funcionário não encontrado.")

def atualizar_funcionario(cpf):
    # Update
    print("\nAtualizando dados do usuário.")
    funcionario = session.query(Funcionario).filter_by(cpf = cpf).first()
    nomee = input("Digite seu nome: ")
    cpff = input("Digite seu cpf: ")
    setorr = input("Digite sua setor: ")
    funcaoo = input("Digite sua funcao: ")
    salarioo = input("Digite seu salario: ")
    telefonee = input("Digite seu telefone: ")


    session.commit()
def excluir_funcionario(cpf):
    print("\nExcluindo um usuário.")
    funcionario = session.query(Funcionario).filter_(cpf = cpf).first()
    session.delete(funcionario)
    session.commit()
    print(f"{funcionario.cpf} excluido com sucesso.")

while True:
    print("""
        === RH System ===
    1 - Adicionar funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário
    5 - Listar todos os funcionários
    0 - Sair do sistema.
    """)
    opcao = int(input("Digite a opção: "))
    match opcao:
        case 1:
            nomee = input("Digite seu nome: ")
            cpff = input("Digite seu cpf: ")
            setorr = input("Digite sua setor: ")
            funcaoo = input("Digite sua funcao: ")
            salarioo = input("Digite seu salario: ")
            telefonee = input("Digite seu telefone: ")
            salvar_funcionario(nomee, cpff, setorr, funcaoo, salarioo, telefonee)
        case 2:
            cpf = input("Digite seu cpf: ")
            pesquisar_um_funcionario(cpf)
        case 3:
            cpf = input("Digite seu cpf: ")
            atualizar_funcionario(cpf)
        case 4:
            cpf = input("Digite seu cpf: ")
            excluir_funcionario(cpf)
        case 5: 
            listar_todos_funcionarios()
        case 0:
            break
        case _:
