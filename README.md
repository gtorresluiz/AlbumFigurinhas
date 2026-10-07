# Álbum de Amor - Duda & Gabriel

Um projeto especial de álbum de figurinhas virtual interativo desenvolvido para celebrar o aniversário de 1 ano de namoro. O sistema traz animações realistas de virada de página, sons imersivos e temas claro/escuro.

## 🌟 Funcionalidades

- **Álbum Interativo**: Navegação com animação de virada de página (PageFlip). No desktop permite arrastar as páginas pelos cantos, enquanto no mobile apresenta um layout otimizado carregando uma figurinha por vez com navegação via setas.
- **Integração Dinâmica**: As figurinhas são carregadas dinamicamente via uma API backend, preenchendo as páginas automaticamente.
- **Sons Realistas**: Áudio processual simulando o atrito do papel ao virar a página (sintetizado via Web Audio API).
- **Modos Visual**: Suporte à alternância entre modo Dark e Light.
- **Efeitos Visuais Premium**: Elementos glitch, cartões flutuantes 3D e selos holográficos na capa do álbum.

## 🛠️ Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla).
- **Animações**: Biblioteca [St.PageFlip](https://nodlik.github.io/StPageFlip/) para renderização e física das páginas do álbum.
- **Backend (Opcional para dados)**: O app espera uma API rodando na mesma origem na rota `/figurinhas` (configurável no `app.js`).

## 🚀 Como Executar Localmente

### Apenas Frontend (Layout e Animações)
Você pode abrir o projeto diretamente no seu navegador.
1. Clone este repositório.
2. Abra o arquivo `frontend/index.html` em qualquer navegador web moderno.
3. *Nota: Para visualizar as figurinhas nas páginas, é necessário rodar a API de backend, caso contrário o álbum exibirá os placeholders vazios para as figurinhas.*

### Integração com Backend
1. Abra o terminal na pasta do backend.
2. Inicie o servidor (ex: FastAPI com `uvicorn main:app --reload`).
3. Acesse a aplicação na porta servida pelo seu backend (ex: `http://localhost:8000`).

## 📱 Responsividade

O design é adaptável para funcionar adequadamente em dispositivos móveis. Em telas menores (mobile), o sistema de arraste de página é desativado em favor de uma navegação suave e sem falhas usando as setas de voltar e avançar, focando na exibição de uma página de figurinhas por vez.
