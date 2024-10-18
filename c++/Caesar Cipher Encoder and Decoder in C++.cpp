#include <iostream>
#include <string>

using namespace std;

// Function to encrypt the text
string caesarCipherEncrypt(string text, int shift) {
    string result = "";
    for (int i = 0; i < text.length(); i++) {
        char ch = text[i];

        if (isalpha(ch)) {
            char base = islower(ch) ? 'a' : 'A';
            ch = (ch - base + shift) % 26 + base;
        }
        result += ch;
    }
    return result;
}

// Function to decrypt the text
string caesarCipherDecrypt(string text, int shift) {
    return caesarCipherEncrypt(text, 26 - shift);
}

int main() {
    string text;
    int shift;

    cout << "Enter text: ";
    getline(cin, text);

    cout << "Enter shift: ";
    cin >> shift;

    string encryptedText = caesarCipherEncrypt(text, shift);
    cout << "Encrypted Text: " << encryptedText << endl;

    string decryptedText = caesarCipherDecrypt(encryptedText, shift);
    cout << "Decrypted Text: " << decryptedText << endl;

    return 0;
}
