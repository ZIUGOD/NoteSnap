# NoteSnap

NoteSnap is a simple web application for publishing notes.

## Installation

Follow these steps to set up and run NoteSnap locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/ZIUGOD/NoteSnap
    ```

2. Navigate to the project directory:
    ```bash
    cd NoteSnap
    ```

3. Create and activate a virtual environment:

    On Linux/macOS:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run database migrations:
    ```bash
    python NoteSnap\manage.py migrate
    ```

6. Start the development server:
    ```bash
    python NoteSnap\manage.py runserver
    ```

Now you can access NoteSnap at http://127.0.0.1:8000/.

## Usage

After setting up and starting NoteSnap, you can:

- Create a user account.
- Publish notes.
- View and manage your notes.

## Contribution

If you want to contribute to NoteSnap, follow these steps:

1. Fork this repository.
2. Create a branch for your modification: `git checkout -b feature/my-feature`.
3. Make your changes and commit them: `git commit -am 'Add my feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Submit a pull request.

## Credits

- Developed by [ZIUGOD](https://github.com/ZIUGOD).
- Inspired by the website of a crazy hacker I used to know who disappeared from the scene for unknown reasons.

