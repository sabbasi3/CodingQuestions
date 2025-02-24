
def play(user_input: str) -> str:
    if not user_input:
        return ""
    
    lines = []
    bytes_data = user_input.encode('ascii')
    for i in range(0, len(bytes_data), 16):
        chunk = bytes_data[i:i+16]
        
        # Hex index
        hex_index = f"{i:08x}: "
        
        # Hex representation
        hex_values = []
        for j in range(0, len(chunk), 2):
            pair = chunk[j:j+2]
            hex_values.append(''.join(f"{b:02x}" for b in pair))
        hex_part = ' '.join(hex_values)
        
        # Padding to align ASCII part
        padding = ' ' * (51 - len(hex_index) - len(hex_part))
        
        # ASCII representation
        ascii_part = ''.join('.' if b == 10 else chr(b) for b in chunk)
        
        lines.append(f"{hex_index}{hex_part}{padding}{ascii_part}")
    
    return '\n'.join(lines)

### DO NOT MODIFY BELOW THIS LINE ###
import sys
if __name__ == "__main__":
    user_input = sys.stdin.read()
    print(play(user_input))


# def play(s):
#     if not s: return ""
#     b=s.encode('ascii')
#     return '\n'.join(f"{i*16:08x}: {' '.join(''.join(f'{x:02x}' for x in b[i*16+j:i*16+j+2]) for j in range(0,len(c),2))}{' '*(51-10-len(c)*2-1)}{''.join('.' if x==10 else chr(x) for x in c)}" for i,c in enumerate([b[i:i+16] for i in range(0,len(b),16)]))

# if __name__=="__main__":
#     import sys;print(play(sys.stdin.read()))


def play(s):
    if not s:
        return ""
    b = s.encode('ascii')
    r = []
    for i in range(0, len(b), 16):
        c = b[i:i + 16]
        h = f"{i:08x}: "
        v = []
        for j in range(0, len(c), 2):
            p = c[j:j + 2]
            v.append(''.join(f"{x:02x}" for x in p))
        t = ' '.join(v)
        r.append(f"{h}{t}{' ' * (51 - len(h) - len(t))}{''.join('.' if x == 10 else chr(x) for x in c)}")
    return '\n'.join(r)

if __name__ == "__main__":
    import sys
    print(play(sys.stdin.read()))



def play(s):
 if not s:return""
 b=s.encode('ascii')
 r=[]
 for i in range(0,len(b),16):
  c=b[i:i+16]
  h=f"{i:08x}: "
  v=[]
  for j in range(0,len(c),2):
   p=c[j:j+2]
   v.append(''.join(f"{x:02x}"for x in p))
  t=' '.join(v)
  r.append(f"{h}{t}{' '*(51-len(h)-len(t))}{''.join('.'if x==10 else chr(x)for x in c)}")
 return'\n'.join(r)
if __name__=="__main__":
  import sys;print(play(sys.stdin.read()))



def play(s):
 if not s:return""
 b=s.encode('ascii');r=[]
 for i in range(0,len(b),16):
  c=b[i:i+16];h=f"{i:08x}: ";v=[]
  for j in range(0,len(c),2):p=c[j:j+2];v.append(''.join(f"{x:02x}"for x in p))
  t=' '.join(v);r.append(f"{h}{t}{' '*(51-len(h)-len(t))}{''.join('.'if x==10else chr(x)for x in c)}")
 return'\n'.join(r)
if __name__=="__main__":import sys;print(play(sys.stdin.read()))
