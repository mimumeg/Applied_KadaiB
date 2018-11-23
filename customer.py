class Customer:
    def __init__(self, first_name, family_name, age):  # 年齢ageを追加
        self.first_name = first_name
        self.family_name = family_name
        self.age = age  # 年齢ageをインスタンス変数に設定

    def full_name(self):
        return self.first_name + " " + self.family_name  # first_name と family_nameの間にスペースを入れた

    def full_age(self):
        return self.age

    def entry_fee(self):
        if self.age <= 3 and self.age >= 0:  # 3歳以下は無料
            return 0
        if self.age > 3 and self.age < 20:  # 4歳以上20歳未満は¥1,000
            return 1000
        if self.age >= 20 and self.age < 65:  # 20歳以上65歳未満は¥1,500
            return 1500
        if self.age >= 65 and self.age < 75:  # 65歳以上は75歳未満は¥1,200
            return 1200
        if self.age >= 75:
            return 500

    def info_csv(self):
        # return f"{self.first_name} {self.family_name}, {self.age}, {self.entry_fee()}"
        # リスト化する
        list = [self.full_name(), self.age, self.entry_fee()]
        list = [str(i) for i in list]
        print(','.join(list))

    def info_tab(self):
        # return f"{self.first_name} {self.family_name} \t {self.age} \t {self.entry_fee()}"
        list = [self.first_name, self.family_name, self.age, self.entry_fee()]
        list = [str(i) for i in list]
        print('\t'.join(list))

    def info_pipe(self):
        # return f"{self.first_name} {self.family_name} \t {self.age} \t {self.entry_fee()}"
        list = f"{self.first_name},{self.family_name},{self.age},{self.entry_fee()}"
        # list = [str(i) for i in list]
        list_new = list.replace(',', '|')
        print(list_new)

if __name__ == "__main__":
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)  # インスタンス化, 年齢15を追加
    ken.full_name()  # "Ken Tanaka" という値を返す
    ken.entry_fee()  # 1000という値を返す
    # print(f"Fee:¥{ken.entry_fee()}")
    ken.info_csv()  # Ken, Tanaka, 15, 1000 を返す

    tom = Customer(first_name="Tom", family_name="Ford", age=57)  # インスタンス化、年齢57を追加
    # tom.full_name()  # "Tom Ford" という値を返す
    # print(tom.display_profile())
    # print(f"Fee:¥{tom.entry_fee()}")
    tom.info_csv()  # Tom, Ford, 57, 1500 を返す

    # ieyasuを追加
    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)  # インスタンス化(家康ぅぅぅぅ！？)
    # ieyasu.full_name()  # "Ieyasu Tokugawa" という値を返す
    # print(ieyasu.display_profile())
    # print(f"Fee:¥{ieyasu.entry_fee()}")  # 1200という値を返す
    ieyasu.info_csv()  # Ieyasu, Tokugawa, 73, 1200 を返す

    # 3歳のtaroを追加
    taro = Customer(first_name="Taro", family_name="Yamada", age=3)  # taroインスタンス化
    taro.info_csv()  # Taro, Tokugawa, 73, 1200 を返す

    # 86歳のminoruを追加
    minoru = Customer(first_name="Minoru", family_name="Tamura", age=86)  # 和製アインシュタインをインスタンス化
    minoru.info_csv()
    print()  # 改行

    # B-7 単一顧客の取得情報をタブ区切り
    ken.info_tab()  # Ken Tanaka    15  1000 を返す
    tom.info_tab()  # Tom Ford    57  1500 を返す
    ieyasu.info_tab()  # Ieyasu Tokugawa   73  1200 を返す
    taro.info_tab()  # Taro Yamda    3   0 を返す
    minoru.info_tab()  # Minoru Tamura    86  500 を返す
    print()  # 改行

    # B-8 単一顧客の取得情報をパイプ区切り
    ken.info_pipe()  # Ken Tanaka | 15 | 1000 を返す
    tom.info_pipe()  # Tom Ford | 57 | 1500 を返す
    ieyasu.info_pipe()  # Ieyasu Tokugawa | 73 | 1200 を返す
    taro.info_pipe()  # Taro Yamada | 3 | 0 を返す
    minoru.info_pipe()  # Minoru Tamura | 86 | 500 を返す
