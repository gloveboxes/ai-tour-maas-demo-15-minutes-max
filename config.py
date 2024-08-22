import dotenv
import os

dotenv.load_dotenv()

phi_endpoint = os.getenv("PHI_ENDPOINT")
phi_key = os.getenv("PHI_KEY")
mistral_endpoint = os.getenv("MISTRAL_ENDPOINT")
mistral_key = os.getenv("MISTRAL_KEY")


config = {
    "phi3": [phi_endpoint, phi_key],
    "mistral": [mistral_endpoint, mistral_key],
}
