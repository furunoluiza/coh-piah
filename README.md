# Introdução à Ciência da Computação com Python Parte 1
Esse jogo foi desenvolvido durante esse curso fornecido pela USP na plataforma do Coursera.

## **Similaridades entre textos - Caso COH-PIAH**
### **Introdução**
Manuel Estandarte é monitor na disciplina Introdução à Produção Textual I na Universidade de Pasárgada (UPA). Durante o período letivo, Manuel descobriu que uma epidemia de COH-PIAH estava se espalhando pela UPA. Essa doença rara e altamente contagiosa faz com que indivíduos contaminados produzam, involuntariamente, textos muito semelhantes aos de outras pessoas. Após a entrega da primeira redação, Manuel desconfiou que alguns alunos estavam sofrendo de COH-PIAH. Manuel, preocupado com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

### **Detecção de autoria**
Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.

### **Traços linguísticos**
Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

- Tamanho médio de palavra: Média simples do número de caracteres por palavra.
- Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
- Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
- Tamanho médio de sentença: Média simples do número de caracteres por sentença.
- Complexidade de sentença: Média simples do número de frases por sentença.
- Tamanho médio de frase: Média simples do número de caracteres por frase.

### **Funcionamento do programa**
A partir da assinatura conhecida de um portador de COH-PIAH, seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. O grau de similaridade entre dois textos, a e b, é dado pela fórmula:

S_{ab} = ((∑{i=1 6}) * ∣∣f_{i,a} - f_{i,b}∣∣) / 6

- S_{ab}        é o grau de similaridade entre os textos  a e b;
- f_{i,a}       é o valor de cada traço linguístico  i no texto  a;
- f_{i,b}       é o valor de cada traço linguístico  i no texto  b;

Perceba que quanto mais similares  a e b forem, menor  S_{ab}será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e, no final, exibir qual texto mais provavelmente foi escrito por algum aluno infectado (ou seja, o texto com assinatura mais similar à assinatura dada).

### **Concluindo**
Basicamente, a tarefa realizada foi implementar corretamente as seguintes funções:  

- compara_assinatura(as_a, as_b)
- calcula_assinatura(texto)
- avalia_textos(textos, ass_cp)
