def reverse_words(text : str)-> str: 
    reversed_text = ""
    for char in text.split():
        sl = {}
        if char.isalpha():
            reversed_text += f'{char[::-1]} '
        else:
            slovo = char
            for i,num in enumerate(char):
                if not char[i].isalpha():
                    sl[i] = num
                    slovo = slovo.replace(sl[i], '')       
            slovo = slovo[::-1]
            for i in sl:
                slovo = slovo[:i] + sl[i] + slovo[i::]
            reversed_text += f'{slovo} '
    return reversed_text.strip()
cases = [
    ("abcd efgh", "dcba hgfe"), 
    ("1","1"),
    ("a1bcd efg!h", "d1cba hgf!e"),
    ("q2wert qw 11qq", "t2rewq wq 11qq"),
    ("", ""),]
for text, reversed_text in cases:
    assert reverse_words(text) == reversed_text
  
