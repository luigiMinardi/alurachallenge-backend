from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler

from re import findall

"""
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    def type_error():
        
        for campo in response.data.keys():
            for index_erro in range(len(response.data[campo])):
                codigo_erro = response.data[campo][index_erro].code
                #locals()[codigo_erro](campo, index_erro)
                if codigo_erro == 'max_length':
                    max_length(campo, index_erro)
                if codigo_erro == 'invalid':
                    invalid(campo, index_erro)
                if codigo_erro == 'blank':
                    blank(campo, index_erro)

    def max_length(campo, index_erro):
            pattern = '[0-9]'
            max_caracteres = ""
            # encontra o maximo de caracteres permitidos na key
            max_caracteres = max_caracteres.join(findall(pattern, response.data[campo][index_erro]))
            # adiciona a nova mensagem na resposta
            response.data[campo][index_erro] = f"{campo} só pode ter {max_caracteres} caracteres!".capitalize()
    def invalid(campo, index_erro):
        response.data[campo][index_erro] = f'{campo} inválida!'.capitalize()

    def blank(campo, index_erro):
        response.data[campo][index_erro] = f'{campo} está em branco, por favor preencha corretamente.'.capitalize()
    
    if isinstance(exc, ValidationError):
        type_error()

    return response


"""
def custom_exception_handler(exc, context):
    # pega a resposta padrão
    response = exception_handler(exc, context)

    # confere se teve algum erro (exception (exc))
    if isinstance(exc, ValidationError):
        # para cada campo com erro (coluna na tabela)
        for key in response.data.keys():
            # pra cada indice na lista de erros
            for index_erro in range(len(response.data[key])):
                codigo_erro = response.data[key][index_erro].code
                # customisa a mensagem de erro do max_length
                if codigo_erro == 'max_length':
                    pattern = '[0-9]'
                    max_caracteres = ""
                    # encontra o maximo de caracteres permitidos na key
                    max_caracteres = max_caracteres.join(findall(pattern, response.data[key][index_erro]))
                    # adiciona a nova mensagem na resposta
                    response.data[key][index_erro] = f"{key} só pode ter {max_caracteres} caracteres!".capitalize()
                # customisa a mensagem de erro do invalid
                elif codigo_erro == 'invalid':
                    response.data[key][index_erro] = f'{key} inválida!'.capitalize()
                # customisa a mensagem de erro do blank
                elif codigo_erro == 'blank':
                    response.data[key][index_erro] = f'{key} está em branco, por favor preencha corretamente.'.capitalize()

    return response
"""#"""
