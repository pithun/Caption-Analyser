MAX_CAPTION_LENGTH = 50

HASHTAG_SYMBOL = '#'

MENTION_SYMBOL = '@'

UNDERSCORE = '_'


def is_valid_caption(word):
    """returns True if caption contains between 0 -MAX_CAPTION_LENGTH characters"""
    if len(word) <= MAX_CAPTION_LENGTH:
        return True


# print(is_valid_caption('Hello Twitter!'))


# so comparing string python compares alphanumerically and alphabets are checked before numbers i.e a < 1 and uppercase
# are identified before lowercase


def compare_captions(str_one, str_two):
    """compares two valid captions and returns 1 if the first comes before the second when sorting alphanumerically
    , returns -1 if the second comes first and returns 0 if both captions are of the same length"""
    valid_capt1 = is_valid_caption(str_one)
    valid_capt2 = is_valid_caption(str_two)
    if valid_capt1 is True and valid_capt2 is True:
        if str_one < str_two:
            return 1
        elif str_one > str_two:
            return -1
        else:
            return 0
    else:
        raise ValueError('Invalid caption length')


# print(compare_captions('Anoth', 'A'))


def clean(text):
    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + ' ' + char
        else:
            clean_str = clean_str + ' '
    return clean_str


# print(clean('i am a boy!!'))


def contains_hashtags_better(caption, hashtag):
    clean_caption = clean(caption)
    hash_tag_list = []
    empty = ''
    for val, r in enumerate(clean_caption):
        if r == HASHTAG_SYMBOL:
            new_one = clean_caption[val + 1:]
            for x in new_one:
                if x == ' ':
                    break
                else:
                    empty = empty + x
            hash_tag_list.append(empty)
            empty = ''
    for h in hash_tag_list:
        if h == '':
            hash_tag_list.remove(h)
    if hashtag in hash_tag_list:
        return True
    else:
        return False


# print(contains_hashtags_better('i love #Python,@tyt #victoria', 'python'))


def is_mentioned(f_word, s_word):
    clean_men = clean(f_word)
    mention_list = []
    empty_men = ''
    for val, r in enumerate(clean_men):
        if r == MENTION_SYMBOL:
            new_men = clean_men[val + 1:]
            for m in new_men:
                if m == ' ':
                    break
                else:
                    empty_men = empty_men + m
            mention_list.append(empty_men)
            empty_men = ''
    for mention in mention_list:
        if mention == '':
            mention_list.remove(mention)
    if s_word in mention_list:
        return True
    else:
        return False

# print(is_mentioned('i love @victoria, @ python', 'victoria'))

# i did it another way which made me to not have to write the whole code again check trial file
# i even used that in the main code
def get_hashtags_better(caption):
    val_or_not = is_valid_caption(caption)
    if val_or_not is True:
        clean_capti = clean(caption)
        hash_tag_list = []
        hash_tag_set = set()
        empty = ''
        for val, r in enumerate(clean_capti):
            if r == HASHTAG_SYMBOL:
                new_one = clean_capti[val + 1:]
                for x in new_one:
                    if x == ' ':
                        break
                    else:
                        empty = empty + x
                hash_tag_set.add(empty)
                empty = ''
        for word in hash_tag_set:
            hash_tag_list.append(word)
        for h in hash_tag_list:
            if h == '':
                hash_tag_list.remove(h)
        return hash_tag_list
    else:
        return 'Invalid caption length'


# print(get_hashtags_better(' i likr #python_hgk@bhj'))


def get_mentions(mentions):
    valid_or_not = is_valid_caption(mentions)
    if valid_or_not is True:
        cleaned_mention = clean(mentions)
        mentioned = []
        mentioned_set = set()
        empty_mentioned = ''
        for val, r in enumerate(cleaned_mention):
            if r == MENTION_SYMBOL:
                new_one = cleaned_mention[val + 1:]
                for cl in new_one:
                    if cl == ' ':
                        break
                    else:
                        empty_mentioned = empty_mentioned + cl
                mentioned_set.add(empty_mentioned)
                empty_mentioned = ''
        for word_m in mentioned_set:
            mentioned.append(word_m)
        for h in mentioned:
            if h == '':
                mentioned.remove(h)
        return mentioned
    else:
        return 'Invalid caption length'


# i did it another way which made me to not have to write the whole code again check trial file

def reverse(content):
    clean_content = clean(content)
    split_content = clean_content.split()
    list_content = []
    empty = ''
    for x in split_content:
        list_content.append(x)
    length = len(list_content) - 1
    for word in range(len(list_content)):
        empty = empty + list_content[length] + ' '
        length = length - 1
    return empty


# print(reverse('#2020is a year tormb!#BLM#COVID19,what a year!!'))


def censor(value):
    vowels = 'aeiou'
    for vow in range(len(vowels)):
        value = value.replace(vowels[vow], '*')
    return value


# print(censor('“Pineapples on pizza should not be allowed!'))

