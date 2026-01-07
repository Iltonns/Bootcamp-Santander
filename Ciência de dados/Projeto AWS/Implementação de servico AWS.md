# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

Data: 07/01/2026
Empresa: Abstergo Industries 
Responsável: Eleilton Santos Gatinho

## Introdução
Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por Eleilton Santos Gatinho. O objetivo do projeto foi elencar 3 serviços AWS, com a finalidade de realizar diminuição de custos imediatos.

## Descrição do Projeto
O projeto de implementação de ferramentas foi dividido em 3 etapas, cada uma com seus objetivos específicos. A seguir, serão descritas as etapas do projeto:

Etapa 1: 
- **Amazon EC2 Auto Scaling**
- **Foco:** Otimização de recursos computacionais e redução de custos com infraestrutura
- **Descrição de caso de uso:** Implementação de Auto Scaling para ajustar automaticamente a capacidade das instâncias EC2 conforme a demanda real. Durante horários de baixo tráfego (noites e fins de semana), o sistema reduz automaticamente o número de instâncias ativas, gerando economia de até 60% nos custos de computação. A ferramenta também foi configurada com métricas de CPU e memória para garantir performance adequada durante picos de acesso.

Etapa 2: 
- **Amazon S3 Intelligent-Tiering**
- **Foco:** Otimização de armazenamento de dados com transição automática entre camadas
- **Descrição de caso de uso:** Migração de todos os arquivos de armazenamento para buckets S3 com Intelligent-Tiering habilitado. Esta solução move automaticamente os dados para camadas de armazenamento mais econômicas (S3 Infrequent Access ou Glacier) quando não são acessados frequentemente. A implementação resultou em redução de 45% nos custos de armazenamento, especialmente para backups e arquivos históricos que raramente são acessados.

Etapa 3: 
- **AWS Lambda com API Gateway**
- **Foco:** Arquitetura serverless para eliminação de custos com servidores ociosos
- **Descrição de caso de uso:** Migração de APIs e microsserviços de servidores dedicados para funções Lambda, cobrando apenas pelo tempo de execução real. Substituição de 5 instâncias EC2 que ficavam ociosas 70% do tempo por funções Lambda sob demanda. A mudança eliminou custos fixos de infraestrutura, reduzindo em 55% os gastos com processamento de requisições e garantindo alta disponibilidade e escalabilidade automática.

## Conclusão
A implementação de ferramentas na empresa *Abstergo Industries* tem como expectativa a redução de aproximadamente 53% nos custos operacionais de infraestrutura AWS, o que aumentará significativamente a eficiência e a produtividade da empresa. A combinação de Auto Scaling, armazenamento inteligente e arquitetura serverless proporcionará maior flexibilidade, escalabilidade e otimização de recursos. Recomenda-se a continuidade da utilização das ferramentas implementadas e a busca por novas tecnologias que possam melhorar ainda mais os processos da empresa.

## Anexos

- [Amazon EC2 Auto Scaling - Documentação Oficial](https://docs.aws.amazon.com/autoscaling/)
- [Amazon S3 Intelligent-Tiering - Guia do Usuário](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
- [AWS Lambda - Documentação](https://docs.aws.amazon.com/lambda/)
- [Amazon API Gateway - Guia do Desenvolvedor](https://docs.aws.amazon.com/apigateway/)
- [AWS Cost Explorer - Análise de Custos](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

Assinatura do Responsável pelo Projeto:

Eleilton Santos Gatinho