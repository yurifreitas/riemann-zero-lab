## Sobre o Turing Check

O método de Turing **não deve ser aplicado globalmente em intervalos curtos**
para valores elevados de *T*, pois a fórmula assintótica de
Riemann–von Mangoldt apresenta **erro local significativo** nesse regime.

Aplicações ingênuas do método podem levar a **falsos negativos**, sugerindo
zeros ausentes ou inconsistências que são apenas artefatos numéricos.

Neste projeto, o **Turing check é aplicado corretamente por blocos disjuntos**,
cada um suficientemente grande para que os termos de erro da fórmula
assintótica permaneçam controlados.

Essa abordagem reflete a **prática consagrada em matemática computacional**,
garantindo que:
- a contagem de zeros seja localmente confiável,
- sobreposições usadas na busca não contaminem a validação,
- e a consistência global da enumeração seja preservada.

O resultado é uma verificação robusta e metodologicamente correta da
completude dos zeros detectados em cada intervalo analisado.
