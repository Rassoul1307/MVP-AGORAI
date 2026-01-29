from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_db  # On importe votre fonction de connexion

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test-db")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # On tente d'exécuter une requête SQL simple
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Connexion à PostgreSQL réussie !"}
    except Exception as e:
        # Si ça plante, on renvoie l'erreur
        raise HTTPException(status_code=500, detail=f"Erreur de connexion : {str(e)}")