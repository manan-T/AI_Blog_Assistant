import streamlit as st 
import google.generativeai as genai 
from apikey import google_gemini_api_key, openai_api_key
from openai import OpenAI 
client = OpenAI(api_key = openai_api_key)
genai.configure(api_key = google_gemini_api_key)
from streamlit_carousel import carousel

single_image = dict(
    title="",
    text="",
    interval=None,
    img="",
    )

# Set up the model
generation_config = {
  "temperature": 0.9,  
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

#setting up our model
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

#set app to wide mode
st.set_page_config(layout="wide")

#title of app
st.title('✍️🤖BlogEra: Your AI Writing Companion')

#subheader
st.subheader("Now you can craft perfect blogs with the help of AI- BlogEra is your new AI Blog Companion")

#sidebar for user input

with st.sidebar:
    st.title("Input your Blog Details")
    st.subheader("Enter Details of the Blog you want to generate")

    #blog title
    blog_title = st.text_input("Blog Title")

    #keywords input
    keywords = st.text_area("Keywords (comma-separated)")

    #number of words
    num_words = st.slider("Number of Words", min_value = 250, max_value = 1000, step = 250)

    #Number of images
    num_images = st.number_input("Number of Images", min_value = 1, max_value = 5, step = 1)

    prompt_parts = [
                f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative and maintains a consistent tone throughout."
    ]
    
    #submit button
    submit_button = st.button("Generate Blog")

if submit_button:
    
    response = model.generate_content(prompt_parts)
    images = []
    images_gallery=[]


    for i in range (num_images):
      image_response = client.images.generate(
      model="dall-e-3",
      prompt=f"Generate a Blog Post Image on the title: {blog_title}",
      size="1024x1024",
      quality="standard",
      n=1,
      )
      new_image=single_image.copy()
      new_image["title"]=f"Image{i+1}"
      new_image["text"]=f"{blog_title}"
      new_image["img"]=image_response.data[0].url
      images_gallery.append(new_image)

      
    st.title("YOUR BLOG IMAGE(S) ARE HERE:")
    carousel(items=images_gallery, width=1)

    st.title("YOUR BLOG POST:")
    st.write(response.text)
  