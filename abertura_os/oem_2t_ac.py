import streamlit as st  
import pandas as pd
import plotly.express as px

def base_oem_2t_ac():
    st.title("O&M 2ª Tranche Acre")
    
    @st.cache_data
    def reader_data():
       """Lê a planilha informada"""
       del_rota = [599,600]
       bd = pd.read_excel(r"C:\Users\OneEngInst\Projetos_python\dashboard\content\base_sip_Concluido.xlsx")
       bd = bd[bd.ROTA.isin(del_rota) == False]
       bd = bd.loc[(bd['IDORIGEM'].isin([2]))]
       bd = bd.loc[(bd['ROTA'].isin([14,15,16,17,21,22,23,24]))]
       bd = bd.loc[(bd['STATUSSRV'].isin([1,2,3,4,6]))]
       bd = bd.loc[(bd['IDTIPOMANUTENCAO'].isin([4]))]
       bd[['IDSIGFI', 'UC', 'ROTA', 'NUMOS']] = bd[['IDSIGFI', 'UC', 'ROTA', 'NUMOS']].astype(str)
       bd = bd[['IDSIGFI','UC','NOMECLIENTE','ROTA','NUMOS','STATUS','LATLONCON','MUNICIPIO', 'ENDERECO','DTCONCLUSAO']] 
       return bd
    
    @st.cache_data
    def reader_data_ins():
         """Lê a planilha de instalações"""
         del_status = ['TREINAMENTO','TREINAMENTO','CANCELADO','CANCELADO         ','DUPLICADOS']
         del_rota = [599,600]
         bd_ins = pd.read_excel(r"C:\Users\OneEngInst\Projetos_python\dashboard\content\base_sip_instalacoes_Geral_ac.xlsx")
         bd_ins = bd_ins[~bd_ins.ROTA.isin(del_rota)]
         bd_ins = bd_ins[~bd_ins.STATUS.isin(del_status)]
         bd_ins = bd_ins.loc[(bd_ins['TIPO'] == 'INS')]
         bd_ins = bd_ins.loc[(bd_ins['IDEMPRESA'].isin([1]))]
         bd_ins = bd_ins.loc[(bd_ins['ROTA'].isin([14,15,16,17,21,22,23,24]))]
         bd_ins = bd_ins.loc[(bd_ins['ETAPA'].isin([3]))]
         bd_ins['IDSERVICOSCONJ'] = bd_ins['IDSERVICOSCONJ'].astype(str)
         bd_ins = bd_ins[['IDSERVICOSCONJ','CODIGOENERGISA','NOMEDOCLIENTE','ROTA','MUNICIPIO', 'ENDERECO','CONCLUSAO','LATITUDE',
                            'LONGITUDE']]
         return bd_ins
   
     # Lê os dados
    bd = reader_data()
    bd_ins = reader_data_ins()
    count_bd = bd['NUMOS'].count()
    count_bdins = bd_ins['IDSERVICOSCONJ'].count()

    # Apresenta as tabelas
    st.subheader("Tabela de Conclusões")
    st.dataframe(bd)

    st.subheader("Tabela de Instalações")
    st.dataframe(bd_ins)
    st.subheader("Quantidade de execuções O&M 1ª Tranche Acre")
    st.write(count_bd)
    st.subheader("Quantidade de Instalações")
    st.write(count_bdins)

# Chama a função principal
if __name__ == "__main__":
    base_oem_2t_ac()