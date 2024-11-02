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

### *Pipelines/DAGs*
<p> Uma pipeline consiste em um conjunto de tarefas ou ações feitas em sequência para atingir um resultado. </p>
<p> No airflow, uma pipeline é representada como uma DAG (Grafo Acíclico Direcionado). As DAGs são criadas em Python de forma simples e com poucas linhas de código. </p>

### *LOGs*
<p> </p>

### *Tasks*
<p> </p>

### *Principais componentes do Airflow*
<p> Webserver: Fornece uma interface gráfica intuitiva aos usuários; </p>
<p> Scheduler: Permite a execução de forma programada das dags. O scheduler é como se fosse o "coração" do Airflow; </p>
<p> Metadata: Se refere ao armazenamento de todos os dados do Airflow. É como o "cérebro" do Airflow; </p>
<p> Executor: Executa as tarefas agendadas pelo Scheduler. </p>

## *Como configurar o sistema*

<p> É possível instalar o airflow com o Docker ou sem. Em meu caso, tentei instalar primeiramente com o Docker, porém acabei cometendo o grande erro de não ler a documentação e tive problemas, já que minha máquina não possui o mínimo de 4 GB de RAM para essa instalação. </p>
<p> A seguir, está o link do tutorial de instalação que eu segui (sem o Docker) e funcionou: 
  <a href="https://medium.com/@sanchesmil/instalando-o-apache-airflow-no-ubuntu-3eba864882c3"> 
    Instalando o Apache AIRFLOW no Ubuntu 
  </a>
</p>

## *Criando sua primeira DAG*

<p> Como já dito, uma DAG é como são representados os pipelines no Airflow. Sua criação não é complicada e existem jeitos diferentes de fazê-la. Vou demonstrar de apenas um jeito para não criar confusão. </p>

### *Passo 1: Importando as bibliotecas necessárias*
<p> Primeiro, vamos importar as bibliotecas que iremos usar: </p>

```python
from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
```
<p> O BashOperator permite a execução de códigos bash (comandos do sistema operacional), já o DummyOperator é usado apenas para "marcar" transições de tasks. </p>
<p> No próximo tópico, explicarei de forma mais detalhada sobre os principais operadores do Airflow. </p>

### *Passo 2: Criando a estrutura da DAG*
<p> Para criar a DAG, é necessário definir alguns de seus componentes: </p>

```python
with DAG(
    dag_id="primeira_dag",
    start_date=datetime(2024, 10, 18),
    schedule_interval="@daily",
    doc_md=exemplo_doc,
    catchup=False
) as dag:
```
<p> O "dag_id" diz respeito a identificação da DAG que você está criando. Ao definir esse id, não utilize espaço entre as palavras, pois isso resultará em erro. 
Ao acessar o webserver, você poderá pesquisar posteriormente pelo nome da dag_id que você adicionou. </p>
<p> O "start_date" é justamente a data de início que a DAG será executada. 
  É importante considerar que ela será executada às 00:00 de cada dia a partir do dia 18/10/2024, pois definimos o schedule_interval como sendo diário. </p>
<p> OBS: Caso você não defina um schedule_interval, a DAG não será executada. </p>
<p> O "doc_md" permite que você crie uma documentação em markdown da sua DAG. Neste caso, dei o nome de "exemplo_doc" para criarmos a nossa documentação, que deve estar escrita acima da criação da DAG, assim:</p>

```python
exemplo_doc = 'Aqui está um exemplo de documentação :)'
```

<p> Por fim, o "catchup" se relaciona à execução de tasks desde a start_date até a data atual que não foram executadas, ou seja, que estejam pendentes.</p>
<p> O catchup deve ser False caso você não queira que essas tasks pendentes sejam executadas, e True caso você queira. Coloquei como False pois isso evita que muitas tarefas acumuladas sejam executadas. </p>

### *Passo 3: Definição de Início, Meio e Fim*
<p> Agora, é necessário especificarmos o início, meio e fim da nossa DAG: </p>

```python
inicia = DummyOperator(task_id="inicia")
hello = BashOperator(task_id="hello", bash_command="echo hello world")
finaliza = DummyOperator(task_id="finaliza")
```
<p> A task_id deve ser única para cada task. Isso permite a identificação das tasks no webserver. </p>

### *Passo 4: Ordem de execução*
<p> Sobre a ordem de execução, apenas é necessário executar (fora do bloco de código da DAG) as variáveis que criamos de acordo com a ordem que queremos dentro de parênteses: </p>

```python
(inicia >> hello >> finaliza)
```
<p> Abaixo, segue o código completo e na ordem exata de todos os passos anteriores: </p>

```python
from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

exemplo_doc = 'Aqui está um exemplo de documentação :)'

with DAG(
    dag_id="primeira_dag",
    start_date=datetime(2024, 10, 18),
    schedule_interval="@daily",
    doc_md=exemplo_doc,
    catchup=False
) as dag:
    inicia = DummyOperator(task_id="inicia")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    finaliza = DummyOperator(task_id="finaliza")

(inicia >> hello >> finaliza)
```

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
  <a href="https://ilegra.com/blog/apache-airflow-maestro-de-pipelines-de-tarefas-agendadas/#:~:text=O%20que%20o%20Airflow%20%C3%A9,de%20sequenciamento%20definidas%2C%20chamados%20DAGs.">
    Apache Airflow: maestro de pipelines de tarefas agendadas
  </a>
 </p>
 <p>
   <a href="https://innowise.com/pt/blog/apache-airflow-introduction/"> 
   O guia definitivo de Apache Airflow
   </a>
 </p>
</p>
