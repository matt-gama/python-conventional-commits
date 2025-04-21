# 🧪 Projeto FastAPI com Commitizen e Pre-commit

Este projeto é um exemplo didático de como utilizar **Commitizen** para versionamento semântico e changelog automático, junto com **Pre-commit** para garantir qualidade nos commits.

## 📁 Estrutura de Diretórios

```
cz-demo-fastapi/
├── app/
│   ├── reouter
|   |   └── webhook.py
│   └── main.py
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
```

---

## ✅ Arquivos de Dependências

### `requirements.txt` (produção)

```txt
fastapi
uvicorn[standard]
```

### `requirements-dev.txt` (desenvolvimento)

```txt
-r requirements.txt

# Commitizen: versionamento semântico e changelog automático
commitizen

# Pre-commit: valida commits antes de finalizar
pre-commit

# Formatador de código (opcional)
black

# Linter (opcional)
flake8

# Testes (opcional)
pytest
```

---

## 🔧 `pyproject.toml`

```toml
[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
update_changelog_on_bump = true
changelog_file = "CHANGELOG.md"
```

---

## ⚙️ `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v3.25.0
    hooks:
      - id: commitizen
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
```

---

## 🧪 Código FastAPI de Exemplo (`app/main.py`)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Commitizen!"}
```

---

## 🚀 Como Usar

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Instalar dependências de desenvolvimento

```bash
pip install -r requirements-dev.txt
```

### 3. Instalar o pre-commit

```bash
pre-commit install
```

### 4. Usar Commitizen para commit padronizado

```bash
cz commit
```

### 5. Gerar changelog e nova versão

```bash
cz bump
```

---

## 🧼 Dica

Nunca inclua `commitizen`, `pre-commit`, `black` etc. em `requirements.txt` de produção. Use sempre `requirements-dev.txt` para dependências de desenvolvimento.

---

## 📦 Comandos Úteis

```bash
git add .
cz commit
cz bump
```

Enjoy!