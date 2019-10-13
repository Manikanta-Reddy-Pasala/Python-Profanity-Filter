from better_profanity import profanity

profanity.load_censor_words()

censored_text = profanity.censor("fuck you")
print(censored_text)

text = "bahen chod sala"
censored_text = profanity.censor(text)
print(censored_text)

custom_badwords = ['bahen chod']
profanity.add_censor_words(custom_badwords)

text = "bahen chod sala"
censored_text = profanity.censor(text)
print(censored_text)
