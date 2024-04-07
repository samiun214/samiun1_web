import streamlit as st
import pyttsx3
import speech_recognition as sr

# Product data
products = {
    "product1": {"name": "Product 1", "price": 100},
    "product2": {"name": "Product 2", "price": 200},
    "product3": {"name": "Product 3", "price": 300}
}

def voice_ai():
    text_to_speech("Hello, I am Amazon AI. How can I help you?", rate=100, volume=0.9, pitch=200)
    discount_codes = ["sat13245", "stuvx12", "d4321ff", "samiun13"]  # List of discount codes

    while True:
        command = take_command()

        if "jacket" in command and ("price" in command or "cost" in command):
            price = 80  # Default price for the jacket
            text_to_speech(f"Hello! This jacket is priced at ${price}.")

        elif any(keyword in command for keyword in ["price this jacket"]):
            price = 80  # Default price for the jacket
            text_to_speech(f"Hello! This jacket is priced at ${price}.")

        elif any(keyword in command for keyword in ["too much", "cheaper", "lower price"]):
            price = 80  # Default price for the jacket
            price, discount_codes = apply_discount(price, discount_codes)  # Apply discount based on available codes
            text_to_speech(f"I understand, but this jacket is of high quality and very popular. "
                           f"Sure, I can do ${price}.")

        elif any(keyword in command for keyword in ["thank you", "no, that's all"]):
            price = 60  # Final discounted price after acceptance
            text_to_speech("Thank you! I appreciate it. I'll take it at $60. "
                           "Should you require anything else later on, don't hesitate to give us a call. "
                           "Have a fantastic day!")
            # Bargaining process finished, announce discount code
            if discount_codes:
                text_to_speech(f"Your discount code for this session is: {discount_codes[0]}")
            else:
                text_to_speech("You don't have any available discount codes.")

        elif "my discount code" in command:
            if discount_codes:
                text_to_speech(f"Your discount code for this session is: {discount_codes[0]}")
            else:
                text_to_speech("You don't have any available discount codes.")

        elif "exit" in command:
            text_to_speech("Exiting the program. Goodbye!")
            break
        else:
            text_to_speech("Unknown command. Please try again.")

def text_to_speech(text, rate=200, volume=1.0, pitch=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  
    engine.setProperty('volume', volume)  
    engine.setProperty('pitch', pitch)  
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        st.write("Recognizing...")
        text = recognizer.recognize_google(audio)
        st.write("You said:", text)
        return text.lower()  # Convert recognized text to lowercase for easier command processing
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError as e:
        st.write("Could not request results; {0}".format(e))
        return ""

def apply_discount(price, discount_codes):
    # Assuming discount_codes is a list containing available discount codes
    if discount_codes:
        discount_code = discount_codes[0]  # Get the first discount code from the list
        # Your discount code logic here (I'm assuming a fixed discount amount for demonstration)
        discount_amount = 10  # Assuming a $10 discount
        discounted_price = price - discount_amount
        st.write(f"Discount code {discount_code} applied. Price after discount: ${discounted_price}")
        discount_codes.pop(0)  # Remove the used discount code from the list
        return discounted_price, discount_codes
    else:
        st.write("No available discount codes.")
        return price, discount_codes

def main():
    st.title("E-commerce Website")

    # Sidebar with product selection
    selected_product = st.sidebar.radio("Select a product:", list(products.keys()))

    # Display product details
    st.write(f"## {products[selected_product]['name']}")
    st.write(f"Price: ${products[selected_product]['price']}")

    # Buttons for Buy, Add to Cart, and Voice AI
    if st.button("Buy"):
        st.write("Buy button clicked!")
        # Add code to handle purchase

    if st.button("Add to Cart"):
        st.write("Add to Cart button clicked!")
        # Add code to add product to cart

    if st.button("Voice AI"):
        st.write("Voice AI button clicked!")
        voice_ai()

if __name__ == "__main__":
    main()
