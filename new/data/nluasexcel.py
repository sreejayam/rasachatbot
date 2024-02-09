import os
import uuid
import pandas as pd

from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData

def excel_to_rasa_nlu():
    """Convert data from Excel file to Rasa NLU format"""
    excel_file_path = "C:\\Users\\sudhe\\OneDrive\\Desktop\\trainingset.xlsx"  # Specify your Excel file path here
    output_folder = "data/nlu/"
    output_format = "yaml"  # Change the output format to YAML

    # Read Excel file
    df = pd.read_excel(excel_file_path)

    # Create messages
    messages = [Message.build(str(row["message"]), row["intent"]) for _, row in df.iterrows()]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    unique_filename = str(uuid.uuid4()) + "." + output_format

    with open(os.path.join(output_folder, unique_filename), "w") as outfile:
        if output_format == "md":
            outfile.write(TrainingData(messages).nlu_as_markdown())
        elif output_format == "json":
            outfile.write(TrainingData(messages).nlu_as_json())
        else:
            outfile.write(TrainingData(messages).nlu_as_yaml())

if __name__ == "__main__":
    excel_to_rasa_nlu()