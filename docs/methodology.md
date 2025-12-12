# Metodologia Numérica

A detecção de zeros é feita em três níveis:

1. Scan rápido com aproximação de Hardy Z (float64)
2. Detecção de mudanças de sinal
3. Refinamento de raízes com aritmética de alta precisão

A validação teórica utiliza uma forma local do método de Turing,
aplicada exclusivamente em blocos disjuntos, evitando contaminação
por overlap.
