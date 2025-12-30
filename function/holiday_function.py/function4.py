def remove_odd_index(s: str) -> str:
    return "".join([s[i] for i in range(len(s)) if i % 2 == 0])

print(remove_odd_index("semicolon"))  
