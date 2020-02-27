fid = open('tmp', 'r')
lines = fid.readlines()
# print(lines)

fod = open('tmp2', 'w')
for i, l in enumerate(lines):
    if ' Dec ' in l:
        # print(l, lines[i-2])
        author_l = lines[i+3].split('·')
        author_l = [item.strip() for item in author_l]
        authors = ', '.join(author_l)
        newl = '- ' + authors + '. ' + lines[i+1]
        fod.write(newl)
