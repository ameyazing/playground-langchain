from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, Optional, Literal
from dotenv import load_dotenv

load_dotenv()

reviews = [
"Its only few days and so far the initial impressions is great. Also after some small hiccups on the installation part, I contacted LG directly and they sent the Engineer for Installation and Demo in the same day afternoon. It was good experience on the installation and demo part. On the fridge, I expected it to be little bigger in size going by the 655L volume. However, good to see it is compact and not oversized. One side is normal fridge and the other full side is deep freezer. We can set the temperature separately for both the sides. Also due to inverter feature it consumes less electricity overall although it is a 3 Star rating fridge. Will share more details after few weeks of using it.",
"Very satisfactory purchase , size is too good its huge , easy to move but lifting is heavy , front quoting is sensitive gets scratch very easily .. but satisfied overAll",
"Product is good but the delivery and installation was very bad. I ordered it on 11th and it was delivered on 17th. I had to call them multiple times to get the delivery date. After delivery, I called them for installation and they said they will come in 2-3 days but they came after 10 days. Overall experience is not good.",
"At starting the refrigerator worked fine but after 6 months the cooling significantly reduced and now at one year the situation is that i cant have any ice or cold water at all. There is cold water to drink only in the morning and no ice in the morning also. I can't leave ice-cream in the freezer as it will completely melt in half an hour"
]

chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# define a TypedDict for the structured output
class Review(TypedDict):
    key_themes: Annotated[list[str], "A list of key themes mentioned in the review, e.g. quality, delivery and installation, value for money, etc."]
    summary: Annotated[str, "A concise summary of the review"]
    sentiment_rating: Annotated[int, "rate the sentiment of the review on a scale of 0 to 9 where 0 is extremely negative and 9 is extremely positive"]
    sentiment_literal: Annotated[Literal["neg", "neu", "pos"], "A literal sentiment label for the review, either 'negative', 'neutral', or 'positive'"]
    pros: Annotated[Optional[list[str]], "A list of pros mentioned in the review, if any"]
    cons: Annotated[Optional[list[str]], "A list of cons mentioned in the review, if any"]

structured_model = chat_model.with_structured_output(Review)

response = structured_model.invoke(reviews[2])
print(response["summary"])
print(response["sentiment_rating"])
print(response["sentiment_literal"])
print(response["key_themes"])
print(response["pros"])
print(response["cons"])
