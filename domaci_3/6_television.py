class Television:
    def __init__(self, current_channel=0, current_channel_name="", channels=[], volume=0):
        self._current_channel = current_channel
        self._current_channel_name = current_channel_name
        self._channels = channels
        self._volume = volume

    def get_current_channel(self):
        return self._current_channel

    def set_current_channel(self, value):
        if 0 <= value < len(self._channels):
            self._current_channel = value
            self._current_channel_name = self._channels[value]
        else:
            print("Invalid channel number.")

    def get_current_channel_name(self):
        return self._current_channel_name

    def get_volume(self):
        return self._volume

    def set_volume(self, value):
        if 0 <= value <= 10:
            self._volume = value
        else:
            print("Invalid volume level.")

    def add_channel(self, channel_name):
        self._channels.append(channel_name)

    def delete_channel(self, channel_name):
        if channel_name in self._channels:
            self._channels.remove(channel_name)
        else:
            print("Channel not found.")

    def increase_volume(self):
        if self._volume < 10:
            self._volume += 1
        else:
            self._volume = 1

    def channel_name(self, channel_number):
        if 1 <= channel_number <= len(self._channels):
            return self._channels[channel_number - 1]
        else:
            return "Invalid channel number."

# Test the Television class
tv = Television(current_channel=0, current_channel_name="Channel 1", channels=["Channel 1", "Channel 2", "Channel 3"], volume=5)
print("Current Channel:", tv.get_current_channel())
print("Current Channel Name:", tv.get_current_channel_name())
print("Volume:", tv.get_volume())

tv.set_current_channel(1)
print("Current Channel:", tv.get_current_channel())
print("Current Channel Name:", tv.get_current_channel_name())

tv.set_volume(7)
print("Volume:", tv.get_volume())

tv.increase_volume()
print("Increased Volume:", tv.get_volume())

tv.add_channel("Channel 4")
print("Channels:", tv._channels)

tv.delete_channel("Channel 1")
print("Channels:", tv._channels)

print("Channel Name (#3):", tv.channel_name(3))

