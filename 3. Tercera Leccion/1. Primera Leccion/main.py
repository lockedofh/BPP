from controller import Controller

class Main(object):
    """Main program which contains the mainProgram method, which 
    invokes the controller.
    """
    def mainProgram(self):
        """Main program."""
        controller = Controller()
        controller.mainController()
        
if __name__ == "__main__":
    mainController = Main()
    mainController.mainProgram()