#Καραγιάννης Δημήτριος
#sdi 2200293  


def complete_parentheses(arith_exp):
    temp = []  # προσωρινή αποθήκευση στοιχείων

    for element in arith_exp:  #προσπέλαση λίστας σύμφωνα με εργαστήριο 0
        if element == ')':
            if len(temp) < 3:    # Πρέπει να έχουμε τουλάχιστον 3 στοιχεία στη temp λίστα π.χ. 1 + 2
                raise ValueError("Not enough elements to form an expression.")
            num2 = temp.pop()  # Τελευταίος αριθμός
            op = temp.pop()     # Τελευταία πράξη
            num1 = temp.pop()   # Προτελευταίος αριθμός
            sub_exp = f"({num1} {op} {num2})"    # Δημιουργία ενός τμήματος έκφρασης (υπό-έκφραση)
            temp.append(sub_exp)      # Πρόσθεση της νέας υπο-έκφρασης στην temp λίστα - το τοποθετεί ως ξεχωρστό στοιχείο
        else:
            temp.append(element)       # Αν είναι αριθμός ή πράξη, την προσθέτουμε στη temp λίστα
    return temp     # Επιστρέφουμε τη λίστα με τις υπο-έκφρασες

# Main
arith_exp = [1, '+', 2, ')', '*', 3, '-', 4, ')', '*', 5, '-', 6, ')', ')', ')']       #εισαγωγή με την μορφή λίστας 
print(complete_parentheses(arith_exp))    


# Εξήγηση κώδικα
# arith_exp: 1+2 -> temp: 1+2 -> μόλις βρει ) πετάει τα 3 τελευταία στοιχεία από το temp -> temp (1+2) 
# έπειτα temp: (1+2)*3-4.... -> κάποια στιμγή temp: (1+2)*(3-4)*(5-6)= a*b*c 
# arith_exp: b*c -> temp: a*b*c -> μόλις βρει ) πετάει τα 3 τελευταία στοιχεία από το temp -> temp (b*c) 
# έπειτα temp: a*(b*c)=a*d ...
