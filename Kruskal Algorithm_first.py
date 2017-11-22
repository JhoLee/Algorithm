##
# 17.11.22
#
# Kruskal Algorithm
#
# 미완성
# 
##
_label = ('a', 'b', 'c', 'd', 'e', 'f', )
_MAX = 98765  # 최대값 예시

origin = [
  [ _MAX,    8,  _MAX,    2,      4,  _MAX],
  [   8,   _MAX,     1,    4,   _MAX,   2],
  [ _MAX, 1, _MAX, _MAX, _MAX, 1],
  [   2,4, _MAX, _MAX, 3, 7],
  [   4,  _MAX,   _MAX,     3,  _MAX,       9],
  [_MAX,    2,    1,    7,    9,  _MAX]
]

n = len(origin)

lines = []

# #
for i in range(0, n):
  ## ##
  for j in range(i+1, n):
    if origin[i][j] != _MAX:
      lines.append([ origin[i][j], _label[i], _label[j]])
      
      
  ## ##      
# #


# # 
print("Lines")
for line in lines:
  print(line)
print()

# #
  
# Sort #
print("After Sorting")
  
for i in range(0, len(lines) - 1):
  for j in range(i, len(lines)):
    if lines[i][0] > lines[j][0]:
      lines[i], lines[j] = lines[j], lines[i]

for line in lines:
  print(line)
print()  
# #
