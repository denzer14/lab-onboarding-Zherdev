def process_transaction(user_id, amount, db_connection):
    status = "pending"

    if amount > 0:
        status = "approved"
        balance = get_balance(user_id)  # noqa: F821
        new_balance = balance - amount
        update_balance(user_id, new_balance)  # noqa: F821

    log_entry = "Transaction finished with status: " + status

    with open("audit_log.txt", "w", encoding="utf-8") as audit_file:
        audit_file.write(log_entry)

    return status
