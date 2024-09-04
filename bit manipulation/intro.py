# converting decimal to binary
# 1 using built-in bin() function
decimal = 5
binary = bin(decimal)  # 0b101
print(binary[2:])  # 101


# sing custum function
def decima_to_binary(n):

    binarynum = ""
    while n > 0:
        binarynum = str(n % 2) + binarynum
        n = n // 2
    return binarynum


print(decima_to_binary(5))


# converting binary to decimal
def binary_to_decimal(n):
    x = len(n)
    num = 0
    p2 = 1
    for i in range(x - 1, -1, -1):
        if n[i] == "1":
            num = num + p2 
        p2 = p2 * 2
    return num


print(binary_to_decimal("101"))

arr = [9, 9, 9]
print([1] + arr)
print([0] * 5)
print(pow(2, 3))


# counting set bits
def count_set_bits(n):
    binarynm = ""
    while n > 0:
        binarynm = str(n % 2) + binarynm
        n = n // 2
    count = binarynm.count("1")
    return count

def count_set_bitsusingbits(n):
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    return count

def count_set_bitsusingbits2nd_method(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count
print(count_set_bitsusingbits2nd_method(13))



# Minimum Bit Flips to Convert Number
def bitflips(start,goal):
    ans = start^goal
    bina = ''
    while ans>0:
        bina = str(ans%2) + bina
        ans = ans//2
    return bina.count('1')
        
print(bitflips(10,7))