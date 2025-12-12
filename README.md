# zero_do_rian

Implementação experimental e paralela para detecção numérica de zeros não triviais
da função zeta de Riemann na linha crítica, com validação via método de Turing
(aplicado corretamente por blocos disjuntos).

Este projeto tem foco em **matemática computacional séria**, separando:
- detecção numérica (rápida e robusta),
- refinamento de precisão,
- e validação teórica local.

Não é uma prova da Hipótese de Riemann.
É um framework experimental para explorar zeros em alturas moderadas (T ≳ 10⁴).

---

## ✨ Características principais

- Scan adaptativo usando aproximação de Hardy Z (float64)
- Refinamento de raízes com `mpmath`
- Paralelismo via `multiprocessing`
- Uso de overlap **apenas para busca**, nunca para contagem
- Validação por **Turing check em blocos disjuntos**
- Deduplicação numérica robusta
- Estrutura clara, modular e extensível

---

## 📂 Estrutura do projeto

adaptive_scan.py # Detecção rápida de mudanças de sinal
├── config.py # Parâmetros globais (T, precisão, blocos)
├── hardy_z.py # Hardy Z de alta precisão (mpmath)
├── z_fast.py # Hardy Z aproximado (float64)
├── zero_finder.py # Refinamento de zeros (mp.findroot)
├── parallel_scan.py # Processamento paralelo de blocos
├── turing_check.py # Validação teórica por blocos
├── theta.py # Função theta de Riemann
├── main.py # Pipeline principal
├── pyproject.toml
└── README.md/


---
---

## ⚙️ Requisitos

- Python ≥ 3.11
- numpy
- mpmath

---


---
Instalação via ambiente virtual (recomendado):

```bash
uv venv --python 3.11
source .venv/bin/activate
python main.py
```

---
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
---


## 🧠 Metodologia (resumo)

- O intervalo `[T_START, T_END]` é dividido em **blocos de busca com overlap**.
- Cada bloco é escaneado rapidamente usando `Z_fast`.
- Intervalos candidatos são refinados com `mpmath`.
- Todos os zeros encontrados são **deduplicados globalmente**.
- Para validação, o intervalo é repartido em **blocos disjuntos reais**.
- O número de zeros em cada bloco é comparado com a fórmula de
  **Riemann–von Mangoldt**, usando **tolerância assintótica adequada**.

Esse procedimento evita falsos negativos comuns ao aplicar o método de Turing
de forma global em janelas curtas e em valores elevados de `T`.

---

## ⚠️ Limitações conhecidas

- A aproximação de Hardy Z utilizada não é otimizada para valores muito grandes
  de `T` (≳ 10⁶).
- O método de Turing empregado é **numérico e local**, não constituindo
  uma prova formal da Hipótese de Riemann.
- Possíveis falhas da lei de Gram ou zeros rasos não são tratados
  simbolicamente.

---

## 📚 Referências conceituais

- Riemann, B. (1859)
- Titchmarsh, *The Theory of the Riemann Zeta-Function*
- Odlyzko, *The Riemann zeta function: zeros and random matrix theory*
- Edwards, *Riemann's Zeta Function*
- Conway (inspiração estrutural: partições, domínios exclusivos, contagem sem ambiguidade)
