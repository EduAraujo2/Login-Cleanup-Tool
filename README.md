<h1>Limpando uma conexão</h1>

## Projeto
Este projeto é para automatizar o processo de limpeza de conexões de login na plataforma CDNTV, facilitando a resolução de problemas de autenticação para os usuários. Através de uma interface web simples, desenvolvida com Flask, e utilizando automação de navegador com Selenium, o sistema permite que os usuários limpem suas conexões de login de forma rápida e eficiente, melhorando a experiência de acesso ao serviço.

Para que o cliente final tenha acesso à opção de limpar a conexão, a empresa deve instalar a aplicação em seus servidores e fornecer o IP correspondente. Com isso, os clientes poderão acessar a ferramenta diretamente via o IP fornecido, sem a necessidade de instalar o projeto em seus próprios computadores.


## Objetivo
O projeto visa facilitar a vida do cliente final, permitindo que ele resolva problemas de login por conta própria, sem a necessidade de esperar por suporte técnico. Dessa forma, os usuários podem restaurar o acesso aos aplicativos, tanto web, mobile, quanto em TVs, de maneira mais ágil, reduzindo o tempo de inatividade e aumentando a satisfação geral com o serviço.


## Funcionalidades
**Limpeza de Conexão:** Automatiza a limpeza de conexões de login que podem estar corrompidas ou travadas na plataforma CDNTV.

**Interface Simples:** Uma interface web permite ao usuário inserir seu login e limpar a conexão com um clique.

**Automação via Selenium:** Usa o Selenium WebDriver para interagir com a página da CDNTV.


## Tecnologias Utilizadas
<table>
  <tbody align="left">
    <tr>
      <td>Python</td>
    </tr>
    <tr>
      <td>Flask</td>
    </tr>
    <tr>
      <td>Selenium</td>
    </tr>
    <tr>
      <td>WebDriver Manager</td>
    </tr>
    <tr>
      <td>Python Dotenv</td>
    </tr>
    <tr>
      <td>HTML/CSS</td>
    </tr>
  </tbody>
</table>


## Pré-requisitos
<table>
  <tbody align="left">
    <tr>
      <td>Python 3.8+</td>
    </tr>
    <tr>
      <td>Um navegador FireFox instalado</td>
  </tbody>
</table>


## Instalação
<table>
  <thead>
    <tr align="left">
      <th>Nº</th>
      <th>Etapas</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>01</td>
      <td>Clone este repositório: </td>
      <td>git clone https://https://github.com/EduAraujo2/Login-Cleanup-Tool.git
cd Login-Cleanup-Tool</td>
    </tr>
    <tr>
      <td>02</td>
      <td>Crie um ambiente virtual (opcional):</td>
      <td>python -m venv | venv\Scripts\activate     # Para Windows</td>
    </tr>
    <tr>
      <td>03</td>
      <td>Instale as dependências:</td>
      <td>pip install -r requirements.txt</td>   
    </tr>
    <tr>
      <td>04</td>
      <td>Variáveis de ambiente:</td>
      <td>Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:</td>
      <td>LINK_SITE="https://link.do.site/login" USERNAME="seu_usuario_adm" PASSWORD="sua_senha_adm" ACCOUNT="https://link.do.site/contas" LOGOUT="https://link.do.site/logout"</td>     
    </tr>
    <tr>
      <td>05</td>
      <td>Execute a aplicação:</td>
      <td>python app.py</td>   
    </tr>
    <tr>
      <td>06</td>
      <td>Acesse a aplicação no navegador:</td>
      <td>http://127.0.0.1:5000/</td>   
    </tr>
  </tbody>
</table>


## Estrutura do projeto
**app.py:** Arquivo principal que contém a lógica do Flask e a automação com Selenium.

**templates:** Contém os arquivos HTML (login.html e resultado.html) usados pela aplicação.

**.env:** Arquivo de configuração de variáveis de ambiente (não incluído no repositório).

**imagem:** Links com imagens png usadas no projeto


## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


## Licença
Este projeto está licenciado sob a Licença Creative Commons Attribution-NonCommercial (CC BY-NC). Isso significa que você pode compartilhar, modificar e utilizar o conteúdo deste projeto, desde que atribua o crédito apropriado ao autor original e não use o material para fins comerciais.