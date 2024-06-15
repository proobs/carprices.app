import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

load_dotenv()

creds = os.getenv('FIREBASE_CREDIS')
# Initialize Firebase Admin SDK
cred = credentials.Certificate(creds)
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_to_firebase(data):
    """
    Saves car price data and specifications to Firestore, creating a unique ID for each entry.
    """
    try:
        # Generate a document ID from the car's make, model, and year
        doc_id = f"{data['specs']['make']}_{data['specs']['model']}_{data['specs']['year']}"
        doc_ref = db.collection('car_prices').document(doc_id)
        doc_ref.set(data)
        print(f"Data saved successfully with ID {doc_id}.")
    except Exception as e:
        print(f"Failed to save data to Firestore: {e}")
