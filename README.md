# URL Shortener

This is a simple URL shortener application built using Python, FastAPI, and SQLite. It allows users to shorten long URLs into shorter, more manageable links.

## Endpoints

### Create Shortened URL

- **Method:** POST
- **Endpoint:** `/`
- **Description:** Create a shortened URL.
- **Request Body:**
  - `original_url` (string): The original long URL to be shortened.
- **Response:**
  - `url` (string): The shortened URL.

### Redirect to Original URL

- **Method:** GET
- **Endpoint:** `/{key}`
- **Description:** Redirects the user to the original URL associated with the provided key.
- **Parameters:**
  - `key` (string): The key associated with the shortened URL.
- **Response:**
  - Redirects the user to the original URL if not expired and active.

### Get Shortened URL Details (Admin Endpoint)

- **Method:** GET
- **Endpoint:** `/admin/{key}`
- **Description:** Retrieve details about the shortened URL.
- **Parameters:**
  - `key` (string): The key associated with the shortened URL.
- **Response:**
  - JSON object containing details about the shortened URL:
    - `original_url` (string): The original long URL.
    - `url` (string): The shortened URL.
    - `created` (int): The time the shortened url was created
    - `expiry` (integer): The expiration date of the shortened URL.
    - `active` (boolean): Indicates if the shortened URL is active.
    - `visits` (int): Indicates the number of times this link has been visited 

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/VictorLoy/url-shortener.git
    ```

2. Navigate to the project directory:

    ```bash
    cd url-shortener
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On Linux/macOS:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Use the provided endpoints to interact with the URL shortener.

## Database

This project uses SQLite as its database to store URLs and their corresponding shortened versions. The database file is `shortener.db` located in the project directory.

## Contributors

- [Victor](https://github.com/VictorLoy)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
