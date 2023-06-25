from outputManager import OutputManager
from inputManager import InputManager
from textManager import TextManager

class Controller(object):
    """Controller class which basically controls all the functionalities from the text menu.
    """
    outputController:OutputManager    
    
    def mainController(self) -> None:
        """Method that invokes all the needed controllers for running the program.
        """
        self.startOutputController()
        self.startInputController()
        self.startTextManagerController()
        self.mainMenuController()

    def mainMenuController(self) -> bool:
        """Loops for the main workflow."""
        try:
            userWantsToExit = False
            while not userWantsToExit:
                self.outputController.showBasicNumberRequest()
                numberEntered = self.inputController.getInteger()
                if numberEntered:
                    self.outputController.showConfirmationMessage(numberEntered)
                    confirmed = self.inputController.getConfirmation()
                    if confirmed:
                        written = self.textManager.writeToFile(numberEntered)
                        if written:
                            self.outputController.showOKResult()     
                            self.outputController.showExitMessage()                   
                            userWantsToExit = self.inputController.getConfirmation()
                else:
                    self.outputController.showErrorGettingNumber()
        except Exception as error:
            self.outputController.showUnexpectedErrorMessage(error)
        finally:
            self.textManager.closeFile()            
        
    def startOutputController(self) -> None:
        """Starts the outputController entity and 
        prompts the welcoming message in console.
        """
        self.outputController = OutputManager()
        self.outputController.showWelcome()
        
    def startInputController(self) -> None:
        """Initializes the inputController entity that
        is later called for controlling the user input."""
        self.inputController = InputManager()
    
    def startTextManagerController(self) -> None:
        """Initializes the textManager entity that is """
        textFileOpened = False
        while not textFileOpened:
            self.textManager = TextManager()
            self.outputController.showFilePathRequest()
            filePath = self.inputController.getFilePath()
            if not filePath:
                filePath = self.textManager.getUsePath()
                self.outputController.showConfirmationMessage(filePath)
                confirmed = self.inputController.getConfirmation()
                if confirmed:
                    fileOpened = self.textManager.openFile(filePath)
                    if fileOpened:
                        textFileOpened = True
                
            