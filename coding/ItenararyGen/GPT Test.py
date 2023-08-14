#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Importing necessary libraries
import openai
from IPython.display import display, clear_output
import ipywidgets as widgets

# Importing necessary CSS module
from IPython.core.display import HTML

# Add this line at the beginning of your code to apply custom CSS
display(HTML('<style>.widget-button { width: auto; }</style>'))

# Define your OpenAI API key
openai.api_key= "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"

# Defining the questions and options
questions_and_options = [
    ("Where are you joining us from?", ["From the bustling cities", "From the tranquil countryside", "From the mystical lands afar", "I'd rather not say"]),
    ("Is this your first exciting journey to Japan?", ["First-time visitor, everything's so new!", "I've been once or twice, but there's more to explore", "Japan is my second home, show me something new", "Custom answer..."]),
    ("What vibe are you looking for?", ["Big city lights and excitement!", "I've had enough of Tokyo and Osaka, show me the real Japan", "A magical mix of urban and countryside", "Custom answer..."]),
    ("Dream Destinations", ["Cherry blossoms and tea ceremonies", "Otaku heaven, anime, and manga galore!", "Ancient temples and samurai adventures", "Custom answer..."]),
    ("Budgeting for Your Adventure", ["Luxury and indulgence, no limits!", "Comfortable, but I love a good bargain", "Adventurous on a budget, show me hidden gems", "Custom answer..."]),
    ("Traditional vs Modern", ["Tradition all the way, show me the ancient arts", "Futuristic Japan, robots, and neon lights!", "A blend of old and new, please", "Custom answer..."]),
    ("Otaku Interests", ["Yes, take me to Akihabara!", "No, but I appreciate the culture", "Custom answer..."]),
    ("Duration of Stay", ["A whirlwind week", "A fortnight of fun", "A month or more, I want to see it all!", "Custom answer..."]),
    ("Are you more a traveler or a vacationer?", ["Explorer at heart, show me the hidden gems", "Vacationer, I need some relaxation", "A bit of both, please", "Custom answer..."]),
    ("What Japanese cuisine is calling your name?", ["Sushi and sashimi, please!", "Ramen and street food delights", "Vegetarian or special dietary needs", "Custom answer..."]),
    ("Are you fascinated by the history and culture of Japan?", ["Yes, take me on a historical journey", "Somewhat, but mix it with modern attractions", "Custom answer..."]),
    ("Are you ready to shop 'til you drop?", ["Designer brands and luxury", "Quirky and unique finds", "Not really interested in shopping", "Custom answer..."]),
    ("Are you seeking adventure and nature's wonders?", ["Hiking and outdoor challenges", "Peaceful gardens and scenic views", "Custom answer..."]),
    ("Ready to experience Japan's nightlife?", ["Karaoke and clubs, let's dance!", "Quiet evenings and cultural shows", "Custom answer..."]),
    ("Any special requests or needs for your trip?", ["Accessibility requirements", "Special occasions or celebrations", "Custom answer..."]),
]

# Placeholder for answers
answers = []

# Function to display question and options
def display_question(question_number):
    clear_output()
    question, options = questions_and_options[question_number]
    progress = f"({question_number + 1}/{len(questions_and_options)})"
    print(f"\nQuestion {question_number + 1} of {len(questions_and_options)}: {question} {progress}\n")
    
    # Widgets for options (without "Custom answer...")
    buttons = [widgets.Button(description=option, layout=widgets.Layout(width='auto')) for option in options if option != "Custom answer..."]
    custom_text = widgets.Text(value='', placeholder='Enter your custom answer here', description='Custom:', disabled=False, continuous_update=False)
    skip_button = widgets.Button(description="Skip", layout=widgets.Layout(width='auto'))
    
    # Displaying widgets
    for button in buttons:
        display(button)
        button.on_click(lambda b: handle_answer(b.description))
    display(custom_text)
    display(skip_button)
    
    # Custom text handler
    def handle_custom_text(change):
        if change['name'] == 'value' and change['new']:
            handle_answer(change['new'])
        
    custom_text.observe(handle_custom_text, 'value')
    
    # Skip button handler
    skip_button.on_click(lambda b: handle_answer("Skip"))    
    
# Function to handle the user's answer
def handle_answer(answer):
    answers.append(answer)
    next_question = len(answers)
    if next_question < len(questions_and_options):
        display_question(next_question)
    else:
        generate_itinerary()

# Function to generate custom itinerary
def generate_itinerary():
    # Constructing the prompt
    prompt = f"Create a {answers[8]}-day itinerary for a traveler coming from {answers[0]} to Japan. They are looking for a {answers[2]} experience and are interested in {answers[4]} {answers[5]} {answers[6]} {answers[7]}. They have a preference for {answers[9]} and would like to engage in {answers[12]}. Their budget is {answers[4]}, and they have the following special requests: {answers[14]}."

    # Call GPT API with the prompt
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=10000)
    itinerary = response.choices[0].text

    print("Your custom itinerary:", itinerary)

# Start the interview process
display_question(0)



# In[ ]:




