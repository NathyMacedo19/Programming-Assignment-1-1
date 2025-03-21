#DepositAccount
def deposit(request, account_id):
    account = Account.objects.get(id=account_id)
    if request.method == "POST":
        amount = float(request.POST["amount"])
        account.balance += amount
        account.save()
        Transaction.objects.create(account=account, amount=amount, transaction_type="Deposit")
        return redirect("dashboard")
    return render(request, "deposit.html", {"account": account})
