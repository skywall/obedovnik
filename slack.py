# -*- coding: utf-8 -*-
import os
from slacker import Slacker

config = {
        "token" : os.environ['SLACK_USER_TOKEN'],
        "channel" : "obedovnik"
}

class SlackBot:
    def __init__(self):
        self.slacker = Slacker(config["token"])
        self.channel = config["channel"]

    def send_snippet(self, title, message):
        self.slacker.files.upload(
            content = message,
            initial_comment = title,
            title = title,
            channels = self.channel
        )

    def send_message(self, message):
        self.slacker.chat.post_message('#' + self.channel, message)

    def send_poll(self, title, options):
        channel_id = self.slacker.channels.get_channel_id(self.channel)
        self.slacker.chat.command(
            channel = channel_id,
            command = '/poll',
            text = "\"" + title + "\" \"" + "\" \"".join((str(res) for res in options)) + "\""
        )

