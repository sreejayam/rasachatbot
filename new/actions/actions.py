# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions
#
#
# # This is a simple example for a custom action which utters "Hello World!"
#
# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []
#
#
#
# # File: actions.py
#
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import mysql.connector
#
# class ActionDataUpdate(Action):
#     def name(self) -> Text:
#         return "action_data_update"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Retrieve user inputs from the conversation
#         name = tracker.get_slot("name")
#         crop_stage = tracker.get_slot("Crop_stage")
#
#         # Connect to the MySQL database
#         db = mysql.connector.connect(
#             host="127.0.0.1",
#             user="root",
#             password="123Sreejaya123",
#             database="db1",
#         )
#
#         # Create a cursor object
#         cursor = db.cursor()
#
#         # Create the "simplify" table if it doesn't exist
#         cursor.execute("CREATE TABLE IF NOT EXISTS simplify (name VARCHAR(255), Crop_stage VARCHAR(255));")
#
#         # Build and execute the SQL query to insert data
#         query = 'INSERT INTO simplify(name, crop_stage) VALUES("{0}", "{1}");'.format(name, crop_stage)
#         cursor.execute(query)
#
#         # Commit the changes to the database
#         db.commit()
#
#         # Display the number of records inserted
#         print(cursor.rowcount, "record inserted")
#
#         # Close the cursor and database connection
#         cursor.close()
#         db.close()
#
#         # Respond to the user
#         dispatcher.utter_message(text=f"Thank you, {name}! Your crop stage ({crop_stage}) has been updated in the database.")
#
#         return []
