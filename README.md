# ia-prende

Uma coleção de componentes e serviços para um agente conversacional: um backend/OS leve (`agent-os`) e uma interface web em Next.js (`agent-ui`). Projeto em desenvolvimento.

## Visão geral

- `agent-os`: componentes e lógica do agente (Python). Contém o ponto de entrada `main.py` e `pyproject.toml`.
- `agent-ui`: aplicação frontend em Next.js (TypeScript/React) com componentes de chat e armazenamento local.

## Estrutura do repositório

- `agent-os/` — código Python do agente e serviços auxiliares.
- `agent-ui/` — aplicação Next.js (frontend).

## Requisitos

- Python 3.10+ (recomendado) para `agent-os`.
- Node.js 18+ e um gerenciador de pacotes (`pnpm`, `npm` ou `yarn`) para `agent-ui`.

## Como rodar (desenvolvimento)

1) Backend (`agent-os`)

```bash
cd agent-os
python -m venv .venv        # criar ambiente virtual (se necessário)
source .venv/bin/activate   # macOS / Linux
pip install -e .            # instala em modo editável a partir do pyproject.toml
python main.py              # executa o agente
```

2) Frontend (`agent-ui`)

```bash
cd agent-ui
# com pnpm (recomendado se disponível)
pnpm install
pnpm dev

# ou com npm
npm install
npm run dev
```

Observação: a UI pode precisar de variáveis de ambiente (tokens de API, URL do backend, etc.). Verifique as referências a variáveis em `agent-ui/src` e defina `.env.local` conforme necessário.

## Desenvolvimento

- Siga as convenções de TypeScript/React em `agent-ui/src` ao adicionar componentes.
- No `agent-os`, mantenha dependências no `pyproject.toml` e prefira funcionalidades testáveis.

## Contribuição

- Abra uma issue descrevendo a proposta ou bug.
- Envie pull requests pequenos e focados com uma descrição clara das mudanças.

## Licença

Este repositório contém arquivos licenciados individualmente; verifique os cabeçalhos de cada pasta para mais informações.

