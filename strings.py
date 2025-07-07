email = "rafaelfranca@soumaissantissimo.com.br"
indice_do_dominio = email.find("@")
email_dominio = email[indice_do_dominio:]

if email_dominio == "@soumaissantissimo.com.br" || ... : #aluno ou docente
  ... #mandar código de verificação por email

# rota de verificar código e criar conta
  #se dominio for de aluno criar conta de aluno
  #se dominio for de docente criar conta de docente
