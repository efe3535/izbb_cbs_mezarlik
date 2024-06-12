import xmltodict

# Ahmet Efe Akyazi, 12 haziran 2024 11:27

# bu kodun amaci 'fetchXml.sh' scripti ile indirilen bilgideki isim ve soyisimlerin bir dosyaya kaydedilerek sunulmasidir


with open("test.xml") as file:
    parsedMezarlik = xmltodict.parse(file.read())
    with open("output.txt", "w") as out:
        for mefta in parsedMezarlik["ArrayOfMeftaBilgisi2"]["MeftaBilgisi2"]:
            out.write(f"{mefta['adi']} {mefta['soyadi']}\n")
print("done!")
