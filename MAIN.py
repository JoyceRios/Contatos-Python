import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

conn.commit()
conn.close()
def inserir_contato(nome, email, telefone):
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)', (nome, email, telefone))

    conn.commit()
    conn.close()
def listar_contatos():
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contatos')

    contatos = cursor.fetchall()

    conn.close()

    return contatos
def buscar_contato(nome):
    conn = sqlite3.connect('contatos.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contatos WHERE nome LIKE ?', (f'%{nome}%',))

    contato = cursor.fetchone()

    conn.close()

    return contato
opcao = ''

while opcao != '4':
    print('1 - Inserir novo contato')
    print('2 - Listar contatos')
    print('3 - Buscar contato por nome')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        email = input('Digite o email do contato: ')
        telefone = input('Digite o telefone do contato: ')

        inserir_contato(nome, email, telefone)

    elif opcao == '2':
        contatos = listar_contatos()

        for contato in contatos:
            print(f'{contato[0]} - {contato[1]} ({contato[2]}) - {contato[3]}')

    elif opcao == '3':
        nome = input('Digite o nome do contato: ')

        contato = buscar_contato(nome)

        if contato:
            print(f'{contato[0]} - {contato[1]} ({contato[2]}) - {contato[3]}')
    else:
        print('Contato não encontrado.')

