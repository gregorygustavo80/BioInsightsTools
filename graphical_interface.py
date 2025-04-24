import streamlit as st
from Bio.Seq import Seq
from Bio import pairwise2
from Bio.Align import substitution_matrices
from Bio.SeqUtils import gc_fraction 
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide")
base="dark"

st.sidebar.title("Opções")

option = st.sidebar.selectbox("Escolha uma opção", ["Selecione...", "Alinhamento BLOSUM62", "Alinhamento PAM250", "Alinhamento de DNA", "Converter DNA para Proteína","Primer Check"])

if option == "Selecione...":
   imagem = Image.open('imagem.png')
   buffer = BytesIO()
   imagem.save(buffer, format="PNG")  
   img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
   
   st.markdown(

        f"""
        <div style="text-align: center;">
        <img src="data:image/png;base64,{img_str}" width="450"/>
        </div>
        """,
        unsafe_allow_html=True
        )

if option == "Alinhamento BLOSUM62":# Título

    st.header(" Matriz BLOSUM62")

    seq1 = st.text_area('Digite a primeira sequência: ').strip().upper()
    seq2 = st.text_area('Digite a segunda sequência: ').strip().upper()

    def alignG(seq1, seq2):
        matrizBlossum = substitution_matrices.load('BLOSUM62')
        alignments = pairwise2.align.globaldx(seq1, seq2, matrizBlossum)
        st.text(pairwise2.format_alignment(*alignments[0]))
        return alignments[0]

    def alignL(seq1, seq2):
        matrizBlossum = substitution_matrices.load('BLOSUM62')
        alignments = pairwise2.align.localdx(seq1, seq2, matrizBlossum)
        st.text(pairwise2.format_alignment(*alignments[0]))
        return alignments[0]

    colG, colL = st.columns([1, 2])

    with colG:
        if st.button('Alinhamento Global'):
            with st.spinner('Carregando...'):
                alinhamento = alignG(seq1, seq2)
                st.success('Operação concluída com sucesso!')

                st.download_button(
                    label="Baixar Resultado",
                    data=str(alinhamento),
                    file_name="AlighGBlosum62.txt",
                    mime="text/plain"
                    )

        with colL:
            if st.button('Alinhamento Local'):
                with st.spinner('Carregando...'):
                    alinhamento = alignL(seq1, seq2)
                    st.success('Operação concluída com sucesso!')

                    st.download_button(
                        label="Baixar Resultado",
                        data=str(alinhamento),
                        file_name="AlighLBlosum62.txt",
                        mime="text/plain"
                    )

elif option == "Alinhamento PAM250":

        st.header("Matriz PAM250")

        seq1 = st.text_area('Digite a primeira sequência:  ').strip().upper()
        seq2 = st.text_area('Digite a segunda sequência:  ').strip().upper()

        def alignG(seq1, seq2):
            matrizPAM = substitution_matrices.load('PAM250')
            alignments = pairwise2.align.globaldx(seq1, seq2, matrizPAM)
            st.text(pairwise2.format_alignment(*alignments[0]))
            return alignments[0]

        def alignL(seq1, seq2):
            matrizPAM = substitution_matrices.load('PAM250')
            alignments = pairwise2.align.localdx(seq1, seq2, matrizPAM)
            st.text(pairwise2.format_alignment(*alignments[0]))
            return alignments[0]

        colG, colL = st.columns([1, 2])

        with colG:
            if st.button('Alinhamento Global  '):
                with st.spinner('Carregando...'):
                    alinhamento = alignG(seq1, seq2)
                    st.success('Operação concluída com sucesso!')

                    st.download_button(
                        label="Baixar Resultado",
                        data=str(alinhamento),
                        file_name="AlignGPAM250.txt",
                        mime="text/plain"
                    )

        with colL:
            if st.button('Alinhamento Local   '):
                with st.spinner('Carregando...'):
                    alinhamento = alignL(seq1, seq2)
                    st.success('Operação concluída com sucesso!')

                    st.download_button(
                        label="Baixar Resultado",
                        data=str(alinhamento),
                        file_name="AlignLPAM250.txt",
                        mime="text/plain"
                    )

elif option == "Alinhamento de DNA":

    st.header("Alinhamento de DNA")
    
    # Caixa de texto 
    seq1 = st.text_area('Insira a primeira sequência de bases para alinhamento: ').strip().upper()
    seq2 = st.text_area('Insira a segunda sequência de bases para alinhamento: ').strip().upper()

    def alignG(seq1, seq2):
        alignseq = pairwise2.align.globalms(seq1, seq2, 5, -4, -2, -0.5)
        st.text(pairwise2.format_alignment(*alignseq[0])) 
        return alignseq[0]

    def alignL(seq1, seq2):
        alignseq = pairwise2.align.localms(seq1, seq2, 5, -4, -2, -0.5)
        st.text(pairwise2.format_alignment(*alignseq[0])) 
        return alignseq[0]
       
    colG, colL = st.columns([1, 2])

    with colG:
        if st.button('Alinhamento Global'):
            with st.spinner('Carregando...'):
                alinhamento = alignG(seq1, seq2)
                st.success('Operação concluída com sucesso!')

                st.download_button(
                    label="Baixar Resultado",
                    data=str(alinhamento),
                    file_name="AlignG.txt",
                    mime="text/plain"
                )

    with colL:
        if st.button('Alinhamento Local'):
            with st.spinner('Carregando...'):
                alinhamento = alignL(seq1, seq2)
                st.success('Operação concluída com sucesso!')

                st.download_button(
                    label="Baixar Resultado",
                    data=str(alinhamento),
                    file_name="AlignL.txt",
                    mime="text/plain"
                )

elif option == "Converter DNA para Proteína":
    st.header("Transformar DNA em Proteína")

    def dna_prot(sequence):
        def ajustar_sequencia(sequence):
            resto = len(sequence) % 3
            if resto != 0:
                sequence = sequence[:-resto]
            return sequence

        seq_ajustada = ajustar_sequencia(sequence)
        dnaM = Seq(seq_ajustada)
        RNAm = dnaM.transcribe()
        prot = RNAm.translate()

        st.text(f'Gene: {seq}')
        st.text(f'RNAm:{RNAm}')
        st.text(f'Proteína: {prot}')

        st.text(' * = códon de parada')
        return seq, RNAm, prot
        

    seq = st.text_area('Insira a sequência de bases: ').strip().upper()

    if st.button('Converter DNA para Proteína'):
        with st.spinner('Carregando'):
            info = dna_prot(seq)
            st.success('Operação concluída com sucesso!')
    
            st.download_button(
                label="Baixar Proteína",
                data=(f'Sequência: {info[0]}\nRNAm: {info[1]}\nProteína: {info[2]}'),
                file_name="proteina.txt",
                mime="text/plain"
            )
     
elif option == "Primer Check":

    st.header("Verifique a qualidade do seu Primer")
    sequence = st.text_area('Insira a sequência: ').strip().upper()

    def analisar_primer(sequence):
        Tamanho = len(sequence)
        gc = gc_fraction(sequence) * 100
        at = 100 - gc

        num_g = sequence.count('G')
        num_c = sequence.count('C')
        num_a = sequence.count('A')
        num_t = sequence.count('T')
        
        tm = 4 * (num_g + num_c) + 2 * (num_a + num_t)

        st.write(f'Tamanho: {Tamanho}')
        st.write(f'Proporção GC: {gc:.1f}%')
        st.write(f'Proporção AT: {at:.1f}%')
        st.write(f'Temperatura de melting (Tm): {tm} °C')
        
        return sequence, Tamanho, gc, at, tm

    if st.button('Verificar'):
        if sequence:
            with st.spinner('Carregando'):
                seq_info = analisar_primer(sequence)
                st.success('Operação concluída com sucesso!')
            
                st.download_button(
                    label="Baixar Informações",
                    data=f"Sequência: {seq_info[0]}\nTamanho: {seq_info[1]}\nProporção GC: {seq_info[2]:.1f}%\nProporção AT: {seq_info[3]:.1f}%\nTemperatura de melting (Tm): {seq_info[4]} °C",
                    file_name="informacoes_primer.txt",
                    mime="text/plain"
                )
        else:
            st.error("Por favor, insira uma sequência de primer.")



