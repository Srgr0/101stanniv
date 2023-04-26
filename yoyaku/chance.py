import csv
import random
from collections import defaultdict

def load_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def remove_duplicates(data):
    email_counts = defaultdict(int)
    for row in data:
        email_counts[row['メールアドレス']] += 1

    return [row for row in data if email_counts[row['メールアドレス']] == 1]

def separate_data_by_first_preference(data):
    separated_data = defaultdict(list)
    for row in data:
        separated_data[row['第一希望']].append(row)
    return separated_data

def shuffle_data(data):
    shuffled_data = data.copy()
    random.shuffle(shuffled_data)
    return shuffled_data

def select_winners(data):
    capacity = 30
    current_total = 0
    winners = []

    for row in data:
        num_participants = int(row['参加人数'].replace('名', ''))
        if current_total + num_participants <= capacity:
            winners.append(row)
            current_total += num_participants
        else:
            break

    return winners

def write_results_to_csv(winners, output_file):
    with open(output_file, mode='a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['タイムスタンプ', 'メールアドレス', '第一希望', '第二希望', '第三希望', '参加人数']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for row in winners:
            writer.writerow(row)

def main():
    input_file = 'tour.csv'
    output_file = '武蔵ツアー結果.csv'

    data = load_csv(input_file)
    data = remove_duplicates(data)

    separated_data = separate_data_by_first_preference(data)

    for key in separated_data:
        event_data = separated_data[key]
        event_data = shuffle_data(event_data)
        winners = select_winners(event_data)
        write_results_to_csv(winners, output_file)

if __name__ == '__main__':
    main()
