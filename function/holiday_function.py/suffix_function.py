def add_ing_or_ly(s: str) -> str:
    if len(s) < 3:
        return s
    if s.endswith("ing"):
        return s + "ly"
    return s + "ing"

print(add_ing_or_ly("abc"))  
print(add_ing_or_ly("string"))
print(add_ing_or_ly("on"))
