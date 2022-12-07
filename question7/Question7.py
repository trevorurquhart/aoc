class Directory:

    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent
        separator = "" if parent is None or parent.is_root() else "/"
        self.full_path = name if parent is None else parent.full_path + separator + name

    def cd(self, arg):
        match arg:
            case "..":
                return self.parent

            case "/":
                d = self
                while d.parent is not None:
                    d = d.parent
                return d

            case _:
                d = next((d for d in self.directories if d.name == arg), None)
                if d is None:
                    d = self.mkdir(arg)
        return d

    def mkdir(self, dir_name):
        d = Directory(dir_name, self)
        self.directories.append(d)
        return d

    def mkfile(self, name, size):
        self.files.append((name, size))

    def file_size(self):
        files = list(zip(*self.files))
        return sum(files[1]) if len(files) > 0 else 0

    def is_root(self):
        return self.parent is None

    def dir_sizes(self, ans=None, parents=None):
        if parents is None:
            parents = []
        if ans is None:
            ans = {}
        dir_size = self.file_size()
        ans[self.full_path] = dir_size
        for p in parents:
            ans[p] += dir_size

        for d in self.directories:
            d.dir_sizes(ans, parents + [self.full_path])

        return ans

    def tree(self, indent=""):
        for f in self.files:
            print(indent + "- " + f[0] + " (" + str(f[1]) + ")")
        for d in self.directories:
            print(indent + "+ " + d.name + " (dir)")
            d.tree(indent + "  ")

    def solve_one(self):
        print(sum([size for d, size in self.dir_sizes().items() if size <= 100000]))

    def solve_two(self):
        dir_sizes = self.dir_sizes()
        to_delete = 30000000 - (70000000 - dir_sizes['/'])
        print(min([size for d, size in dir_sizes.items() if size >= to_delete]))


def parse_dir(cmds):
    d = None
    for cmd in cmds:
        match cmd.split():
            case ["cd", arg]:
                if d is None:
                    d = Directory(arg)
                else:
                    d = d.cd(arg)

            case ["dir", arg]:
                d.mkdir(arg)

            case [size, file] if size.isdigit():
                d.mkfile(file, int(size))

    return d.cd("/")


with open('question_data.txt') as q:
    lines = [line.replace('$', '').strip() for line in q.readlines()]
    directory = parse_dir(lines)
    # directory.tree()
    directory.solve_one()
    directory.solve_two()
