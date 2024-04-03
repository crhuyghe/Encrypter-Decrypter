# Encrypter-Decrypter

This project is meant to take files of any type and encrypt them so that they may be securely stored or transferred.
It takes a file and a public key as inputs and can use them to either encrypt a file or decrypt one that was already
encrypted.


In order to encrypt a file for the current instance of the application:
1. Launch the Encrypter-Decrypter application in a supported version of Python
2. Press the “Open File” button on the left side of the application
3. In the file explorer window, select the file to be encrypted
4. Click the “Copy this instance’s public key” button
5. Paste the public key into the text field on the left side of the application
6. Press the encrypt button
7. Choose an output file path

In order to encrypt a file for a separate instance of the application:
1. Launch the target instance
2. Obtain the public key for this instance by pressing the “Copy this instance’s public key” button
3. Transfer the key onto the system to encrypt the file
4. Launch the instance intended to encrypt the file
5. Press the “Open File” button on the left side of the application
6. In the file explorer window, select the file to be encrypted
7. Input the public key of the other instance into the text field on the left side of the application
8. Press the encrypt button
9. Choose an output file path

In order to decrypt a file that was encrypted for the current instance of the application:
1. Launch the instance of the application that originally encrypted the file
2. Obtain the public key for this instance by pressing the “Copy this instance’s public key” button
3. If the file was encrypted by the current instance of the application, steps 3 and 4 can be skipped
4. Transfer the key onto the system to encrypt the file
5. Launch the instance intended to encrypt the file
6. Press the “Open File” button on the right side of the application
7. In the file explorer window, select the file to be decrypted
8. Input the public key of the instance that encrypted the file into the text field on the right side of the application
9. Press the decrypt button
10. Choose an output file path
