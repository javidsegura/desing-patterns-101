
"""

Intent: simplifies the calling of several methods from the client. Provides reduced interface that may not use the full extend of the librariy functioanlity

"""

class TV():
      def __init__(self) -> None:
            pass
      def on(self):
            print(f"Turned on TV")
      def set_input(self, channel: str):
            print(f"Setting tv input to {channel}")
      def off(self):
            print(f"Turning off TV")

class AMP():
      def __init__(self) -> None:
            pass
      def on(self):
            print(f"Turned on AMP")
      def set_source(self, channel: str):
            print(f"Channel is: {channel}")
      def set_volume(self, level: int):
            print(f"Setting volume to: {level}")
      def off(self):
            print(f"Turning off AMP")

class Streamer():
      def __init__(self) -> None:
            pass
      def on(self):
            print(f"Turning on streamer")
      def play_movie(self, movie_name: str) -> None:
            print(f"Playing: {movie_name}")
      def off(self):
            print(f"Turning off streamer")

class HomeTheaterFacade():
      def __init__(self, tv: TV, amp: AMP, streamer: Streamer) -> None:
            self._tv = tv
            self._amp = amp
            self._streamer = streamer
      def watch_movie(self, movie_name: str):
            self._tv.on()
            self._amp.on()
            self._amp.set_source("HDMI1")
            self._amp.set_volume(15)
            self._tv.set_input("HDMI1")
            self._streamer.on()
            self._streamer.play_movie(movie_name)
      def end_movie(self):
            print("\nShutting down the home theater...")
            self._streamer.off()
            self._tv.off()
            self._amp.off()

if __name__ == "__main__":
      tv = TV()
      amp = AMP()
      streamer = Streamer()
      home_theater = HomeTheaterFacade(tv, amp, streamer)
      home_theater.watch_movie("Avatar")