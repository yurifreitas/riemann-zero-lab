# Riemann-zero-lab

Implementação experimental e paralela para **detecção numérica, validação e análise estatística**
dos zeros não triviais da função zeta de Riemann na **linha crítica**.

O projeto adota uma abordagem de **matemática experimental rigorosa**, separando de forma clara:

- detecção numérica rápida e robusta,
- refinamento de precisão,
- validação teórica local.

> **Este projeto não é uma prova da Hipótese de Riemann.**  
> Seu objetivo é fornecer um framework reproduzível para exploração computacional
> dos zeros da zeta em alturas moderadas (*T* ≳ 10⁴).

---

## ✨ Características principais

- Scan adaptativo usando a função de Hardy \( Z(t) \) em `float64`
- Refinamento de raízes com alta precisão via `mpmath`
- Execução paralela com `multiprocessing`
- Uso de *overlap* **exclusivamente para busca**, nunca para contagem
- Validação rigorosa por **método de Turing aplicado em blocos disjuntos**
- Deduplicação numérica robusta de raízes
- Estrutura clara, modular e facilmente extensível

---

## 🔬 Metodologia

1. O intervalo \([T_{\text{start}}, T_{\text{end}}]\) é dividido em blocos com sobreposição
   apenas para **detecção inicial** de mudanças de sinal.
2. Cada bloco é processado de forma independente e paralela.
3. As raízes detectadas são refinadas com alta precisão.
4. Os resultados são deduplicados globalmente.
5. A contagem de zeros é validada por um **Turing check correto**, aplicado
   em blocos **sem sobreposição**.
6. Estatísticas espectrais e análises adicionais são computadas a partir do
   conjunto validado de zeros.

---

## 📊 Análises incluídas

- Estatísticas de espaçamento normalizado entre zeros
- Comparação empírica com predições da **Random Matrix Theory (GUE)**
- Detecção explícita de falhas da Lei de Gram
- Análise de compensação local de zeros entre intervalos de Gram
- Visualizações avançadas:
  - histogramas
  - funções de distribuição acumulada (CDF)
  - mapas de correlação
  - *heatmaps* espectrais

---

## 🧠 Insight experimental

Os experimentos indicam que as aparentes falhas da Lei de Gram **não decorrem de
irregularidade no espaçamento dos zeros**, mas da **acumulação quantizada da fase
(\(\arg \zeta\)) entre pontos consecutivos de Gram**.

Os zeros emergem como eventos discretos associados à dinâmica de fase, e não
como uma simples progressão espacial regular.

---

## 🛠️ Stack tecnológica

- Python
- NumPy
- mpmath
- multiprocessing
- matplotlib

---

## 🎯 Objetivo

Fornecer um ambiente experimental confiável para:

- matemática computacional
- teoria analítica dos números
- estudos espectrais
- investigações na interface entre matemática e física




---
Instalação via ambiente virtual (recomendado):

```bash
uv venv --python 3.11
source .venv/bin/activate
python main.py
```

---


## 🎯 Resultados
Zeros encontrados: 230
Primeiros zeros:
10000.0907527738456702649384698701380796170367373777738190614
10000.5914415437572407338313807314835900895646968836590182174
10000.9634080788181716402389334827620803704780483891982123981
10002.2637144184409839759860884602941002152963563238106642391
10002.9974889109424167366544842185906060574960524572362486603
10004.0238963633618118170957331298140347052381369012623386817
10004.7127779313143496559128748628510716429447248810221040736
10005.2832063645087179518377063645202744443284480876906499621
10006.0654732349218323348567116890187203430375812935137324373
10007.3632647658060136727479214425888147738066560229836499337

Turing check: True
Plot salvo em: gaps_advanced.png

=== GAP STATISTICS ===
Total gaps: 229
Mean gap: 1.023625
Std  gap: 0.466172
Min  gap: 0.116841
Max  gap: 3.248938

=== GRAM LAW CHECK ===
Gram points: 235
Gram failures: 59
First Gram failures:
  [2 zeros] between 10000.0295320154344144741692709551021232426806248317944901045 and 10000.8817821426846340752775569200457570765014995190794306816
  [0 zeros] between 10009.4037417847275286444770738740739100326582813736158553643 and 10010.2558836118432005184900361238251260674978546083233520039
  [2 zeros] between 10010.2558836118432005184900361238251260674978546083233520039 and 10011.1080156005679907466520179351321309918624734672807038359
  [2 zeros] between 10023.8888156250894780843539682403503109772662186779554188005 and 10024.7407903596185281878918306103988593565034505009345405643
  [0 zeros] between 10024.7407903596185281878918306103988593565034505009345405643 and 10025.5927552757508203846238191118440996665508003136007723935
(zero_do_rian) yuri@yuri-pc zero_do_rian % 

---

## 📚 Referências conceituais

- Riemann, B. (1859)
- Titchmarsh, *The Theory of the Riemann Zeta-Function*
- Odlyzko, *The Riemann zeta function: zeros and random matrix theory*
- Edwards, *Riemann's Zeta Function*
- Conway (inspiração estrutural: partições, domínios exclusivos, contagem sem ambiguidade)


### Embora a Lei de Gram falhe localmente, os desvios obedecem a uma lei de conservação: excessos e déficits de zeros se compensam em escalas curtas.