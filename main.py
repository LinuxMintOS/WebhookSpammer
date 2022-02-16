import requests
from discord_webhooks import DiscordWebhooks

webhook_url = input('WEBHOOK URL ')

message = input('WHAT SHALL IT SPAM ')
ilosc = int(input('HOW MANY AMOUNT OF MESSAGES '))


webhook = DiscordWebhooks(webhook_url)

webhook.set_content(title='whats tilte',
                    description=message,
                    color=0xF58CBA)

webhook.set_footer(text='whats footer')



for i in range(ilosc):
    webhook.send()
