import streamlit as st
import datetime
from PIL import Image
import smtplib
import email.message

st.set_page_config(
    page_title="Agendamento",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================================================================================
# importando os dados

#image = Image.open('timac2.png')
#st.sidebar.image(image)


# Sider Bar=============================================================================================================
st.sidebar.markdown('## Menu:')
menu = st.sidebar.radio(
    "Selecione:",
    ('Inicio', 'Vendas', 'Agendamento'))

# Config Menu ==========================================================================================================
if menu == 'Inicio':
    st.title('Análises Inteligência de Mercado\n')
    st.write(
        'Nesse projeto vamos analisar varios indicadores com objetivo e melhorar o resultad da nossa equipe.')
    st.markdown('## Informações Importantes:')
    st.info('Data para Alocações sempre até dia 25 de todos os meses.')
    st.info('CTC tem até 3 dias (incluindo finais de semana) para lançar as visitas passadas.')



if menu == 'Vendas':
    st.title('Teste Vendas')


if menu == 'Agendamento':

    st.title('\n\nAgende sua consulta\n\n\n\n')
    nome = st.text_input("Nome Completo")
    e = st.text_input("E-mail")
    option = st.selectbox(
        'Deseja agendar para qual especialidade?',
        ('Cardio', 'Terapia', 'Para bebes'))

    st.write('Você escolheu:', option)

    d = st.date_input(
        "Selecione para que data deseja agendar",
        datetime.date(2023, 1, 1))
    st.write('Data escolhida:', d)

    t = st.time_input('Escolha um dos Horarios disponiveis', datetime.time(8, 45))
    st.write('Horario escolhido', t)

    if st.button('Confirmar agendamento'):
        st.write('CONFIRMADO!')


        def enviar_email():
            corpo_email = f"""
            <p>Olá {nome}, confirmamos seu agendamento para {option}!</p>
            <p>Será no dia: {d}</p>
            <p>No Horario: {t}</p>
            """

            msg = email.message.Message()
            msg['Subject'] = "Confirmação de Agendamento"
            msg['From'] = 'helionsc.work@gmail.com'
            msg['To'] = f'{e}'
            password = 'xyjpqhveoymisapx'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


        enviar_email()

    else:
        st.write('Aguardando confirmação')
