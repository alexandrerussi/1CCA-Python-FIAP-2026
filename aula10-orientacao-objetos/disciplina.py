class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"Disciplina: {self.nome} | Prof.: {self.professor}")

# TEMPORÁRIO
# cs = Disciplina("Computer Science", "Maumau")
# print(cs.professor)
# cs.exibir_infos()