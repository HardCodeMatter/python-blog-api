import firebase_admin
from firebase_admin import credentials, firestore_async

from .config import firebase_settings


class FirestoreClient:
    def __init__(self) -> None:
        cred = credentials.Certificate(firebase_settings.CERTIFICATE_URL)
        firebase_admin.initialize_app(cred, {
            'project_id': firebase_settings.PROJECT_ID
        })

        self.db = firestore_async.client()

    async def get_document_by_id(self, collection_name: str, document_id: str):
        try:
            doc_ref = self.db.collection(collection_name).document(document_id)
            doc = await doc_ref.get()

            if doc.exists:
                return doc.to_dict()['content']
            else:
                print(f'Document "{document_id}" doesn\'t exist in collection "{collection_name}".')
                return None
        except Exception as e:
            print(f'Error getting document: {e}')
            return None


firestore_client = FirestoreClient()
