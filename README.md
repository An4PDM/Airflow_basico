# *Conteúdo Básico sobre Airflow*
<p> Este repositório tem o objetivo de servir de consulta para quem deseja começar os estudos de Airflow.</p>
<p> Em minha jornada de aprendizado desse tema, percebi que não haviam muitos materiais de fácil entendimento para iniciantes. </p>
<p> Gastei muito mais tempo procurando por tutoriais do que, de fato, estudando. </p>
<p> Por isso, resolvi criar esse projeto para servir como base para estudantes terem um "norte" de por onde começar, além disso estarei recomendando os materiais gratuitos que me ajudaram. </p>
<p> Checklist de conteúdos: </p>
<ul>
  <li> Conceitos fundamentais; </li>
  <li> Como configurar o sistema; </li>
  <li> Entendendo a interface do Airflow; </li>
  <li> Criando sua primeira DAG; </li>
  <li> Operadores. </li>
</ul>

## *Conceitos fundamentais*
<p> O Airflow nada mais é do que uma ferramenta de orquestração de workflows (fluxos de trabalho), ou seja, ele permite que o usuário defina "sequências" de atividades relacionadas a dados, sendo possível agendar tasks (tarefas) e executar processos. </p>
<p> Essa ferramenta é extremamente importante para profissionais que trabalham com Engenharia de Dados e Big Data, pois ela facilita a construção de pipelines e manipulação de um grande volume de dados. </p>
<p> Uma frase de um artigo da Medium sobre o Airflow, me fez refletir sobre a complexidade de certas ferramentas de ETL:
"Para a grande maioria dos cenários, uma infraestrutura de ETL simples, com scripts bem escritos e bem documentada é muito mais do que o suficiente."
</p>
<p> O Airflow é exatamente isso: uma infraestrutura simples e bem documentada que facilita a vida dos profissionais de dados.</p>

### *Pipelines*
<p> Uma pipeline consiste em um conjunto de tarefas ou ações feitas em sequência para atingir um resultado. </p>
<p> No airflow, uma pipeline é representada como uma DAG (Grafo Acíclico Direcionado). As DAGs são criadas em Python de forma simples e com poucas linhas de código. </p>

### *Principais componentes do Airflow*
<p> Webserver: Fornece uma interface gráfica intuitiva aos usuários; </p>
<p> Scheduler: Permite a execução de forma programada das dags. O scheduler é como se fosse o "coração" do Airflow; </p>
<p> Metadata: Se refere ao armazenamento de todos os dados do Airflow. É como o "cérebro" do Airflow; </p>
<p> Executor: Executa as tarefas agendadas pelo Scheduler. </p>


<p> Referências: 
 <p>
  <a href="https://www.anselme.com.br/2023/08/09/o-basico-de-apache-airflow/#:~:text=O%20que%20%C3%A9%20DAG,-DAG%20%C3%A9%20o&text=O%20b%C3%A1sico%20do%20Apache%20Airflow%20inclui%20destacar%20que%20h%C3%A1%20uma,orquestradores%2C%20como%20o%20Apache%20Oozie."> 
    Básico de apache Airflow
  </a>
 </p>
 <p>
  <a href="https://medium.com/data-hackers/primeiros-passos-com-o-apache-airflow-etl-f%C3%A1cil-robusto-e-de-baixo-custo-f80db989edae"> 
    Primeiros passos com Apache Airflow 
  </a>
 </p>
 <p> 
   <a href="https://docs.tecnisys.com.br/tdp/2.2.0/03-tdp-conceitos/tdp-airflow.html"> 
     Apache Airflow: Componentes principais
   </a>
 </p>
 <p>
   <a href="https://innowise.com/pt/blog/apache-airflow-introduction/"> 
   O guia definitivo de Apache Airflow
   </a>
 </p>
</p>
