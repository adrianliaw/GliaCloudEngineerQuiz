from django.apps import AppConfig


examples = [
    "I must not have understood what you were asking for",
    "The client wanted it changed at the last minute",
    "What did I tell you about using parts of the system you don't understand?",
    "It's not a code problem - our users need more training",
    "I haven't been able to reproduce that",
    "It must be because of a leap year",
    "I can have a look but there's a lot of if statements in that code!",
    "This code was not supposed to go in to production yet",
    "I thought I fixed that",
    "I have never seen that before in my life",
    "It worked yesterday",
]

class ExcusesConfig(AppConfig):
    name = 'excuses'

    def ready(self):
        Sentence = self.get_model("Sentence")
        if Sentence.objects.count() == 0:
            for sentence in examples:
                Sentence.objects.create(content_text=sentence)
