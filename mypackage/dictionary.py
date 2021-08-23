class myDictionary():
    def __init__(self, myWord, mySynonym):
        self.myWord = {
            "Ayah" : "seorang pria pemimpin keluarga",
            "Ibu" : "seorang wanita yang melahirkan anak",
            "Anak" : "seseorang yang dilahirkan oleh ibu"
            }
        self.mySynonym = {
            "Ayah" : "Bapak",
            "Ibu" : "Mama",
            "Anak" : "Putra/Putri"
        }
        return myWord
    def func(self):
        print(self.myWord)
        print(self.mySynonym)
        return