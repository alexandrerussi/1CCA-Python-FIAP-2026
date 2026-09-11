from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    stage = input("Etapa de vendas: ")

    # validar os dados
    # depois dos dados validados...
    # preciso modelar os dados do lead como dict... (model.py)
    print(model_lead(name, email, stage))

    # agora... com os dados modelados como dict, preciso enviar para o leads.json
    # o control.py irá auxiliar a enviar os dados para o json
    control.create_lead(model_lead(name, email, stage))

    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    print(leads)

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()