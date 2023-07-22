class ChaeserCheffire:
    def __init__(self, msg, key):
        self.msg = msg
        self.key = key

    def getMSG(self):
        return self.msg

    def getKey(self):
        return self.key

    # The method checks if "letter" is a lowercase letter, an uppercase letter or a number
    # The encryption key "key" is applied to the letter (+ int(key)) 
    # to shift the letter by the desired number of positions.
    def charMoveEncypt(self, letter, key):
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) - ord('a') + int(key)) % 26 + ord('a')) # letter between 0 -> 25 lowercase
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) - ord('A') + int(key)) % 26 + ord('A')) # letter between 0 -> 25 uppercase
        elif '0' <= letter <= '9':
            letter = chr((ord(letter) - ord('0') + int(key)) % 10 + ord('0')) # letter between 0 -> 9 number
        return letter

    #@staticmethod
    def charMoveDencypt(self, letter, key):
        if 'a' <= letter <= 'z':
            letter = chr((ord(letter) - ord('a') - int(key)) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            letter = chr((ord(letter) - ord('A') - int(key)) % 26 + ord('A'))
        elif '0' <= letter <= '9':
            letter = chr((ord(letter) - ord('0') - int(key)) % 10 + ord('0'))
        return letter

    #@staticmethod
    def encryptMSG(self, text, key):
        encryptedString = ""
        txtLen = len(text)
        for i in range(txtLen):
            charOfText = text[i]
            encryptedString += self.charMoveEncypt(charOfText, key)
        return encryptedString

    #@staticmethod
    def dencryptMSG(self, text, key):
        dencryptedString = ""
        for i in range(len(text)):
            charOfText = text[i]
            dencryptedString += self.charMoveDencypt(charOfText, key)
        return dencryptedString