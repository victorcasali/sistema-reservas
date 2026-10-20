# Planejamento: Sistema de Reservas do Sabor da Esquina

## Problema

O dono do restaurante controla as reservas num caderno. Isso gerou três problemas:

1. Duas famílias foram reservadas para a mesma mesa, no mesmo dia e horário.
2. Uma reserva de 8 pessoas foi aceita numa mesa de 4 lugares.
3. Para cancelar uma reserva, ele perde tempo procurando o nome no caderno.

O sistema deve impedir os dois primeiros erros e tornar a busca e o cancelamento rápidos.

---

## 1. O que o sistema precisa guardar

O sistema guarda três fichas: **Mesa**, **Cliente** e **Reserva**. A Reserva junta as outras duas, dizendo *quem* reservou, *qual mesa*, *quando* e *para quantas pessoas*.

### Mesa
- número da mesa (identifica a mesa; não se repete)
- quantidade de lugares (capacidade máxima)

### Cliente
- nome
- telefone (para contato, caso seja preciso avisar algo)

### Reserva
- número da reserva (gerado automaticamente pelo sistema, em ordem crescente; serve para editar ou cancelar com facilidade)
- cliente (quem fez a reserva)
- mesa (qual mesa foi reservada)
- data (data completa, por exemplo 25/10/2026, e não só o dia da semana)
- horário (um dos horários pré-estabelecidos)
- quantidade de pessoas (necessária para conferir se cabe na mesa)

---

## 2. Regras que o sistema precisa garantir

Cada regra pode ser respondida com sim ou não.

1. **Sem conflito:** não pode existir duas reservas com a mesma **mesa + data + horário**.
2. **Capacidade:** a quantidade de pessoas da reserva não pode ser maior que a quantidade de lugares da mesa.
3. **Mesa existente:** só é possível reservar uma mesa que esteja cadastrada.
4. **Horário válido:** só é possível reservar nos horários pré-estabelecidos.
5. **Data válida:** não é possível reservar para uma data que já passou.
6. **Número único:** o número da reserva é gerado pelo sistema, nunca se repete e não pode ser digitado à mão.
7. **Reserva existente:** só é possível editar ou cancelar um número de reserva que exista.
8. **Edição segura:** ao editar uma reserva (mesa, data, horário ou pessoas), as regras 1 a 5 são conferidas de novo.
9. **Dados obrigatórios:** nome e telefone do cliente são obrigatórios para criar uma reserva.

---

## 3. O que o dono do restaurante precisa conseguir fazer

- Cadastrar uma mesa (número e quantidade de lugares)
- Listar as mesas cadastradas
- Criar uma reserva
- Ver as reservas de um dia, ordenadas por horário
- Buscar uma reserva pelo número
- Buscar reservas pelo nome do cliente
- Editar uma reserva
- Cancelar uma reserva (a reserva é removida e a mesa fica livre)
- Ver quais mesas estão livres numa data e horário

---

## Decisões tomadas

- **Horários pré-estabelecidos:** o restaurante trabalha com uma lista fixa de horários (exemplo a ajustar: 12:00, 19:00, 20:00, 21:00). Isso simplifica a checagem de conflito.
- **Duração da reserva:** nesta versão, uma reserva ocupa a mesa apenas no horário escolhido. O controle de quanto tempo a mesa fica ocupada fica para uma versão futura.
- **Data completa:** guardamos a data inteira, e não só o dia da semana, para que "sábado dia 25" e "sábado dia 1º" não conflitem entre si.
- **Cancelar remove:** cancelar apaga a reserva. Guardar histórico de reservas canceladas fica para uma versão futura.
- **Número da reserva:** cresce em ordem de criação, o que também mostra a ordem de chegada dos pedidos.

## Fora do escopo desta versão

- Duração da reserva e liberação automática da mesa
- Prioridade entre reservas
- Histórico de reservas canceladas
- Interface gráfica (a versão 1 roda no terminal)
- Consulta de endereço do cliente por CEP (ideia para depois, para praticar API)