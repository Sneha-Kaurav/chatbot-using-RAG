from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="AIzaSyBzGHUo_yeZ4babsuo3K6sE4Z7aq-qJju0")
response = model.invoke("Write me an essay about marie with 100 words.")
print(response.content)