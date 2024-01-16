# Roche_Hackthon_Fizz_buzz_challenge

# Fizz-Buzz Server

## Overview

This is a simple Fizz-Buzz server implemented in Python using Flask. The server exposes a REST API endpoint for Fizz-Buzz and a statistics endpoint.

## Getting Started

### Prerequisites

- Python 3.x
- Flask (install using `pip install Flask`)

#### Navigate to the project directory:

- cd Fizz-Buzz-Server
**Create and activate a virtual environment (optional but recommended):**
   python -m venv venv
**Activate virtual environment:**
- On Bash : source venv/bin/activate  
- On Windows: .\venv\Scripts\activate

**Install dependencies:**

- pip install -r requirements.txt

**Usage**

#### Run the Fizz-Buzz server:
- python fizzbuzz_server.py

The server will start on http://127.0.0.1:5000/.

Open your web browser or use a tool like curl or Postman to interact with the server.

Fizz-Buzz Endpoint: http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz
Statistics Endpoint: http://127.0.0.1:5000/statistics

**Running Tests**

- pytest test_fizzbuzz_server.py

**Project Structure**

fizzbuzz_server.py: Main server implementation.
test_fizzbuzz_server.py: Pytest unit tests.
requirements.txt: List of project dependencies.

### Installation

1. Clone the repository:

  https://github.com/SunkariApoorva/Roche_Hackthon_Fizz_buzz_challenge.git
