class Customer:
    def __init__(self, first_name, family_name, age):  # 年齢ageを追加
        self.first_name = first_name
        self.family_name = family_name
        self.age = age  # 年齢ageをインスタンス変数に設定

    def full_name(self):
        return self.first_name + self.family_name



if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)  # インスタンス化, 年齢15を追加
    ken.full_name()  # "Ken Tanaka" という値を返す
    ken.age  # 15 という値を返す

    tom = Customer(first_name="Tom", family_name="Ford", age=57)  # インスタンス化、年齢57を追加
    tom.full_name()  # "Tom Ford" という値を返す
    tom.age  # 57 という値を返す

    # ieyasuを追加
    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    ieyasu.age  # 73 という値を返す
    # print(ieyasu.full_name())
