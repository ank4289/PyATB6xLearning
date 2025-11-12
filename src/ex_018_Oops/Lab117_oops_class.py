class Person:
    Name=None
    Id=None
    Work=None

    def name(self):
        print("Ankit is the name")

    def new_name(self,nam):
        print("Today is a name",nam)

    def id(self):
        print("id is 123")

    def sleep(self):
        print("tester")


Ankit=Person()
print(Ankit.Name)
Ankit.name()
Ankit.new_name("Bharat")