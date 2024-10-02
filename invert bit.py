def invert_bits(original_bit):
  invert_bit = ""
  for bit in original_bit:
    if bit == " ":
        invert_bit += " "
    elif bit == "1":
        invert_bit += "0"
    else:
        invert_bit += "1"
  return invert_bit

while True :
  original_bit = str(input("The bit : "))
  result = invert_bits(original_bit)
  print(result)