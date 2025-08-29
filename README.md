# Array Processing API

## Description
This project implements a REST API designed to process an array of mixed data types. It provides a single POST endpoint that accepts an array and returns a structured JSON object containing personal identification details and the results of various data manipulation and categorization operations performed on the input array.

## Core Features
- **API Endpoint for Data Processing:** A single publicly accessible API endpoint at `/bfhl` for POST requests.
- **Data Categorization:** Parses input array elements into even numbers, odd numbers, alphabets, or special characters.
- **Numerical and Alphabetical Operations:** Sums all numerical values, converts alphabets to uppercase, and creates a concatenated string from alphabetical characters with alternating capitalization.
- **Structured JSON Response:** Returns a consistent and predictable JSON response format.
- **Error Handling:** Gracefully manages invalid or missing input data with appropriate HTTP status codes and structured error responses.

## Local Setup
To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Areen-09/bajaj_oa.git
    cd bajaj_oa
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the FastAPI application:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### `POST /bfhl`
Processes an array of mixed data types and returns categorized and transformed data.

**Request Body:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Success Response (Code 200):**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

**Error Response (Code 400 or other relevant error code):**
```json
{
  "is_success": false,
  "user_id": "john_doe_17091999",
  "error_message": "Invalid input: 'data' field is required and must be an array."
}
```

## Deployment
This project is configured for deployment on [Vercel](https://vercel.com/). You can deploy it by connecting your GitHub repository to your Vercel account and triggering a new deployment.

## Contact
For any questions or feedback, please contact [Your Name/Email/GitHub Profile].
