INSTRUCTIONS:

To start using Bilge, we need a text to be encrypted obviously.

First write whatever you want to be encrypted into the file "text.txt"

Then run the file "bilge.py" (our main module).

You will be greeted with a CLI menu.

From there the program will ask you for a seed and a key for both encryption and decryption.

Both seed and key have to be integers as for now. 
(I intend to change that in the future, at least for the seed.)

While the seed can be both positive and negative integers, the key HAS TO BE a positive integer. 
(Even though you enter a negative number, the program converts it to positive.)

The sizes of the numbers aren't a problem AS LONG AS YOU DON'T FORGET what you chose for your seed and key. 
(Obviously don't enter a hundred gazillion, as python has its limits.)

After you enter the seed and key you chose, the program will encrypt your text and write it back in the file "text.txt"

When you want to decrypt your text, simply put it back into the file "text.txt" and before running the file "bilge.py" don't forget to save the file "text.txt"
!!! (!!! Because the program also encrypts every space and \n in the file "text.txt", you must always use Ctrl+A before you copy/paste !!!) !!!

When decrypting, enter the seed and the key you had chosen for encrypting and the program will decrypt your text and write it back into the file "text.txt"

!!! ALWAYS CHECK THE SEED AND KEY YOU CHOSE BEFORE PROCEEDING, AS ANY TINY MISTAKE WILL BE CATASTROPHIC !!!
!!! AND AGAIN, DON'T FORGET THAT ANY space AND \n YOU HAVE ENTERED IS IMPORTANT !!!

Thank you for your interest!
