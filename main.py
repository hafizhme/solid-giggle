from machine import LexicalAnalyzer

la = LexicalAnalyzer(input())

token = la.generateTokenLexic()

print(*token, " ")