import streamlit as st

# Título grande
st.title("QUAL LINHA ELSEVE É PERFEITA PARA VOCÊ?")

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

import streamlit as st

def main():
    st.title("QUAL LINHA ELSEVE É PERFEITA PARA VOCÊ?")
    st.write("Bem-vindo(a) ao teste de tipo de cabelo!")

resposta = st.radio("Seu cabelo tem caspa?", ("SIM", "NÃO"))
if resposta == "SIM":
   st.write(diretorio["LINHA HIDRA DETOX CASPA"]['link'])
   st.image(diretorio["LINHA HIDRA DETOX CASPA"]['imagem'])

elif resposta == "NÃO":
    resposta_adicional1 = st.radio("Você quer usar antes da escova?", ("SIM", "NÃO"))
    if resposta_adicional1 == "SIM": 
       st.write(diretorio["LINHA QUERALISO"]['link'])
       st.image(diretorio["LINHA QUERALISO"]['imagem'])
    elif resposta_adicional1 == "NÃO":
         resposta_adicional2 = st.radio("Seu cabelo tem química?", ("SIM", "NÃO"))
         if resposta_adicional2 == "SIM": 
            resposta_adicional3 = st.radio("Ele é pintado?", ("SIM", "NÃO"))
            if resposta_adicional3 == "SIM":
               st.write(diretorio["LINHA COLORVIVE"]['link'])
               st.image(diretorio["LINHA COLORVIVE"]['imagem'])
            elif resposta_adicional3 == "NÃO":
               st.write(diretorio['LINHA REPARAÇÃO TOTAL PÓS QUÍMICA']['link'])
               st.image(diretorio["LINHA REPARAÇÃO TOTAL PÓS QUÍMICA"]['imagem'])
         elif resposta_adicional2 == "NÃO":
               resposta_adicional4 = st.radio("Seu cabelo tem frizz?", ("SIM", "NÃO"))
               if resposta_adicional4 == "SIM":
                  st.write(diretorio['LINHA SUPREME CONTROL']['link'])
                  st.image(diretorio['LINHA SUPREME CONTROL']['imagem'])
               elif resposta_adicional4 == "NÃO":
                    resposta_adicional5 = st.radio("Ele tem queda?", ("SIM", "NÃO"))
                    if resposta_adicional5 == "SIM":
                       st.write(diretorio['LINHA ARGININA']['link'])
                       st.image(diretorio['LINHA ARGININA']['imagem'])
                    elif resposta_adicional5 == "NÃO":
                           resposta_adicional6 = st.radio("Ele está danificado?", ("SIM", "NÃO"))
                           if resposta_adicional6 == 'SIM':
                              resposta_adicional7 = st.radio("Ele está muito ou pouco danificado?", ("MUITO", "POUCO"))
                              if resposta_adicional7 == 'MUITO':
                                 st.write(diretorio['LINHA REPARAÇÃO TOTAL 5 PROFUNDA']['link'])
                                 st.image(diretorio['LINHA REPARAÇÃO TOTAL 5 PROFUNDA']['imagem'])
                              elif resposta_adicional7 == 'POUCO':
                                 st.write(diretorio['LINHA REPARAÇÃO TOTAL 5']['link'])
                                 st.image(diretorio['LINHA REPARAÇÃO TOTAL 5']['imagem'])
                           elif resposta_adicional6 == 'NÃO':
                                resposta_adicional8 = st.radio("Ele está desidratado?", ("SIM", "NÃO"))
                                if resposta_adicional8 == 'SIM':
                                   resposta_adicional9 = st.radio('Muito?' ("SIM", "NÃO"))
                                   if resposta_adicional9 == 'SIM':
                                      st.write(diretorio['LINHA HIALURONICO']['link'])
                                      st.image(diretorio['LINHA HIALURONICO']['imagem'])
                                   elif resposta_adicional9 == 'NÃO':
                                      resposta_adicional10 = st.radio("Qual seu tipo de cabelo?", ("OLEOSO", "MISTO", "SECO"))
                                      if resposta_adicional10 == 'OLEOSO':
                                         st.write(diretorio['LINHA PURE HIALURONICO']['link'])
                                         st.image(diretorio['LINHA PURE HIALURONICO']['imagem'])
                                      elif resposta_adicional10 == 'MISTO':
                                         st.write(diretorio['LINHA DETOX']['link'])
                                         st.image(diretorio['LINHA DETOX']['imagem'])
                                      elif resposta_adicional10 == 'SECO':
                                         resposta_adicional11 = st.radio("Textura do cabelo?", ("LISO", "CACHEADO"))
                                         if resposta_adicional11 == "SECO":
                                             st.write(diretorio['LINHA OLEO EXTRAORDINARIO']['link'])
                                             st.image(diretorio['LINHA OLEO EXTRAORDINARIO']['imagem'])
                                         elif resposta_adicional11 == "CACHEADO":
                                            st.write(diretorio['LINHA OLEO EXTRAORDINARIO CACHOS']['link'])
                                            st.image(diretorio['LINHA OLEO EXTRAORDINARIO CACHOS']['imagem'])
                                elif resposta_adicional8 == "NÃO":
                                     resposta_adicional11 = st.radio("Qual é seu tipo de cabelo?", ("LISO", "CACHEADO"))
                                     if resposta_adicional11 == "LISO":
                                          resposta_adicional12 = st.radio("Quer mais liso ou mais longo?", ("LISO", "LONGO"))     
                                          if resposta_adicional12 == "LISO":
                                             st.write(diretorio['LINHA LISO DOS SONHOS']['link'])
                                             st.image(diretorio['LINHA LISO DOS SONHOS']['imagem'])
                                          elif resposta_adicional12 == 'LONGO':
                                               st.write(diretorio['LINHA LONGO DOS SONHOS']['link'])
                                               st.image(diretorio['LINHA LONGO DOS SONHOS']['imagem'])
                                     elif resposta_adicional11 == "CACHEADO":
                                          st.write(diretorio['LINHA CACHOS DOS SONHOS']['link'])
                                          st.image(diretorio['LINHA CACHOS DOS SONHOS']['imagem'])
