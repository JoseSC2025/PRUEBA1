import streamlit as st

st.set_page_config(page_title="Quiz de Python", layout="centered")
st.title("🐍 Quiz de Sintaxis de Python")
st.subheader("Responde las siguientes preguntas:")

# Preguntas y respuestas correctas
preguntas = [
    {
        "pregunta": "¿Cuál es la sintaxis correcta para definir una función en Python?",
        "opciones": ["func myFunction():", "def myFunction():", "function myFunction():"],
        "respuesta": "def myFunction():"
    },
    {
        "pregunta": "¿Cómo se accede al tercer elemento de una lista llamada `mi_lista`?",
        "opciones": ["mi_lista[2]", "mi_lista(3)", "mi_lista[3]"],
        "respuesta": "mi_lista[2]"
    },
    {
        "pregunta": "¿Cuál es la estructura correcta de un bucle `for` en Python?",
        "opciones": ["for x in range(5)", "foreach x in range(5)", "for x = 1 to 5"],
        "respuesta": "for x in range(5)"
    },
    {
        "pregunta": "¿Qué hace la instrucción `if`?",
        "opciones": ["Ejecuta código si una condición es verdadera", "Repite una instrucción", "Define una función"],
        "respuesta": "Ejecuta código si una condición es verdadera"
    },
    {
        "pregunta": "¿Cuál de las siguientes líneas añade un elemento a una lista?",
        "opciones": ["lista.add('hola')", "lista.append('hola')", "lista.insert('hola')"],
        "respuesta": "lista.append('hola')"
    }
]

respuestas_usuario = []

# Mostrar preguntas
for i, item in enumerate(preguntas):
    st.markdown(f"**{i + 1}. {item['pregunta']}**")
    respuesta = st.radio(
        label="Selecciona una opción:",
        options=item["opciones"],
        key=f"pregunta_{i}"
    )
    respuestas_usuario.append(respuesta)

# Botón para verificar respuestas
if st.button("Verificar mis respuestas"):
    puntaje = 0
    for i, respuesta in enumerate(respuestas_usuario):
        if respuesta == preguntas[i]["respuesta"]:
            puntaje += 1

    st.markdown(f"### ✅ Obtuviste **{puntaje} de 5** respuestas correctas.")

    if puntaje == 5:
        st.balloons()
        st.success("🎉 ¡Excelente! Respondiste todo correctamente.")
    elif puntaje >= 3:
        st.info("👍 Buen trabajo. ¡Sigue practicando!")
    else:
        st.warning("📘 Sigue repasando. Puedes hacerlo mejor.")
