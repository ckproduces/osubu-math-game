from random import randint, choice
import os

def dispatch_rule(array_length, rule, level):
    if rule == "+":
        base_num = randint(1, 100 + level ** 5)
        num_to_add = randint(1, 100 + level ** 5)
        numbers = [base_num]
        for i in range(7):
            numbers.append((num_to_add * (i + 1)) + base_num)
        return numbers[0: 7], {"rule": rule, "base_num": base_num, "rule_num": num_to_add}
    
    elif rule == "-":
        base_num = randint(1, 100 + level ** 5)
        num_to_subtract = randint(1, 100 + level ** 5)
        numbers = [base_num]
        for i in range(7):
            numbers.append(base_num - (num_to_subtract * (i + 1)))
        return numbers[0: 7], {"rule": rule, "base_num": base_num, "rule_num": num_to_subtract}

    elif rule == "*":
        base_num = randint(1, 100 + level ** 2)
        num_to_multiply = randint(2, 10 + level ** 2)
        numbers = [base_num]
        prev_number = base_num
        for i in range(7):
            numbers.append(prev_number * num_to_multiply)
            prev_number = numbers[-1]
        return numbers[0: 7], {"rule": rule, "base_num": base_num, "rule_num": num_to_multiply}
    
    elif rule == "^":
        base_num = randint(2, max(2, level - 5))
        power = randint(2, max(2, level - 5))
        numbers = [base_num]
        prev_number = base_num
        for i in range(7):
            numbers.append(prev_number ** power)
            prev_number = numbers[-1]
        return numbers[0: 7], {"rule": rule, "base_num": base_num, "rule_num": power}

def reduce_array(array, level):
    cut_start = randint(0, level)
    cut_end = level - cut_start
    return array[2:7]

class Game:
    def __init__(self, level=1):
        self.level = level
        self.rule_types = ["+", "-", "*", "^"]
        self.sequence, self.rule = dispatch_rule(10, choice(self.rule_types), self.level)
        self.sequence = reduce_array(self.sequence, self.level)
        self.numbers_got_so_far = [self.sequence]

    def clear(self):
        os.system('cls||clear')
        
    def next_level(self):
        self.level += 1
        self.sequence, self.rule = dispatch_rule(10, choice(self.rule_types), self.level)
        while self.sequence in self.numbers_got_so_far:
            self.sequence, self.rule = dispatch_rule(10, choice(self.rule_types), self.level)
        self.sequence = reduce_array(self.sequence, self.level)
        self.numbers_got_so_far.append(self.sequence)
    
    def get_sequence(self):
        print("Sayı dizisi:")
        print(', '.join([str(number) for number in self.sequence]))
    
    def check_answer(self):
        answer = input("Kuralı tahmin et: ")
        if answer == f"{self.rule['rule']}{self.rule['rule_num']}" or answer == f"{self.rule['rule_num']}{self.rule['rule']}":
            return True
        else:
            return False
        

    def start(self, clear=clear):
        clear(self)
        print("Oşubu'ya hoş geldin!")
        print("Sana farklı sayı dizileri vereceğiz.")
        print("Sayı dizilerinin kuralını tahmin etmeye çalış!")
        print("Kuralı tahmin etmek için +, -, * veya ^ işaretlerini kullanabilirsin.")
        print("Cevabını 4* veya ^3 şeklinde yazabilirsin.")
        print("Başlamak için herhangi bir tuşa bas.")
        input()
        clear(self)


game = Game()
game.start()
while True:
    game.get_sequence()
    print("")
    if game.check_answer():
        if game.level == 10:
            print("Tebrikler! Oyunu bitirdin.")
            print("Gerçek bir Oşubu hesaplayıcısısın, güç seninle olsun.")
            break
        print(f"Doğru bildin! {game.level + 1}. seviyeye geçtin.")
        input("Devam etmek için herhangi bir tuşa bas.")
        game.next_level()
    else:
        print(f"Yanlış cevap. {game.level}. seviyede oyunu kaybettin.")
        print(f"Doğru cevap: {game.rule['rule']}{game.rule['rule_num']}")
        break
