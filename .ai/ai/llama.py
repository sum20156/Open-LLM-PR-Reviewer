import requests
import json
import sys


# The URL of the API endpoint
#url = 'https://08ae-34-85-154-100.ngrok-free.app/generate'

# The header specifying that the data being sent is in JSON format
headers = {'Content-Type': 'application/json'}



from ai.ai_bot import AiBot




class LLama(AiBot):


    def __init__(self,url,standards):
        self.__standards = standards
        self._url =url

    def ai_request_diffs(self, code, diffs):
        stream = self.send_message(AiBot.build_ask_text(code=code, diffs=diffs,standards=self.__standards))
        return stream
    
    #@staticmethod
    def send_message(self,prompt):
        # Converting the dictionary to a JSON formatted string
        data = {
            "prompt": prompt
        }
        data_json = json.dumps(data)

        # Sending the POST request and storing the response
        response = requests.post(self._url, headers=headers, data=data_json,verify=False)

        # Printing the response text to see the output from the API
        return response.text
    

if __name__ == "__main__":

    llama = LLama(standards=sys.argv[1])
    result = llama.send_message(sys.argv[1])
    print(result)
    