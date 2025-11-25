class Solution:
    def generateTag(self, caption: str) -> str:
        newCaption = ""
        firstLetter = True
        veryFirstLetter = True
        newCaption += "#"
        index = 0
        while(index < len(caption) and len(newCaption) < 100):
            if(caption[index] == " "):
                firstLetter = True
            elif(firstLetter == True and veryFirstLetter == True):
                newCaption += caption[index].lower()
                veryFirstLetter = False
                firstLetter = False
            elif(firstLetter == True):
                newCaption += caption[index].upper()
                firstLetter = False
            else:
                newCaption += caption[index].lower()
            index += 1
        return newCaption
    # This is assuming that only spaces are used as the delimiters
    # The goal here is to change the string such that it starts with a #, then is camel case, then non english characters are removed, and up to 100 characters only
    # Of course the new caption starts with # before we loop
    # Note that we need a distinction between the first letter of the first word of the sentence (which should be lowercase) and the first letter of every subsequent word
    # The first condition statement is there to skip spaces (and also to know we are meeting another first letter)
    # The second condition statement is there for the very first letter of the whole sentence, it makes this lowercase to follow camel case
    # Once the second condition statement is met, very First Letter will be false and can never be triggered again
    # The third condition statement works in conjunction with the first, once we find a space, firstLetter will be made true again
    # So the third condition statement, once met (not anymore a space), we add that as an upper case, this is to comply with camel case
    # Otherwise, while moving forward after the first letter of subsequent words, we add them as a lower case