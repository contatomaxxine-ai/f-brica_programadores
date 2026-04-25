programa {
  funcao inicio() {
    inteiro nota,frequencia
    escreva("digite a nota:")
    leia(nota)
    escreva("digite a frequencia:")
    leia(frequencia)
    escreva("---comparações---")
    escreva("nota > frequencia = ",(nota>frequencia e nota==frequencia),"\n")
    escreva("nota >= frequencia =",(nota>=frequencia e nota!=frequencia),"\n")
    escreva("nota < frequencia =", (nota<frequencia e nota>frequencia),"n")
    escreva("nota <= frequencia =", (nota<=frequencia e nota==frequencia),"n")
    escreva("nota != frequencia =", (nota!=frequencia e nota<frequencia),"n")
    escreva("nota == frequencia =", (nota==frequencia e nota!=frequencia),"n")

     

  }
}
