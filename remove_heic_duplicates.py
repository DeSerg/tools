import sys
import os

ScriptPath = os.getcwd()

def main(args):
    dir_path_rel = args[0]
    dir_path = os.path.join(ScriptPath, dir_path_rel)

    print('Looking for duplicate filenames in directory {}'.format(dir_path))

    filename_count = {}

    for filename in os.listdir(dir_path):
        dot_pos = filename.rfind('.')
        if dot_pos == -1:
            continue
        filename_no_ext = filename[:dot_pos]
        filename_count[filename_no_ext] = filename_count.get(filename_no_ext, 0) + 1


    dup_list = dict(filter(lambda elem: elem[1] > 1, filename_count.items())).keys()

    print('Duplicates found: \n{}\n'.format('\n'.join(dup_list)))

    print('Remove MOV copies? (y/N)')
    reply = sys.stdin.readline()
    reply = reply.strip()
    if reply != 'y':
        print('Removing canceled')
        return


    dup_set = set(dup_list)
    for filename in os.listdir(dir_path):
        if not filename.endswith('.MOV'):
            continue

        filename_no_ext = filename[:-4]
        if filename_no_ext not in dup_set:
            continue

        print('Removing file {}'.format(filename))
        os.remove(os.path.join(dir_path, filename))

if __name__ == '__main__':
    main(sys.argv[1:])
