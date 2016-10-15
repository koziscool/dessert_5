
import sys

def preprocess( filename, k):
    f = open(filename)
    raw_words = f.read().split()
    words = [ word.lower().strip("';:,.?!") for word in raw_words ]

    all_neigbors, counts = {}, {}

    for word_index, word in enumerate( words ):
        these_neighbors = set()

        if word not in all_neigbors:
            all_neigbors[word] = {}

        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

        for i in xrange( word_index - k, word_index + k + 1 ):
            if i in xrange( len(words) ):
                neighbor_word = words[i]
                if neighbor_word not in these_neighbors and i != word_index:
                    if neighbor_word not in all_neigbors[word]:
                        all_neigbors[word][neighbor_word] = 1
                    else:
                        all_neigbors[word][neighbor_word] += 1
                    these_neighbors.add( neighbor_word )

    return all_neigbors, counts


def cooccurrence( anchor_word, compare_word, neighbors, counts ):
    if anchor_word not in counts or compare_word not in neighbors[anchor_word]:
        return 0

    return neighbors[anchor_word][compare_word] / float( counts[anchor_word] )


if __name__ =='__main__':
    neighbors, counts = preprocess( sys.argv[1], int(sys.argv[2]))

    while True:
        my_input = raw_input( "Enter two words or q to quit: ").split()
        if my_input[0] == 'q':
            break

        print "%.2f" % cooccurrence( my_input[0], my_input[1], neighbors, counts )
