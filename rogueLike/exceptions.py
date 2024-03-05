class Impossible(Exception):
    """An action that is impossible to perform."""

class QuitWithoutSaving(SystemExit):
    """An exception to raise when the player quits without saving."""   