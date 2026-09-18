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
    leads = control.read_leads() # array / lista

    print(f"## | {"Nome":<10} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia")
        return

    # chamar o control e passar nossa query (busca)
    # o control irá verificar se existe a query no leads.json
    # e irá retornar os resultados da busca []
    found_leads = control.read_leads_search(query)
    print(f"## | {"Nome":<15} | E-mail")
    for i, lead in found_leads:
        print(f"{i:02d} | {lead["name"]:<15} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar os leads")
    else:
        print(f"Leads exportados para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Busca (nome/e-mail)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()