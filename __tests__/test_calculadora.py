# 1 - Bibliotecas, frameworks e referências externas
import pytest
from utils.utils import ler_csv  #função de leitura de arquivos csv

# Funções que serão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# 2 - Testes

def test_somar_dois_numeros():
    
    # Padrão/ Standard AAA (se diz Triple A/ 3A) = Arrange/preparar os dados, Act/execute, Assert/validar
    
    # ARRANGE/ Prepara/Configura
    # Dados entrada e saída
    num1 = 5
    num2 = 6
    resultado_esperado = 11
    
    # ACT/ Executa 
    resultado_obtido = somar_dois_numeros(num1, num2)
    
    # ASSERT/ Valida
    
    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():
    
    num1 = 15
    num2 = 6
    resultado_esperado = 9
    
    resultado_obtido = subtrair_dois_numeros(num1, num2)
    
    assert resultado_esperado == resultado_obtido
    
def test_multiplicar_dois_numeros():
    
    num1 = 5
    num2 = 3
    resultado_esperado = 15
    
    resultado_obtido = multiplicar_dois_numeros(num1, num2)
    
    assert resultado_esperado == resultado_obtido
    
    
def test_dividir_dois_numeros():
    
    num1 = 15
    num2 = 3
    resultado_esperado = 5
    
    resultado_obtido = dividir_dois_numeros(num1, num2)
    
    assert resultado_esperado == resultado_obtido
    

def test_dividir_por_zero():
    
    num1 = 40
    num2 = 0
    resultado_esperado = "Não é possível dividir por zero"
    
    resultado_obtido = dividir_dois_numeros(num1, num2)
    
    assert resultado_esperado == resultado_obtido

# Test Baseados em Dados = Data Driven Tests (DDT) = Massa de Testes
    #Dados em uma lista
    #Dados em um arquivo, vários formatos:csv (texto separado por vírgulas), json, xml, dat...
    
@pytest.mark.parametrize("num1, num2, resultado_esperado",
                         [ # array/matriz
                            (4, 5, 9), #tupla/registro
                            (7, 0, 7),
                            (-15, 5, -10),
                            (5, 0.55, 5.55)
                         ]
                        )    

def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):
    
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista
    
    # ACT/ Executa 
    resultado_obtido = somar_dois_numeros(num1, num2)
    
    # ASSERT/ Valida
    
    assert resultado_esperado == resultado_obtido
 
 
@pytest.mark.parametrize("num1, num2, resultado_esperado",
                         ler_csv("./fixtures/massa_somar.csv")
                         )
    
def test_somar_dois_numeros_lista_csv(num1, num2, resultado_esperado):
    
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista
    
    # ACT/ Executa 
    resultado_obtido = somar_dois_numeros(float(num1), float(num2))
    
    # ASSERT/ Valida
    
    assert float(resultado_esperado) == resultado_obtido

    