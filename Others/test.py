import openai

# openai.api_key = "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"
openai.api_key = "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"

response = openai.Completion.create(
    # model="text-davinci-003",
    # model="davinci:ft-personal-2023-01-12-09-33-04",
    # model="davinci:ft-personal-2023-01-12-19-17-53",
    model="davinci:ft-personal-2023-01-12-22-59-27",
    prompt="Hi! Who are you?"+"\n\n\n###\n\n",
    temperature=0,
  max_tokens=250,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=[" END"]
    # stop=[" Human:", " AI:"]
    )
print("======\n")
print("Response ->"+response.choices[0].text)
print("======\n")
# response.choices[0].text



# import openpyxl
# dataframe = openpyxl.load_workbook("TestExce2.xlsx")
 
# # Define variable to read sheet
# dataframe1 = dataframe.active
 
# # Iterate the loop to read the cell values
# for row in range(0, dataframe1.max_row):
#     for col in dataframe1.iter_cols(1, dataframe1.max_column):
#         a=str(col[row].value)
#         splitData=a.split(":")
#         print("{\"prompt\": \""+str(splitData[0])+"\",\"completion\": \""+splitData[1]+" END\"}")



# import os
# import openai

# openai.api_key = "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"

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Extract the name and mailing address from this email:\n\nDear Kelly,\n\nIt was great to talk to you at the seminar. I thought Jane's talk was quite good.\n\nThank you for the book. Here's my address 2111 Ash Lane, Crestview CA 92002\n\nBest,\n\nMaya hansen\n\nName:",
#   temperature=0,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# print(response["choices"][0].text)