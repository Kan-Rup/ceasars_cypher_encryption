import string;
    
from encryption import EncoderDecorder;


class EncrDecr_interface:
    
    # this function is used to take input from the user : taking the key to be used for encryption or decryption
    #
    def getKeyInput(self):
        
        print("Please enter a key (number between 1 and 26 + R or L (e.g. 11R,94L,25R, 08R, or 05L...). enter '@' to cancel.");
        
        key = input();
        
        if( self.validateKey(key) ):
            
            print("key is valid!");
            return key;
        
        elif (key == '@'):
            return '@CANCEL';
        
        else:
        
            print("error!");    
            return "@ERR";
        
        
    # some checks are done to make sure that the key is in correct range and in right format
    #
    def validateKey(self,key):

        key_valid = False;

        if( len(key) == 3 ):
            
            shift = key[0:2];
            shift_dir = key[2];
            
            try:
            
                if( int(shift) in list( range(1,27) ) ):
                    
                    if(shift_dir == 'R' or shift_dir == 'r' or shift_dir == 'L' or shift_dir == 'l'):
                        
                        key_valid = True;
                    
            except ValueError:
                
                print("Error in key input");
                
                key_valid = False;
                
        
        return key_valid;



    # this function is used to take input from user : taking the text to be encrypted or decrypted (plaintext / cyphertext)
    #
    def getTextInput(self):
        
        charList = string.ascii_lowercase + string.digits;
        
        print("Please enter the text to be processed (lower case letters & numbers (no space or symbols)) Enter '@' to Cancel.");
        
        
        iptText = input();

        iptText = iptText.lower();
        
        inputValid = True;
        
        
        for c in iptText:
            
            cmatch = False;
            
            for cc in charList:
                
                if(c == cc): cmatch = True; break;
            
            if(cmatch): continue;
            else: inputValid = False; break;
        
        
        if(inputValid):         print("text input valid!");     return iptText;
        elif(iptText == '@'):   print("Cancelled!");            return '@CANCEL';
        else:                   print("text input error!");     return "@ERR";



    # presenting the user with the main options of the program
    #
    def mainMenu(self):

        print("");
        print("------------------------------------------------------------------------------------");
        print("+++ Ceasar's Cypher : English letters + numbers 0 - 9 +++");
        print("Please enter '1' to encrypt, '2' to decrypt, 'H' for help text, 'A' for about, 'Q' to quit program.");
        print("------------------------------------------------------------------------------------");
        print("");

        opt_1 = input();

        key = "00-Z";

        
        if(opt_1 == 'Q' or opt_1 == 'q'):
            
            # the user has chosen to exit program
        
            print("Exiting program... Good-Bye!");
            
        elif(opt_1 == '1'):
            
            # user has chosen to encrypt some text
                
            print("Encrypting..."); 
            
            key = self.getKeyInput();
            
            if(key != "@ERR"):

                if(key != '@CANCEL'):

                    shift_num = key[0:2];

                    shift_dir = key[2];

                    print("shift number : " + shift_num + ", shift direction : " + shift_dir);
                    
                    iptTxt = self.getTextInput();
                    
                    if(iptTxt != '@ERR'):
                        
                        if(iptTxt != '@CANCEL'):
                            print("Plain Text: "+iptTxt);
                            
                            #make an encryptor object
                            #
                            EncrDcdr = EncoderDecorder();
                            
                            #pass the plaintext and key to encryptor for encryption
                            #
                            cypTxt = EncrDcdr.process_text(1,iptTxt,shift_num,shift_dir);
                            
                            print("");
                            print("------------------------------------------------");
                            print("ENCODED: " + cypTxt);
                            print("------------------------------------------------");
                            print("");
                            
                        else:
                            print("Plaintext input cancelled.");
                        
                    else:
                        print("Error inputting plaintext!");
                        
                        
                        
                else:
                    print("Cancelled!");
                    
            else:
                print("Error in input!");
                    
            self.mainMenu();
            
            
        elif(opt_1 == '2'):

            # user has chosen to decrypt some text

            print("Decrypting..."); 
            
            key = self.getKeyInput();
            
            if(key != "@ERR"):
                
                if(key != '@CANCEL'):

                    shift_num = key[0:2];

                    shift_dir = key[2];

                    print("shift number : " + shift_num + ", shift direction : " + shift_dir);
                    
                    iptTxt = self.getTextInput();
                    
                    if(iptTxt != '@ERR'):
                        
                        if(iptTxt != '@CANCEL'):
                        
                            print("Plain text :"+iptTxt);
                            
                            # make an encryptor object
                            #
                            EncrDcdr = EncoderDecorder();
                            
                            # pass the key and cypher text to the encryptor, for decryption
                            #
                            cypTxt = EncrDcdr.process_text(0,iptTxt,shift_num,shift_dir);
                            
                            print("");
                            print("------------------------------------------------");
                            print("DECODED: " + cypTxt);
                            print("------------------------------------------------");
                            print("");
                            
                        else:
                            print("Cypher-text inputting cancelled.");
                        
                    else:
                        print("Error inputting cypher-text");
                        
                else:
                    print("Cancelled!");
                    
            else:
                print("Error in input!");
            
            self.mainMenu();
            
        elif(opt_1 == 'H' or opt_1 == 'h'):
            
            print("=== HELP TEXT ===");
            print("==============================================================================================");
            print("");
            print("This is a simple encryption and decryption program. It can turn a string of words and numbers");
            print("into a meaningless string of characters which no one an understand (encryption), and that garbled");
            print("set of characters can be turned back into a meaningful word and number string, if you also have the"); 
            print("key code that was used to make the garbled text (decryption).");
            print("");
            print("Sending encrypted messages between two people who have the secret of the key is a way of");
            print("communicating in secret; with messages that only the two end people will understand.");
            print("");
            print("This program uses a 'Ceasar's Cypher' method of encryption. You can find graphical image");
            print("representation of the cypher by searching on a search engine online."); 
            print("");
            print("");
            print("");
            print("E.g. Take the letter 'b'. If you encrypt that with the key '03r', you would get the letter 'e',"); 
            print("because you moved 3 shifts to the right."); 
            print("If you encrypt 'b' with the key '04l', you would get 'x'. Because you have moved 4 shifts in the");
            print("leftward direction."); 
            print("Notice here that the start of the alphabet is attached to the end of the alphabet. Also, once");
            print("you start going rightward past 'z', you then start moving rightward past 'a'. The letters are");
            print("arranged in a circle.");
            print("The numbers are also arranged in a circle. starting at 1, ending at 0. 0 connects back to 1.");
            print("");
            print("");
            print("");
            print("Main menu : first select whether you want to encrypt or decrypt. Enter 1 to start encypting a");
            print("string of words and numbers. Enter 2 to start decrypting.");
            print("");
            print("Then in the next prompt, enter the key. A key is a combination of two digits and the letter R/r or");
            print("the letter L/l."); 
            print("");
            print("R or r stands for 'Right' (moving the cypher circle in the right direction).");
            print("L or l stands for 'left' (moving the cypher circle in the left direction).");
            print("");
            print("There is a number between 01 and 26 before the letter; this is the shift number that will alter");
            print("the letters and numbers of plain-text.");
            print("");
            print("Examples of keys : 01r , 22r , 05l , 15l , 25r, 26l");
            print("");
            print("");
            print("");
            print("Note : when you are decrypting , don't enter the opposite direction key to what you used to"); 
            print("encrypt. If you used '15r' key to encrypt, enter that same '15r' key to decrypt also. The");
            print("program will sort out the opposite direction for decryption mechanic.");
            print("");
            print("After entering the key, you have to enter either the plain-text or cypher text , depending on ");
            print("whether you are encrypting or decrypting. Once you get the cypher text, you can get the plain text");
            print("again, by entering the key and cypher text in the decryption option.");
            print("");
            print("");
            print("");
            print("NOTE : using a shift of 26 gives you back the plain text you just typed in! This is because the");
            print("cypher circle has gone one exact full circle, coming back to where it was at the start.");
            print("");
            print("NOTE : using a shift of 10 or 20, the numbers you typed in the plain text will come out unencrypted!");
            print("This is because there are 10 digits, and a shift of 10 will have the digit circle returning to where");
            print("it was at the start!.");
            print("");
            print("CONCLUSION : don't use a key with shift 26, 20 or 10.");
            print("");
            print("==============================================================================================");
            print("");
            print("Note: This encryption can be easily cracked. This program is only made for educational and casual");
            print("situations");
            print("");
            print("- Help text printed above -");
            print("");
            
            self.mainMenu();
            
        elif(opt_1 == 'A' or opt_1 == 'a'):
            
            print("\nABOUT INFORMATION");
            print("=================");
            print("");
            print("+++ Ceasar's Cypher - (Simple encryption and decryption of a string of text and numbers) +++");
            print("[Version:1]--[Patch:1]--[Label:First release]--[dev:KR]--[Date:08/11/21]");
            print("");
            print("Copyright © (2021) Kanishka Rupasinghe");
            print("");
            print("This program comes with ABSOLUTELY NO WARRANTY");
            print("This software is licenced under GPLv3 or later version");
            print("Please read licence document for licencing details and rights relevant to you");
            print("Readme file also contains relevant information");
            print("\n\n");
            
            self.mainMenu();
            
        else:
            print("Error. Bad input. Please enter '1' , '2' , 'h' or 'a' .");

            self.mainMenu();




# An interface object is made and then its main menu function is called (which starts everything).

interface = EncrDecr_interface();
interface.mainMenu();
