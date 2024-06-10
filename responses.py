from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Well, you\'re awfully silent...'
    
    
    # GREETINGS
    elif 'hello' in lowered:
        return choice([
            'Ooh ooh, hello there! 🐵',
            'Hello, my friend!',
            'Yo yo yo, what\'s up? 🦍',
        ])
        
    elif 'how are you' in lowered:
        return 'Ooh, I\'m banana-tastic! 🍌'

    elif 'hi' in lowered:
        return 'Hi there! 🙉'
    
    elif 'hey' in lowered:
        return 'Hey, how\'s it going? 🐒'
    
    elif 'good morning' in lowered:
        return 'Good morning! 🌞'
    
    elif 'good afternoon' in lowered:
        return 'Good afternoon! 🌅'
    
    elif 'good evening' in lowered:
        return 'Good evening! 🌌'
    
    elif 'howdy' in lowered:
        return 'Howdy partner! 🤠'
    
    elif 'what\'s up' in lowered:
        return 'Not much, just hanging out! 🙈'
    
    elif 'greetings' in lowered:
        return 'Greetings! 🌟'
    
    elif 'hola' in lowered:
        return 'Hola amigo! 🎉'
    
    elif 'bye' in lowered:
        return 'Catch you later, buddy! 👋'
    
    # FUNCTIONS
    elif 'roll dice' in lowered:
        return f'You rolled {randint(1, 6)} 🎲'
    
    # BOT DOESN'T UNDERSTAND
    else:
        return choice([
            'I\'m sorry, I don\'t understand... 🤔',
            'I\'m not sure what you mean... 🙉',
            'I\'m a bit confused... 🐒',
            'Could you repeat that?',
            'Ooh ooh, I\'m scratching my head on that one... 🙈',
            'Hmm, let me scratch my chin and think about it... 🤔',
            'I\'m a bit bananas about this one... 🍌',
            'Sorry, my monkey brain is on vacation right now... 🏝️',
        ])
