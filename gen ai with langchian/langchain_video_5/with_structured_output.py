from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional

model = ChatOllama(
    model = "llama3.1:8b",
    num_ctx = 1024

)

class review(BaseModel):
    key_themes:list[str] = Field(description="key themes from the review")

    summary:str = Field(description="give the brief summary of the review")

    sentiment: Literal["positive","negative"]= Field("return the sentiment of the review either positiven negative and neutral")

    pros : Optional[str] = Field(default=None,description="write the pros of the review")

    name : Optional[str] = Field(default=None,description="write the name of the reviewer")

structured_model = model.with_structured_output(review)

result = structured_model.invoke("""
AI Mode conversation: review of asus tuf a15 rtx 2050


You said: review of asus tuf a15 rtx 2050

review of asus tuf a15 rtx 2050
The ASUS TUF Gaming A15 (FA506NFR) with an RTX 2050 is a budget-focused gaming laptop that pairs an entry-level graphics card with a surprisingly capable processor.

Key Specifications

• Processor: AMD Ryzen 7 7435HS (8 cores, 16 threads, up to 4.5 GHz boost)
• Graphics: NVIDIA GeForce RTX 2050 (4GB GDDR6, 60W TGP)
• RAM: 16GB DDR5 (4800 MHz, upgradeable)
• Storage: 512GB NVMe M.2 SSD
• Display: 15.6-inch FHD (1920 x 1080) IPS-level, 144Hz refresh rate
• Battery: 48Whr, 3-cell Li-ion
• Weight: 2.30 kg

Performance Review

• Gaming: The RTX 2050 (60W TGP) handles older, lighter, or eSports titles smoothly (such as Counter-Strike 2, Fortnite on lower/medium settings, or GTA V). However, it struggles or requires heavy compromises (like upscaling and low-to-medium presets) for modern, VRAM-heavy AAA releases.
• Processor & Multitasking: The Ryzen 7 7435HS is snappy and handles day-to-day productivity, schoolwork, and lighter content creation well, though the laptop lacks an integrated GPU in some variants which can impact power efficiency.
• Display: The 144Hz FHD panel provides a smooth visual experience for fast-motion gaming and scrolling, typical of budget gaming laptops in this tier.
• Keyboard & Build: Features a backlit keyboard with transparent keycaps (except the WASD cluster) and MIL-STD-810H military-grade durability, though the plastic chassis is prone to fingerprint smudges. The right-side exhaust vent can also blow warm air near your mouse hand during long gaming sessions.
• Battery Life: The small 48Whr battery yields modest unplugged runtime, meaning you will need to stay plugged in for heavy tasks or gaming.

Value and Verdict

Opinions on community forums like Reddit (r/Asustuf) are mixed. Users generally note that at higher price points (above ₹60,000), an RTX 2050 configuration is poor value because RTX 3050 or RTX 4050 laptops frequently sell for a similar cost and deliver a significant performance leap. However, if found at a steep discount (around ₹55,000 or lower), it serves as a sturdy entry-level machine for light gaming and daily work.
Are you looking at a specific price for this laptop, or would you like recommendations for alternative gaming laptops in your budget?
• 
YouTube·Hardware Geek
Asus TUF Gaming A15 Review – Ryzen 7 7435HS & RTX 2050 ...
Asus TUF Gaming A15 Review – Ryzen 7 7435HS & RTX 2050 Performance Test! which might not leave you a wishing for just a little mor...
1m
• 
Reddit
Asus Tuf A15 Ryzen 7 With Rtx 2050 is Good Or Bad Under ...
Laptop Value: The Asus TUF A15 with RTX 2050 and Ryzen 7 is generally considered a poor value under 60k, as RTX 3050 models with m...
• 
Amazon.in
ASUS TUF Gaming A15, AMD Ryzen 7 7435HS Gaming Laptop(NVIDIA RTX 2050-4GB/60W TGP/16GB RAM/512GB SSD/FHD/15.6"/144Hz/RGB KB/48WHr/Windows 11//Graphite Black/2.30 Kg) FA506NFR-HN045W : Amazon.in: Toys & Games
ASUS TUF Gaming A15, AMD Ryzen 7 7435HS Gaming Laptop(NVIDIA RTX 2050-4GB/60W TGP/16GB RAM/512GB SSD/FHD/15.6"/144Hz/RGB KB/48WHr/
Show all

in paragraqph

The ASUS TUF Gaming A15 featuring the NVIDIA GeForce RTX 2050 and the AMD Ryzen 7 7435HS processor serves as a rugged, entry-level gaming laptop tailored for budget-conscious users. Its performance is well-suited for everyday multitasking, schoolwork, and esports titles like Fortnite or Counter-Strike 2, though modern AAA games will require scaling down to lower graphic presets due to the 4GB VRAM limitation. While the 144Hz FHD display keeps fast-paced motion fluid and the MIL-STD-810H military-grade build ensures physical durability, the laptop makes typical budget compromises, including a plastic chassis prone to fingerprints, a right-side exhaust that blows warm air onto your mouse hand, and a small 48Whr battery that demands you stay near a power outlet. User feedback indicates that while it is a reliable starter machine, its value depends heavily on the price; it is a solid buy if heavily discounted, but if it approaches the cost of laptops equipped with an RTX 3050 or RTX 4050, those alternatives offer a much larger leap in gaming performance.
Are you considering buying this laptop at a specific price, or would you like to compare it against other options in your current budget?


by mrityuanjay kuamr kewat
""")

print(result.summary)
print(result.sentiment)
print(result.key_themes)
print(result.name)