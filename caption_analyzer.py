import caption_analyser_functions as capt
import trial


owners_name = 'Pithun\'s'
users_caption = input('Welcome to ' + owners_name + ' caption Analyser. Enter a Caption: ')
valid_or_not = capt.is_valid_caption(users_caption)
while not valid_or_not:
    users_caption = input('Enter a caption (with a max of 50 characters): ')
    valid_or_not = capt.is_valid_caption(users_caption)
display_option = int(input('Please select one of the following analysis options: \n   1. Contains specific hashtag '
                           '\n   2. Contains specific mention\n   3. View all hashtags\n   4. View all mentions\n   '
                           '5. Reverse caption\n   6. Censor caption\n   7. Analyse another caption\n   8. Quit program'
                           '\nselect an option : '))
while display_option != 8:
    if display_option == 1:
        display_option_1 = input('Please enter a hashtag you would like to check: ')
        status = capt.contains_hashtags_better(users_caption, display_option_1)
        if status is True:
            print('\n', display_option_1 + ' is a valid hashtag in ' + users_caption)
        else:
            print('\n', display_option_1 + ' is not a valid hashtag in ' + users_caption)
    elif display_option == 2:
        display_option_2 = input('Please enter a mention you would like to check: ')
        status_2 = capt.is_mentioned(users_caption, display_option_2)
        if status_2 is True:
            print('\n', display_option_2 + ' is a valid mention in ' + users_caption)
        else:
            print('\n', display_option_2 + ' is not a valid mention in ' + users_caption)
    elif display_option == 3:
        all_hastags = trial.get_hashtags_better(users_caption)
        print('\n', users_caption + ' contains', len(all_hastags), 'hashtags: ')
        for hashtags in all_hastags:
            print('#' + hashtags)
    elif display_option == 4:
        all_mentions = trial.mentiongetter(users_caption)
        print('\n', users_caption + ' contains', len(all_mentions), 'mentions: ')
        for mentions in all_mentions:
            print('@' + mentions)
    elif display_option == 5:
        reversed_caption = capt.reverse(users_caption)
        print('\n', users_caption + ' reversed: ' + reversed_caption)
    elif display_option == 6:
        censored_caption = capt.censor(users_caption)
        print('\n', users_caption + ' censored: ' + censored_caption)
    elif display_option == 7:
        while display_option == 7:
            users_caption = input('Enter another caption to analyse: ')
            valid_or_not = capt.is_valid_caption(users_caption)
            while not valid_or_not:
                users_caption = input('Enter a caption (with a max of 50 characters): ')
                valid_or_not = capt.is_valid_caption(users_caption)
            display_option = int(
                input('Please select one of the following analysis options: \n   1. Contains specific hashtag '
                      '\n   2. Contains specific mention\n   3. View all hashtags\n   4. View all mentions\n   '
                      '5. Reverse caption\n   6. Censor caption\n   7. Analyse another caption\n   8. Quit program'
                      '\nselect an option : '))
            if display_option == 1:
                display_option_1 = input('Please enter a hashtag you would like to check: ')
                status = capt.contains_hashtags_better(users_caption, display_option_1)
                if status is True:
                    print(display_option_1 + ' is a valid hashtag in ' + users_caption)
                else:
                    print(display_option_1 + ' is not a valid hashtag in ' + users_caption)
            elif display_option == 2:
                display_option_2 = input('Please enter a mention you would like to check: ')
                status_2 = capt.is_mentioned(users_caption, display_option_2)
                if status_2 is True:
                    print(display_option_2 + ' is a valid mention in ' + users_caption)
                else:
                    print(display_option_2 + ' is not a valid mention in ' + users_caption)
            elif display_option == 3:
                all_hastags = trial.get_hashtags_better(users_caption)
                print(users_caption + ' contains', len(all_hastags), 'hashtags: ')
                for hashtags in all_hastags:
                    print('#' + hashtags)
            elif display_option == 4:
                all_mentions = trial.mentiongetter(users_caption)
                print(users_caption + ' contains', len(all_mentions), 'mentions: ')
                for mentions in all_mentions:
                    print('@' + mentions)
            elif display_option == 5:
                reversed_caption = capt.reverse(users_caption)
                print(users_caption + ' reversed: ' + reversed_caption)
            elif display_option == 6:
                censored_caption = capt.censor(users_caption)
                print(users_caption + ' censored: ' + censored_caption)

    if display_option < 1 or display_option > 8:
        while display_option < 1 or display_option > 8:
            print('Invalid option')
            display_option = int(input('Enter an option again: \n   1. Contains specific hashtag '
                                       '\n   2. Contains specific mention\n   3. View all hashtags\n   4. View all '
                                       'mentions\n '
                                       '  5. Reverse caption\n   6. Censor caption\n   7. Analyse another caption\n   '
                                       '8. Quit program '
                                       '\nselect an option : '))

    elif 1 <= display_option < 8:
        display_option = int(
            input('Please select one of the following analysis options: \n   1. Contains specific hashtag '
                  '\n   2. Contains specific mention\n   3. View all hashtags\n   4. View all mentions\n   '
                  '5. Reverse caption\n   6. Censor caption\n   7. Analyse another caption\n   8. Quit program'
                  '\nselect an option : '))


    elif display_option == 8:
        break

print('Thank you for using ' + owners_name + ' caption analyser, Goodbye!!!')

# Complete

