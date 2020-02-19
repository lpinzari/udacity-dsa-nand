
## Keypad Combinations

A keypad on a cellphone has alphabets for all numbers between 2 and 9. 

You can make different combinations of alphabets by pressing the numbers.

For example, if you press 23, the following combinations are possible:

`ad, ae, af, bd, be, bf, cd, ce, cf`

Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2.
Likewise, if the user types 32, the order would be

`da, db, dc, ea, eb, ec, fa, fb, fc`


Given an integer `num`, find out all the possible strings that can be made using digits of input `num`. 
Return these strings in a list. The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.


```python
def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    print('---- keypad({}) ---- START'.format(num))
    if num <= 1:
        print('Base case: [""]')
        print('---- keypad({}) ---- END'.format(num))
        return [""]
    elif 1 < num <= 9:
        print('Base case: {}'.format(get_characters(num)))
        print('---- keypad({}) ---- END'.format(num))
        return list(get_characters(num))

    last_digit = num % 10
    small_output = keypad(num//10)
    keypad_string = get_characters(last_digit)
    print('---- keypad({}) ---- CALL'.format(num))
    print('last_digit: {}'.format(last_digit))
    print('small_output: {}'.format(small_output))
    print('keypad_string: {}'.format(keypad_string))
    output = list()
    print('for loop: keypad_string')
    for character in keypad_string:
        print('  character: {}'.format(character))
        print('  for loop: small_output')
        for item in small_output:
            print('\t - item: {}'.format(item))
            new_item = item + character
            print('\t - new_item: {} + {} = {}'.format(item, character, new_item))
            output.append(new_item)
    
    print('output: {}'.format(output))
    print('---- keypad({}) ---- END'.format(num))
    return output

```


```python
def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")
```


```python
# Base case: list with empty string
input = 0
expected_output = [""]
test_keypad(input, expected_output)
```

    ---- keypad(0) ---- START
    Base case: [""]
    ---- keypad(0) ---- END
    Yay. We got it right.



```python
# Example case
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
test_keypad(input, expected_output)
```

    ---- keypad(23) ---- START
    ---- keypad(2) ---- START
    Base case: abc
    ---- keypad(2) ---- END
    ---- keypad(23) ---- CALL
    last_digit: 3
    small_output: ['a', 'b', 'c']
    keypad_string: def
    for loop: keypad_string
      character: d
      for loop: small_output
    	 - item: a
    	 - new_item: a + d = ad
    	 - item: b
    	 - new_item: b + d = bd
    	 - item: c
    	 - new_item: c + d = cd
      character: e
      for loop: small_output
    	 - item: a
    	 - new_item: a + e = ae
    	 - item: b
    	 - new_item: b + e = be
    	 - item: c
    	 - new_item: c + e = ce
      character: f
      for loop: small_output
    	 - item: a
    	 - new_item: a + f = af
    	 - item: b
    	 - new_item: b + f = bf
    	 - item: c
    	 - new_item: c + f = cf
    output: ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
    ---- keypad(23) ---- END
    Yay. We got it right.



```python
# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)
```

    ---- keypad(32) ---- START
    ---- keypad(3) ---- START
    Base case: def
    ---- keypad(3) ---- END
    ---- keypad(32) ---- CALL
    last_digit: 2
    small_output: ['d', 'e', 'f']
    keypad_string: abc
    for loop: keypad_string
      character: a
      for loop: small_output
    	 - item: d
    	 - new_item: d + a = da
    	 - item: e
    	 - new_item: e + a = ea
    	 - item: f
    	 - new_item: f + a = fa
      character: b
      for loop: small_output
    	 - item: d
    	 - new_item: d + b = db
    	 - item: e
    	 - new_item: e + b = eb
    	 - item: f
    	 - new_item: f + b = fb
      character: c
      for loop: small_output
    	 - item: d
    	 - new_item: d + c = dc
    	 - item: e
    	 - new_item: e + c = ec
    	 - item: f
    	 - new_item: f + c = fc
    output: ['da', 'ea', 'fa', 'db', 'eb', 'fb', 'dc', 'ec', 'fc']
    ---- keypad(32) ---- END
    Yay. We got it right.



```python
# Example case
input = 8
expected_output = sorted(["t", "u", "v"])
test_keypad(input, expected_output)
```

    ---- keypad(8) ---- START
    Base case: tuv
    ---- keypad(8) ---- END
    Yay. We got it right.



```python
input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)
```

    ---- keypad(354) ---- START
    ---- keypad(35) ---- START
    ---- keypad(3) ---- START
    Base case: def
    ---- keypad(3) ---- END
    ---- keypad(35) ---- CALL
    last_digit: 5
    small_output: ['d', 'e', 'f']
    keypad_string: jkl
    for loop: keypad_string
      character: j
      for loop: small_output
    	 - item: d
    	 - new_item: d + j = dj
    	 - item: e
    	 - new_item: e + j = ej
    	 - item: f
    	 - new_item: f + j = fj
      character: k
      for loop: small_output
    	 - item: d
    	 - new_item: d + k = dk
    	 - item: e
    	 - new_item: e + k = ek
    	 - item: f
    	 - new_item: f + k = fk
      character: l
      for loop: small_output
    	 - item: d
    	 - new_item: d + l = dl
    	 - item: e
    	 - new_item: e + l = el
    	 - item: f
    	 - new_item: f + l = fl
    output: ['dj', 'ej', 'fj', 'dk', 'ek', 'fk', 'dl', 'el', 'fl']
    ---- keypad(35) ---- END
    ---- keypad(354) ---- CALL
    last_digit: 4
    small_output: ['dj', 'ej', 'fj', 'dk', 'ek', 'fk', 'dl', 'el', 'fl']
    keypad_string: ghi
    for loop: keypad_string
      character: g
      for loop: small_output
    	 - item: dj
    	 - new_item: dj + g = djg
    	 - item: ej
    	 - new_item: ej + g = ejg
    	 - item: fj
    	 - new_item: fj + g = fjg
    	 - item: dk
    	 - new_item: dk + g = dkg
    	 - item: ek
    	 - new_item: ek + g = ekg
    	 - item: fk
    	 - new_item: fk + g = fkg
    	 - item: dl
    	 - new_item: dl + g = dlg
    	 - item: el
    	 - new_item: el + g = elg
    	 - item: fl
    	 - new_item: fl + g = flg
      character: h
      for loop: small_output
    	 - item: dj
    	 - new_item: dj + h = djh
    	 - item: ej
    	 - new_item: ej + h = ejh
    	 - item: fj
    	 - new_item: fj + h = fjh
    	 - item: dk
    	 - new_item: dk + h = dkh
    	 - item: ek
    	 - new_item: ek + h = ekh
    	 - item: fk
    	 - new_item: fk + h = fkh
    	 - item: dl
    	 - new_item: dl + h = dlh
    	 - item: el
    	 - new_item: el + h = elh
    	 - item: fl
    	 - new_item: fl + h = flh
      character: i
      for loop: small_output
    	 - item: dj
    	 - new_item: dj + i = dji
    	 - item: ej
    	 - new_item: ej + i = eji
    	 - item: fj
    	 - new_item: fj + i = fji
    	 - item: dk
    	 - new_item: dk + i = dki
    	 - item: ek
    	 - new_item: ek + i = eki
    	 - item: fk
    	 - new_item: fk + i = fki
    	 - item: dl
    	 - new_item: dl + i = dli
    	 - item: el
    	 - new_item: el + i = eli
    	 - item: fl
    	 - new_item: fl + i = fli
    output: ['djg', 'ejg', 'fjg', 'dkg', 'ekg', 'fkg', 'dlg', 'elg', 'flg', 'djh', 'ejh', 'fjh', 'dkh', 'ekh', 'fkh', 'dlh', 'elh', 'flh', 'dji', 'eji', 'fji', 'dki', 'eki', 'fki', 'dli', 'eli', 'fli']
    ---- keypad(354) ---- END
    Yay. We got it right.


<span class="graffiti-highlight graffiti-id_9ibtd5w-id_haj1ksk"><i></i><button>Hide Solution</button></span>


```python
def keypad(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))

    last_digit = num % 10
    small_output = keypad(num//10)
    keypad_string = get_characters(last_digit)
    output = list()
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    return output

```
