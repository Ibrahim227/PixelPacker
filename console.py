#!/usr/bin/python3
"""Import required libraries/modules"""
import cmd

from models.address import Address
from models.base_model import BaseModel
from models.compressedimages import CompressedImages
from models.compressionparameters import CompressionParameters
from models.images import Images
from models.user import User

classes = {
    "Address": Address, "Images": Images, "CompressionParameters": CompressionParameters,
    "User": User, "CompressedImages": CompressedImages, "BaseModel": BaseModel
}


class PIXELPACKERCommand(cmd.Cmd):
    """PixelPacker console"""
    prompt = "(pixelpacker)"

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """overwriting empty line method"""
        return False

    def do_quit(self):
        """Quit console"""
        return True


if __name__ == "__main__":
    PIXELPACKERCommand().cmdloop()
