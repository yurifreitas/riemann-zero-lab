## 🔬 Metodologia

1. O intervalo \([T_{\text{start}}, T_{\text{end}}]\) é particionado em blocos
   parcialmente sobrepostos **exclusivamente para a fase de detecção inicial**
   de mudanças de sinal da função de Hardy \(Z(t)\).

2. Cada bloco é processado de forma **independente e paralela**, permitindo
   varredura eficiente do intervalo total sem introduzir dependências entre
   regiões distintas.

3. Os candidatos a zero identificados na fase de varredura são submetidos a
   **refinamento numérico de alta precisão**, garantindo convergência estável
   e localização confiável das raízes.

4. As raízes refinadas são **deduplicadas globalmente**, eliminando ocorrências
   redundantes geradas pelas sobreposições usadas apenas na busca.

5. A completude da enumeração é verificada por meio de um **Turing check
   aplicado corretamente em blocos disjuntos**, sem sobreposição, assegurando
   que a validação da contagem não seja contaminada por artefatos numéricos
   locais.

6. A partir do conjunto final e validado de zeros, são computadas
   **estatísticas espectrais e análises adicionais**, incluindo espaçamentos
   normalizados, correlações e estudos comparativos com modelos teóricos.

Essa metodologia garante uma separação rigorosa entre **detecção**, **refinamento**
e **validação**, resultando em um pipeline experimental confiável, reproduzível
e alinhado com as melhores práticas da matemática computacional.
