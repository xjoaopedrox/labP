from models.dados_iniciais import reservas

def nova_reserva(nome_hospede, numero_quarto):
    reserva = {
        "hospede": nome_hospede,
        "quarto": numero_quarto
    }
    reservas.append(reserva)
