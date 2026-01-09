Enunciado:
Nesta tarefa, você desenvolverá um servidor Web simples em Python, capaz de processar apenas uma requisição. Seu servidor web:
(i) criará um socket de conexão quando quando contato por um cliente (navegador);
(ii) receberá a requisição HTTP dessa conexão;
(iii) analisará a requisição para determinar o arquivo específico sendo requisitado;
(iv) obterá o arquivo requisitado do sstema de arquivo do servidor;
(v) criará uma mensagem de resposta HTTP consistindo no arquivo requisitado precedido por linhas de cabeçalho;
(vi) enviará a resposta pela conexão TCP ao navegador requisitante. Se um navegador requisitar um arquivo que não está presente no seu servidor, seu servidor deverá retornar uma mensagem de erro "404 not found"


