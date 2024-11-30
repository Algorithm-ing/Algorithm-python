max_width,max_height=map(int,input().split())
dotted_lines=int(input())
cut_lines = [[0,max_width],[0,max_height]]
for _ in range(dotted_lines):
    i,line_number=map(int,input().split())
    cut_lines[i^1].append(line_number)
max_lines=[]
for cut_line in cut_lines:
    cut_line_asc = sorted(cut_line)
    max_line = max(cut_line_asc[i+1]-cut_line_asc[i] for i in range(len(cut_line_asc)-1))
    max_lines.append(max_line)
print(max_lines[0]*max_lines[1])