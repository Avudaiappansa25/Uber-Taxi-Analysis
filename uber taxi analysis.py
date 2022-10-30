class Node:
    def _init_(self, data):
        self.left = None
        self.right = None
        # self.up=10
        self.data = data


class Tree:
    def _init_(self):
        # self.nood=[]
        # self.length=len(self.nood)
        self.rot = []

    def create(self, root):
        return Node(root)

    def insert(self, node, data):
        if node is None:
            b = self.create(data)
            # self.nood.append(b.data)
            return b
        elif (data < node.data):
            node.left = self.insert(node.left, data)
        elif (data >= node.data):
            node.right = self.insert(node.right, data)

        return node

    def order(self, root):
        if root is not None:
            self.rot.append(root.data)
            # print('-->',root.data,)
            self.order(root.left)
            # print('-->',root.data,)
            self.order(root.right)
            # print('-->',root.data,)

    def sort(self, root):
        if (self.rot[0] == ' Karamadai'):
            print("\033[1;32m")
            print("\033[4;32m")
            print("* CIRCUMSTANCES :**\033[0;39m ")
        elif (self.rot[0] == 'SANTRO 4 seats'):
            print("\033[1;32m")
            print("\033[4;32m")
            print("* CARS AVAILABLE :**\033[0;39m ")
        else:
            print("\033[1;32m")
            print("\033[4;32m")
            print("* CUSTOMERS ORDER :**\033[0;39m ")
        ar = []
        ar.append(self.rot[0])
        for i in range(1, len(self.rot)):
            ar.append(self.rot[i])
            for j in range(0, len(ar)):
                if (ar[j] > ar[i]):
                    a = ar[j]
                    ar[j] = ar[i]
                    ar[i] = a
        for i in ar:
            print(i)
        print("*")
        self.rot.clear()

    def search(self, root, element):
        try:
            if root is None or root.data == element:
                print("{} : is in the Circumstances".format(root.data))
                return 0
            elif (root.data > element):
                return self.search(root.left, element)
            elif (root.data < element):
                return self.search(root.right, element)

        except Exception as e:
            print("SORRY LOCATION NOT FOUND")
            return 1

    def successor(self, node):
        current = node
        while (current.left != None):
            current = current.left
        return current

    def delete(self, root, data):
        if root is None:
            return None
        elif (data < root.data):
            root.left = self.delete(root.left, data)
        elif (data > root.data):
            root.right = self.delete(root.right, data)
        else:
            if root.left and root.right is None:
                root = None
            elif root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.successor(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def limit(self, root, start, dest):
        if root is None:
            return
        if (start < root.data):
            self.limit(root.left, start, dest)
        if (start <= root.data and dest >= root.data):
            print(root.data, '<--->', end="")
        if (dest > root.data):
            self.limit(root.right, start, dest)

    def limit1(self, root, start, dest):
        if root is None:
            return
        if (start < root.data):
            self.limit(root.left, start, dest)
        if (start <= root.data and dest >= root.data):
            print(root.data, '<--->', end="")
        if (dest > root.data):
            self.limit(root.right, start, dest)

    def message(self):
        from twilio.rest import Client
        account_sid = "AC7dd967ee348997951c92ae1e6c70095f"
        auth_token = "82e1007d8ba3f38d25b44b7f02e656ec"
        client = Client(account_sid, auth_token)
        client.messages.create(from_="+16612997307", body="Your uber verification code is:8090", to="+919361259521")


tree = Tree()
print("\033[1;36m ")
print("****")
print("                            *   UBER   *                                ")
print("****")
print('\033[0;39m ')
root = tree.create("01104 Karamadai")
tree.insert(root, "01012 Ghandipuram")
tree.insert(root, "02104 Anaimalai")
tree.insert(root, "01653 Annur")
tree.insert(root, "01201 Chettipalayam")
tree.insert(root, "01049 Chinnavedampatti")
tree.insert(root, "01109 Dhaliyur")
tree.insert(root, "03212 Gudalur")
tree.insert(root, "01022 Idikarai")
tree.insert(root, "01103 Irugur")
tree.insert(root, "01402 Kannampalayam")
poot = tree.create('12:09 Ananth Raj')
tree.insert(poot, '12:02 Nesamani')
tree.insert(poot, '12:07 Tanmay Singh')
tree.insert(poot, '12:17 Jonathan')
tree.insert(poot, '12:23 Adii Sawant')
tree.insert(poot, '12:27 Nesamani')
coot = Node('SANTRO 4 seats')
tree.insert(coot, 'INNOVA CRYSTA 4 seats')
tree.insert(coot, 'HONDA AMAZE 6 seats')
tree.insert(coot, 'SWIFT 4 seats')
tree.insert(coot, 'CIAZ 6 seats')
tree.insert(coot, 'XCENT 4 seats ')
# print("* Cars Available :*")
tree.order(coot)
tree.sort(coot)
# print("*Customers Ordered :*")
tree.order(poot)
tree.sort(poot)
# print("*Circumstances :")
tree.order(root)
tree.sort(root)
while (1):
    name = input("TIME AND Customer Name :")
    ac = input("A/C or Non A/C :")
    start = (input("Current Location :"))
    x = tree.search(root, start)
    if (x == 1):
        start = (input("Please Enter Current Location Correctly :"))
        x = tree.search(root, start)

    dest = (input("Destination :"))
    y = tree.search(root, dest)
    if (y == 1):
        start = (input("Please Enter Destination Correctly :"))
        y = tree.search(root, start)
    car = input("(N)Car to be Choosen :")
    if (car == 'N'):
        print('\n')
        print("Please wait for few seconds ")
        tree.insert(coot, 'ALTO 4 seats')
        tree.insert(coot, 'INDICA 6 seats')
        tree.insert(coot, 'WAGON 4 seats')
        tree.insert(coot, 'RENAULT KWID 6 seats')
        tree.order(coot)
        tree.sort(coot)
        car = input("(N) Car to be Chosen :")
    phnm = input("Phone number:")
    tree.message()
    if (start < dest):
        print('|^|')
        tree.limit(root, start, dest)
    if (start > dest):
        print('|^|')
        st = start
        des = dest
        tree.limit1(root, des, st)
    print('|^|')
    veri = input(" Verified :")
    if (veri == 's' or veri == 'S'):
        tree.delete(poot, name)
        tree.order(poot)
        tree.sort(root)
    print('\n')
    tree.delete(coot, car)
    tree.order(coot)
    tree.sort(coot)
    print('\n')