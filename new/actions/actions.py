# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector as mc

#############sql##################################################
class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("name")
        email=tracker.get_slot("email")
        try:
            db=mc.connect(
                host="127.0.0.1",
                user="root",
                password="123Sreejaya123",
                database='rasa',
            )
            cur=db.cursor()
            insert_query="INSERT INTO users(name,email) VALUES(%s,%s)"
            data=(name,email)
            cur.execute(insert_query,data)
            db.commit()
            db.close()
        except Exception as e:
            print("Error : ", e)





        dispatcher.utter_message(response="utter_thanks")

        return []



class ActionShowAllData(Action):

    def name(self) -> Text:
        return "action_show_all_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("name")
        email=tracker.get_slot("email")
        try:
            db=mc.connect(
                host="127.0.0.1",
                user="root",
                password="123Sreejaya123",
                database='rasa',
            )
            cur=db.cursor()
            select_query="SELECT name,email FROM users"
            cur.execute(select_query)
            data=cur.fetchall()
            db.close()
            if data:
                entries="\n".join([f"(name:{row[0]},email{row[1]})" for row in data])
                response=f"Sure, these are the details of the database:\n{entries}"
            else:
                response="The database is empty"
            dispatcher.utter_message(text=response)


        except Exception as e:
            print("Error : ", e)

            dispatcher.utter_message(text="Sorry,Something went wrong")






        dispatcher.utter_message(response="utter_thanks")

        return []


#########################################################################
class ActionEnterPhoneNumber(Action):
    def name(self) -> Text:
        return "action_enter_phone_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the phone number entity from the tracker
        phone_number = tracker.get_slot("number")

        # Validate if the phone number is extracted
        if phone_number:
            dispatcher.utter_message(f"Great! You've entered the phone number: {phone_number}. How many sheets did you used")
        else:
            dispatcher.utter_message("I'm sorry, but I couldn't detect a valid phone number.")

        return []

#################################################
import openai
from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

CHAT_GPT_CUSTOM_ACTION_ = 'ChatGPT (custom_action): '

# To reduce configuration file parsing time overhead
OPENAI_ENGINE_VERSION = "gpt-3.5-turbo-0125"
OPENAPI_API_KEY = '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'
MAX_TOKENS = 1024
TEXT_PROPERTY_NAME = 'text'
OPEN_AI_GPT_METHOD_NAME = "open_ai_gpt"
VERY_FIRST = 0
TEMPERATURE_CHOICE = 0.5
STOP_AT = None
NUMBER_OF_QUERY = 1


def ask_chatgpt(user_message_text):
    # OpenAI API Key
    openai.api_key = OPENAPI_API_KEY

    # Use OpenAI API to get the response for the given user text and intent
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot."},
            {"role": "user", "content": user_message_text},
        ],
        max_tokens=MAX_TOKENS,
        n=NUMBER_OF_QUERY,
        stop=STOP_AT,
        temperature=TEMPERATURE_CHOICE,
    ).choices[VERY_FIRST].message['content']

    # Return the response from OpenAI
    return response



class OpenAiGpt(Action):

    def name(self) -> Text:
        return OPEN_AI_GPT_METHOD_NAME

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the latest user text
        user_text = tracker.latest_message.get(TEXT_PROPERTY_NAME)
        openai.api_key = OPENAPI_API_KEY

        prompt = self.buildprompt(user_text)
        # Dispatch the response from OpenAI to the user
        dispatcher.utter_message(CHAT_GPT_CUSTOM_ACTION_ + ask_chatgpt(user_text))

        return []

    @staticmethod
    def buildprompt(user_text):
        return (f"The user said: {user_text}\n"
                f"ChatGPT: "
                )