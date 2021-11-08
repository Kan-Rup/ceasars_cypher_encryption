
import string;


class EncoderDecorder:

    # the lowercase letters from 'a' to 'z'
    #
    letters = string.ascii_lowercase;
    
    digits = ['0','1','2','3','4','5','6','7','8','9'];
    
    
    # find and return the list index of a given lowercase letter
    #
    def letterSearch(self,letter):
        
        letterPosition = 100;
        
        for i in range(len(self.letters)):
            
            if(self.letters[i] == letter):
                letterPosition = i;
                break;
            
        return letterPosition;
            
            
    # find and return the list index of a given digit
    #
    def digitSearch(self,digit):
        
        digitPosition = 100;
        
        for i in range(len(self.digits)):
            
            if(self.digits[i] == digit):
                digitPosition = i;
                break;
            
        return digitPosition;
    
    
    # either encrypt or decrypt a given string of text, using the given key,
    # and give back the result.
    #
    def process_text(self,encryptDecrypt,plainText,shift,shift_dir):
        
        # encryptDecrypt : whether to encrypt or decrypt.
        # plainText :   the text to process. Saying plaintext, but this could be either
        #               plaintext or cyphertext depending on what operation is requested.
        # shift : how many positions to turn the cypher circle
        # shift_dir : which direction to turn the cypher circle
        
        
        
        # get the lengths of the letter list and the digit list.
        # this is used later to find the max index number.
        #
        indexLetters = len(self.letters) - 1;
        indexDigits = len(self.digits) - 1;
        
        
        
        
        # this variable is modified until it indicates which direction to operate on the text
        #
        direction_multiply = 1;
        
        # this is explained below (in the for loop part)
        #
        if(shift_dir == 'R' or shift_dir == 'r'): direction_multiply = -1;
        elif(shift_dir == 'L' or shift_dir == 'l'): direction_multiply = 1;
        
        # encryption is given the normal direction
        # decryption is basically the same operation, but altering the characters in
        # the backward direction.
        # so, if indicated decryption, reverse the direction by multiplying by -1.
        #
        if(encryptDecrypt == 1): direction_multiply *= 1;
        elif(encryptDecrypt == 0): direction_multiply *= -1;
    
        
        
        
        
        # the processed result is collected into this variable
        # (cyphertext if encrypting / plaintext if decrypting)
        #
        cypherText = '';
        
        
        # go over each character of the given text to be processed
        #
        for char in plainText:
            
            isNumber = char.isdigit();
        
            
            if(isNumber):

                #how many steps to shift
                shiftsToGo = int(shift);
                
                #the index position of the character being altered
                position = self.digitSearch(str(char));
    
                #the list position arrow/indicator which is shifted one way or other
                idx = position;
    
                while(True):
                    
                    # do the below set of steps shift-number amount of times
                    
                    
                    # modify the position arrow rightward or leftward
                    #
                    # multiply 1 by direction digit, and subtract that (-1 or 1) from idx
                    # which will either increase idx position indicator by 1, or decrease it
                    # by 1
                    #
                    # because 'R' / right is -1, subtracting -1 from idx increases it by 1 
                    #(greater indexes are in rightward direction)
                    #
                    # and 'L' is 1, subtracting 1 from idx decreases it by 1
                    #(smaller indexes are in leftward direction)
                    #
                    shiftsToGo -= 1;
                    idx -= (1 * direction_multiply);
                    
                    
                    # idx being -1 means, the circle has been shifting in leftward direction and
                    # has gone past 0 to -1. So set the idx to 9, so it can continue going leftward from max 
                    # index (indexes are arranged in a circle in ceasars cypher)
                    #
                    # idx being (length of digit list + 1) means that it has gone rightward past the highest 
                    # index, so set the idx to 0 so that it can keep going rightward. 
                    # (again, the indexes are arranged in a circle).
                    #
                    if(idx == -1): idx = indexDigits;
                    elif(idx == indexDigits + 1): idx = 0;
                    
                    
                    # when shifts number has run out, it means its time to select the character from the
                    # digits list, from list index -(idx).
                    # 
                    # this picked altered character is placed in the cyphertext string.
                    # and it corresponds to the original character (char).
                    #
                    if(shiftsToGo == 0):
                        
                        cypherText += self.digits[idx]; 
                        
                        break;
                        
            else:
                
                # do the same as above, but use the characters list instead of digits list.
                # see if you can see what is being done, now that you've seen the section above.
                
                shiftsToGo = int(shift);
            
                position = self.letterSearch(char);
            
                idx = position;
                
                
                while(True):
                    
                    shiftsToGo -= 1;
                    idx -= (1 * direction_multiply);
                    
                    if(idx == -1): idx = indexLetters;
                    elif(idx == indexLetters + 1): idx = 0;
                    
                    if(shiftsToGo == 0):
                        
                        cypherText += self.letters[idx]; 
                        
                        break;
                     
        #give back the collected cyphertext (or plaintext) back to the calling function in the end.
        #
        return cypherText;
                    
                    
        

        
    
