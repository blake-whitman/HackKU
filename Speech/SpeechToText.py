import speech_recognition as sr

def speech_to_text():
    # initialize recognizer class
    r = sr.Recognizer()

    ingredients = []
    cont = True
    while cont:
        # Reading Microphone as source
        with sr.Microphone() as source:
            print("Say an ingredient you have or say 'done' when finished:")
            audio_text = r.listen(source)
        
        try:
            # using google speech recognition
            ingredient = r.recognize_google(audio_text, language='en-US')
            if ingredient.lower() == 'done':
                cont = False
                break
            ingredients.append(ingredient)
            print(f"Ingredient Added: {ingredient}")
        except:
            print("Sorry, I did not catch that. Please try again or say 'done'")
    return ingredients
