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