from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Ciência da Computação")
# print(aluno1.notas_por_disciplina)

# criar / instanciar 2 disciplinas
sers = Disciplina("Soluções Renováveis", "Tritiack")
model_mat = Disciplina("Modelagem Matemática", "Roberto")
# print(sers.nome)
# model_mat.exibir_infos()

# matricular o aluno nas 2 disciplinas
aluno1.matricular(sers)
aluno1.matricular(model_mat)
# print(aluno1.disciplinas[1].professor)

# adicionar notas do aluno referente às disciplinas
aluno1.adicionar_nota(sers, 10)
aluno1.adicionar_nota(sers, 8)
aluno1.adicionar_nota(model_mat, 5)
aluno1.adicionar_nota(model_mat, 3)
# print(aluno1.notas_por_disciplina)

print(aluno1.calcular_media_d(model_mat))