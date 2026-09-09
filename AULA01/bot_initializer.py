BOT_NAME = "RPA_FINANCEIRO_01"
MAX_RETRIES = 3
EXECUTION_TIMEOUT = 45.5
IS_PRODUCTION = False

print(f"--- Inicializando Robô ---")
print(f"Nome do Robô: {BOT_NAME} | Tipo: {type(BOT_NAME)}")
print(f"Tentativas Máximas: {MAX_RETRIES} | Tipo: {type(MAX_RETRIES)}")
print(f"Timeout de Execução: {EXECUTION_TIMEOUT}s | Tipo: {type(EXECUTION_TIMEOUT)}")
print(f"Ambiente de Produção: {IS_PRODUCTION} | Tipo: {type(IS_PRODUCTION)}")
