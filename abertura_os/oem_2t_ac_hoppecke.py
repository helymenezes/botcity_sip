import streamlit as st  
import pandas as pd
import plotly.express as px

def base_oem_2t_ac_hoppecke():
    st.title("O&M 2ª Tranche Acre Hoppecke")
    
    @st.cache_data
    def reeder_data():
       """Lê a planilha informada"""
       del_status = ['TREINAMENTO','TREINAMENTO','CANCELADOS','DUPLICADOS']
       del_rota = [599,600]
       bd = pd.read_excel(r"C:\Users\OneEngInst\Projetos_python\dashboard\content\base_sip_Concluido.xlsx")
       bd = bd[bd.ROTA.isin(del_rota) == False]
       bd = bd[bd.STATUS.isin(del_status) == False]
       return bd
   
    bd = reeder_data()
    st.dataframe(bd)