def fake_bin(x):
    for idx, char in enumerate(x):
        if int(char) < 5:
            x[idx] = '0'
        else:
            x[idx] = '1'
    return x
x = "12345"
print(fake_bin(x))