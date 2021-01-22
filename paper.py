from scidownl.scihub import *
print("Silahkan Download Journal atau paper yang anda inginkan ")
filePath = input("Masukkan serial no DOI: ")
print("contoh tempat penyimpanan >> D:\Download")
output = input("Mau simpan dimana : ")
DOI = filePath
output_file = output
sci = SciHub(DOI, output_file).download(choose_scihub_url_index=3)