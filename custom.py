# def mood_response():
#     happy = 'elated'
#     sad= 'low-spirited'
#     okay= 'content'
#     anxious= 'nervous'

# def mood_response(happy):
#     if happy: 
#         print(mood_response)

# def mood_response(sad):
#     if sad: 
#         print(mood_response)

# def mood_response(okay):
#     if okay: 
#         print(mood_response)

# def mood_response(anxious):
#     if anxious: 
#         print(mood_response)

def mood_response(mood):
    if mood == 'happy':return "Great it's important to enjoy each moment in life"
    elif mood == 'sad':return "I'm sorry you're sad right now, can I do anything to help?"
    elif mood == 'okay': return"The glass is half full, I hope it gets even better for you"
    elif mood == 'anxious':return "I've had my moments of being nervous, you can overcome those feelings"
    else: return "Regardless of how you feel, I'm here to listen"