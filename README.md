# gc-bricks

Aprendendo sobre Datalakes com dados de [Counter Strike](https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/) da [Gamers Club (GC)](https://gamersclub.gg/).

[<img src="https://i.ibb.co/VxZz16c/gczinha.png" alt="gc" width=90>](https://gamersclub.gg/) &nbsp;&nbsp; [<img src="https://i.ibb.co/Qd2WzJ0/Apache-Spark.png" alt="Apache-Spark" width=120>](https://spark.apache.org/) &nbsp;&nbsp; [<img src="https://i.ibb.co/M2RF1Vb/deltalake.png" alt="deltalake" width=100>](https://delta.io/) &nbsp;&nbsp; [<img src="https://i.ibb.co/G95JWPM/databricks.png" alt="databricks" width=85>](https://databricks.com/)

## Sumário

* [1. Sobre o projeto](#sobre-o-projeto)

* [2 Ferramentas utilizadas](#ferramentas-utilizadas)

* [3 Sobre os dados](#sobre-os-dados)

* [4 Sobre o autor](#sobre-o-autor)

* [5 Como apoiar](#como-apoiar)

## Sobre o projeto

A ideia principal deste projeto é a criação de um Datalake utilizando os dados públicos que a Gamers Clube disponibilizou no Kaggle. É esperado que os exemplos construidos auxiliem os primeiros passos de quem se interesse pelo tema. Assim, começaremos do básico e evoluiremos em conjuto com a comunidade.

Realizaremos as primeiras ingestões de dados na camada `raw`, consolidação em DeltaLake para camada `bronze`, qualidade de dados e padronizações em `silver` e visões analíticas em `gold`. Assim, construiremos pipelines de dados end-to-end.
## Ferramentas Utilizadas

Para a construção deste projeto contaremos com os seguintes componentes:
1. AWS S3 - Storage de armazenamentos dos dados. É onde todos os nossos dados serão guardados, seja em arquivos `.csv`, `.parquet` ou `.json`.
2. Apache Spark - Motor de processamento de dados. Esse cara que realizará todo processamento dos nossos dados e levando ele para camadas mais trabalhadas. Bem como nosso facilitador para realizar consultas em nossos dados para gerar indights, análises, modelos preditivos, etc.
3. Delta Lake - Framework de estrutura de arquivos e pastas para criação de Lakehouses. Com isso, temos a possibilidade de ter operações de `UPDATE` e `DELETE` em nosso Datalake, simulando um ambiente análogo ao de DataWarehouse (chamado datalakehouse).
4. Databricks - SaaS para Big Data. Este componente provisiona clusters Apache Spark auto geridos, bem como todas features de Delta Lake para criação de nosso projeto. Além de funcionalidades adicionais que facilitam nosso trabalho, como: orquestrador de execução, ambiente de desenvolvimento em notebooks, versionamento de código, trabalho compartilhado e outros.
5. Redash - Ferramenta para Data Visualization - É importante fornecer na ponta os resultados obtidos para os tomadores de decisão, assim, escolhemos o Redash para ser nossa ferramenta de Dashboards.

## Sobre os dados

Vamos utilizar os dados da Gamers Club para realizar todos os passos. Você pode encontrar os dados disponíveis no [Kaggle](https://www.kaggle.com/gamersclub/brazilian-csgo-plataform-dataset-by-gamers-club), em formato `.csv`.

Estes dados representam uma pequena parcela dos serviços disponíveis na plataforma da Gamers Club. Abaixo temos as tabelas contidas no dataset:

- tb_lobby_stats_player: Tabela com estatísticas das Lobbies (partidas) de cada player. São mais de 150.000 linhas de dados
- tb_medalha: Tabela com a descrições das medalhas disponíveis na GC e seu tipo. São mais de 40 linhas com medalhas distintas.
- tb_players: Tabela com informações cadastrais dos players amostrados. São mais de 2.500 players distintos.
- tb_players_medalha: Tabela com informações das medalhas que cada player adquiriu e expiração. São mais de 32.000 linhas.

Temos ainda um esquema do relacionamento destes dados:

<img src="https://user-images.githubusercontent.com/4283625/157664295-45b60786-92a4-478d-a044-478cdc6261d7.jpg" alt="" width="650">
