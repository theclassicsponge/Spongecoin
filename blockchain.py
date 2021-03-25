blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(value, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value
    to the blockchain

    Arguments:
        :value: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1])
    """

    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, value])


def get_transaction_value():
    """ Return the input of the user (a new transaction amount)
     as a float"""
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
          is_valid = True
        else:
            is_valid = False
        break

#     for block in blockchain:
#         if block_index == 0:
#             block_index += 1
#            continue
#         elif block[0] == blockchain[block_index - 1]:
#            is_valid = True
#        else:
#            is_valid = False
#           break
#        block_index += 1
    return is_valid


# Get the first transaction input and add the value to the blockchain

waiting_for_input = True


while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(last_transaction=get_last_blockchain_value(), value=tx_amount)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        print("Thanks for using Spongecoin!")
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid blockchain!")
        break
else:
    print("user left!")


print('Done!')
