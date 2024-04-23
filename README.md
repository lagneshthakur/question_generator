# Question Generator Flask App

This is a Flask application that generates questions based on a given input.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lagneshthakur/question-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd question-generator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:

    ```bash
    python main.py
    ```

2. Open your web browser and go to `http://localhost:8001`.

3. Verify that you see a Hello World! to ensure app is running

## Testing with Postman

To test the `generate_question` and `generate_questions` endpoints, you can use Postman, a popular API testing tool. Follow the steps below to get started:

1. Download and install Postman from the [official website](https://www.postman.com/downloads/).

2. Launch Postman and import the provided collection by clicking on the **Import** button.

3. Once the collection is imported, you will see the available endpoints listed in the left sidebar.

4. Select the `Generate Question` or `Generate Questions` endpoint and click on the **Send** button to make a request.

5. Inspect the response to see the generated question(s) based on the provided input.

6. Feel free to modify the request parameters or body to test different scenarios.

Remember to start the Flask app before making requests with Postman. Refer to the **Usage** section above for instructions on running the app.

Happy testing!

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.
