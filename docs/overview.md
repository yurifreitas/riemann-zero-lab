## Visão Geral

Este projeto implementa um **pipeline experimental completo e reproduzível**
para a **localização, validação e análise estatística** dos zeros não triviais
da função zeta de Riemann na **linha crítica**.

A arquitetura foi desenhada com foco explícito em:

- **consistência numérica**,  
- **separação clara de responsabilidades computacionais**,  
- **validação teórica local rigorosa**.

O pipeline distingue de forma explícita entre:
- detecção rápida de candidatos a zero,
- refinamento de alta precisão,
- e validação independente da contagem de zeros.

> **O objetivo do projeto não é provar a Hipótese de Riemann.**

Em vez disso, o projeto fornece uma **base sólida para matemática experimental**,
permitindo a exploração controlada de zeros em alturas moderadas, a reprodução
de fenômenos clássicos da teoria analítica dos números e a realização de
análises estatísticas confiáveis sobre o espectro da zeta.

A ênfase está na **reprodutibilidade**, na **correção metodológica** e na
possibilidade de extensão para estudos comparativos, tanto numéricos quanto
estatísticos, na interface entre matemática e física.
