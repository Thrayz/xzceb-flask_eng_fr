import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
tl = language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

tl.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

def english_to_french(text_to_translate):
   
    if text_to_translate is None:
        return None
    translated = tl.translate(text=text_to_translate,model_id="en-fr").get_result()
    translation = translated['translations'][0]['translation']
    return translation

def french_to_english(text_to_translate):
    
    if text_to_translate is None:
        return None
    translated = tl.translate(text=text_to_translate,model_id="fr-en").get_result()
    translation = translated['translations'][0]['translation']
    return translation