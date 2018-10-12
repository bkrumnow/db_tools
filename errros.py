class Error(Exception):
   """Base class for other exceptions"""
   pass
   
class FilesNotFoundException(Error):
    """ Raised when no sql files are found
    """
    pass