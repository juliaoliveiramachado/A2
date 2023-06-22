import streamlit as st

imagem_url = "https://www.loreal-paris.ru/-/media/project/loreal/brand-sites/oap/emea/ru/resized-photo/2000x600_oap_reno_elseve-res.jpg?rev=6c12448c223d4bbaa8c6a3510f999bc2&cx=0.44&cy=0.38&cw=2000&ch=600&hash=3CBBF0AD10FFCFD83FAB19291EBC3E5F12AEC9AB"
st.image(imagem_url, use_column_width=True)
st.title("QUAL ELSEVE É PERFEITO PARA VOCÊ?")
st.write("A Loreal Elseve tem 16 linhas de cabelo! Com tantas opções maravilhosas fica dificil saber qual é a mais indicada para você, por isso fizemos o Teste de Cabelo Elseve! Descubra sua linha capilar ideal em menos de 3 minutos!")

diretorio = {
    "LINHA HIDRA DETOX CASPA":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/hydra-detox-anti-caspa',
        'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgbc0HxB_VgYrmBI5hgM4u-_byijruGtLfiQ&usqp=CAU'},
    "LINHA QUERALISO":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/quera-liso-mq-230-c',
        'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjn4yBejAqDr2hBktSeCbtXtXCKGqKRbK6fA&usqp=CAU'},
    "LINHA COLORVIVE":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/colorvive',
     'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/colorvive/color-vive-c-atalogo.jpg'},
    "LINHA REPARAÇÃO TOTAL PÓS QUÍMICA":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/reparacao-total-5-pos-quimica',
     'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/tr5-pos-quimica/posquimicacatalogo.jpg'},
    "LINHA SUPREME CONTROL":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/supreme-control-4d',
     'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/supreme-control-4d/catalogo-supreme.jpg'},
    "LINHA ARGININA":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/arginina-resist',
     'imagem': 'https://4.bp.blogspot.com/-o734azKE_Fs/T4iCfauqMuI/AAAAAAAABAE/VZPWdk_PJY8/s1600/arginina1.jpg'},
    "LINHA REPARAÇÃO TOTAL 5 PROFUNDA":
    {'link': "https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/reparacao-total-5-extra-profundo",
     'imagem': "https://i.ytimg.com/vi/LIfN-2Qp_gc/maxresdefault.jpg"},
    "LINHA REPARAÇÃO TOTAL 5":
    {'link': "https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/reparacao-total-5-extra-profundo",
     'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/tr5/rt5.jpg'},
    "LINHA PURE HIALURONICO":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/pure-hialuronico',
     'imagem': "https://epocacosmeticos.vteximg.com.br/arquivos/ids/532886-500-500/loreal-paris-elseve-pure-hialuronico-shampoo--5-.jpg?v=638104421191000000"},
    "LINHA DETOX":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/hydra-detox',
     'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/hydra-detox/hydradetox-48hr-catalogo2.jpg'},
    "LINHA OLEO EXTRAORDINARIO":
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/oleo-extraordinario',
     'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/extraordinary-oil/nutricaocatalogo.jpg'},
    'LINHA OLEO EXTRAORDINARIO CACHOS':
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/oleo-extraordinario-cachos',
     'imagem': 'https://www.loreal-paris.com.br/-/media/project/loreal/brand-sites/oap/americas/br/products/hair/hair-care/elseve/extraordinary-oil/oleo-extraordinario-cachos2.jpg'},
    'LINHA LISO DOS SONHOS':
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/liso-dos-sonhos',
     'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXgAGoCTyEyYvkyXwTHNds5hBGc9BGSTQJRw&usqp=CAU'},
    'LINHA LONGO DOS SONHOS':
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/liso-dos-sonhos',
     'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAl08gjdDyFzgbu6-lwMocIQ4TVRGmTOYM5zexa1mtDiJIT9W_mQ88rCF-c3n_tMKr2Oc&usqp=CAU'},
    'LINHA CACHOS DOS SONHOS':
    {'link': 'https://www.loreal-paris.com.br/cuidados-com-o-cabelo/elseve/cachos-longos-dos-sonhos',
     'imagem': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS287TsHFN6F5LST1G01JDkibCmO46fa50kNA&usqp=CAU'}
}

st.write("1. Seu cabelo tem caspa?")
caspaSim = st.checkbox("SIM", key="caspa_1", value=False)
caspaNao = st.checkbox("NÃO", key="caspa_2", value=False)

if caspaSim:
    st.write(diretorio["LINHA HIDRA DETOX CASPA"]["link"])
    st.image(diretorio["LINHA HIDRA DETOX CASPA"]["imagem"])

elif caspaNao:
    st.write("2. Você quer usar antes da escova?")
    escovaSim = st.checkbox("SIM", key="escova_1")
    escovaNao = st.checkbox("NÃO", key="escova_2")

    if escovaSim:
        st.write(diretorio["LINHA QUERALISO"]["link"])
        st.image(diretorio["LINHA QUERALISO"]["imagem"])
    elif escovaNao:
        st.write("3. Seu cabelo tem química?")

        quimicaSim = st.checkbox("SIM", key="quimica_1")
        quimicaNao = st.checkbox("NÃO", key="quimica_2")

        if quimicaSim:
            st.write("3.1. Ele é pintado?")
            pintadoSim = st.checkbox("SIM", key="pintado_1")
            pintadoNao = st.checkbox("NÃO", key="pintado_2")

            if pintadoSim:
                st.write(diretorio["LINHA COLORVIVE"]["link"])
                st.image(diretorio["LINHA COLORVIVE"]["imagem"])

        if quimicaNao:
            st.write("4. Ele tem frizz?")
            frizzSim = st.checkbox("SIM", key="frizz_1")
            frizzNao = st.checkbox("NÃO", key="frizz_2")

            if frizzSim:
                st.write(diretorio["LINHA SUPREME CONTROL"]["link"])
                st.image(diretorio["LINHA SUPREME CONTROL"]["imagem"])

            elif frizzNao:
                st.write("5. Ele tem queda?")
                quedaSim = st.checkbox("SIM", key="queda_1")
                quedaNao = st.checkbox("NÃO", key="queda_2")

                if quedaSim:
                    st.write(diretorio['LINHA ARGININA']['link'])
                    st.image(diretorio['LINHA ARGININA']['imagem'])

                elif quedaNao:
                    st.write("6. Ele está danificado?")
                    danificadoSim = st.checkbox("SIM", key="danificado_1")
                    danificadoNao = st.checkbox("NÃO", key="danificado_2")

                    if danificadoSim:
                       st.write("6.1 Ele está muito danificado?")
                       superdanificadoSim = st.checkbox("SIM", key="superdanificado_1")
                       superdanificadoNao = st.checkbox("NÃO", key="superdanificado_2")
 
                       if superdanificadoSim:
                          st.write(diretorio['LINHA REPARAÇÃO TOTAL 5 PROFUNDA']['link'])
                          st.image(diretorio['LINHA REPARAÇÃO TOTAL 5 PROFUNDA']['imagem'])

                       elif superdanificadoNao: 
                          st.write(diretorio['LINHA REPARAÇÃO TOTAL 5']['link'])
                          st.image(diretorio['LINHA REPARAÇÃO TOTAL 5']['imagem'])

                    elif danificadoNao:
                       st.write("7. Ele está desidratado?")
                       desidratadoSim = st.checkbox("SIM", key="desidratado_1")
                       desidratadoNao = st.checkbox("NÃO", key="desidratado_2")

                       if desidratadoSim:
                          st.write("7.1 Ele está muito desidratado?")
                          muitodesidratadoSim = st.checkbox("SIM", key="muitodesidratado_1")
                          muitodesidratadoNao = st.checkbox("NÃO", key="muitodesidratado_2")

                          if muitodesidratadoSim:
                              st.write(diretorio['LINHA HIDRA DETOX']['link'])
                              st.image(diretorio['LINHA HIDRA DETOX']['imagem'])

                          elif muitodesidratadoNao:
                              st.write("7.2 Ele é oleoso?")
                              oleosoSim = st.checkbox("SIM", key="tipo_1")
                              oleosoNao = st.checkbox("NÃO", key="tipo_2")

                              if oleosoSim:
                                 st.write(diretorio['LINHA PURE HIALURONICO']['link'])
                                 st.image(diretorio['LINHA PURE HIALURONICO']['imagem'])

                              elif oleosoNao:
                                 st.write("7.3 Seu cabelo é cacheado?")
                                 cabelocacheadoSim = st.checkbox("SIM", key="tipo_1")
                                 cabelocacheadoNao = st.checkbox("NÃO", key="tipo_2")

                                 if cabelocacheadoSim:
                                    st.write(diretorio['LINHA OLEO EXTRAORDINARIO CACHOS']['link'])
                                    st.image(diretorio['LINHA OLEO EXTRAORDINARIO CACHOS']['imagem'])

                                 elif cabelocacheadoNao:
                                    st.write(diretorio['LINHA OLEO EXTRAORDINARIO']['link'])
                                    st.image(diretorio['LINHA OLEO EXTRAORDINARIO']['imagem'])

                       elif desidratadoNao:
                         st.write("8. Seu cabelo é cacheado?")
                         cacheadoSim = st.checkbox("SIM", key="tipo_1")
                         cacheadoNao = st.checkbox("NÃO", key="tipo_2")

                         if cacheadoSim:
                            st.write(diretorio['LINHA CACHOS DOS SONHOS']['link'])
                            st.image(diretorio['LINHA CACHOS DOS SONHOS']['imagem'])

                         elif cacheadoNao:
                            st.write("9. Quer o seu cabelo mais longo")
                            longoSim = st.checkbox("SIM", key="tipo_1")
                            longoNao = st.checkbox("NÃO", key="tipo_2")

                            if longoSim:
                               st.write(diretorio['LINHA LONGO DOS SONHOS']['link'])
                               st.image(diretorio['LINHA LONGO DOS SONHOS']['imagem'])

                            elif longoNao:
                                st.write(diretorio['LINHA LISO DOS SONHOS']['link'])
                                st.image(diretorio['LINHA LISO DOS SONHOS']['imagem'])
