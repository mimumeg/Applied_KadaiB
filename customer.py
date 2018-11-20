class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        return self.first_name + self.family_name



if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka")  # インスタンス化
    ken.full_name()  # "Ken Tanaka" という値を返す
    print(ken.full_name())

    tom = Customer(first_name="Tom", family_name="Ford")  # インスタンス化
    tom.full_name()  # "Tom Ford" という値を返す
    print(tom.full_name())
