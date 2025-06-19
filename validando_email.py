# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:

def validar_email(email):
    
    if " " in email:
        return "E-mail inválido"
    
    
    if email.count("@") != 1 or email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"
    
    parte_usuario, parte_dominio = email.split("@")
    if "." not in parte_dominio:
        return "E-mail inválido"
    
    return "E-mail válido"


print(validar_email(email))   