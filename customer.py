class Customer:
    def __init__(self, first_name, family_name, age):  # 年齢ageを追加
        self.first_name = first_name
        self.family_name = family_name
        self.age = age  # 年齢ageをインスタンス変数に設定

    def full_name(self):
        return self.first_name + self.family_name

    def full_age(self):
        return self.age

    def entry_fee(self):
        if self.age >= 0 and self.age < 20:
            return 1000
        if self.age >= 20 and self.age < 65:
            return 1500
        if self.age >= 65:
            return 1200

    def info_csv(self):
        return f"{self.first_name}, {self.family_name}, {self.age}, {self.entry_fee()}"

if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)  # インスタンス化, 年齢15を追加
    # ken.full_name()  # "Ken Tanaka" という値を返す
    ken.entry_fee()  # 1000という値を返す
    # print(f"Fee:¥{ken.entry_fee()}")
    print(ken.info_csv())  # Ken, Tanaka, 15, 1000 を返す

    tom = Customer(first_name="Tom", family_name="Ford", age=57)  # インスタンス化、年齢57を追加
    # tom.full_name()  # "Tom Ford" という値を返す
    # print(tom.display_profile())
    # print(f"Fee:¥{tom.entry_fee()}")
    print(tom.info_csv())  # Tom, Ford, 57, 1500 を返す

    # ieyasuを追加
    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)  # インスタンス化(家康ぅぅぅぅ！？)
    # ieyasu.full_name()  # "Ieyasu Tokugawa" という値を返す
    # print(ieyasu.display_profile())
    # print(f"Fee:¥{ieyasu.entry_fee()}")  # 1200という値を返す
    print(ieyasu.info_csv())  # Ieyasu, Tokugawa, 73, 1200 を返す
