import dotenv
import os
import base64

dotenv.load_dotenv()

phi_endpoint = os.getenv("PHI_ENDPOINT")
phi_key = os.getenv("PHI_KEY")
mistral_endpoint = os.getenv("MISTRAL_ENDPOINT")
mistral_key = os.getenv("MISTRAL_KEY")

# The key is obfuscated to prevent accidental exposure when doing a live debug demo
# as it shows up in the debug variables. This is not a secure way to store keys.


def obfuscate_key(key):
    base64_encoded = base64.b64encode(key.encode("utf-8")).decode("utf-8")
    transformed = "".join([char * 10 for char in base64_encoded])
    padded = transformed + "XYZ123" * 10
    return padded


def deobfuscate_key(key):
    unpadded = key.rstrip("XYZ123" * 10)
    reversed_transform = unpadded[::10]
    original_key = base64.b64decode(
        reversed_transform.encode("utf-8")).decode("utf-8")
    return original_key


config = {
    "phi3": [phi_endpoint, obfuscate_key(phi_key)],
    "mistral": [mistral_endpoint, obfuscate_key(mistral_key)],
}
