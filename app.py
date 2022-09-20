from cgitb import text
import streamlit as st
import json
from streamlit_lottie import st_lottie

# from PIL import Image \ Importar imagens
# var = Image.open('diretório')
# st.image(var)

# Função p/ request de animação local

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Animações

lottieAnimation1 = load_lottiefile('C:\\Users\\heito\\OneDrive\\Área de Trabalho\\VSCode\\portfolioPage\\visualFiles\Anim1.json')
lottieAnimation2 = load_lottiefile('C:\\Users\\heito\\OneDrive\\Área de Trabalho\\VSCode\\portfolioPage\\visualFiles\Anim2.json')

st.set_page_config(page_title='Meu Projeto', page_icon=':mortar_board:', layout='wide')

# Load css

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Cabeçalho

with st.container():
    st.subheader('Oi, meu nome é Heitor Fidelis! :hatching_chick:')
    st.title('Estudante de tecnologia :computer: | Brasil - PE :sunny:')
    st.write('UPE - Universidade de Pernambuco')
    st.write('Engenharia Elétrica de Telecomunicações')
    linkedin = '[LinkedIn](https://www.linkedin.com/in/hfidelis/)'
    gitHub = '[GitHub](https://github.com/hfidelis)'
    st.write(linkedin)
    st.write(gitHub)

# Descrição

with st.container():
    st.write('---') # Linha divisória
    l_column, r_column = st.columns(2) # Parâmetro '2' tamanho das colunas
    with l_column:
        st.header('Lorem ipsum :wrench:')
        st.write('##')
        st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ut justo malesuada, dignissim lacus egestas, pretium nisl. Donec quis lorem lacinia, volutpat est sed, vehicula nulla. Sed sodales ullamcorper pellentesque. Quisque in malesuada massa. Aliquam erat volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean tincidunt dui nec tortor ultricies, quis commodo metus vulputate. Fusce scelerisque, nunc nec porttitor porta, enim leo auctor augue, at porttitor tortor lorem id magna. Praesent viverra est quis erat luctus vehicula. Morbi ipsum velit, euismod at commodo ac, varius a justo. Proin sollicitudin efficitur nisi vitae sollicitudin. Curabitur ac leo et leo feugiat viverra. Integer in nisi a metus lacinia eleifend et vel mauris. Nulla dignissim sem finibus lectus viverra pretium. Curabitur pretium lacus fermentum, lacinia est vel, dictum nibh. In auctor ullamcorper aliquet.')
    with r_column:
        st_lottie(lottieAnimation1, height=400, quality='high', key='Animação_1')
        
# Bio 2

with st.container():
    st.write('---') # Linha divisória
    st.header('Minha Bio :bow:')
    st.write('##') # Espaço em branco
    pic_column, text_column = st.columns((0.5, 1.5))
    with pic_column:
        st_lottie(lottieAnimation2, quality='high', height=250, key='Animação_2')
    with text_column:
        st.subheader('Lorem Ipsum')
        st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ut justo malesuada, dignissim lacus egestas, pretium nisl. Donec quis lorem lacinia, volutpat est sed, vehicula nulla. Sed sodales ullamcorper pellentesque. Quisque in malesuada massa. Aliquam erat volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean tincidunt dui nec tortor ultricies, quis commodo metus vulputate. Fusce scelerisque, nunc nec porttitor porta, enim leo auctor augue, at porttitor tortor lorem id magna. Praesent viverra est quis erat luctus vehicula. Morbi ipsum velit, euismod at commodo ac, varius a justo. Proin sollicitudin efficitur nisi vitae sollicitudin. Curabitur ac leo et leo feugiat viverra. Integer in nisi a metus lacinia eleifend et vel mauris. Nulla dignissim sem finibus lectus viverra pretium. Curabitur pretium lacus fermentum, lacinia est vel, dictum nibh. In auctor ullamcorper aliquet.')
        
# Contato 

with st.container():
    st.write('---')
    st.header('Entre em contato comigo! :smiley_cat:')
    st.write('###')
    
    # formsubmit.co \ Contatos
    contact = """ <form action="https://formsubmit.co/heitorc88@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Seu nome" required>
     <input type="email" name="email" placeholder="Seu e-mail" required>
     <textarea name="mensagem" placeholder="Sua mensagem" required></textarea>
     <button type="submit">Enviar</button>
    </form> """
    
    l_column2, r_column2 = st.columns(2)
    with l_column2:
        st.markdown(contact, unsafe_allow_html=True)
        st.write('---')
    with r_column2:
        st.empty()
