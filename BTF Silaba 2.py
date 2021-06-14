# Autor: Junior Obom
# 10/08/2017

# Forma palavras através de silabas e não de letra em letra

Alfa1=['a','e', 'i', 'o', 'u']

Alfa2=('ba','be','bi','bo','bu','ca','ce','ci','co','cu','da','de','di','do','du','fa','fe','fi','fo','fu','ga','ge','gi','go','gu','ha','he','hi','ho','ia','ie','io','iu','hu','ja','je','ji','jo','ju','ka','ke','ki','ko','ku','la','le','li','lo','lu','ma','me','mi','mo','mu','na','ne','ni','no','nu','pa','pe','pi','po','pu','qu','ra','re','ri','ro','ru','sa','se','si','so','su','ta','te','ti','to','tu','va','ve','vi','vo','vu','wa','we','wi','wo','wu','xa','xe','xi','xo','xu','za','ze','zi','zo','zu')


Alfa3=('cha','che','chi','cho','chu','nha','nhe','nhi','nho','nhu','rra','rre','rri','rro','rru','ssa','sse','ssi','sso','ssu','qua','que','qui','quo') 

Nums=list('0123456789')


for i1 in (Alfa2):
    for i2 in (Alfa2):
        for i3 in (Alfa2):
            for i4 in (Alfa2):
                y=(i1+i2+i3+i4)
                print(y)
                if(y=='goiabada'):
                    print('Encontrada')
                    exit()
