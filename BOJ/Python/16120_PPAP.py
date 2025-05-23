def is_ppap(s: str) -> bool:
    st = []
    for c in s:
        
        st.append(c)

        # print(st[-4:])
        while ''.join(st[-4:]) == "PPAP":
            # print(st[-4:])
            for i in range(3):
                st.pop()
        
        


    if len(st) == 1 and st[0] == "P":
        return True    
    else:
        return False
    
        
    
        


s = input().strip()
print("PPAP" if is_ppap(s) else "NP")

    
