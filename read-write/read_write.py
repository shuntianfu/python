
# with open('test.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)
#     
# print(f.closed)


# with open('test.txt', 'r') as f:
#     f_contents = f.readlines()
#     print(f_contents)
    
# print statement ends with newline

# with open('test.txt', 'r') as f:
#     f_contents = f.readline()
#     print(f_contents, end='')
#     f_contents = f.readline()
#     print(f_contents, end='')
#     f_contents = f.readline()
#     print(f_contents, end='')
#     f_contents = f.readline()
#     print(f_contents, end='')
    
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line, end='')


# with open('test.txt', 'r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)     
#     print(f_contents, end='')

# with open('test.txt', 'r') as f:
#     size_to_read = 2 
#     f_contents = f.read(size_to_read)     
#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)

# with open('test.txt', 'r') as f:
#     size_to_read = 2 
#     f_contents = f.read(size_to_read)     
#     print(f_contents, end='')
#     f_contents = f.read(size_to_read)     
#     print(f_contents)


# with open('test.txt', 'r') as f:
#     size_to_read = 2 
#     f_contents = f.read(size_to_read)     
#     print(f_contents, end='')
#     f.seek(0)
#     f_contents = f.read(size_to_read)     
#     print(f_contents)

# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.write('Test')

# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)
#     with open('test_copy.txt', 'r') as pf:
#         print(pf.read(), end='')

# with open('/home/zhang/desktop/wallpaper/wallpaper1.jpg', 'rb') as rf:
#     with open('montain.jpg', 'wb') as wf:
#         chunk_size = 100000
#         rf_chunk = rf.read(chunk_size)

# with open('/home/zhang/desktop/wallpaper/wallpaper1.jpg', 'rb') as rf:
#     with open('montain.jpg', 'wb') as wf:
#         chunk_size = 4000
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
    








# f = open('test.txt', 'r')
 

# print(f.name)
# print(f.mode)
# 
# # close file
# f.close()


