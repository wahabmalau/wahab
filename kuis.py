tugas penilaian mahasiswa

#input

nama = input("Nama:").strip()

if nama.lower() "andi":

target - 70

elif nama.lower() "budi":

target= 75

elif nama.lower()

"citra":

target 80

else:

taret None

print("masukan nama mahasiswa yang tidak lulus:")

if target is not None:

percobaan 1

lulus False

while percobaan <- 3: nilai - int (input(f"nilai{percobaan}:"))

if nilai > target:

lulus True

break

percobaan + 1

print("\nOutput")

if lulus:

else:

print(f"{nama) lulus")

print("f{nama}tidak lulus)