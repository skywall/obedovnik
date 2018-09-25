# -*- coding: utf-8 -*-
import os
from slacker import Slacker

class Settings:
    def __init__(self):
        self.token = os.environ['HOME']
        self.channel = "obedovnik"

class SlackBot:
    def __init__(self, settings):
        self.slacker = Slacker(settings.token)
        self.channel = settings.channel

    def sendSnippet(self, title, message):
        self.slacker.files.upload(
            content = message,
            initial_comment = title,
            title = title,
            channels = self.channel
        )

    def sendMessage(self, message):
        self.slacker.chat.post_message('#' + self.channel, message)

    def sendPoll(self, title, options):
        channelId = self.slacker.channels.get_channel_id(self.channel)
        self.slacker.chat.command(
            channel = channelId,
            command = '/poll',
            text = title + " " + " ".join(options)
        )
        
slackBot = SlackBot(Settings())
slackBot.sendMessage("Obedovnik na dnes:")
slackBot.sendSnippet("Catanni", "Cestoviny")
slackBot.sendSnippet("Suzies", "Steak")
slackBot.sendPoll("Pošušnáníčko?", ["first", "second", "third"])

