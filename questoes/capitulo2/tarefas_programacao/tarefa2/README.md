Enunciado:

Nesta tarefa de programação, você escreverá um programa ping do cliente em Python. Seu cliente enviará
uma mensagem ping simples a um servidor, receberá uma mensagem pong correspondente de volta do servidor
e determinará o atraso entre o momento em que o cliente enviou a mensagem ping e recebeu a mensagem pong.
Esse atraso é denominado tempo de viagem de ida e volta (round-trip time — RTT). A funcionalidade oferecida
pelo cliente e servidor é semelhante à fornecida pelo programa ping padrão, disponível nos sistemas operacionais
modernos. Porém, os programas ping padrão usam o Internet Control Message Protocol (ICMP) (que veremos
no Capítulo 4). Aqui, criaremos um programa ping baseado em UDP, fora do padrão (porém simples!).
Seu programa ping deverá enviar 10 mensagens ping ao servidor de destino por meio de UDP. Para cada
mensagem, seu cliente deverá determinar e imprimir o RTT quando a mensagem pong correspondente for re-
tornada. Como o UDP é um protocolo não confiável, um pacote enviado pelo cliente ou servidor poderá ser
perdido. Por esse motivo, o cliente não poderá esperar indefinidamente por uma resposta a uma mensagem ping.
Você deverá fazer que o cliente espere até 1 s por uma resposta do servidor; se nenhuma resposta for recebida, o
cliente deverá considerar que o pacote foi perdido e imprimir uma mensagem de acordo.
Nesta tarefa, você receberá o código completo para o servidor (disponível no site de apoio). Sua tarefa é
escrever o código cliente, que será semelhante ao código do servidor. Recomendamos que, primeiro, você estude
cuidadosamente o código do servidor. Depois, poderá escrever seu código cliente, cortando e colando à vontade
as linhas do código do servidor.

Planejamento:

1. Qual diferença entre implementar um servidor que recebe chamadas UDP?
2. Qual a diferença entre realizar uma requisição em UDP e uma requisição em TCP?
3. Como calcular o tempo de atraso?

Fontes:
 
 https://wiki.python.org/moin/UdpCommunication
 https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
