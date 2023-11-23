# Szallodai adatbázis kötelező program

## A weboldal futtatásához szükséges lépések

### 1. Lépés: Node.js telepítése

A Node.js telepítéséhez látogasson el a [Node.js](https://nodejs.org/en/) oldalra, és töltse le a legfrissebb LTS verziót. A telepítő futtatása után a Node.js és a Node Package Manager (npm) is települ a számítógépére.

### 2. Lépés: Angular CLI telepítése

Az angular CLI telepítéséhez nyissa meg a parancssort, és futtassa a következő parancsot:

```bash
npm install -g @angular/cli
```

### 3. Lépés: Futtatás

A weboldal futtatásához nyissa meg a parancssort a projekt gyökérkönyvtárában, és futtassa a következő parancsot:

```bash
ng serve --open
```

Ezután a weboldal elérhető lesz a böngészőben a http://localhost:4200/ címen.

## API futtatása

A backend API futtatásához szükséges a [Python](https://www.python.org/) és a pip telepítése. A pip telepítéséhez nyissa meg a parancssort, és futtassa a következő parancsot:

```bash
python -m pip install --upgrade pip
```

Ha még nincs telepítve a virtualenv csomag, akkor a következő paranccsal telepíthető:

```bash
pip install virtualenv
```

Ezután létrehozunk egy virtuális környezetet a projekt /server könyvtárában a következő paranccsal:

```bash
python -m venv .venv
```

A virtuális környezet aktiválásához a következő parancsot kell futtatni:

```bash
# Windows alatt:
.venv\Scripts\activate

# Linux alatt:
source .venv/bin/activate
```

Ezután a virtuális környezetben a következő paranccsal telepíthetőek a szükséges csomagok:

```bash
pip install -r requirements.txt 
```

Ezután a backend API futtatható a következő paranccsal:

```bash
uvicorn main:app --reload
```

## Felhasznált technológiák

- [Angular](https://angular.io/)
- [Angular Material](https://material.angular.io/)
- [Node.js](https://nodejs.org/en/)
- [npm](https://www.npmjs.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/)
