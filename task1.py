def res(t):
    rever = t[::-1]
    return rever

def reverse_words(text): 
    sl = {}
    reversed_text = ""
    for char in text:
        if char.isalpha():
            reversed_text += f'{res(char)} '
        else:
            slovo = char
            for i,num in enumerate(char):
                if not char[i].isalpha():
                    sl[i] = num
                    slovo = slovo.replace(sl[i], '')
                    
            slovo = res(slovo)
            
            for i in sl:
                slovo = slovo[:i] + sl[i] + slovo[i::]
            reversed_text += f'{slovo} '
            
    return reversed_text

if __name__ == '__main___':
    cases = [
        ("abcd efgh", "dcba hgfe"), 
        ("a1bcd efg!h, d1cba hgf!e"),
        ("", ""),
]
    for text, reversed_text in cases:
        assert reverse_words(text) == reversed_text