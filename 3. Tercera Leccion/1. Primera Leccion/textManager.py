from os import path
from pathlib import Path
from io import TextIOWrapper
from wrappers import catchExceptions

class TextManager(object):
    """Class containing the needed methods for opening,
    closing and appending data to a file, given its path."""
    file:TextIOWrapper

    @catchExceptions
    def openFile(self, filePath:str) -> None:
        """Gets the absolute path of the txt file and opens it in append mode.
        If not existing, creates it.
        
        :param filePath: relative or absolute file directory to open."""
        filePath = path.abspath(Path(filePath))
        self.file = open(filePath, "a+")
        return True
    
    @catchExceptions
    def writeToFile(self, valueToWrite:int) -> None:
        """Tries to write certain value to the text file.
        
        :param valueToWrite: number that gets written down in the file.
        File needs to be open previously."""
        self.file.write(f"{valueToWrite}\n")
        return True
        
    @catchExceptions
    def closeFile(self) -> None:
        """Closes the file."""
        self.file.close()
        return True

    def getUsePath(self) -> str:
        """Gets the current user path."""
        return path.expanduser(r"~/automaticFile.txt")
        return True
    