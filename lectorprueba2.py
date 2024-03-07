import fitz
import re
# READING THE STATEMENT OF ACCOUNT IN PDF

# Open the PDF
doc = fitz.open("efaa312e00e67c18969cfbab164e7e4b.pdf")

# List for storing final data
datos_finales_lista = []

# Iterate on each document page
for page_num in range(doc.page_count):
    page = doc[page_num]

    # Get page text
    text = page.get_text()
    print(text)
    print(type(text))

    # Define patterns with more flexible regular expressions
    patron_intereses = re.compile(r"Intereses[^\d]*([\d,]+[.\d]+)")
    # patron_iva = re.compile(r"IVA de Intereses[^\d]*([\d,]+[.\d]+)")
    patron_comisiones = re.compile(r"Comisión[^\d]*([\d,]+[.\d]+)") # VERIFICAR
    # patron_iva_comision = re.compile(r"IVA Comisión[^\d]*([\d,]+[.\d]+)")

    # Search for matches with patterns
    match_intereses = patron_intereses.findall(text)
    # match_iva = patron_iva.search(text)
    match_comisiones = patron_comisiones.findall(text)
    # match_iva_comision = patron_iva_comision.search(text)

    # Debugging: Print page text and regular expression results
    # print(f"Texto de la página {page_num + 1}:\n{text}")
    print(f"Match Intereses: {match_intereses}")
    # print(f"Match IVA: {match_iva}")
    print(f"Comisiones: {match_comisiones}")

    # Process the interest amount
    if match_intereses:
        monto_intereses = float(match_intereses[1].replace(",", ""))
    else:
        monto_intereses = 0.0

    if match_intereses:
        monto_iva_intereses = float(match_intereses[2].replace(",", ""))
    else:
        monto_iva_intereses = 0.0
    
    if match_intereses:
        monto_intereses_moratorios = float(match_intereses[3].replace(",",""))
    else:
        monto_intereses_moratorios = 0.0
    
    if match_intereses:
        monto_iva_interes_moratorio = float(match_intereses[4].replace(",",""))
    else:
        monto_iva_interes_moratorio = 0.0
    
    # Process the commission amount
    if match_comisiones:
        monto_comision = float(match_comisiones[1].replace(",", ""))
    else:
        monto_comisiones = 0.0
    
    if match_comisiones:
        monto_iva_comision = float(match_comisiones[2].replace(",", ""))
    else:
        monto_iva_comisiones = 0.0
    
    '''
    # Process the amount of IVA commissions
    if match_iva_comision:
        monto_iva_comision = float(match_iva_comision.group(1).replace(",", ""))
    else:
        monto_iva_comision = 0.0
    '''

    # Storing final data in a dictionary
    datos_finales = {
        'intereses': monto_intereses,
        'IVA de interes': monto_iva_intereses,
    
        # **** TO DO (confirm payment intereses moratorios) ****
        #'Intereses moratorios': monto_intereses_moratorios,
        #'IVA de intereses moratorios': monto_iva_interes_moratorio,
        
        'Comision': monto_comision,
        'IVA comision': monto_iva_comision
        
        }
    datos_finales_lista.append(datos_finales)

# Print final data:
for datos in datos_finales_lista:
    print(datos)
