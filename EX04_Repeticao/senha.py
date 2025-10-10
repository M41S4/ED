## 4) Programa - senha: Defina uma senha correta dentro do programa 
## (por exemplo: "1234"). Depois, peça para o usuário digitar uma senha. 
##Enquanto a senha digitada for diferente da senha correta, imprimir "❌Senha incorreta!" ,  q
##uando a senha correta for digitada,  imprimir"✅Senha correta!".
##Dica: Use uma repetição (while) e um operador relacional de comparação == (igual) ou != (diferente).

senha_correta = "1234"
senha_user = str(input())

while senha_user != senha_correta:
  print("Senha incorreta")
  senha_user = str(input())
if senha_user == senha_correta:
  print("Senha correta")