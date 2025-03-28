from actions.action import Action
from config import sides


class RotateUp(Action):
    def __init__(self, clockwise=True):
        super().__init__()
        self.clockwise = clockwise

    def ApplyRotation(self, Rcube):
        # Rotate the Up face (layer UP) using the provided rotate function.
        self.RotateFace(Rcube, sides["UP"], self.clockwise)

        # Save the affected stickers from the FRONT top row.
        temp = Rcube.state[sides["FRONT"], 0, :].copy()

        if self.clockwise:
            # For a clockwise U move:
            # FRONT top row becomes the RIGHT top row.
            Rcube.state[sides["FRONT"], 0, :] = Rcube.state[sides["RIGHT"], 0, :].copy()
            # RIGHT top row becomes the BACK top row.
            Rcube.state[sides["RIGHT"], 0, :] = Rcube.state[sides["BACK"], 0, :].copy()
            # BACK top row becomes the LEFT top row.
            Rcube.state[sides["BACK"], 0, :] = Rcube.state[sides["LEFT"], 0, :].copy()
            # LEFT top row becomes the saved FRONT top row.
            Rcube.state[sides["LEFT"], 0, :] = temp
        else:
            # For a counterclockwise U move:
            # FRONT top row gets the LEFT top row.
            Rcube.state[sides["FRONT"], 0, :] = Rcube.state[sides["LEFT"], 0, :].copy()
            # LEFT top row gets the BACK top row.
            Rcube.state[sides["LEFT"], 0, :] = Rcube.state[sides["BACK"], 0, :].copy()
            # BACK top row gets the RIGHT top row.
            Rcube.state[sides["BACK"], 0, :] = Rcube.state[sides["RIGHT"], 0, :].copy()
            # RIGHT top row gets the saved FRONT top row.
            Rcube.state[sides["RIGHT"], 0, :] = temp
        return Rcube
