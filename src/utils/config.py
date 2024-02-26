from pydantic_settings import BaseSettings, SettingsConfigDict


class FirebaseSettings(BaseSettings):
    FIRESTORE_CERTIFICATE_URL: str
    FIRESTORE_PROJECT_ID: str

    @property
    def CERTIFICATE_URL(self):
        return f'{self.FIRESTORE_CERTIFICATE_URL}'
    
    @property
    def PROJECT_ID(self):
        return f'{self.FIRESTORE_PROJECT_ID}'
    
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='allow'
    )


firebase_settings = FirebaseSettings()
