import random
import csv

class CompteBancaire:
    def __init__(self, id_client, solde=0):
        self.id_client = id_client
        self.numero_compte = int(str(id_client) + str(random.randint(0, 100)))
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant} Dh. Nouveau solde : {self.solde} Dh")

    def retirer(self, montant):
        if montant > self.solde:
            print("Fonds insuffisants !")
        else:
            self.solde -= montant
            print(f"Retrait de {montant} Dh. Nouveau solde : {self.solde} Dh")

    def afficher_info(self):
        print(f"ID Client : {self.id_client}, Numéro de Compte : {self.numero_compte}, Solde : {self.solde}")

class Banque:
    def __init__(self):
        self.comptes = {}
        self.secret_client = {}
        self.client_compte = {}

    def ajouter_compte(self, id_client):
        if id_client not in self.comptes:
            nouveau_compte = CompteBancaire(id_client)
            self.comptes[id_client] = nouveau_compte
            secret = input(f"Définir un code secret pour le client {id_client} : ")
            self.secret_client[id_client] = secret
            self.client_compte[id_client] = nouveau_compte.numero_compte
            print(f"Compte créé avec succès pour le client {id_client}.")
        else:
            print(f"Le compte existe déjà pour le client {id_client}.")

    def supprimer_compte(self, id_client):
        if id_client in self.comptes:
            del self.comptes[id_client]
            del self.secret_client[id_client]
            del self.client_compte[id_client]
            print(f"Compte supprimé avec succès pour le client {id_client}.")
        else:
            print(f"Aucun compte trouvé pour le client {id_client}.")

    def afficher_comptes(self):
        for compte in self.comptes.values():
            compte.afficher_info()

    def menu_client(self, id_client):
        while True:
            print("\nMenu Client :")
            print("1. Modifier le mot de passe")
            print("2. Afficher le solde")
            print("3. Déposer de l'argent")
            print("4. Retirer de l'argent")
            print("5. Quitter")

            choix = input("Entrez votre choix : ")

            if choix == '1':
                old_mdp = input("Saisir l'ancien mot de passe : ")
                while old_mdp != self.secret_client[id_client]:
                    print("Ancien mot de passe invalide!")
                    old_mdp = input("Saisir l'ancien mot de passe : ")
                nouveau_mot_de_passe = input("Entrez un nouveau mot de passe : ")
                self.secret_client[id_client] = nouveau_mot_de_passe
                print("Mot de passe modifié avec succès.")

            elif choix == '2':
                numero_compte = self.client_compte[id_client]
                print(f"Votre solde est : {self.comptes[id_client].solde} Dh")

            elif choix == '3':
                montant = float(input("Entrez le montant à déposer : "))
                self.comptes[id_client].deposer(montant)

            elif choix == '4':
                montant = float(input("Entrez le montant à retirer : "))
                self.comptes[id_client].retirer(montant)

            elif choix == '5':
                print("Sortie du menu client. Au revoir !")
                break

            else:
                print("Choix invalide. Veuillez entrer une option valide.")

    def ajouter_client(self, num_cl, mdp_cl, num_c, solde_c):
        self.secret_client[num_cl] = mdp_cl
        self.comptes[num_cl] = CompteBancaire(num_cl, solde_c)
        self.client_compte[num_cl] = num_c

    def supprimer_client(self, num_c):
        if num_c in self.comptes:
            del self.comptes[num_c]
            for client, compte in self.client_compte.items():
                if compte == num_c:
                    del self.secret_client[client]
                    del self.client_compte[client]
                    break
            print(f"Client avec le compte {num_c} supprimé avec succès.")
        else:
            print(f"Aucun compte trouvé avec le numéro {num_c}.")

def modifier_mot_de_passe_client(banque, id_client, nouveau_mot_de_passe, old_mdp):
    if id_client in banque.secret_client:
        if banque.secret_client[id_client] == old_mdp:
            banque.secret_client[id_client] = nouveau_mot_de_passe
            print("Mot de passe modifié avec succès.")
        else:
            print("Ancien mot de passe incorrect.")
    else:
        print(f"Client {id_client} non trouvé.")

def deposer(banque, id_client, montant):
    if id_client in banque.client_compte:
        numero_compte = banque.client_compte[id_client]
        if numero_compte in banque.comptes:
            banque.comptes[numero_compte].deposer(montant)
        else:
            print(f"Compte {numero_compte} non trouvé.")
    else:
        print(f"Client {id_client} non trouvé.")

def retirer(banque, id_client, montant):
    if id_client in banque.client_compte:
        numero_compte = banque.client_compte[id_client]
        if numero_compte in banque.comptes:
            banque.comptes[numero_compte].retirer(montant)
        else:
            print(f"Compte {numero_compte} non trouvé.")
    else:
        print(f"Client {id_client} non trouvé.")

generer_numero_compte = lambda num_cl: int(str(num_cl) + str(random.randint(0, 100)))

def ecrire_fichier_csv(banque, nom_fichier):
    with open(nom_fichier, 'w', newline='') as csvfile:
        noms_champs = ['Client', 'Code Secret']
        ecrivain = csv.DictWriter(csvfile, fieldnames=noms_champs)

        ecrivain.writeheader()
        for client, code_secret in banque.secret_client.items():
            ecrivain.writerow({'Client': client, 'Code Secret': code_secret})
    print(f"Informations client écrites dans {nom_fichier}.")

def manipuler_ensembles_listes_tuples(banque):
    ensemble_compte = set(banque.client_compte.values())
    liste_compte = list(ensemble_compte)
    tuple_compte = tuple(liste_compte)
    return liste_compte, tuple_compte, ensemble_compte

# Création de la banque
banque = Banque()

while True:
    print("\nMenu Principal :")
    print("1. Menu Agent Bancaire")
    print("2. Menu Client")
    print("3. Quitter")

    choix_principal = input("Entrez votre choix : ")

    if choix_principal == '1':
        print("\nMenu Agent Bancaire :")
        print("1. Ajouter un Client")
        print("2. Supprimer un Client")
        print("3. Afficher tous les Clients")
        print("4. Écrire dans un fichier CSV")
        print("5. Manipuler des ensembles, listes et tuples")
        print("6. Quitter")

        choix_agent = input("Entrez votre choix : ")

        if choix_agent == '1':
            num_cl = int(input("Entrez l'ID du client : "))
            mdp_cl = input("Entrez le mot de passe du client : ")
            num_c = generer_numero_compte(num_cl)
            solde_c = float(input("Entrez le solde initial : "))
            banque.ajouter_client(num_cl, mdp_cl, num_c, solde_c)

        elif choix_agent == '2':
            num_c = int(input("Entrez le numéro de compte à supprimer : "))
            banque.supprimer_client(num_c)

        elif choix_agent == '3':
            print("Clients :")
            for client, code_secret in banque.secret_client.items():
                print(f"Client {client} : Code Secret - {code_secret}")

        elif choix_agent == '4':
            nom_fichier = input("Entrez le nom du fichier CSV : ")
            ecrire_fichier_csv(banque, nom_fichier)

        elif choix_agent == '5':
            liste_compte, tuple_compte, ensemble_compte = manipuler_ensembles_listes_tuples(banque)
            print(f"Liste : {liste_compte}")
            print(f"Tuple : {tuple_compte}")
            print(f"Ensemble : {ensemble_compte}")

        elif choix_agent == '6':
            print("Sortie de l'application. Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez entrer une option valide.")

    elif choix_principal == '2':
        id_client = int(input("Entrez votre ID client : "))
        if id_client in banque.secret_client:
            mot_de_passe = input("Entrez votre mot de passe : ")
            if mot_de_passe == banque.secret_client[id_client]:
                banque.menu_client(id_client)
            else:
                print("Mot de passe incorrect. Accès refusé.")
        else:
            print("Client non trouvé.")

    elif choix_principal == '3':
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Veuillez entrer une option valide.")
