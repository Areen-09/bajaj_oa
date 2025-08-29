from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Union, Dict

app = FastAPI()

class RequestData(BaseModel):
    data: List[Union[str, int, float]]

def categorize_input_data(input_array: List[Union[str, int, float]]) -> Dict:
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []

    for item in input_array:
        item_str = str(item)
        if item_str.isdigit():
            num = int(item_str)
            if num % 2 == 0:
                even_numbers.append(item_str)
            else:
                odd_numbers.append(item_str)
        elif item_str.isalpha():
            alphabets.append(item_str.upper())
        else:
            special_characters.append(item_str)
            
    return {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
    }

def calculate_total_sum(odd_numbers_str: List[str], even_numbers_str: List[str]) -> str:
    total_sum = 0
    for num_str in odd_numbers_str:
        total_sum += int(num_str)
    for num_str in even_numbers_str:
        total_sum += int(num_str)
    return str(total_sum)

def process_alphabet_string(alphabets_list: List[str]) -> str:
    concat_string = "".join(alphabets_list)
    reversed_string = concat_string[::-1]
    alternating_caps_string = ""
    for i, char in enumerate(reversed_string):
        if i % 2 == 0:
            alternating_caps_string += char.upper()
        else:
            alternating_caps_string += char.lower()
    return alternating_caps_string

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Array Processing API!",
        "github_repository": "https://github.com/Areen-09/bajaj_oa.git",
        "bfhl_endpoint_info": {
            "path": "/bfhl",
            "method": "POST",
            "description": "This endpoint processes an array of mixed data types (strings, integers, floats) and returns categorized and transformed data. It expects a JSON body with a 'data' key containing a list.",
            "example_request_body": {
                "data": ["a", "1", "334", "4", "R", "$"]
            }
        },
        "details": "For more detailed information, including API contract, setup instructions, and deployment, please refer to the GitHub repository."
    }

@app.post("/bfhl")
def process_array(request: RequestData):
    try:
        categorized_data = categorize_input_data(request.data)
        total_sum = calculate_total_sum(categorized_data["odd_numbers"], categorized_data["even_numbers"])
        alphabet_string = process_alphabet_string(categorized_data["alphabets"])
        
        response_data = {
            "is_success": True,
            "user_id": "areen_agrawal_09102003",
            "email": "areen.agrawal2022@vitstudent.ac.in",
            "roll_number": "22BEC0921",
            "odd_numbers": categorized_data["odd_numbers"],
            "even_numbers": categorized_data["even_numbers"],
            "alphabets": categorized_data["alphabets"],
            "special_characters": categorized_data["special_characters"],
            "sum": total_sum,
            "concat_string": alphabet_string
        }
        return response_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
