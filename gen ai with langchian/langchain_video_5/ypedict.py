from typing import TypedDict,Annotated, Optional
import ollama

class review (TypedDict):
    key_themes: Annotated[list[str], 'give the list of keythemes from the review']
    summary: Annotated[str, 'brief summary of the review']
    sentiment:Annotated[str, 'return the sentiment of the review either negative, postive or neutral']
    prons:Annotated[Optional[list[str]],'list the prons  from the review']
    cons:Annotated[Optional[list[str]],'list the cons from the review ']

structured_model= model.with_structured_output(review)

result =structured_model.invoke("""• Price: ₹37,999 (8GB/256GB), ₹39,999 (12GB/256GB), and ₹41,999 (12GB/512GB)
• Display: 6.67-inch 1.5K quad-curved AMOLED, 120Hz refresh rate, 5,000 nits peak brightness
• Processor: MediaTek Dimensity 9300+ (4nm)
• Rear Cameras: 50MP primary (IMX921), 50MP periscope telephoto (IMX882/IMX883 with 3x optical zoom), 8MP ultrawide
• Front Camera: 32MP
• Battery & Charging: 5,500mAh battery with 90W fast charging (charger included in-box)
• Software: Funtouch OS 15 based on Android 15 (3 OS updates and 4 years of security patches)

Pros

• Powerful Performance: The MediaTek Dimensity 9300+ chip handles heavy gaming, multitasking, and daily use with zero lag.
• Great Telephoto Camera: The 50MP periscope telephoto lens with 3x optical zoom and strong portrait processing stands out in this price bracket according to 91Mobiles.
• Vibrant Display: The 6.67-inch quad-curved AMOLED panel is bright, sharp, and fluid at 120Hz.
• Slim & Lightweight Build: At 7.43mm thick and 192g, it feels very comfortable and premium in the hand.
• In-Box Accessories: Vivo includes both a fast charger and a protective case in the retail box.

Cons

• Plastic Frame: Despite the glass back and nice satin finish, the side frame is plastic rather than metal.
• Lower Durability Rating: It features an IP64 dust and splash resistance rating, which lags behind IP68 or IP69 competitors in the same tier.
• Pre-installed Bloatware: Funtouch OS comes with several third-party apps pre-installed, though most can be uninstalled.
• No Wireless Charging: It supports fast wired 90W charging but lacks wireless charging capabilities.
""")

print(result)
print(result['summary'])
print(result['sentiment'])
print(result['prons'])
print(result['cons'])