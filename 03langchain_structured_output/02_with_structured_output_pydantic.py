from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Optional, Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

reviews = [
"Its only few days and so far the initial impressions is great. Also after some small hiccups on the installation part, I contacted LG directly and they sent the Engineer for Installation and Demo in the same day afternoon. It was good experience on the installation and demo part. On the fridge, I expected it to be little bigger in size going by the 655L volume. However, good to see it is compact and not oversized. One side is normal fridge and the other full side is deep freezer. We can set the temperature separately for both the sides. Also due to inverter feature it consumes less electricity overall although it is a 3 Star rating fridge. Will share more details after few weeks of using it.",
"Very satisfactory purchase , size is too good its huge , easy to move but lifting is heavy , front quoting is sensitive gets scratch very easily .. but satisfied overAll",
"Product is good but the delivery and installation was very bad. I ordered it on 11th and it was delivered on 17th. I had to call them multiple times to get the delivery date. After delivery, I called them for installation and they said they will come in 2-3 days but they came after 10 days. Overall experience is not good.",
"At starting the refrigerator worked fine but after 6 months the cooling significantly reduced and now at one year the situation is that i cant have any ice or cold water at all. There is cold water to drink only in the morning and no ice in the morning also. I can't leave ice-cream in the freezer as it will completely melt in half an hour",
"When it comes to refrigerators, the Samsung 580 L French Door Refrigerator stands out as a true marvel of modern appliance engineering. With its convertible design, digital inverter technology, and frost-free operation, it's a powerhouse of convenience and efficiency. The standout feature of this refrigerator is its spacious French door design, providing easy access to both fresh and frozen foods. The 580-liter capacity ensures ample room for all your groceries, making it ideal for families or those who like to stock up on essentials. One of the most impressive aspects of this refrigerator is its convertible functionality. With the touch of a button, you can transform the freezer into additional fridge space, giving you the flexibility to adapt to your changing storage needs. Whether you're hosting a party and need extra room for appetizers or simply need more space for fresh produce, this feature is incredibly convenient. The digital inverter technology is another highlight of this refrigerator. Not only does it ensure efficient cooling, but it also helps to maintain a consistent temperature, keeping your food fresher for longer. Additionally, the frost-free operation means you'll never have to deal with the hassle of defrosting the freezer, saving you time and effort in the long run. In terms of design, the Samsung 580 L French Door Refrigerator is sleek and modern, making it a stylish addition to any kitchen. The stainless steel finish is not only aesthetically pleasing but also easy to clean and resistant to fingerprints. While this refrigerator boasts an impressive array of features, it's not without its drawbacks. Some users have reported issues with the ice maker, experiencing occasional jams or slow ice production. Additionally, the price point may be a bit steep for some consumers, but given the quality and features offered, it's a worthwhile investment for those in need of a reliable and spacious refrigerator. Overall, the Samsung 580 L French Door Refrigerator is a top contender in the world of kitchen appliances. Its innovative design, advanced technology, and ample storage space make it a must-have for anyone seeking convenience and efficiency in their home.",
"Yesssss!!!!"
]

chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# define a TypedDict for the structured output
class Review(BaseModel):
    key_themes: list[str] = Field(description="A list of key themes mentioned in the review, e.g. quality, delivery and installation, value for money, etc.")
    summary: str = Field(description="A concise summary of the review")
    sentiment_rating: int = Field(ge=1, le=5, description="rate the sentiment of the review on a scale of 1 to 5 where 1 is extremely negative and 5 is extremely positive")
    sentiment_literal: Literal["neg", "neu", "pos"] = Field(description="A literal sentiment label for the review, either 'negative', 'neutral', or 'positive'")
    pros: Optional[list[str]] = Field(default=None, description="A list of pros mentioned in the review, if any")
    cons: Optional[list[str]] = Field(default=None, description="A list of cons mentioned in the review, if any")

structured_model = chat_model.with_structured_output(Review)

response = structured_model.invoke(reviews[5])
print(response.summary)
print(response.sentiment_rating)
print(response.sentiment_literal)
print(response.key_themes)
print(response.pros)
print(response.cons)
