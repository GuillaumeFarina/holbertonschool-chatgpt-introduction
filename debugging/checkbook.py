class Checkbook:
    def __init__(self):
        # Initialisation de l'objet Checkbook avec un solde initial de 0.0
        self.balance = 0.0

    def deposit(self, amount):
        # Méthode pour déposer un montant sur le compte
        self.balance += amount  # Ajoute le montant au solde actuel
        print("Deposited ${:.2f}".format(amount))  # Affiche le montant déposé
        print("Current Balance: ${:.2f}".format(self.balance))  # Affiche le solde actuel

    def withdraw(self, amount):
        # Méthode pour retirer un montant du compte
        if amount > self.balance:
            # Vérifie si le montant demandé est supérieur au solde disponible
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount  # Soustrait le montant du solde actuel
            print("Withdrew ${:.2f}".format(amount))  # Affiche le montant retiré
            print("Current Balance: ${:.2f}".format(self.balance))  # Affiche le solde actuel

    def get_balance(self):
        # Méthode pour afficher le solde actuel
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Fonction principale qui gère l'interaction avec l'utilisateur
    cb = Checkbook()  # Crée une nouvelle instance de Checkbook
    while True:
        # Boucle infinie pour gérer les opérations jusqu'à ce que l'utilisateur choisisse de quitter
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break  # Quitte la boucle si l'utilisateur entre 'exit'
        elif action.lower() == 'deposit':
            # Si l'utilisateur choisit de déposer de l'argent
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)  # Appelle la méthode deposit pour ajouter l'argent au compte
        elif action.lower() == 'withdraw':
            # Si l'utilisateur choisit de retirer de l'argent
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)  # Appelle la méthode withdraw pour retirer l'argent du compte
        elif action.lower() == 'balance':
            # Si l'utilisateur souhaite consulter le solde actuel
            cb.get_balance()  # Appelle la méthode get_balance pour afficher le solde
        else:
            print("Invalid command. Please try again.")  # Message d'erreur pour commande invalide

if __name__ == "__main__":
    # Point d'entrée du script, exécute la fonction main si le script est lancé directement
    main()
