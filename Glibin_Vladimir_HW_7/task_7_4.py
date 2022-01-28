import os

saize_files = {
  100: 0,
  1000: 0,
  10000: 0,
  100000: 0
}
folder = os.path.join(os.getcwd(), 'some_data')
for root, dirs, files in os.walk(folder):
    for file in files:
        path = os.path.join(root, file)
        size = os.stat(path).st_size
        print(os.path.basename(path))
        if size <= 100:
            saize_files[100] +=1
        elif 100 <= size <= 1000:
            saize_files[1000] += 1
        elif 1000 <= size <= 10000:
            saize_files[10000] += 1
        elif 10000 <= size <= 100000:
            saize_files[100000] += 1

print(saize_files)

