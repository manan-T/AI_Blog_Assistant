# **BlogEra: Your AI Writing Companion**

BlogEra is an innovative application that leverages the power of AI to help you craft perfect blog posts effortlessly. Using the advanced capabilities of Google's Gemini AI model and OpenAI's DALL-E, BlogEra generates engaging blog content and relevant images based on user input. Built with Streamlit, this tool offers an intuitive and interactive interface for users to create and customize their blogs.

## Features

- **AI-Powered Blog Generation**: Generate comprehensive, engaging blog posts based on your specified title and keywords.
- **Customizable Content**: Specify the number of words and incorporate keywords to tailor the content to your needs.
- **Image Generation**: Generate up to 5 images related to your blog title using OpenAI's DALL-E model.
- **Interactive Interface**: Easy-to-use sidebar for inputting blog details and generating content.
- **Wide Layout**: Streamlit's wide layout mode for a better user experience.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/BlogEra.git
    cd BlogEra
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up API keys**:
    - Create a file named `apikey.py` in the project directory.
    - Add your Google Gemini AI and OpenAI API keys:
    ```python
    google_gemini_api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
    openai_api_key = "YOUR_OPENAI_API_KEY"
    ```

5. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Input Blog Details**: In the sidebar, enter the blog title, keywords, number of words, and number of images.
2. **Generate Blog**: Click the "Generate Blog" button to generate the blog content and images.
3. **View Results**: The generated blog images will be displayed in a carousel, followed by the blog content.
