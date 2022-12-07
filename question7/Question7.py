class Directory:

    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent

    def cd(self, arg):
        if arg == "..":
            return self.parent
        if arg == "/":
            d = self
            while d.parent is not None:
                d = d.parent
            return d

        # cd arg
        dir = next((d for d in self.directories if d.name == arg), None)
        if dir is None:
            self.add_dir(arg)
        return dir

    def add_dir(self, dir_name):
        self.directories.append(Directory(dir_name, self))

    def add_file(self, name, size):
        self.files.append((name, size))

    def file_size(self):
        files = list(zip(*self.files))
        return sum(files[1]) if len(files) > 0 else 0

    def visit(self, visitor, parents=[]):
        dir_size = self.file_size()
        full_path = "/" if len(parents) == 0 else parents[-1:][0] + self.name + "/"
        visitor[full_path] = dir_size
        for p in parents:
            visitor[p] += dir_size

        p = parents + [full_path]
        for d in self.directories:
            d.visit(visitor, p)

    def tree(self, indent=""):
        for f in self.files:
            print(indent + "- " + f[0] + " (" + str(f[1]) + ")")
        for d in self.directories:
            print(indent + "- " + d.name + " (dir)")
            d.tree(indent + "  ")

    def solve_one(self):
        dir_sizes = {}
        self.visit(dir_sizes)
        print(sum([size for d, size in dir_sizes.items() if size <= 100000]))

    def solve_two(self):
        dir_sizes = {}
        self.visit(dir_sizes)
        used_space = dir_sizes['/']
        free_now = 70000000 - used_space
        to_delete = 30000000 - free_now
        print(min([size for d, size in dir_sizes.items() if size >= to_delete]))


def parse_dir(lines):
    dir = None
    for line in lines:
        cmd = line.split(" ")
        a = cmd[0]
        b = cmd[1] if len(cmd) > 1 else None
        if a == "cd":
            if dir is None:
                dir = Directory(b)
            else:
                dir = dir.cd(b)

        if a == "dir":
            dir.add_dir(b)

        if a.isdigit():
            dir.add_file(b, int(a))

    return dir.cd("/")


with open('question_data.txt') as f:
    lines = [line.replace('$', '').strip() for line in f.readlines()]
    dir = parse_dir(lines)
    # dir.tree()
    dir.solve_one()
    dir.solve_two()
