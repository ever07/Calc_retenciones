#Calculadora de retenciones
import streamlit as st

def app():
    #titulo
    st.title("Calculadora de Salarios y deducciones")

    #ingreso del salario
    salario = st.number_input("Ingresa tu salario Mensual")

    st.info("DEDUCCIONES MENSUALES")

    #calcular afp empleado
    st.subheader("AFP Empleado:")
    st.text("El descuento de AFP es igual al 7.25% de tu salario.")
    afp_emp = round(salario * (7.25/100),2)
    st.text(f"$ {afp_emp}")

    #calcular afp patronal
    st.subheader("AFP Patronal:")
    st.text("Aporte a AFP hecho por tu empleador, equivale al 8.75% de tu salario mensual,"
            "esta cantidad no se resta del monto que recibirás a final de mes (Art. 16. Ley Integral Del Sistema de Pensiones).")
    afp_pat = round(salario * (8.75/100),2)
    st.text(f"$ {afp_pat}")

    #calcular isss empleado
    st.subheader("ISSS Empleado:")
    st.text("El descuento de ISSS es igual al 3% de tu salario, con un techo de $30 mensuales.")
    isss_emp = round(salario * (3/100),2)
    if salario < 1000:
        st.text(f"$ {isss_emp}")
    else:
        st.text("$ 30.00")

    #calcular isss patronal
    st.subheader("ISSS Patronal:")
    st.text("Aporte a ISSS hecho por tu empleador, equivale al 7.5% de tu salario mensual,"
            "esta cantidad no se resta del monto que recibirás a final de mes.")
    isss_pat = round(salario * (7.5/100),2)
    st.text(f"$ {isss_pat}")

    #calculo de renta
    st.subheader("RENTA:")
    menosDeducciones = salario - afp_emp - isss_emp
    tramo = 0

    if menosDeducciones > 0.1 and menosDeducciones <= 472.00:
        st.text(f"$ {tramo}")
    elif menosDeducciones >= 472.01 and menosDeducciones <= 895.24:
        tramo = 17.67 + (menosDeducciones - 472.00) * 0.1
        st.text(f"$ {tramo}")
    elif menosDeducciones >= 895.25 and menosDeducciones <= 2038.10:
        tramo = 60 + (menosDeducciones - 895.24) * 0.2
        st.text(f"$ {tramo}")
    elif menosDeducciones >= 2038.11 and menosDeducciones <= 1000000000:
        tramo = 288.57 + (menosDeducciones - 2038.10) * 0.3
        st.text(f"$ {tramo}")

    #Descuentos totales
    st.subheader("DESCUENTOS TOTALES")
    descuentos = round(afp_emp + isss_emp + tramo,2)
    st.text(f"$ {descuentos}")

    #salario liquido mensual
    salario_liq = salario - descuentos
    st.subheader("SALARIO LIQUIDO MENSUAL")
    st.header(f"$ {salario_liq}")


    st.success("DEDUCCIONES QUINCENALES")

    salario_q = round(salario / 2, 2)

    #calcular afp empleado
    st.subheader("AFP Empleado:")
    st.text("El descuento de AFP es igual al 7.25% de tu salario.")
    afp_emp_q = round(salario_q * (7.25/100),2)
    st.text(f"$ {afp_emp_q}")

    #calcular afp patronal
    st.subheader("AFP Patronal:")
    st.text("Aporte a AFP hecho por tu empleador, equivale al 8.75% de tu salario mensual,"
            "esta cantidad no se resta del monto que recibirás a final de mes (Art. 16. Ley Integral Del Sistema de Pensiones).")
    afp_pat_q = round(salario_q * (8.75/100),2)
    st.text(f"$ {afp_pat_q}")

    #calcular isss empleado
    st.subheader("ISSS Empleado:")
    st.text("El descuento de ISSS es igual al 3% de tu salario, con un techo de $30 mensuales.")
    isss_emp_q = round(salario_q * (3/100),2)
    if salario_q < 500:
        st.text(f"$ {isss_emp_q}")
    else:
        st.text("$ 15.00")

    #calcular isss patronal
    st.subheader("ISSS Patronal:")
    st.text("Aporte a ISSS hecho por tu empleador, equivale al 7.5% de tu salario mensual,"
            "esta cantidad no se resta del monto que recibirás a final de mes.")
    isss_pat_q = round(salario_q * (7.5/100),2)
    st.text(f"$ {isss_pat_q}")

    #calculo de renta
    st.subheader("RENTA QUINCENAL:")
    menosDeducciones_q = salario_q - afp_emp_q - isss_emp_q
    tramo_q = 0

    if menosDeducciones_q > 0.1 and menosDeducciones_q <= 236.00:
        st.text(f"$ {tramo_q}")
    elif menosDeducciones_q >= 236.01 and menosDeducciones_q <= 447.62:
        tramo_q = 8.83 + (menosDeducciones_q - 236.00) * 0.1
        st.text(f"$ {round(tramo_q,2)}")
    elif menosDeducciones_q >= 447.63 and menosDeducciones_q <= 1019.05:
        tramo_q = 30 + (menosDeducciones_q - 447.62) * 0.2
        st.text(f"$ {round(tramo_q,2)}")
    elif menosDeducciones_q >= 1019.06 and menosDeducciones_q <= 1000000000:
        tramo_q = 144.28 + (menosDeducciones_q - 1019.05) * 0.3
        st.text(f"$ {round(tramo_q,2)}")

    #Descuentos totales
    st.subheader("DESCUENTOS TOTALES QUINCENAL")
    descuentos_q = round(afp_emp_q + isss_emp_q + tramo_q,2)
    st.text(f"$ {descuentos_q}")

    #salario liquido mensual
    salario_liq_q = salario_q - descuentos_q
    st.subheader("SALARIO LIQUIDO QUINCENAL")
    st.header(f"$ {salario_liq_q}")


app()