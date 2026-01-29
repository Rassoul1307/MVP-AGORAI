from sqlalchemy import text

def test_connection():
    try:
        # On crée une instance de session
        db = SessionLocal()
        # On tente une requête simple (SELECT 1)
        db.execute(text("SELECT 1"))
        print("✅ Connexion à PostgreSQL réussie !")
        db.close()
    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")

if __name__ == "__main__":
    test_connection()