# Text Generation LLM Application

## Description

A full-stack application that leverages a pre-trained language model (`distilgpt2`) to generate text based on user-provided prompts. The frontend is built with React, and the backend utilizes FastAPI to serve the model.

## Technologies Used

- **Frontend:**
  - React
  - Axios
  - CSS

- **Backend:**
  - Python
  - FastAPI
  - Uvicorn
  - Transformers (Hugging Face)
  - PyTorch

## Installation

### Backend

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/tredavis/text-generation-app.git
    cd text-generation-backend
    ```

2. **Set Up Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Backend Server:**

    ```bash
    uvicorn main:app --reload
    ```

### Frontend

1. **Navigate to Frontend Directory:**

    ```bash
    cd ../text-generation-frontend
    ```

2. **Install Dependencies:**

    ```bash
    npm install
    ```

3. **Run the React App:**

    ```bash
    npm start
    ```

## Usage

1. **Access the Frontend:**

    Open `http://localhost:3000` in your browser.

2. **Generate Text:**

    - Enter a prompt in the textarea.
    - Click "Generate Text" to receive generated content.

## Deployment 

# TODO:

- **Backend:** [Heroku Link]()
- **Frontend:** [Vercel Link]()


## Challenges and Learnings

- Implementing CORS to allow frontend and backend communication.
- Managing asynchronous requests and loading states in React.
- Optimizing model loading and ensuring efficient API responses.

## Future Improvements

- Implement user authentication.
- Add more customization options for text generation (e.g., temperature, top_k).
- Enhance the UI/UX with better design and animations.

## License

[MIT](./LICENSE)