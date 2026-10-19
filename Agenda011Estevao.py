#Professor

from tokenize import Double


-nome: String
-idade: Int
-formação: String

+definirNome(nome: String):
+retornarNome(): String
+definirIdade(idade: int): void
+retornarIdade(): int
+definirFormação(formação: String): void
+retornarFormação(): String

#Aluno

-nome: String
-idade: Int
-curso: String

+definirNome(nome: String): void
+retornarNome(): String
+definirIdade(idade: int): void
+retornarIdade(): int
+definirCurso(curso: String): void
+retornarCurso(): String

#Secretaria

-nome: String
-idade: Int
-departamento: String

+definirNome(nome: String): void
+retornarNome(): String
+definirIdade(idade: int): void
+retornarIdade(): int
+definirDepartamento(departamento: String): void
+retornarDepartamento(): String

#matricula

-matricula: Int
-nome: String
+CalcularVendas():Double 

#Vendedor

-comissao: float
+CalcularVendas():Double

#Diretor

-grafiticação: float
+CalcularVendas():Double






