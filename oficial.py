import streamlit as st

imagem_url = "https://www.loreal-paris.ru/-/media/project/loreal/brand-sites/oap/emea/ru/resized-photo/2000x600_oap_reno_elseve-res.jpg?rev=6c12448c223d4bbaa8c6a3510f999bc2&cx=0.44&cy=0.38&cw=2000&ch=600&hash=3CBBF0AD10FFCFD83FAB19291EBC3E5F12AEC9AB"
st.image(imagem_url, use_column_width=True)
st.title("QUAL ELSEVE É PERFEITO PARA VOCÊ?")
st.write("A Loreal Elseve tem 16 linhas de cabelo! Com tantas opções maravilhosas fica dificil saber qual é a mais indicada para você, por isso fizemos o Teste de Cabelo Elseve! Descubra sua linha capilar ideal em menos de 3 minutos!")
    
diretorio = {
    "LINHA HIDRA DETOX CASPA": 
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/hydra-detox-anti-caspa', 'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgbc0HxB_VgYrmBI5hgM4u-_byijruGtLfiQ&usqp=CAU'},
    "LINHA QUERALISO":
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/quera-liso-mq-230-c', 'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjn4yBejAqDr2hBktSeCbtXtXCKGqKRbK6fA&usqp=CAU'}, 
     "LINHA COLORVIVE":
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/colorvive', 'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/colorvive/color-vive-c-atalogo.jpg'},    
     "LINHA REPARAÇÃO TOTAL PÓS QUÍMICA":
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/reparacao-total-5-pos-quimica', 'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/tr5-pos-quimica/posquimicacatalogo.jpg'},
     "LINHA SUPREME CONTROL":
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/supreme-control-4d', 'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/supreme-control-4d/catalogo-supreme.jpg'},
     "LINHA ARGININA":
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/arginina-resist', 'imagem': 'https://4.bp.blogspot.com/-o734azKE_Fs/T4iCfauqMuI/AAAAAAAABAE/VZPWdk_PJY8/s1600/arginina1.jpg'},
      "LINHA REPARAÇÃO TOTAL 5 PROFUNDA":
       {'link': "https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/reparacao-total-5-extra-profundo", 'imagem': "https://i.ytimg.com/vi/LIfN-2Qp_gc/maxresdefault.jpg"},
      "LINHA REPARAÇÃO TOTAL 5":
       {'link': "https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/reparacao-total-5-extra-profundo", 'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/tr5/rt5.jpg'},
      "LINHA HIALURONICO":
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/pure-hialuronico', 'imagem': "https://epocacosmeticos.vteximg.com.br/arquivos/ids/532886-500-500/loreal-paris-elseve-pure-hialuronico-shampoo--5-.jpg?v=638104421191000000"},
      "LINHA DETOX":
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/hydra-detox', 'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/hydra-detox/hydradetox-48hr-catalogo2.jpg'},
      "LINHA OELO EXTRAORDINARIO":
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/oleo-extraordinario', 'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/extraordinary-oil/nutricaocatalogo.jpg'},
      'LINHA OLEO EXTRAORDINARIO CACHOS':
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/oleo-extraordinario-cachos', 'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/extraordinary-oil/oleo-extraordinario-cachos2.jpg'},
      'LINHA LISO DOS SONHOS':
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/liso-dos-sonhos', 'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXgAGoCTyEyYvkyXwTHNds5hBGc9BGSTQJRw&usqp=CAU'},
      'LINHA LONGO DOS SONHOS':
       {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/liso-dos-sonhos', 'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAl08gjdDyFzgbu6-lwMocIQ4TVRGmTOYM5zexa1mtDiJIT9W_mQ88rCF-c3n_tMKr2Oc&usqp=CAU'},
      'LINHA CACHOS DOS SONHOS':
      {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/cachos-longos-dos-sonhos', 'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS287TsHFN6F5LST1G01JDkibCmO46fa50kNA&usqp=CAU'}
}

resposta = st.checkbox("Seu cabelo tem caspa?", ("SIM", "NÃO"))
print(resposta)
if resposta:
    print(diretorio["LINHA HIDRA DETOX CASPA"]['link'])
    st.write(diretorio["LINHA HIDRA DETOX CASPA"]['link'])
    st.image(diretorio["LINHA HIDRA DETOX CASPA"]['imagem'])
elif resposta == "NÃO":
    resposta_adicional1 = st.checkbox("Você quer usar antes da escova?", ("SIM", "NÃO"))
    print(resposta_adicional1)
    if resposta_adicional1 == "SIM": 
        st.write(diretorio["LINHA QUERALISO"]['link'])
        st.image(diretorio["LINHA QUERALISO"]['imagem'])
    elif resposta_adicional1 == "NÃO":
        resposta_adicional2 = st.checkbox("Seu cabelo tem química?", ("SIM", "NÃO"))
        print(resposta_adicional2)
        if resposta_adicional2 == "SIM":
            resposta_adicional3 = st.checkbox("Ele é pintado?", ("SIM", "NÃO"))
            print(resposta_adicional3)
            if resposta_adicional3 == "SIM":
                st.write(diretorio["LINHA COLORVIVE"]['link'])
                st.image(diretorio["LINHA COLORVIVE"]['imagem'])
            elif resposta_adicional3 == "NÃO":
                st.write(diretorio['LINHA REPARAÇÃO TOTAL PÓS QUÍMICA']['link'])
                st.image(diretorio["LINHA REPARAÇÃO TOTAL PÓS QUÍMICA"]['imagem'])
        elif resposta_adicional2 == "NÃO":
            resposta_adicional4 = st.checkbox("Seu cabelo tem frizz?", ("SIM", "NÃO"))
            print(resposta_adicional4)
            if resposta_adicional4 == "SIM":
                st.write(diretorio['LINHA SUPREME CONTROL']['link'])
                st.image(diretorio['LINHA SUPREME CONTROL']['imagem'])
            elif resposta_adicional4 == "NÃO":
                resposta_adicional5 = st.checkbox("Ele tem queda?", ("SIM", "NÃO"))
                print(resposta_adicional5)
                if resposta_adicional5 == "SIM":
                    st.write(diretorio['LINHA ARGININA']['link'])
                    st.image(diretorio['LINHA ARGININA']['imagem'])
                elif resposta_adicional5 == "NÃO":
                    resposta_adicional6 = st.checkbox("Ele está danificado?", ("SIM", "NÃO"))
                    print(resposta_adicional6)
                    if resposta_adicional6 == 'SIM':
                        resposta_adicional7 = st.checkbox("Ele está muito ou pouco danificado?", ("MUITO", "POUCO"))
                        print(resposta_adicional7)
                        if resposta_adicional7 == 'MUITO':
                            st.write(diretorio['LINHA REPARAÇÃO TOTAL 5 PROFUNDA']['link'])
                            st.image(diretorio['LINHA REPARAÇÃO TOTAL 5 PROFUNDA']['imagem'])
                        elif resposta_adicional7 == 'POUCO':
                            st.write(diretorio['LINHA REPARAÇÃO TOTAL 5']['link'])
                            st.image(diretorio['LINHA REPARAÇÃO TOTAL 5']['imagem'])
