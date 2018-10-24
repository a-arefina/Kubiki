# -*- coding: utf-8 -*-

cubes = ("ояйпмъ", "эинщбт", "ёыпбкр", "уехзчб", "оижцгх", "еилцвп",
         "еагфмк", "еомщнт", "аядсйш", "иувшлс", "юазчрф", "аожьдк")

DEB = False


# returns cube set model in the form
# {letter: [IDs of cubes containing the letter], ...}
# ID of a cube is its sequence number in cube_set
def make_cube_set_model(cube_set):
    model = {}
    for i, word in enumerate(cube_set):
        for letter in word:
            model.setdefault(letter, [])
            model[letter].append(i)
    return model


# removes cube with ID == cube_id from the model
def clear_cube_set_model(model, cube_id):
    return {l: [i for i in model[l] if i != cube_id] for l in model}


def get_letter_frequencies_in_word(word):
    return {letter: word.count(letter) for letter in set(word)}


# checks that each letter from string occurs enough times in the cubes represented by model
# i.e. if string contains a letter twice, but there is only 1 cube with this letter in model
# this check doesn't pass
def check_enough_letters_in_cubes(model, string):
    letter_freqs = get_letter_frequencies_in_word(string)
    return not any(len(model[l]) < letter_freqs[l] for l in letter_freqs)


# checks if a set of words (word_set) can be built with cubes from cube_set
# each cube is represented as a sequence of letters on it
# if yes, returns list of pairs (letter, cube_ID),
# indicating what cube should be taken for each letter to build word_set
# (ID of a cube is its sequence number in cube_set)
# returns empty list otherwise
def check_word_set(word_set, cube_set):

    # check that number of cubes is not less than total number of letters in word_set
    if sum(len(word) for word in word_set) > len(cube_set):
        if DEB: print("not enough cubes")
        return []

    # build a model of cubes from cube_set in the form
    # {letter: [IDs of cubes containing the letter], ...}
    model = make_cube_set_model(cube_set)

    # merge all words to check in a single string
    # actual letter order in it doesn't matter
    words = ''.join(word_set)

    # check if cubes contain all letters from word_set
    for l in set(words):
        if l not in model:
            if DEB: print("letter {} not present in cubes".format(l))
            return []


    #####

    # performs recursive step #i
    #
    # if N is an original number of letters and M is an original number of cubes
    # than words_i contains N-i letters that are still not assigned to a cube,
    # model_i contains M-i cubes that are not assigned to a letter
    #
    # checks if all letters can be assigned to a cube
    # selects the letter (let denote it L*) that has the least number of cubes that contain it
    # and assigns it to a cube (C*),
    # then tries to remove the cube C* from the model and the letter L* from words_i and to perform next step (i+1)
    # if it is not successful, tries to select another cube for the letter L*
    # (step i with model_i modified: C* is removed from list of cube IDs fo L*)
    #
    # returns True when sequence of letters to assign becomes empty
    # returns False when it is impossible to assign any letter
    def inner_fun(i, words_i, model_i):
        if DEB: print("+++ inner_fun {} +++".format(i))
        if DEB: print(sorted(sorted(model_i.items()), key=lambda l: len(l[1]), reverse=True))

        # checks that each letter from words_i occurs enough times in the cubes from model_i
        if not check_enough_letters_in_cubes(model_i, words_i):
            if DEB: print("not enough letters in cubes")
            return False

        # select the letter that has the least number of cubes that contain it
        # may also shuffle before sorting to add randomness
        words_i = sorted(words_i, key=lambda l: len(model_i[l]))
        if DEB: print(words_i)
        letter = words_i[0]
        cube_numbers = model_i[letter]

        # assign a cube to letter
        cube_num = cube_numbers.pop(0)  # can also make random choice # model_i is changed here

        # remember the choice
        ans[i] = (letter, cube_num)
        if DEB: print("new letter added: ", ans[:i + 1])

        # make a model without the cube chosen for the next recursive step
        model_i1 = clear_cube_set_model(model_i, cube_num)
        words_i1 = words_i[1:]

        if len(words_i1) == 0:
            if DEB: print("all letters found")
            return True
        else:
            # perform next recursive step for next letter or try to choose another cube for the same letter
            return inner_fun(i + 1, words_i1, model_i1) or inner_fun(i, words_i, model_i)

    #####

    # prepare the list to remember letter-cube pairs
    ans = [None] * len(words)
    res = inner_fun(0, words, model)
    if not res:
        ans = []

    return ans

if __name__ == "__main__":
    # cubes3 = (  "mas", "amk", "sak", "smk", "asd")
    # print(check_word_set(('masa',), cubes3))

    print(check_word_set(('папа', 'женя', 'маша'), cubes))
    print(check_word_set(('зонд', 'цирк', 'ёжик'), cubes))

    print(check_word_set(('папа', 'женя', 'мама'), cubes))
    print(check_word_set(('зонт', 'цирк', 'ёжик'), cubes))
