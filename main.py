from machine import LexicalAnalyzer

la = LexicalAnalyzer(input("Input  : "))

token = la.generateTokenLexic()
parser = la.parser()

print("Token  :",*token, " ")
print("Valid  :",parser)
