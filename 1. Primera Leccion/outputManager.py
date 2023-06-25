from wrappers import printOut

class OutputManager(object):
    """Class containing all the methods that will be called from the controller in order to have all the prompts in the same way
    and structure.
    """
    
    @printOut
    def showWelcome(self) -> str:
        """Prompts a welcoming message to the console menu."""
        message = "This is a console program. This will write to a certain text file the number you enter next.\n"\
                    "Take into consideration just integers are considerated as valid numbers.\n"\
                    "If anything apart from that is entered, the value won't be valid.\n"\
                    f"{'*' * 100}"
        return message

    @printOut
    def showConfirmationMessage(self, valueToConfirm:object=None) -> str:
        """Prints out a confirmation message and prints in it the value to confirm in case it is needed.
        
        :param valueToConfirm: data that user has input in the command line. Used for confirming it before writting it down."""
        if valueToConfirm:
            message = f"Are you sure {valueToConfirm} is the value to entry? [y/n]"
        else:
            message = "Are you sure to continue? [y/n]"
        return message
    
    @printOut
    def showExitMessage(self) -> str:
        """Confirms if user wants to exit."""
        message = "Do you want to exit? [y/n]"
        return message
    
    @printOut
    def showOKResult(self) -> str:
        """A confirmation message everything went as expected."""
        message = "Value entered in the text file."
        return message
    
    @printOut
    def showBasicNumberRequest(self) -> str:
        """A message prompts for entering another value."""
        message = "Enter a number to insert in the text file."
        return message
    
    @printOut
    def showFilePathRequest(self) -> str:
        """A message prompts for entering a path that will correspond to the
        text file to open."""
        message = "Enter the path to the .txt file.\n"\
                    "If not, an `automaticFile.txt` will be created in the user's directory.\n"\
                    "You can enter relative and absolutes paths."
        return message
    
    @printOut
    def showErrorGettingNumber(self) -> str:
        """In case the value entered by the user and catched in the prompt is not castable
        to integer, this method is invoked, which basically prompts to user the value entered was
        not an integer, as expected."""
        message = "The value entered could not be recognized as an integer."
        return message
            
    @printOut
    def showUnexpectedErrorMessage(self, error:Exception) -> str:
        """In case an unhandled error is raised, this message is printed out."""
        message = f"Unexpected error ({error}) raised.\nProgram will stop."