# Sergio García, Nicolás Peña, Sebastian Rodríguez

class DES_clase():
    # Se crea la función XOR que recibe dos bits para compararlos y entregar su valor de verdad correspondiente al XOR:
    def XOR(bit1, bit2):
        if bit1==0 and bit2==0:
            return 0
        elif bit1==0 and bit2==1:
            return 1
        elif bit1==1 and bit2==0:
            return 1
        elif bit1==1 and bit2==1:
            return 0
    # Se crean todas las SBOX
    S1 = {}
    S1["000000"] = "1110" #14
    S1["000010"] = "0100" #4
    S1["000100"] = "1101" #13
    S1["000110"] = "0001" #1
    S1["001000"] = "0010" #2
    S1["001010"] = "1111" #15
    S1["001100"] = "1011" #11
    S1["001110"] = "1000" #8
    S1["010000"] = "0011" #3
    S1["010010"] = "1010" #10
    S1["010100"] = "0110" #6
    S1["010110"] = "1100" #12
    S1["011000"] = "0101" #5
    S1["011010"] = "1001" #9
    S1["011100"] = "0000" #0
    S1["011110"] = "0111" #7

    S1["000001"] = "0000" #0
    S1["000011"] = "1111" #15
    S1["000101"] = "0111"#7
    S1["000111"] = "0100"#4
    S1["001001"] = "1110"#14
    S1["001011"] = "0010"#2
    S1["001101"] = "1101"#13
    S1["001111"] = "0001"#1
    S1["010001"] = "1010"#10
    S1["010011"] = "0110"#6
    S1["010101"] = "1100"#12
    S1["010111"] = "1011"#11
    S1["011001"] = "1001"#9
    S1["011011"] = "0101"#5
    S1["011101"] = "0011"#3
    S1["011111"] = "1000"#8

    S1["100000"] = "0100"#4
    S1["100010"] = "0001"#1
    S1["100100"] = "1110"#14
    S1["100110"] = "1000"#8
    S1["101000"] = "1101"#13
    S1["101010"] = "0110"#6
    S1["101100"] = "0010"#2
    S1["101110"] = "1011"#11
    S1["110000"] = "1111"#15
    S1["110010"] = "1100"#12
    S1["110100"] = "1001"#9
    S1["110110"] = "0111"#7
    S1["111000"] = "0011"#3
    S1["111010"] = "1010"#10
    S1["111100"] = "0101"#5
    S1["111110"] = "0000"#0

    S1["100001"] = "1111"#15
    S1["100011"] = "1100"#12
    S1["100101"] = "1000"#8
    S1["100111"] = "0010"#2
    S1["101001"] = "0100"#4
    S1["101011"] = "1001"#9
    S1["101101"] = "0001"#1
    S1["101111"] = "0111"#7
    S1["110001"] = "0101"#5
    S1["110011"] = "1011"#11
    S1["110101"] = "0011"#3
    S1["110111"] = "1110"#14
    S1["111001"] = "1010"#10
    S1["111011"] = "0000"#0
    S1["111101"] = "0110"#6
    S1["111111"] = "1101"#13

    S2 = {}
    S2["000000"] = "1111"#15
    S2["000010"] = "0001"# 1
    S2["000100"] = "1000"#8
    S2["000110"] = "1110"#14
    S2["001000"] = "0110"#6
    S2["001010"] = "1011"#11
    S2["001100"] = "0011"#3
    S2["001110"] = "0100"#4
    S2["010000"] = "1001"#9
    S2["010010"] = "0111"#7
    S2["010100"] = "0010"#2
    S2["010110"] = "1101"#13
    S2["011000"] = "1100"#12
    S2["011010"] = "0000"#0
    S2["011100"] = "0101"#5
    S2["011110"] = "1010"#10

    S2["000001"] = "0011"#3
    S2["000011"] = "1101"#13
    S2["000101"] = "0100"#4
    S2["000111"] = "0111"#7
    S2["001001"] = "1111"#15
    S2["001011"] = "0010"#2
    S2["001101"] = "1000"#8
    S2["001111"] = "1110"#14
    S2["010001"] = "1100"#12
    S2["010011"] = "0000"#0
    S2["010101"] = "0001"#1
    S2["010111"] = "1010"#10
    S2["011001"] = "0110"#6
    S2["011011"] = "1001"#9
    S2["011101"] = "1011"#11
    S2["011111"] = "0101"#5

    S2["100000"] = "0000"#0
    S2["100010"] = "1110"#14
    S2["100100"] = "0111"#7
    S2["100110"] = "1011"#11
    S2["101000"] = "1010"#10
    S2["101010"] = "0100"#4
    S2["101100"] = "1101"#13
    S2["101110"] = "0001"#1
    S2["110000"] = "0101"#5
    S2["110010"] = "1000"#8
    S2["110100"] = "1100"#12
    S2["110110"] = "0110"#6
    S2["111000"] = "1001"#9
    S2["111010"] = "0011"#3
    S2["111100"] = "0010"#2
    S2["111110"] = "1111"#15

    S2["100001"] = "1101"#13
    S2["100011"] = "1000"#8
    S2["100101"] = "1010"#10
    S2["100111"] = "0001"#1
    S2["101001"] = "0011"#3
    S2["101011"] = "1111"#15
    S2["101101"] = "0100"#4
    S2["101111"] = "0010"#2
    S2["110001"] = "1011"#11
    S2["110011"] = "0110"#6
    S2["110101"] = "0111"#7
    S2["110111"] = "1100"#12
    S2["111001"] = "0000"#0
    S2["111011"] = "0101"#5
    S2["111101"] = "1110"#14
    S2["111111"] = "1001"#9

    S3 = {}
    S3["000000"] = "1010"#10
    S3["000010"] = "0000"#0
    S3["000100"] = "1001"#9
    S3["000110"] = "1110"#14
    S3["001000"] = "0110"#6
    S3["001010"] = "0011"#3
    S3["001100"] = "1111"#15
    S3["001110"] = "0101"#5
    S3["010000"] = "0001"#1
    S3["010010"] = "1101"#13
    S3["010100"] = "1100"#12
    S3["010110"] = "0111"#7
    S3["011000"] = "1011"#11
    S3["011010"] = "0100"#4
    S3["011100"] = "0010"#2
    S3["011110"] = "1000"#8

    S3["000001"] = "1101"#13
    S3["000011"] = "0111"#7
    S3["000101"] = "0000"#0
    S3["000111"] = "1001"#9
    S3["001001"] = "0011"#3
    S3["001011"] = "0100"#4
    S3["001101"] = "0110"#6
    S3["001111"] = "1010"#10
    S3["010001"] = "0010"#2
    S3["010011"] = "1000"#8
    S3["010101"] = "0101"#5
    S3["010111"] = "1110"#14
    S3["011001"] = "1100"#12
    S3["011011"] = "1011"#11
    S3["011101"] = "1111"#15
    S3["011111"] = "0001"#1

    S3["100000"] = "1101"#13
    S3["100010"] = "0110"#6
    S3["100100"] = "0100"#4
    S3["100110"] = "1001"#9
    S3["101000"] = "1000"#8
    S3["101010"] = "1111"#15
    S3["101100"] = "0011"#3
    S3["101110"] = "0000"#0
    S3["110000"] = "1011"#11
    S3["110010"] = "0001"#1
    S3["110100"] = "0010"#2
    S3["110110"] = "1100"#12
    S3["111000"] = "0101"#5
    S3["111010"] = "1010"#10
    S3["111100"] = "1110"#14
    S3["111110"] = "0111"#7

    S3["100001"] = "0001"#1
    S3["100011"] = "1010"#10
    S3["100101"] = "1101"#13
    S3["100111"] = "0000"#0
    S3["101001"] = "0110"#6
    S3["101011"] = "1001"#9
    S3["101101"] = "1000"#8
    S3["101111"] = "0111"#7
    S3["110001"] = "0100"#4
    S3["110011"] = "1111"#15
    S3["110101"] = "1110"#14
    S3["110111"] = "0011"#3
    S3["111001"] = "1011"#11
    S3["111011"] = "0101"#5
    S3["111101"] = "0010"#2
    S3["111111"] = "1100"#12


    S4 = {}
    S4["000000"] = "0111"#7
    S4["000010"] = "1101"#13
    S4["000100"] = "1110"#14
    S4["000110"] = "0011"#3
    S4["001000"] = "0000"#0
    S4["001010"] = "0110"#6
    S4["001100"] = "1001"#9
    S4["001110"] = "1010"#10
    S4["010000"] = "0001"#1
    S4["010010"] = "0010"#2
    S4["010100"] = "1000"#8
    S4["010110"] = "0101"#5
    S4["011000"] = "1011"#11
    S4["011010"] = "1100"#12
    S4["011100"] = "0100"#4
    S4["011110"] = "1111"#15

    S4["000001"] = "1101"#13
    S4["000011"] = "1000"#8
    S4["000101"] = "1011"#11
    S4["000111"] = "0101"#5
    S4["001001"] = "0110"#6
    S4["001011"] = "1111"#15
    S4["001101"] = "0000"#0
    S4["001111"] = "0011"#3
    S4["010001"] = "0100"#4
    S4["010011"] = "0111"#7
    S4["010101"] = "0010"#2
    S4["010111"] = "1100"#12
    S4["011001"] = "0001"#1
    S4["011011"] = "1010"#10
    S4["011101"] = "1110"#14
    S4["011111"] = "1001"#9

    S4["100000"] = "1010"#10
    S4["100010"] = "0110"#6
    S4["100100"] = "1001"#9
    S4["100110"] = "0000"#0
    S4["101000"] = "1100"#12
    S4["101010"] = "1011"#11
    S4["101100"] = "0111"#7
    S4["101110"] = "1101"#13
    S4["110000"] = "1111"#15
    S4["110010"] = "0001"#1
    S4["110100"] = "0011"#3
    S4["110110"] = "1110"#14
    S4["111000"] = "0101"#5
    S4["111010"] = "0010"#2
    S4["111100"] = "1000"#8
    S4["111110"] = "0100"#4

    S4["100001"] = "0011"#3
    S4["100011"] = "1111"#15
    S4["100101"] = "0000"#0
    S4["100111"] = "0110"#6
    S4["101001"] = "1010"#10
    S4["101011"] = "0001"#1
    S4["101101"] = "1101"#13
    S4["101111"] = "1000"#8
    S4["110001"] = "1001"#9
    S4["110011"] = "0100"#4
    S4["110101"] = "0101"#5
    S4["110111"] = "1011"#11
    S4["111001"] = "1100"#12
    S4["111011"] = "0111"#7
    S4["111101"] = "0010"#2
    S4["111111"] = "1110"#14

    S5 = {}
    S5["000000"] = "0010"#2
    S5["000010"] = "1100"#12
    S5["000100"] = "0100"#4
    S5["000110"] = "0001"#1
    S5["001000"] = "0111"#7
    S5["001010"] = "1010"#10
    S5["001100"] = "1011"#11
    S5["001110"] = "0110"#6
    S5["010000"] = "1000"#8
    S5["010010"] = "0101"#5
    S5["010100"] = "0011"#3
    S5["010110"] = "1111"#15
    S5["011000"] = "1101"#13
    S5["011010"] = "0000"#0
    S5["011100"] = "1110"#14
    S5["011110"] = "1001"#9

    S5["000001"] = "1110"#14
    S5["000011"] = "1011"#11
    S5["000101"] = "0010"#2
    S5["000111"] = "1100"#12
    S5["001001"] = "0100"#4
    S5["001011"] = "0111"#7
    S5["001101"] = "1101"#13
    S5["001111"] = "0001"#1
    S5["010001"] = "0101"#5
    S5["010011"] = "0000"#0
    S5["010101"] = "1111"#15
    S5["010111"] = "1010"#10
    S5["011001"] = "0011"#3
    S5["011011"] = "1001"#9
    S5["011101"] = "1000"#8
    S5["011111"] = "0110"#6

    S5["100000"] = "0100"#4
    S5["100010"] = "0010"#2
    S5["100100"] = "0001"#1
    S5["100110"] = "1011"#11
    S5["101000"] = "1010"#10
    S5["101010"] = "1101"#13
    S5["101100"] = "0111"#7
    S5["101110"] = "1000"#8
    S5["110000"] = "1111"#15
    S5["110010"] = "1001"#9
    S5["110100"] = "1100"#12
    S5["110110"] = "0101"#5
    S5["111000"] = "0110"#6
    S5["111010"] = "0011"#3
    S5["111100"] = "0000"#0
    S5["111110"] = "1110"#14

    S5["100001"] = "1011"#11
    S5["100011"] = "1000"#8
    S5["100101"] = "1100"#12
    S5["100111"] = "0111"#7
    S5["101001"] = "0001"#1
    S5["101011"] = "1110"#14
    S5["101101"] = "0010"#2
    S5["101111"] = "1101"#13
    S5["110001"] = "0110"#6
    S5["110011"] = "1111"#15
    S5["110101"] = "0000"#0
    S5["110111"] = "1001"#9
    S5["111001"] = "1010"#10
    S5["111011"] = "0100"#4
    S5["111101"] = "0101"#5
    S5["111111"] = "0011"#3

    S6 = {}
    S6["000000"] = "1100"#12
    S6["000010"] = "0001"#1
    S6["000100"] = "1010"#10
    S6["000110"] = "1111"#15
    S6["001000"] = "1001"#9
    S6["001010"] = "0010"#2
    S6["001100"] = "0110"#6
    S6["001110"] = "1000"#8
    S6["010000"] = "0000"#0
    S6["010010"] = "1101"#13
    S6["010100"] = "0011"#3
    S6["010110"] = "0100"#4
    S6["011000"] = "1110"#14
    S6["011010"] = "0111"#7
    S6["011100"] = "0101"#5
    S6["011110"] = "1011"#11

    S6["000001"] = "1010"#10
    S6["000011"] = "1111"#15
    S6["000101"] = "0100"#4
    S6["000111"] = "0010"#2
    S6["001001"] = "0111"#7
    S6["001011"] = "1100"#12
    S6["001101"] = "1001"#9
    S6["001111"] = "0101"#5
    S6["010001"] = "0110"#6
    S6["010011"] = "0001"#1
    S6["010101"] = "1101"#13
    S6["010111"] = "1110"#14
    S6["011001"] = "0000"#0
    S6["011011"] = "1011"#11
    S6["011101"] = "0011"#3
    S6["011111"] = "1000"#8

    S6["100000"] = "1001"#9
    S6["100010"] = "1110"#14
    S6["100100"] = "1111"#15
    S6["100110"] = "0101"#5
    S6["101000"] = "0010"#2
    S6["101010"] = "1000"#8
    S6["101100"] = "1100"#12
    S6["101110"] = "0011"#3
    S6["110000"] = "0111"#7
    S6["110010"] = "0000"#0
    S6["110100"] = "0100"#4
    S6["110110"] = "1010"#10
    S6["111000"] = "0001"#1
    S6["111010"] = "1101"#13
    S6["111100"] = "1011"#11
    S6["111110"] = "0110"#6

    S6["100001"] = "0100"#4
    S6["100011"] = "0011"#3
    S6["100101"] = "0010"#2
    S6["100111"] = "1100"#12
    S6["101001"] = "1001"#9
    S6["101011"] = "0101"#5
    S6["101101"] = "1111"#15
    S6["101111"] = "1010"#10
    S6["110001"] = "1011"#11
    S6["110011"] = "1110"#14
    S6["110101"] = "0001"#1
    S6["110111"] = "0111"#7
    S6["111001"] = "0110"#6
    S6["111011"] = "0000"#0
    S6["111101"] = "1000"#8
    S6["111111"] = "1101"#13

    S7 = {}
    S7["000000"] = "0100"#4
    S7["000010"] = "1011"#11
    S7["000100"] = "0010"#2
    S7["000110"] = "1110"#14
    S7["001000"] = "1111"#15
    S7["001010"] = "0000"#0
    S7["001100"] = "1000"#8
    S7["001110"] = "1101"#13
    S7["010000"] = "0011"#3
    S7["010010"] = "1100"#12
    S7["010100"] = "1001"#9
    S7["010110"] = "0111"#7
    S7["011000"] = "0101"#5
    S7["011010"] = "1010"#10
    S7["011100"] = "0110"#6
    S7["011110"] = "0001"#1

    S7["000001"] = "1101"#13
    S7["000011"] = "0000"#0
    S7["000101"] = "1011"#11
    S7["000111"] = "0111"#7
    S7["001001"] = "0100"#4
    S7["001011"] = "1001"#9
    S7["001101"] = "0001"#1
    S7["001111"] = "1010"#10
    S7["010001"] = "1110"#14
    S7["010011"] = "0011"#3
    S7["010101"] = "0101"#5
    S7["010111"] = "1100"#12
    S7["011001"] = "0010"#2
    S7["011011"] = "1111"#15
    S7["011101"] = "1000"#8
    S7["011111"] = "0110"#6

    S7["100000"] = "0001"#1
    S7["100010"] = "0100"#4
    S7["100100"] = "1011"#11
    S7["100110"] = "1101"#13
    S7["101000"] = "1100"#12
    S7["101010"] = "0011"#3
    S7["101100"] = "0111"#7
    S7["101110"] = "1110"#14
    S7["110000"] = "1010"#10
    S7["110010"] = "1111"#15
    S7["110100"] = "0110"#6
    S7["110110"] = "1000"#8
    S7["111000"] = "0000"#0
    S7["111010"] = "0101"#5
    S7["111100"] = "1001"#9
    S7["111110"] = "0010"#2

    S7["100001"] = "0110"#6
    S7["100011"] = "101"#13
    S7["100111"] = "1000"#8
    S7["101001"] = "0001"#1
    S7["101011"] = "0100"#4
    S7["101101"] = "1010"#10
    S7["101111"] = "0111"#7
    S7["110001"] = "1001"#9
    S7["110011"] = "0101"#5
    S7["110101"] = "0000"#0
    S7["110111"] = "1111"#15
    S7["111001"] = "1110"#14
    S7["111011"] = "0010"#2
    S7["111101"] = "0011"#3
    S7["111111"] = "1100"#12



    S8 = {}
    S8["000000"] = "1101"#13
    S8["000010"] = "0010"#2
    S8["000100"] = "1000"#8
    S8["000110"] = "0100"#4
    S8["001000"] = "0110"#6
    S8["001010"] = "1111"#15
    S8["001100"] = "1011"#11
    S8["001110"] = "0001"#1
    S8["010000"] = "1010"#10
    S8["010010"] = "1001"#9
    S8["010100"] = "0011"#3
    S8["010110"] = "1110"#14
    S8["011000"] = "0101"#5
    S8["011010"] = "0000"#0
    S8["011100"] = "1100"#12
    S8["011110"] = "0111"#7

    S8["000001"] = "0001"#1
    S8["000011"] = "1111"#15
    S8["000101"] = "1101"#13
    S8["000111"] = "1000"#8
    S8["001001"] = "1010"#10
    S8["001011"] = "0011"#3
    S8["001101"] = "0111"#7
    S8["001111"] = "0100"#4
    S8["010001"] = "1100"#12
    S8["010011"] = "0101"#5
    S8["010101"] = "0110"#6
    S8["010111"] = "1011"#11
    S8["011001"] = "0000"#0
    S8["011011"] = "1110"#14
    S8["011101"] = "1001"#9
    S8["011111"] = "0010"#2

    S8["100000"] = "0111"#7
    S8["100010"] = "1011"#11
    S8["100100"] = "0100"#4
    S8["100110"] = "0001"#1
    S8["101000"] = "1001"#9
    S8["101010"] = "1100"#12
    S8["101100"] = "1110"#14
    S8["101110"] = "0010"#2
    S8["110000"] = "0000"#0
    S8["110010"] = "0110"#6
    S8["110100"] = "1010"#10
    S8["110110"] = "1101"#13
    S8["111000"] = "1111"#15
    S8["111010"] = "0011"#3
    S8["111100"] = "0101"#5
    S8["111110"] = "1000"#8

    S8["100001"] = "0010"#2
    S8["100011"] = "0001"#1
    S8["100101"] = "1110"#14
    S8["100111"] = "0111"#7
    S8["101001"] = "0100"#4
    S8["101011"] = "1010"#10
    S8["101101"] = "1000"#8
    S8["101111"] = "1101"#13
    S8["110001"] = "1111"#15
    S8["110011"] = "1100"#12
    S8["110101"] = "1001"#9
    S8["110111"] = "0000"#0
    S8["111001"] = "0011"#3
    S8["111011"] = "0101"#5
    S8["111101"] = "0110"#6
    S8["111111"] = "1011"#11

    # Se crea la función de cifrado DES que recibe el texto claro y la llave.
    def DES (texto_claro, llave):

        # Primero se crean listas apartes donde se guardará el texto cifrado, la parte izquierda y derecha del texto claro y la llave.
        TCI = []
        L0 = []
        R0 = []
        key = []

        # Se recorre el texto claro y se separa en dos mitades iguales, guardándolas la lista correspondiente.
        for x in range(64):
            bit = int(texto_claro[x])
            if x<=31:
                L0.append(bit)
            if x>31:
                R0.append(bit)
            # Como la parte derecha del texto  claro pasa sin ser cifrada, se guarda directamente en la primera mitad del texto cifrado
            TCI.append(bit)

        # Se guarda la llave en su correspondiente lista
        for y in range(48):
            bit_key = int(llave[y])
            key.append(bit_key)

        # Se realiza la expansión con la parte derecha del texto claro y se guarda en una lista
        expan = []
        expan.append(R0[31])
        expan.append(R0[0])
        expan.append(R0[1])
        expan.append(R0[2])
        expan.append(R0[3])
        expan.append(R0[4])
        
        expan.append(R0[3])
        expan.append(R0[4])
        expan.append(R0[5])
        expan.append(R0[6])
        expan.append(R0[7])
        expan.append(R0[8])
        
        expan.append(R0[7])
        expan.append(R0[8])
        expan.append(R0[9])
        expan.append(R0[10])
        expan.append(R0[11])
        expan.append(R0[12])
        
        expan.append(R0[11])
        expan.append(R0[12])
        expan.append(R0[13])
        expan.append(R0[14])
        expan.append(R0[15])
        expan.append(R0[16])
        
        expan.append(R0[15])
        expan.append(R0[16])
        expan.append(R0[17])
        expan.append(R0[18])
        expan.append(R0[19])
        expan.append(R0[20])
        
        expan.append(R0[19])
        expan.append(R0[20])
        expan.append(R0[21])
        expan.append(R0[22])
        expan.append(R0[23])
        expan.append(R0[24])
        
        expan.append(R0[23])
        expan.append(R0[24])
        expan.append(R0[25])
        expan.append(R0[26])
        expan.append(R0[27])
        expan.append(R0[28])
        
        expan.append(R0[27])
        expan.append(R0[28])
        expan.append(R0[29])
        expan.append(R0[30])
        expan.append(R0[31])
        expan.append(R0[0])
        
        # Se utiliza la función XOR con la expansión de R0, que ahora es de 48 bits, con la llave y la cadena resultante se guarda en una lista
        expanXOR = []
        for j in range(48):
            expanXOR.append(DES_clase.XOR(expan[j], key[j]))
        # Se crean ocho listas distintas que simulan las entradas de las ocho sbox diferentes
        lista1=[]
        lista2=[]
        lista3=[]
        lista4=[]
        lista5=[]
        lista6=[]
        lista7=[]
        lista8=[]

        # Se agregan los bits del resultado de la función XOR entre la expansión de R0 y la llave en grupos de seis en sus correspondientes listas
        for j in range(6):
            lista1.append(expanXOR[j])
        for j in range(6):
            lista2.append(expanXOR[j+6])
        for j in range(6):
            lista3.append(expanXOR[j+12])
        for j in range(6):
            lista4.append(expanXOR[j+18])
        for j in range(6):
            lista5.append(expanXOR[j+24])
        for j in range(6):
            lista6.append(expanXOR[j+30])
        for j in range(6):
            lista7.append(expanXOR[j+36])
        for j in range(6):
            lista8.append(expanXOR[j+42])


        Mi_string1 = ""
        Mi_string2 = "" 
        Mi_string3 = "" 
        Mi_string4 = "" 
        Mi_string5 = "" 
        Mi_string6 = "" 
        Mi_string7 = "" 
        Mi_string8 = "" 

        # Se utiliza la conversión de las sbox previamente creadas y se guarda como una cadena de caracteres 
        for i in range(6):
            Mi_string1 += str(lista1[i])
        PS1=DES_clase.S1[Mi_string1]
        for i in range(6):
            Mi_string2 += str(lista2[i])
        PS2=DES_clase.S2[Mi_string2]
        for i in range(6):
            Mi_string3 += str(lista3[i])
        PS3=DES_clase.S3[Mi_string3]
        for i in range(6):
            Mi_string4 += str(lista4[i])
        PS4=DES_clase.S4[Mi_string4]
        for i in range(6):
            Mi_string5 += str(lista5[i])
        PS5=DES_clase.S5[Mi_string5]
        for i in range(6):
            Mi_string6 += str(lista6[i])
        PS6=DES_clase.S6[Mi_string6]
        for i in range(6):
            Mi_string7 += str(lista7[i])
        PS7=DES_clase.S7[Mi_string7]
        for i in range(6):
            Mi_string8 += str(lista8[i])
        PS8=DES_clase.S8[Mi_string8]

        # Se unen todas las partes de la reducción con las sbox en la variable endbox (la cual tiene 32 bits)
        endbox=PS1+PS2+PS3+PS4+PS5+PS6+PS7+PS8

        # Se crea la lista PP donde se guarda cada bit que se encuentra en la variable endbox
        PP=[]
        
        # Se crea la lista AP para realizar la permutación de la función f correspondiente a la red de Feistel
        AP=[]
        for x in range(32):
            PP.append(endbox[x])
        
        AP.append(PP[15])
        AP.append(PP[6])
        AP.append(PP[19])
        AP.append(PP[20])
        AP.append(PP[28])
        AP.append(PP[11])
        AP.append(PP[27])
        AP.append(PP[16])
        AP.append(PP[0])
        AP.append(PP[14])
        AP.append(PP[22])
        AP.append(PP[25])
        AP.append(PP[4])
        AP.append(PP[17])
        AP.append(PP[30])
        AP.append(PP[9])
        AP.append(PP[1])
        AP.append(PP[7])
        AP.append(PP[23])
        AP.append(PP[13])
        AP.append(PP[31])
        AP.append(PP[26])
        AP.append(PP[2])
        AP.append(PP[8])
        AP.append(PP[18])
        AP.append(PP[12])
        AP.append(PP[29])
        AP.append(PP[5])
        AP.append(PP[21])
        AP.append(PP[10])
        AP.append(PP[3])
        AP.append(PP[24])
        aiua = []
        xor2 = []

        # Se agregan los bits de la permutación como enteros en la lista xor2
        for i in range(32):
            xor2.append(int(AP[i]))

        # En la lista aiua se guarda el resultado de ejecutar la función XOR entre la parte izquierda del texto claro y la última permutación realizada
        for y in range(32):
            aiua.append(DES_clase.XOR(L0[y],xor2[y]))

        # Como en la lista TCI ya está la primera mitad del texto cifrado, se una la segunda mitad que corresponde al contenido de la lista aiua
        for x in aiua:
            TCI.append(int(x))

        # Se guarda el texto cifrado como una cadena de caracteres
        texto_cifrado = ""
        for bit in TCI:
            texto_cifrado+=str(bit)
        
        # Por último se retorna el texto cifrado
        return texto_cifrado

    # Se crea la función de descifrado
    def descifrar(texto_cifrado, llave):
        tex_decifrar = ""
        L1 = []
        R1 = []
        for x in range(64):
            bit = int(texto_cifrado[x])
            if x<=31:
                R1.append(bit)
            if x>31:
                L1.append(bit)
            
        for x in range(32):
            tex_decifrar += str(L1[x])
        for x in range(32):
            tex_decifrar += str(R1[x])
        
        
        TC=DES_clase.DES(tex_decifrar, llave)
        tex_decifrar1=""
        R2=[]
        L2=[]
        for x in range(64):
            bit = int(TC[x])
            if x<=31:
                R2.append(bit)
            if x>31:
                L2.append(bit)
            
        for x in range(32):
            tex_decifrar1 += str(L2[x])
        for x in range(32):
            tex_decifrar1 += str(R2[x])
        return tex_decifrar1  


    def main():
        print("Presione 'e' si desea encriptar y presione 'd' si desea desencriptar: ")
        info = input()

        if(info == 'e'):
            print("Ingrese la llave: ")
            llave = str(input())
            
            if(len(llave) != 48):
                print("ERROR!!")
                return

            print("Ingrese el texto claro: ")
            texto_claro = str(input())

            if(len(texto_claro) != 64):
                print("ERROR!!")
                return
            
            print(DES_clase.DES(texto_claro, llave))
            
        elif(info == 'd'):
            print("Ingrese la llave: ")
            llave = str(input())

            if(len(llave) != 48):
                print("ERROR!!")
                return  
            
            print("Ingrese el texto cifrado: ")
            texto_cifrado = str(input())
            
            if(len(texto_cifrado) != 64):
                print("ERROR!!")
                return
            
            print(DES_clase.descifrar(texto_cifrado, llave))

        return 0

def gen_llaves(llave):
  llave56 = ""

  #se dropean 8 bits
  llave56+=llave[56]
  llave56+=llave[48]
  llave56+=llave[40]
  llave56+=llave[32]
  llave56+=llave[24]
  llave56+=llave[16]
  llave56+=llave[8]
  llave56+=llave[0]
  llave56+=llave[57]
  llave56+=llave[49]
  llave56+=llave[41]
  llave56+=llave[33]
  llave56+=llave[25]
  llave56+=llave[17]
  llave56+=llave[9]
  llave56+=llave[1]
  llave56+=llave[58]
  llave56+=llave[50]
  llave56+=llave[42]
  llave56+=llave[34]
  llave56+=llave[26]
  llave56+=llave[18]
  llave56+=llave[10]
  llave56+=llave[2]
  llave56+=llave[59]
  llave56+=llave[51]
  llave56+=llave[43]
  llave56+=llave[35]
  llave56+=llave[62]
  llave56+=llave[54]
  llave56+=llave[46]
  llave56+=llave[38]
  llave56+=llave[30]
  llave56+=llave[22]
  llave56+=llave[14]
  llave56+=llave[6]
  llave56+=llave[61]
  llave56+=llave[53]
  llave56+=llave[45]
  llave56+=llave[37]
  llave56+=llave[29]
  llave56+=llave[21]
  llave56+=llave[13]
  llave56+=llave[5]
  llave56+=llave[60]
  llave56+=llave[52]
  llave56+=llave[44]
  llave56+=llave[36]
  llave56+=llave[28]
  llave56+=llave[20]
  llave56+=llave[12]
  llave56+=llave[4]
  llave56+=llave[27]
  llave56+=llave[19]
  llave56+=llave[11]
  llave56+=llave[3]

  
  #sub_llave 1
  sub_llave_1 = []
  for x in range(56):
    if x==55:
      sub_llave_1.append(llave56[0])
    else:
      sub_llave_1.append(llave56[x+1])


  #sub_llave 2
  sub_llave_2 = []
  for x in range(56):
    if x==55:
      sub_llave_1.append(sub_llave_1[0])
    else:
      sub_llave_1.append(sub_llave_1[x+1])

  #sub_llave 3
  sub_llave_3 = []
  for x in range(56):
    if x==55:
      sub_llave_3.append(sub_llave_2[1])
    elif x==54:
      sub_llave_3.append(sub_llave_2[0])
    else:
      sub_llave_3.append(sub_llave_2[x+2])

  #sub_llave 4
  sub_llave_4 = []
  for x in range(56):
    if x==55:
      sub_llave_4.append(sub_llave_3[1])
    elif x==54:
      sub_llave_4.append(sub_llave_3[0])
    else:
      sub_llave_4.append(sub_llave_3[x+2])

  #sub_llave 5
  sub_llave_5 = []
  for x in range(56):
    if x==55:
      sub_llave_5.append(sub_llave_4[1])
    elif x==54:
      sub_llave_5.append(sub_llave_4[0])
    else:
      sub_llave_5.append(sub_llave_4[x+2])


  #sub_llave 6
  sub_llave_6 = []
  for x in range(56):
    if x==55:
      sub_llave_6.append(sub_llave_5[1])
    elif x==54:
      sub_llave_6.append(sub_llave_5[0])
    else:
      sub_llave_6.append(sub_llave_5[x+2])


  #sub_llave 7
  sub_llave_7 = []
  for x in range(56):
    if x==55:
      sub_llave_7.append(sub_llave_6[1])
    elif x==54:
      sub_llave_7.append(sub_llave_6[0])
    else:
      sub_llave_7.append(sub_llave_6[x+2])


  #sub_llave 8
  sub_llave_8 = []
  for x in range(56):
    if x==55:
      sub_llave_8.append(sub_llave_7[1])
    elif x==54:
      sub_llave_8.append(sub_llave_7[0])
    else:
      sub_llave_8.append(sub_llave_7[x+2])

  #sub_llave 9
  sub_llave_9 = []
  for x in range(56):
    if x==55:
      sub_llave_9.append(sub_llave_8[0])
    else:
      sub_llave_9.append(sub_llave_8[x+1])

  #sub_llave 10
  sub_llave_10 = []
  for x in range(56):
    if x==55:
      sub_llave_10.append(sub_llave_9[1])
    elif x==54:
      sub_llave_10.append(sub_llave_9[0])
    else:
      sub_llave_10.append(sub_llave_9[x+2])


  #sub_llave 11
  sub_llave_11 = []
  for x in range(56):
    if x==55:
      sub_llave_11.append(sub_llave_10[1])
    elif x==54:
      sub_llave_11.append(sub_llave_10[0])
    else:
      sub_llave_11.append(sub_llave_10[x+2])


  #sub_llave 12
  sub_llave_12 = []
  for x in range(56):
    if x==55:
      sub_llave_12.append(sub_llave_11[1])
    elif x==54:
      sub_llave_12.append(sub_llave_11[0])
    else:
      sub_llave_12.append(sub_llave_11[x+2])


  #sub_llave 13
  sub_llave_13 = []
  for x in range(56):
    if x==55:
      sub_llave_13.append(sub_llave_12[1])
    elif x==54:
      sub_llave_13.append(sub_llave_12[0])
    else:
      sub_llave_13.append(sub_llave_12[x+2])


  #sub_llave 14
  sub_llave_14 = []
  for x in range(56):
    if x==55:
      sub_llave_14.append(sub_llave_13[1])
    elif x==54:
      sub_llave_14.append(sub_llave_13[0])
    else:
      sub_llave_14.append(sub_llave_13[x+2])

  #sub_llave 15
  sub_llave_15 = []
  for x in range(56):
    if x==55:
      sub_llave_15.append(sub_llave_14[1])
    elif x==54:
      sub_llave_15.append(sub_llave_14[0])
    else:
      sub_llave_15.append(sub_llave_14[x+2])

  #sub_llave 16
  sub_llave_16 = []
  for x in range(56):
    if x==55:
      sub_llave_16.append(sub_llave_15[0])
    else:
      sub_llave_16.append(sub_llave_15[x+1])



  #se comprimen las sub_llaves de 56 bits en sub_llaves de 48 bits
      
  #llave 1
  llave_1=""
  llave_1+=sub_llave_1[13]
  llave_1+=sub_llave_1[16]
  llave_1+=sub_llave_1[10]
  llave_1+=sub_llave_1[23]
  llave_1+=sub_llave_1[0]
  llave_1+=sub_llave_1[4]
  llave_1+=sub_llave_1[2]
  llave_1+=sub_llave_1[27]
  llave_1+=sub_llave_1[14]
  llave_1+=sub_llave_1[5]
  llave_1+=sub_llave_1[20]
  llave_1+=sub_llave_1[9]
  llave_1+=sub_llave_1[22]
  llave_1+=sub_llave_1[18]
  llave_1+=sub_llave_1[11]
  llave_1+=sub_llave_1[3]
  llave_1+=sub_llave_1[25]
  llave_1+=sub_llave_1[7]
  llave_1+=sub_llave_1[15]
  llave_1+=sub_llave_1[6]
  llave_1+=sub_llave_1[26]
  llave_1+=sub_llave_1[19]
  llave_1+=sub_llave_1[12]
  llave_1+=sub_llave_1[1]
  llave_1+=sub_llave_1[40]
  llave_1+=sub_llave_1[51]
  llave_1+=sub_llave_1[30]
  llave_1+=sub_llave_1[36]
  llave_1+=sub_llave_1[46]
  llave_1+=sub_llave_1[54]
  llave_1+=sub_llave_1[29]
  llave_1+=sub_llave_1[39]
  llave_1+=sub_llave_1[50]
  llave_1+=sub_llave_1[44]
  llave_1+=sub_llave_1[32]
  llave_1+=sub_llave_1[47]
  llave_1+=sub_llave_1[43]
  llave_1+=sub_llave_1[48]
  llave_1+=sub_llave_1[38]
  llave_1+=sub_llave_1[55]
  llave_1+=sub_llave_1[33]
  llave_1+=sub_llave_1[52]
  llave_1+=sub_llave_1[45]
  llave_1+=sub_llave_1[41]
  llave_1+=sub_llave_1[49]
  llave_1+=sub_llave_1[35]
  llave_1+=sub_llave_1[28]
  llave_1+=sub_llave_1[31]
  sub_llaves.append(llave_1)

  #llave 2
  llave_2=""
  llave_2+=sub_llave_2[13]
  llave_2+=sub_llave_2[16]
  llave_2+=sub_llave_2[10]
  llave_2+=sub_llave_2[23]
  llave_2+=sub_llave_2[0]
  llave_2+=sub_llave_2[4]
  llave_2+=sub_llave_2[2]
  llave_2+=sub_llave_2[27]
  llave_2+=sub_llave_2[14]
  llave_2+=sub_llave_2[5]
  llave_2+=sub_llave_2[20]
  llave_2+=sub_llave_2[9]
  llave_2+=sub_llave_2[22]
  llave_2+=sub_llave_2[18]
  llave_2+=sub_llave_2[11]
  llave_2+=sub_llave_2[3]
  llave_2+=sub_llave_2[25]
  llave_2+=sub_llave_2[7]
  llave_2+=sub_llave_2[15]
  llave_2+=sub_llave_2[6]
  llave_2+=sub_llave_2[26]
  llave_2+=sub_llave_2[19]
  llave_2+=sub_llave_2[12]
  llave_2+=sub_llave_2[1]
  llave_2+=sub_llave_2[40]
  llave_2+=sub_llave_2[51]
  llave_2+=sub_llave_2[30]
  llave_2+=sub_llave_2[36]
  llave_2+=sub_llave_2[46]
  llave_2+=sub_llave_2[54]
  llave_2+=sub_llave_2[29]
  llave_2+=sub_llave_2[39]
  llave_2+=sub_llave_2[50]
  llave_2+=sub_llave_2[44]
  llave_2+=sub_llave_2[32]
  llave_2+=sub_llave_2[47]
  llave_2+=sub_llave_2[43]
  llave_2+=sub_llave_2[48]
  llave_2+=sub_llave_2[38]
  llave_2+=sub_llave_2[55]
  llave_2+=sub_llave_2[33]
  llave_2+=sub_llave_2[52]
  llave_2+=sub_llave_2[45]
  llave_2+=sub_llave_2[41]
  llave_2+=sub_llave_2[49]
  llave_2+=sub_llave_2[35]
  llave_2+=sub_llave_2[28]
  llave_2+=sub_llave_2[31]
  sub_llaves.append(llave_2)


  #llave 3
  llave_3=""
  llave_3+=sub_llave_3[13]
  llave_3+=sub_llave_3[16]
  llave_3+=sub_llave_3[10]
  llave_3+=sub_llave_3[23]
  llave_3+=sub_llave_3[0]
  llave_3+=sub_llave_3[4]
  llave_3+=sub_llave_3[2]
  llave_3+=sub_llave_3[27]
  llave_3+=sub_llave_3[14]
  llave_3+=sub_llave_3[5]
  llave_3+=sub_llave_3[20]
  llave_3+=sub_llave_3[9]
  llave_3+=sub_llave_3[22]
  llave_3+=sub_llave_3[18]
  llave_3+=sub_llave_3[11]
  llave_3+=sub_llave_3[3]
  llave_3+=sub_llave_3[25]
  llave_3+=sub_llave_3[7]
  llave_3+=sub_llave_3[15]
  llave_3+=sub_llave_3[6]
  llave_3+=sub_llave_3[26]
  llave_3+=sub_llave_3[19]
  llave_3+=sub_llave_3[12]
  llave_3+=sub_llave_3[1]
  llave_3+=sub_llave_3[40]
  llave_3+=sub_llave_3[51]
  llave_3+=sub_llave_3[30]
  llave_3+=sub_llave_3[36]
  llave_3+=sub_llave_3[46]
  llave_3+=sub_llave_3[54]
  llave_3+=sub_llave_3[29]
  llave_3+=sub_llave_3[39]
  llave_3+=sub_llave_3[50]
  llave_3+=sub_llave_3[44]
  llave_3+=sub_llave_3[32]
  llave_3+=sub_llave_3[47]
  llave_3+=sub_llave_3[43]
  llave_3+=sub_llave_3[48]
  llave_3+=sub_llave_3[38]
  llave_3+=sub_llave_3[55]
  llave_3+=sub_llave_3[33]
  llave_3+=sub_llave_3[52]
  llave_3+=sub_llave_3[45]
  llave_3+=sub_llave_3[41]
  llave_3+=sub_llave_3[49]
  llave_3+=sub_llave_3[35]
  llave_3+=sub_llave_3[28]
  llave_3+=sub_llave_3[31]
  sub_llaves.append(llave_3)

  #llave 4
  llave_4=""
  llave_4+=sub_llave_4[13]
  llave_4+=sub_llave_4[16]
  llave_4+=sub_llave_4[10]
  llave_4+=sub_llave_4[23]
  llave_4+=sub_llave_4[0]
  llave_4+=sub_llave_4[4]
  llave_4+=sub_llave_4[2]
  llave_4+=sub_llave_4[27]
  llave_4+=sub_llave_4[14]
  llave_4+=sub_llave_4[5]
  llave_4+=sub_llave_4[20]
  llave_4+=sub_llave_4[9]
  llave_4+=sub_llave_4[22]
  llave_4+=sub_llave_4[18]
  llave_4+=sub_llave_4[11]
  llave_4+=sub_llave_4[3]
  llave_4+=sub_llave_4[25]
  llave_4+=sub_llave_4[7]
  llave_4+=sub_llave_4[15]
  llave_4+=sub_llave_4[6]
  llave_4+=sub_llave_4[26]
  llave_4+=sub_llave_4[19]
  llave_4+=sub_llave_4[12]
  llave_4+=sub_llave_4[1]
  llave_4+=sub_llave_4[40]
  llave_4+=sub_llave_4[51]
  llave_4+=sub_llave_4[30]
  llave_4+=sub_llave_4[36]
  llave_4+=sub_llave_4[46]
  llave_4+=sub_llave_4[54]
  llave_4+=sub_llave_4[29]
  llave_4+=sub_llave_4[39]
  llave_4+=sub_llave_4[50]
  llave_4+=sub_llave_4[44]
  llave_4+=sub_llave_4[32]
  llave_4+=sub_llave_4[47]
  llave_4+=sub_llave_4[43]
  llave_4+=sub_llave_4[48]
  llave_4+=sub_llave_4[38]
  llave_4+=sub_llave_4[55]
  llave_4+=sub_llave_4[33]
  llave_4+=sub_llave_4[52]
  llave_4+=sub_llave_4[45]
  llave_4+=sub_llave_4[41]
  llave_4+=sub_llave_4[49]
  llave_4+=sub_llave_4[35]
  llave_4+=sub_llave_4[28]
  llave_4+=sub_llave_4[31]
  sub_llaves.append(llave_4)

  #llave 5
  llave_5=""
  llave_5+=sub_llave_5[13]
  llave_5+=sub_llave_5[16]
  llave_5+=sub_llave_5[10]
  llave_5+=sub_llave_5[23]
  llave_5+=sub_llave_5[0]
  llave_5+=sub_llave_5[4]
  llave_5+=sub_llave_5[2]
  llave_5+=sub_llave_5[27]
  llave_5+=sub_llave_5[14]
  llave_5+=sub_llave_5[5]
  llave_5+=sub_llave_5[20]
  llave_5+=sub_llave_5[9]
  llave_5+=sub_llave_5[22]
  llave_5+=sub_llave_5[18]
  llave_5+=sub_llave_5[11]
  llave_5+=sub_llave_5[3]
  llave_5+=sub_llave_5[25]
  llave_5+=sub_llave_5[7]
  llave_5+=sub_llave_5[15]
  llave_5+=sub_llave_5[6]
  llave_5+=sub_llave_5[26]
  llave_5+=sub_llave_5[19]
  llave_5+=sub_llave_5[12]
  llave_5+=sub_llave_5[1]
  llave_5+=sub_llave_5[40]
  llave_5+=sub_llave_5[51]
  llave_5+=sub_llave_5[30]
  llave_5+=sub_llave_5[36]
  llave_5+=sub_llave_5[46]
  llave_5+=sub_llave_5[54]
  llave_5+=sub_llave_5[29]
  llave_5+=sub_llave_5[39]
  llave_5+=sub_llave_5[50]
  llave_5+=sub_llave_5[44]
  llave_5+=sub_llave_5[32]
  llave_5+=sub_llave_5[47]
  llave_5+=sub_llave_5[43]
  llave_5+=sub_llave_5[48]
  llave_5+=sub_llave_5[38]
  llave_5+=sub_llave_5[55]
  llave_5+=sub_llave_5[33]
  llave_5+=sub_llave_5[52]
  llave_5+=sub_llave_5[45]
  llave_5+=sub_llave_5[41]
  llave_5+=sub_llave_5[49]
  llave_5+=sub_llave_5[35]
  llave_5+=sub_llave_5[28]
  llave_5+=sub_llave_5[31]
  sub_llaves.append(llave_5)

  #llave 6
  llave_6=""
  llave_6+=sub_llave_6[13]
  llave_6+=sub_llave_6[16]
  llave_6+=sub_llave_6[10]
  llave_6+=sub_llave_6[23]
  llave_6+=sub_llave_6[0]
  llave_6+=sub_llave_6[4]
  llave_6+=sub_llave_6[2]
  llave_6+=sub_llave_6[27]
  llave_6+=sub_llave_6[14]
  llave_6+=sub_llave_6[5]
  llave_6+=sub_llave_6[20]
  llave_6+=sub_llave_6[9]
  llave_6+=sub_llave_6[22]
  llave_6+=sub_llave_6[18]
  llave_6+=sub_llave_6[11]
  llave_6+=sub_llave_6[3]
  llave_6+=sub_llave_6[25]
  llave_6+=sub_llave_6[7]
  llave_6+=sub_llave_6[15]
  llave_6+=sub_llave_6[6]
  llave_6+=sub_llave_6[26]
  llave_6+=sub_llave_6[19]
  llave_6+=sub_llave_6[12]
  llave_6+=sub_llave_6[1]
  llave_6+=sub_llave_6[40]
  llave_6+=sub_llave_6[51]
  llave_6+=sub_llave_6[30]
  llave_6+=sub_llave_6[36]
  llave_6+=sub_llave_6[46]
  llave_6+=sub_llave_6[54]
  llave_6+=sub_llave_6[29]
  llave_6+=sub_llave_6[39]
  llave_6+=sub_llave_6[50]
  llave_6+=sub_llave_6[44]
  llave_6+=sub_llave_6[32]
  llave_6+=sub_llave_6[47]
  llave_6+=sub_llave_6[43]
  llave_6+=sub_llave_6[48]
  llave_6+=sub_llave_6[38]
  llave_6+=sub_llave_6[55]
  llave_6+=sub_llave_6[33]
  llave_6+=sub_llave_6[52]
  llave_6+=sub_llave_6[45]
  llave_6+=sub_llave_6[41]
  llave_6+=sub_llave_6[49]
  llave_6+=sub_llave_6[35]
  llave_6+=sub_llave_6[28]
  llave_6+=sub_llave_6[31]
  sub_llaves.append(llave_6)


  #llave 7
  llave_7=""
  llave_7+=sub_llave_7[13]
  llave_7+=sub_llave_7[16]
  llave_7+=sub_llave_7[10]
  llave_7+=sub_llave_7[23]
  llave_7+=sub_llave_7[0]
  llave_7+=sub_llave_7[4]
  llave_7+=sub_llave_7[2]
  llave_7+=sub_llave_7[27]
  llave_7+=sub_llave_7[14]
  llave_7+=sub_llave_7[5]
  llave_7+=sub_llave_7[20]
  llave_7+=sub_llave_7[9]
  llave_7+=sub_llave_7[22]
  llave_7+=sub_llave_7[18]
  llave_7+=sub_llave_7[11]
  llave_7+=sub_llave_7[3]
  llave_7+=sub_llave_7[25]
  llave_7+=sub_llave_7[7]
  llave_7+=sub_llave_7[15]
  llave_7+=sub_llave_7[6]
  llave_7+=sub_llave_7[26]
  llave_7+=sub_llave_7[19]
  llave_7+=sub_llave_7[12]
  llave_7+=sub_llave_7[1]
  llave_7+=sub_llave_7[40]
  llave_7+=sub_llave_7[51]
  llave_7+=sub_llave_7[30]
  llave_7+=sub_llave_7[36]
  llave_7+=sub_llave_7[46]
  llave_7+=sub_llave_7[54]
  llave_7+=sub_llave_7[29]
  llave_7+=sub_llave_7[39]
  llave_7+=sub_llave_7[50]
  llave_7+=sub_llave_7[44]
  llave_7+=sub_llave_7[32]
  llave_7+=sub_llave_7[47]
  llave_7+=sub_llave_7[43]
  llave_7+=sub_llave_7[48]
  llave_7+=sub_llave_7[38]
  llave_7+=sub_llave_7[55]
  llave_7+=sub_llave_7[33]
  llave_7+=sub_llave_7[52]
  llave_7+=sub_llave_7[45]
  llave_7+=sub_llave_7[41]
  llave_7+=sub_llave_7[49]
  llave_7+=sub_llave_7[35]
  llave_7+=sub_llave_7[28]
  llave_7+=sub_llave_7[31]
  sub_llaves.append(llave_7)


  #llave 8
  llave_8=""
  llave_8+=sub_llave_8[13]
  llave_8+=sub_llave_8[16]
  llave_8+=sub_llave_8[10]
  llave_8+=sub_llave_8[23]
  llave_8+=sub_llave_8[0]
  llave_8+=sub_llave_8[4]
  llave_8+=sub_llave_8[2]
  llave_8+=sub_llave_8[27]
  llave_8+=sub_llave_8[14]
  llave_8+=sub_llave_8[5]
  llave_8+=sub_llave_8[20]
  llave_8+=sub_llave_8[9]
  llave_8+=sub_llave_8[22]
  llave_8+=sub_llave_8[18]
  llave_8+=sub_llave_8[11]
  llave_8+=sub_llave_8[3]
  llave_8+=sub_llave_8[25]
  llave_8+=sub_llave_8[7]
  llave_8+=sub_llave_8[15]
  llave_8+=sub_llave_8[6]
  llave_8+=sub_llave_8[26]
  llave_8+=sub_llave_8[19]
  llave_8+=sub_llave_8[12]
  llave_8+=sub_llave_8[1]
  llave_8+=sub_llave_8[40]
  llave_8+=sub_llave_8[51]
  llave_8+=sub_llave_8[30]
  llave_8+=sub_llave_8[36]
  llave_8+=sub_llave_8[46]
  llave_8+=sub_llave_8[54]
  llave_8+=sub_llave_8[29]
  llave_8+=sub_llave_8[39]
  llave_8+=sub_llave_8[50]
  llave_8+=sub_llave_8[44]
  llave_8+=sub_llave_8[32]
  llave_8+=sub_llave_8[47]
  llave_8+=sub_llave_8[43]
  llave_8+=sub_llave_8[48]
  llave_8+=sub_llave_8[38]
  llave_8+=sub_llave_8[55]
  llave_8+=sub_llave_8[33]
  llave_8+=sub_llave_8[52]
  llave_8+=sub_llave_8[45]
  llave_8+=sub_llave_8[41]
  llave_8+=sub_llave_8[49]
  llave_8+=sub_llave_8[35]
  llave_8+=sub_llave_8[28]
  llave_8+=sub_llave_8[31]
  sub_llaves.append(llave_8)


  #llave 9
  llave_9=""
  llave_9+=sub_llave_9[13]
  llave_9+=sub_llave_9[16]
  llave_9+=sub_llave_9[10]
  llave_9+=sub_llave_9[23]
  llave_9+=sub_llave_9[0]
  llave_9+=sub_llave_9[4]
  llave_9+=sub_llave_9[2]
  llave_9+=sub_llave_9[27]
  llave_9+=sub_llave_9[14]
  llave_9+=sub_llave_9[5]
  llave_9+=sub_llave_9[20]
  llave_9+=sub_llave_9[9]
  llave_9+=sub_llave_9[22]
  llave_9+=sub_llave_9[18]
  llave_9+=sub_llave_9[11]
  llave_9+=sub_llave_9[3]
  llave_9+=sub_llave_9[25]
  llave_9+=sub_llave_9[7]
  llave_9+=sub_llave_9[15]
  llave_9+=sub_llave_9[6]
  llave_9+=sub_llave_9[26]
  llave_9+=sub_llave_9[19]
  llave_9+=sub_llave_9[12]
  llave_9+=sub_llave_9[1]
  llave_9+=sub_llave_9[40]
  llave_9+=sub_llave_9[51]
  llave_9+=sub_llave_9[30]
  llave_9+=sub_llave_9[36]
  llave_9+=sub_llave_9[46]
  llave_9+=sub_llave_9[54]
  llave_9+=sub_llave_9[29]
  llave_9+=sub_llave_9[39]
  llave_9+=sub_llave_9[50]
  llave_9+=sub_llave_9[44]
  llave_9+=sub_llave_9[32]
  llave_9+=sub_llave_9[47]
  llave_9+=sub_llave_9[43]
  llave_9+=sub_llave_9[48]
  llave_9+=sub_llave_9[38]
  llave_9+=sub_llave_9[55]
  llave_9+=sub_llave_9[33]
  llave_9+=sub_llave_9[52]
  llave_9+=sub_llave_9[45]
  llave_9+=sub_llave_9[41]
  llave_9+=sub_llave_9[49]
  llave_9+=sub_llave_9[35]
  llave_9+=sub_llave_9[28]
  llave_9+=sub_llave_9[31]
  sub_llaves.append(llave_9)


  #llave 10
  llave_10=""
  llave_10+=sub_llave_10[13]
  llave_10+=sub_llave_10[16]
  llave_10+=sub_llave_10[10]
  llave_10+=sub_llave_10[23]
  llave_10+=sub_llave_10[0]
  llave_10+=sub_llave_10[4]
  llave_10+=sub_llave_10[2]
  llave_10+=sub_llave_10[27]
  llave_10+=sub_llave_10[14]
  llave_10+=sub_llave_10[5]
  llave_10+=sub_llave_10[20]
  llave_10+=sub_llave_10[9]
  llave_10+=sub_llave_10[22]
  llave_10+=sub_llave_10[18]
  llave_10+=sub_llave_10[11]
  llave_10+=sub_llave_10[3]
  llave_10+=sub_llave_10[25]
  llave_10+=sub_llave_10[7]
  llave_10+=sub_llave_10[15]
  llave_10+=sub_llave_10[6]
  llave_10+=sub_llave_10[26]
  llave_10+=sub_llave_10[19]
  llave_10+=sub_llave_10[12]
  llave_10+=sub_llave_10[1]
  llave_10+=sub_llave_10[40]
  llave_10+=sub_llave_10[51]
  llave_10+=sub_llave_10[30]
  llave_10+=sub_llave_10[36]
  llave_10+=sub_llave_10[46]
  llave_10+=sub_llave_10[54]
  llave_10+=sub_llave_10[29]
  llave_10+=sub_llave_10[39]
  llave_10+=sub_llave_10[50]
  llave_10+=sub_llave_10[44]
  llave_10+=sub_llave_10[32]
  llave_10+=sub_llave_10[47]
  llave_10+=sub_llave_10[43]
  llave_10+=sub_llave_10[48]
  llave_10+=sub_llave_10[38]
  llave_10+=sub_llave_10[55]
  llave_10+=sub_llave_10[33]
  llave_10+=sub_llave_10[52]
  llave_10+=sub_llave_10[45]
  llave_10+=sub_llave_10[41]
  llave_10+=sub_llave_10[49]
  llave_10+=sub_llave_10[35]
  llave_10+=sub_llave_10[28]
  llave_10+=sub_llave_10[31]
  sub_llaves.append(llave_10)


  #llave 11
  llave_11=""
  llave_11+=sub_llave_11[13]
  llave_11+=sub_llave_11[16]
  llave_11+=sub_llave_11[10]
  llave_11+=sub_llave_11[23]
  llave_11+=sub_llave_11[0]
  llave_11+=sub_llave_11[4]
  llave_11+=sub_llave_11[2]
  llave_11+=sub_llave_11[27]
  llave_11+=sub_llave_11[14]
  llave_11+=sub_llave_11[5]
  llave_11+=sub_llave_11[20]
  llave_11+=sub_llave_11[9]
  llave_11+=sub_llave_11[22]
  llave_11+=sub_llave_11[18]
  llave_11+=sub_llave_11[11]
  llave_11+=sub_llave_11[3]
  llave_11+=sub_llave_11[25]
  llave_11+=sub_llave_11[7]
  llave_11+=sub_llave_11[15]
  llave_11+=sub_llave_11[6]
  llave_11+=sub_llave_11[26]
  llave_11+=sub_llave_11[19]
  llave_11+=sub_llave_11[12]
  llave_11+=sub_llave_11[1]
  llave_11+=sub_llave_11[40]
  llave_11+=sub_llave_11[51]
  llave_11+=sub_llave_11[30]
  llave_11+=sub_llave_11[36]
  llave_11+=sub_llave_11[46]
  llave_11+=sub_llave_11[54]
  llave_11+=sub_llave_11[29]
  llave_11+=sub_llave_11[39]
  llave_11+=sub_llave_11[50]
  llave_11+=sub_llave_11[44]
  llave_11+=sub_llave_11[32]
  llave_11+=sub_llave_11[47]
  llave_11+=sub_llave_11[43]
  llave_11+=sub_llave_11[48]
  llave_11+=sub_llave_11[38]
  llave_11+=sub_llave_11[55]
  llave_11+=sub_llave_11[33]
  llave_11+=sub_llave_11[52]
  llave_11+=sub_llave_11[45]
  llave_11+=sub_llave_11[41]
  llave_11+=sub_llave_11[49]
  llave_11+=sub_llave_11[35]
  llave_11+=sub_llave_11[28]
  llave_11+=sub_llave_11[31]
  sub_llaves.append(llave_11)

  #llave 12
  llave_12=""
  llave_12+=sub_llave_12[13]
  llave_12+=sub_llave_12[16]
  llave_12+=sub_llave_12[10]
  llave_12+=sub_llave_12[23]
  llave_12+=sub_llave_12[0]
  llave_12+=sub_llave_12[4]
  llave_12+=sub_llave_12[2]
  llave_12+=sub_llave_12[27]
  llave_12+=sub_llave_12[14]
  llave_12+=sub_llave_12[5]
  llave_12+=sub_llave_12[20]
  llave_12+=sub_llave_12[9]
  llave_12+=sub_llave_12[22]
  llave_12+=sub_llave_12[18]
  llave_12+=sub_llave_12[11]
  llave_12+=sub_llave_12[3]
  llave_12+=sub_llave_12[25]
  llave_12+=sub_llave_12[7]
  llave_12+=sub_llave_12[15]
  llave_12+=sub_llave_12[6]
  llave_12+=sub_llave_12[26]
  llave_12+=sub_llave_12[19]
  llave_12+=sub_llave_12[12]
  llave_12+=sub_llave_12[1]
  llave_12+=sub_llave_12[40]
  llave_12+=sub_llave_12[51]
  llave_12+=sub_llave_12[30]
  llave_12+=sub_llave_12[36]
  llave_12+=sub_llave_12[46]
  llave_12+=sub_llave_12[54]
  llave_12+=sub_llave_12[29]
  llave_12+=sub_llave_12[39]
  llave_12+=sub_llave_12[50]
  llave_12+=sub_llave_12[44]
  llave_12+=sub_llave_12[32]
  llave_12+=sub_llave_12[47]
  llave_12+=sub_llave_12[43]
  llave_12+=sub_llave_12[48]
  llave_12+=sub_llave_12[38]
  llave_12+=sub_llave_12[55]
  llave_12+=sub_llave_12[33]
  llave_12+=sub_llave_12[52]
  llave_12+=sub_llave_12[45]
  llave_12+=sub_llave_12[41]
  llave_12+=sub_llave_12[49]
  llave_12+=sub_llave_12[35]
  llave_12+=sub_llave_12[28]
  llave_12+=sub_llave_12[31]
  sub_llaves.append(llave_12)


  #llave 13
  llave_13=""
  llave_13+=sub_llave_13[13]
  llave_13+=sub_llave_13[16]
  llave_13+=sub_llave_13[10]
  llave_13+=sub_llave_13[23]
  llave_13+=sub_llave_13[0]
  llave_13+=sub_llave_13[4]
  llave_13+=sub_llave_13[2]
  llave_13+=sub_llave_13[27]
  llave_13+=sub_llave_13[14]
  llave_13+=sub_llave_13[5]
  llave_13+=sub_llave_13[20]
  llave_13+=sub_llave_13[9]
  llave_13+=sub_llave_13[22]
  llave_13+=sub_llave_13[18]
  llave_13+=sub_llave_13[11]
  llave_13+=sub_llave_13[3]
  llave_13+=sub_llave_13[25]
  llave_13+=sub_llave_13[7]
  llave_13+=sub_llave_13[15]
  llave_13+=sub_llave_13[6]
  llave_13+=sub_llave_13[26]
  llave_13+=sub_llave_13[19]
  llave_13+=sub_llave_13[12]
  llave_13+=sub_llave_13[1]
  llave_13+=sub_llave_13[40]
  llave_13+=sub_llave_13[51]
  llave_13+=sub_llave_13[30]
  llave_13+=sub_llave_13[36]
  llave_13+=sub_llave_13[46]
  llave_13+=sub_llave_13[54]
  llave_13+=sub_llave_13[29]
  llave_13+=sub_llave_13[39]
  llave_13+=sub_llave_13[50]
  llave_13+=sub_llave_13[44]
  llave_13+=sub_llave_13[32]
  llave_13+=sub_llave_13[47]
  llave_13+=sub_llave_13[43]
  llave_13+=sub_llave_13[48]
  llave_13+=sub_llave_13[38]
  llave_13+=sub_llave_13[55]
  llave_13+=sub_llave_13[33]
  llave_13+=sub_llave_13[52]
  llave_13+=sub_llave_13[45]
  llave_13+=sub_llave_13[41]
  llave_13+=sub_llave_13[49]
  llave_13+=sub_llave_13[35]
  llave_13+=sub_llave_13[28]
  llave_13+=sub_llave_13[31]
  sub_llaves.append(llave_13)

  #llave 14
  llave_14=""
  llave_14+=sub_llave_14[13]
  llave_14+=sub_llave_14[16]
  llave_14+=sub_llave_14[10]
  llave_14+=sub_llave_14[23]
  llave_14+=sub_llave_14[0]
  llave_14+=sub_llave_14[4]
  llave_14+=sub_llave_14[2]
  llave_14+=sub_llave_14[27]
  llave_14+=sub_llave_14[14]
  llave_14+=sub_llave_14[5]
  llave_14+=sub_llave_14[20]
  llave_14+=sub_llave_14[9]
  llave_14+=sub_llave_14[22]
  llave_14+=sub_llave_14[18]
  llave_14+=sub_llave_14[11]
  llave_14+=sub_llave_14[3]
  llave_14+=sub_llave_14[25]
  llave_14+=sub_llave_14[7]
  llave_14+=sub_llave_14[15]
  llave_14+=sub_llave_14[6]
  llave_14+=sub_llave_14[26]
  llave_14+=sub_llave_14[19]
  llave_14+=sub_llave_14[12]
  llave_14+=sub_llave_14[1]
  llave_14+=sub_llave_14[40]
  llave_14+=sub_llave_14[51]
  llave_14+=sub_llave_14[30]
  llave_14+=sub_llave_14[36]
  llave_14+=sub_llave_14[46]
  llave_14+=sub_llave_14[54]
  llave_14+=sub_llave_14[29]
  llave_14+=sub_llave_14[39]
  llave_14+=sub_llave_14[50]
  llave_14+=sub_llave_14[44]
  llave_14+=sub_llave_14[32]
  llave_14+=sub_llave_14[47]
  llave_14+=sub_llave_14[43]
  llave_14+=sub_llave_14[48]
  llave_14+=sub_llave_14[38]
  llave_14+=sub_llave_14[55]
  llave_14+=sub_llave_14[33]
  llave_14+=sub_llave_14[52]
  llave_14+=sub_llave_14[45]
  llave_14+=sub_llave_14[41]
  llave_14+=sub_llave_14[49]
  llave_14+=sub_llave_14[35]
  llave_14+=sub_llave_14[28]
  llave_14+=sub_llave_14[31]
  sub_llaves.append(llave_14)


  #llave 15
  llave_15=""
  llave_15+=sub_llave_15[13]
  llave_15+=sub_llave_15[16]
  llave_15+=sub_llave_15[10]
  llave_15+=sub_llave_15[23]
  llave_15+=sub_llave_15[0]
  llave_15+=sub_llave_15[4]
  llave_15+=sub_llave_15[2]
  llave_15+=sub_llave_15[27]
  llave_15+=sub_llave_15[14]
  llave_15+=sub_llave_15[5]
  llave_15+=sub_llave_15[20]
  llave_15+=sub_llave_15[9]
  llave_15+=sub_llave_15[22]
  llave_15+=sub_llave_15[18]
  llave_15+=sub_llave_15[11]
  llave_15+=sub_llave_15[3]
  llave_15+=sub_llave_15[25]
  llave_15+=sub_llave_15[7]
  llave_15+=sub_llave_15[15]
  llave_15+=sub_llave_15[6]
  llave_15+=sub_llave_15[26]
  llave_15+=sub_llave_15[19]
  llave_15+=sub_llave_15[12]
  llave_15+=sub_llave_15[1]
  llave_15+=sub_llave_15[40]
  llave_15+=sub_llave_15[51]
  llave_15+=sub_llave_15[30]
  llave_15+=sub_llave_15[36]
  llave_15+=sub_llave_15[46]
  llave_15+=sub_llave_15[54]
  llave_15+=sub_llave_15[29]
  llave_15+=sub_llave_15[39]
  llave_15+=sub_llave_15[50]
  llave_15+=sub_llave_15[44]
  llave_15+=sub_llave_15[32]
  llave_15+=sub_llave_15[47]
  llave_15+=sub_llave_15[43]
  llave_15+=sub_llave_15[48]
  llave_15+=sub_llave_15[38]
  llave_15+=sub_llave_15[55]
  llave_15+=sub_llave_15[33]
  llave_15+=sub_llave_15[52]
  llave_15+=sub_llave_15[45]
  llave_15+=sub_llave_15[41]
  llave_15+=sub_llave_15[49]
  llave_15+=sub_llave_15[35]
  llave_15+=sub_llave_15[28]
  llave_15+=sub_llave_15[31]
  sub_llaves.append(llave_15)


  #llave 16
  llave_16=""
  llave_16+=sub_llave_16[13]
  llave_16+=sub_llave_16[16]
  llave_16+=sub_llave_16[10]
  llave_16+=sub_llave_16[23]
  llave_16+=sub_llave_16[0]
  llave_16+=sub_llave_16[4]
  llave_16+=sub_llave_16[2]
  llave_16+=sub_llave_16[27]
  llave_16+=sub_llave_16[14]
  llave_16+=sub_llave_16[5]
  llave_16+=sub_llave_16[20]
  llave_16+=sub_llave_16[9]
  llave_16+=sub_llave_16[22]
  llave_16+=sub_llave_16[18]
  llave_16+=sub_llave_16[11]
  llave_16+=sub_llave_16[3]
  llave_16+=sub_llave_16[25]
  llave_16+=sub_llave_16[7]
  llave_16+=sub_llave_16[15]
  llave_16+=sub_llave_16[6]
  llave_16+=sub_llave_16[26]
  llave_16+=sub_llave_16[19]
  llave_16+=sub_llave_16[12]
  llave_16+=sub_llave_16[1]
  llave_16+=sub_llave_16[40]
  llave_16+=sub_llave_16[51]
  llave_16+=sub_llave_16[30]
  llave_16+=sub_llave_16[36]
  llave_16+=sub_llave_16[46]
  llave_16+=sub_llave_16[54]
  llave_16+=sub_llave_16[29]
  llave_16+=sub_llave_16[39]
  llave_16+=sub_llave_16[50]
  llave_16+=sub_llave_16[44]
  llave_16+=sub_llave_16[32]
  llave_16+=sub_llave_16[47]
  llave_16+=sub_llave_16[43]
  llave_16+=sub_llave_16[48]
  llave_16+=sub_llave_16[38]
  llave_16+=sub_llave_16[55]
  llave_16+=sub_llave_16[33]
  llave_16+=sub_llave_16[52]
  llave_16+=sub_llave_16[45]
  llave_16+=sub_llave_16[41]
  llave_16+=sub_llave_16[49]
  llave_16+=sub_llave_16[35]
  llave_16+=sub_llave_16[28]
  llave_16+=sub_llave_16[31]
  sub_llaves.append(llave_16)
  
  return sub_llaves

def DES_comp(texto_claro, llave):
    TC = [texto_claro[x] for x in range (64)]

    #permutacion inicial:
    texto_permutado = ""
    texto_permutado += str(TC[57])
    texto_permutado += str(TC[49])
    texto_permutado += str(TC[41])
    texto_permutado += str(TC[33])
    texto_permutado += str(TC[25])
    texto_permutado += str(TC[17])
    texto_permutado += str(TC[9])
    texto_permutado += str(TC[1])

    texto_permutado += str(TC[59])
    texto_permutado += str(TC[51])
    texto_permutado += str(TC[43])
    texto_permutado += str(TC[35])
    texto_permutado += str(TC[27])
    texto_permutado += str(TC[19])
    texto_permutado += str(TC[11])
    texto_permutado += str(TC[3])

    texto_permutado += str(TC[61])
    texto_permutado += str(TC[53])
    texto_permutado += str(TC[45])
    texto_permutado += str(TC[37])
    texto_permutado += str(TC[29])
    texto_permutado += str(TC[21])
    texto_permutado += str(TC[13])
    texto_permutado += str(TC[5])

    texto_permutado += str(TC[63])
    texto_permutado += str(TC[55])
    texto_permutado += str(TC[47])
    texto_permutado += str(TC[39])
    texto_permutado += str(TC[31])
    texto_permutado += str(TC[23])
    texto_permutado += str(TC[15])
    texto_permutado += str(TC[7])
    
    texto_permutado += str(TC[56])
    texto_permutado += str(TC[48])
    texto_permutado += str(TC[40])
    texto_permutado += str(TC[32])
    texto_permutado += str(TC[24])
    texto_permutado += str(TC[16])
    texto_permutado += str(TC[8])
    texto_permutado += str(TC[0])

    texto_permutado += str(TC[58])
    texto_permutado += str(TC[50])
    texto_permutado += str(TC[42])
    texto_permutado += str(TC[34])
    texto_permutado += str(TC[26])
    texto_permutado += str(TC[18])
    texto_permutado += str(TC[10])
    texto_permutado += str(TC[2])

    texto_permutado += str(TC[60])
    texto_permutado += str(TC[52])
    texto_permutado += str(TC[44])
    texto_permutado += str(TC[36])
    texto_permutado += str(TC[28])
    texto_permutado += str(TC[20])
    texto_permutado += str(TC[12])
    texto_permutado += str(TC[4])

    texto_permutado += str(TC[62])
    texto_permutado += str(TC[55])
    texto_permutado += str(TC[46])
    texto_permutado += str(TC[38])
    texto_permutado += str(TC[30])
    texto_permutado += str(TC[22])
    texto_permutado += str(TC[14])
    texto_permutado += str(TC[6])
    
    

    #generacion de llaves
    
    #aqui se llama la funcion que genera las llaves
    sub_llaves = gen_llaves(llave)

    #rondas de cifrado
    texto_a_cifrar = texto_permutado
    for x in range (16):
        texto_a_cifrar = DES_clase.DES(texto_a_cifrar, sub_llaves[x])


    #permutacion final
    texto_cifrado = ""

    texto_cifrado += texto_a_cifrar[39]
    texto_cifrado += texto_a_cifrar[7]
    texto_cifrado += texto_a_cifrar[47]
    texto_cifrado += texto_a_cifrar[15]
    texto_cifrado += texto_a_cifrar[55]
    texto_cifrado += texto_a_cifrar[23]
    texto_cifrado += texto_a_cifrar[63]
    texto_cifrado += texto_a_cifrar[31]

    texto_cifrado += texto_a_cifrar[38]
    texto_cifrado += texto_a_cifrar[6]
    texto_cifrado += texto_a_cifrar[46]
    texto_cifrado += texto_a_cifrar[14]
    texto_cifrado += texto_a_cifrar[54]
    texto_cifrado += texto_a_cifrar[22]
    texto_cifrado += texto_a_cifrar[62]
    texto_cifrado += texto_a_cifrar[30]

    texto_cifrado += texto_a_cifrar[37]
    texto_cifrado += texto_a_cifrar[5]
    texto_cifrado += texto_a_cifrar[45]
    texto_cifrado += texto_a_cifrar[13]
    texto_cifrado += texto_a_cifrar[53]
    texto_cifrado += texto_a_cifrar[21]
    texto_cifrado += texto_a_cifrar[61]
    texto_cifrado += texto_a_cifrar[29]
    
    texto_cifrado += texto_a_cifrar[36]
    texto_cifrado += texto_a_cifrar[4]
    texto_cifrado += texto_a_cifrar[44]
    texto_cifrado += texto_a_cifrar[12]
    texto_cifrado += texto_a_cifrar[52]
    texto_cifrado += texto_a_cifrar[20]
    texto_cifrado += texto_a_cifrar[60]
    texto_cifrado += texto_a_cifrar[28]

    texto_cifrado += texto_a_cifrar[35]
    texto_cifrado += texto_a_cifrar[3]
    texto_cifrado += texto_a_cifrar[43]
    texto_cifrado += texto_a_cifrar[11]
    texto_cifrado += texto_a_cifrar[51]
    texto_cifrado += texto_a_cifrar[19]
    texto_cifrado += texto_a_cifrar[59]
    texto_cifrado += texto_a_cifrar[27]

    texto_cifrado += texto_a_cifrar[34]
    texto_cifrado += texto_a_cifrar[2]
    texto_cifrado += texto_a_cifrar[42]
    texto_cifrado += texto_a_cifrar[10]
    texto_cifrado += texto_a_cifrar[50]
    texto_cifrado += texto_a_cifrar[18]
    texto_cifrado += texto_a_cifrar[58]
    texto_cifrado += texto_a_cifrar[26]

    texto_cifrado += texto_a_cifrar[33]
    texto_cifrado += texto_a_cifrar[1]
    texto_cifrado += texto_a_cifrar[41]
    texto_cifrado += texto_a_cifrar[9]
    texto_cifrado += texto_a_cifrar[49]
    texto_cifrado += texto_a_cifrar[17]
    texto_cifrado += texto_a_cifrar[57]
    texto_cifrado += texto_a_cifrar[25]

    texto_cifrado += texto_a_cifrar[32]
    texto_cifrado += texto_a_cifrar[0]
    texto_cifrado += texto_a_cifrar[40]
    texto_cifrado += texto_a_cifrar[8]
    texto_cifrado += texto_a_cifrar[48]
    texto_cifrado += texto_a_cifrar[16]
    texto_cifrado += texto_a_cifrar[56]
    texto_cifrado += texto_a_cifrar[24]


    return texto_cifrado

def main_final():
    texto_claro = input("Ingrese el texto claro: ")
    while len(texto_claro)>64 or len(texto_claro)<64:
        print("Ese texto no es valido - No son los bits correctos")
        texto_claro = input("Ingrese el texto claro: ")

    llave = input("Ingrese la llave de 64 bits: ")
    while len(llave)>64 or len(llave)<64:
        print("Esa llave no es valida - No son los bits correctos")
        llave = input("Ingrese la llave de 64 bits: ")

    x = DES_comp(texto_claro, llave)
    print("Su texto cifrado es: ")
    print(x)

main_final()