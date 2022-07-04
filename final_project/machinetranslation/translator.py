"""
This is the translator file
"""

#import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
version_lt='2018-05-01'
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url)

# Function for translating English to French

def english_to_french(text1):
    """
    This function translates english to french
    """
    if text1=="":
        return "null"
    frenchtranslation = language_translator.translate(text=text1, model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(text1):
    """
    This function translates french to english
    """
    if text1=="":
        return "null"
    englishtranslation = language_translator.translate(text=text1, model_id='fr-en').get_result()
    return englishtranslation.get("translations")[0].get("translation")

