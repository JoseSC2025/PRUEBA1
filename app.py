import streamlit as st
from preguntas import preguntas

st.set_page_config(page_title="Aprende Python", layout="centered")

st.title("💡 Aprende Python: Bucles y Condicionales")
st.markdown("""
Este mini curso te enseña cómo usar `while`, `for` e `if` en Python.  
Lee cada explicación, luego responde el quiz al final.
""")

with st.expander("📘 ¿Cómo funciona un bucle while?"):
    st.markdown("El bucle `while` ejecuta su bloque **mientras la condición sea verdadera**.")
    st.code("""
i = 0
while i < 5:
    print(i)
    i += 1
""")

with st.expander("📗 ¿Cómo funciona un bucle for?"):
    st.markdown("El bucle `for` repite un bloque **para cada valor de una secuencia**.")
    st.code("""
for i in range(5):
    print(i)
""")

with st.expander("📙 ¿Cómo funciona una condición if?"):
    st.markdown("`if` evalúa una condición y ejecuta un bloque si es verdadera.")
    st.code("""
x = 10
if x > 5:
    print("Mayor que 5")
""")

st.header("📝 Quiz interactivo")

respuestas_usuario = []
for idx, q in enumerate(preguntas):
    st.subheader(f"Pregunta {idx+1}: {q['pregunta']}")
    opcion = st.radio("Selecciona una respuesta:", q["opciones"], key=f"q{idx}")
    respuestas_usuario.append(opcion)

if st.button("Ver puntaje"):
    puntaje = 0
    for r, q in zip(respuestas_usuario, preguntas):
        if r == q["respuesta"]:
            puntaje += 1
    st.success(f"Obtuviste {puntaje} de 10 puntos.")
    
    if puntaje == 10:
        st.balloons()
    elif puntaje >= 7:
        st.info("¡Buen trabajo! Sigue practicando.")
    else:
        st.warning("Puedes hacerlo mejor. Revisa los conceptos.")

