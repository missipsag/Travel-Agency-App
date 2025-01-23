import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # Charger les variables d'environnement

class ModeleVoyage:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("HOST"), 
            user=os.getenv("USERNAME"),
            password=os.getenv("PASSWORD"), 
            database='agence_voyages'
        )
        self.cursor = self.conn.cursor()

    def creer_table_voyage(self): 
        query = """ 
            CREATE TABLE IF NOT EXISTS consultations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                destination  VARCHAR(100),
                date_depart DATE, 
                date_retour DATE, 
                prix FLOAT,
                places_disponibles INT,
                description TEXT           
            )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def ajouter_voyage(self, data):
        query = """
            INSERT INTO consultations (destination, date_depart, date_retour, prix, places_disponibles, description)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, data)
        self.conn.commit()

    def get_voyage(self):
        self.cursor.execute("SELECT * FROM consultations")
        return self.cursor.fetchall()

    def rechercher_voyage(self, destination):
        query = "SELECT * FROM consultations WHERE destination LIKE %s"
        self.cursor.execute(query, (f"%{destination}%",))
        return self.cursor.fetchall()

    def supprimer_voyage(self, id): 
        self.cursor.execute("DELETE FROM consultations WHERE id = %s", (id,))
        self.conn.commit()

    def __del__(self): 
        try:
            if self.cursor:
                self.cursor.close()
        except ReferenceError:
            pass
        try:
            if self.conn:
                self.conn.close()
        except ReferenceError:
            pass