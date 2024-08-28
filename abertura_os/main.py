#import a biblioteca 
import streamlit as st
import oem_1t_ac
import oem_2t_ac_hoppecke
import oem_2t_ac
import oem_2t_mt



st.sidebar.title('Selecione a tranche')
# lista de seleção para seleção de tranche para análise
pages_operation = st.sidebar.selectbox( 'Operações',[
   'O&M 1ª Tranche AC',
   'O&M 2ª Tranche AC',
   'O&M 2ª Tranche AC - Hoppecke',
   'O&M 2ª Tranche MT' 
])

#Aplicar condicional para seleção de tranche
if pages_operation == 'O&M 1ª Tranche AC':
    oem_1t_ac.base_oem_1t_ac()
elif pages_operation == 'O&M 2ª Tranche AC':
    oem_2t_ac.base_oem_2t_ac()
elif pages_operation == 'O&M 2ª Tranche AC - Hoppecke':
    oem_2t_ac_hoppecke.base_oem_2t_ac_hoppecke()
elif pages_operation == 'O&M 2ª Tranche MT':
    oem_2t_mt.base_oem_2t_mt()