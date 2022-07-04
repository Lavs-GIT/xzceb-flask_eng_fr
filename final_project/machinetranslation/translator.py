import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/be85874b-7169-46e2-810e-ae031d4176cb')

# Function for translating English to French

def english_to_french(text1):
    """
    This function translates english to french
    """
    if text=="":
        return "null"
    
    frenchtranslation = language_translator.translate(text=text1, model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(text1):
    """
    This function translates french to english
    """
    if text=="":
        return "null"

    englishtranslation = language_translator.translate(text=text1, model_id='fr-en').get_result()
    return englishtranslation.get("translations")[0].get("translation")
    
