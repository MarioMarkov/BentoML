"""
This type stub file was generated by pyright.
"""

from .base import Type
from .isobmff import IsoBmff

class Jpeg(Type):
    """
    Implements the JPEG image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Jpx(Type):
    """
    Implements the JPEG2000 image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Apng(Type):
    """
    Implements the APNG image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> bool:
        ...
    


class Png(Type):
    """
    Implements the PNG image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Gif(Type):
    """
    Implements the GIF image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Webp(Type):
    """
    Implements the WEBP image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Cr2(Type):
    """
    Implements the CR2 image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Tiff(Type):
    """
    Implements the TIFF image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> bool:
        ...
    


class Bmp(Type):
    """
    Implements the BMP image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Jxr(Type):
    """
    Implements the JXR image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Psd(Type):
    """
    Implements the PSD image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Ico(Type):
    """
    Implements the ICO image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Heic(IsoBmff):
    """
    Implements the HEIC image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> bool:
        ...
    


class Dcm(Type):
    MIME = ...
    EXTENSION = ...
    OFFSET = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> Literal[False]:
        ...
    


class Dwg(Type):
    """Implements the Dwg image type matcher."""
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf):
        ...
    


class Xcf(Type):
    """Implements the Xcf image type matcher."""
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf):
        ...
    


class Avif(IsoBmff):
    """
    Implements the AVIF image type matcher.
    """
    MIME = ...
    EXTENSION = ...
    def __init__(self) -> None:
        ...
    
    def match(self, buf): # -> bool:
        ...
    

