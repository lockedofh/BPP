from wrappers import catchExceptions

class InputManager(object):
    """Class containing all the methods and input checkings."""
    
    @catchExceptions
    def getInteger(self) -> int:
        """Asks input to user and later checks if
        the input is castable to int.
        If it is, returns the value already casted."""
        number = input("Number to enter: ")
        numberCasted = int(number)
        return numberCasted
            
    @catchExceptions
    def getConfirmation(self) -> bool:
        """Asks to the user `y` or `n`.
        If none is enterd by the user, takes it as `y` by default."""
        optionsMapping = {"y": True, "n": False}
        confirmation = input("").lower()
        confirmationMapped = optionsMapping.get(confirmation, True)
        return confirmationMapped
    
    @catchExceptions
    def getFilePath(self) -> str:
        """Asks a file path, being the file that will later be opened and where the
        values will be written down."""
        filePath = input("Path to the file: ")
        return filePath