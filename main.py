import function as f
import tkinter as tk
import pdb

def encrypter(message, key):
    output_text.delete('1.0', tk.END)
    forward = 0
    backward = len(message) - 1

    for i in message:
        for j in key:
            val1, val2 = 0, 0
            bin_val = f.dec_to_bin_8bit(ord(i))

            if bin_val[0] == '1':
                val1 += 8
            if bin_val[1] == '1':
                val1 += 4
            if bin_val[2] == '1':
                val1 += 2
            if bin_val[3] == '1':
                val1 += 1

            if bin_val[4] == '1':
                val2 += 8
            if bin_val[5] == '1':
                val2 += 4
            if bin_val[6] == '1':
                val2 += 2
            if bin_val[7] == '1':
                val2 += 1

            i = chr(ord(j) ^ f.bin_to_dec(f.permutation(f.two_char_to_bin(f.substitution(val1), f.substitution(val2)))))

        if ord(i) < 33:
            k = ord(i) + 256
            i = chr(k)

        if 126 < ord(i) < 161:
            k = ord(i) + 162
            i = chr(k)

        message = message[:forward] + i + message[:backward]
        forward += 1
        backward -= 1

    label['text'] = 'Encrypted\nMessage'
    output_text.insert(1.0, message)

def decrypt(message, key):
    output_text.delete('1.0', tk.END)
    forward = 0
    backward = len(message) - 1

    for i in message:
        pos = len(key) - 1

        if 256 <= ord(i) <= 288:
            k = ord(i) - 256
            i = chr(k)

        if 289 <= ord(i) <= 322:
            k = ord(i) - 162
            i = chr(k)

        for j in key:
            binary = f.reverse_permutation(f.dec_to_bin_8bit(ord(i) ^ ord(key[pos])))
            i = chr(f.bin_to_dec(f.dec_to_bin_4bit(f.reverse_substitution(f.bin_to_dec_4bit(binary[0:4]))) +
                                 f.dec_to_bin_4bit(f.reverse_substitution(f.bin_to_dec_4bit(binary[4:8])))))
            pos -= 1
        message = message[:forward] + i + message[:backward]
        forward += 1
        backward -= 1

    label['text'] = 'Decrypted\nMessage'
    output_text.insert(1.0, message)

root = tk.Tk()
root.title('Encryption and Decryption Tool')

canvas = tk.Canvas(root, height=600, width=1000, bg='#FFDAB9') 
head_label = tk.Label(canvas, text='Encryption And Decryption', font=('verdana', 30), bg='#000000', fg='WHITE')  
message_label = tk.Label(canvas, text='Message:', font=('verdana', 20), bg='#FFDAB9', fg='#800000') 
key_label = tk.Label(canvas, text='Key:', font=('verdana', 20), bg='#FFDAB9', fg='#800000') 
output_label = tk.Label(canvas, text='Output ↓', font=('verdana', 25), bg='#FFDAB9', fg='blue')
label = tk.Label(canvas, text='Encrypted\nMessage:', font=('verdana', 20), bg='#FFDAB9', fg='#800000') 
message_entry = tk.Entry(canvas, width=40, font=('verdana', 20))
key_entry = tk.Entry(canvas, width=40, font=('verdana', 20))
output_text = tk.Text(canvas, height=1, width=40, borderwidth=1, font=('verdana', 20))
encrypt_button = tk.Button(canvas, text='Encrypt', font=('verdana', 20), command=lambda: encrypter(message_entry.get(), key_entry.get()))
decrypt_button = tk.Button(canvas, text='Decrypt', font=('verdana', 20), command=lambda: decrypt(message_entry.get(), key_entry.get()))

canvas.pack()
head_label.place(x=550, y=25, anchor='center')
message_label.place(x=40, y=70)
message_entry.place(x=200, y=70)
key_label.place(x=60, y=130)
key_entry.place(x=200, y=130)
output_label.place(x=520, y=200, anchor='center')
label.place(x=40, y=220)
output_text.place(x=200, y=240)
encrypt_button.place(x=380, y=320)
decrypt_button.place(x=550, y=320)

root.mainloop()