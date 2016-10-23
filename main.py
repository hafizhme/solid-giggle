from machine import LexicalAnalyzer

la = LexicalAnalyzer(input("Input  : "))

token = la.generateTokenLexic()

print("Output :",*token, " ")
