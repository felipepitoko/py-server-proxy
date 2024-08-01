# py-server-proxy
Servidor extremamente simples para interceptar requisições HTTP.

V 1.1
<ul>
  <li>A rota /api/receive também aceita query params, que serão salvos caso sejam recebidos.</li>
</ul>

<h2>Passos para usar como um proxy</h2>
<ul>
  <li>Iniciar o servidor localmente, executando o script main</li>
  <li>Servir o localhost:5000 através do ngrok</li>
  <li>Fazer chamadas POST de qualquer lugar para a url gerada pelo ngrok</li>
  <li>Exemplo: 123455.ngrok-free.app/api/receive</li>
  <li>Todos os bodys recebidos são salvos como json localmente</li>
</ul>
