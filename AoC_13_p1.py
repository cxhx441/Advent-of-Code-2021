class Paper:
    def __init__(self, coords):
        self.coords = coords

    def get_size(self):
        width, height = 0, 0
        for coord in self.coords:
            if coord[1] > width:
                width = coord[1]
            if coord[0] > height:
                height = coord[0]
        return (width+1, height+1)

    def __str__(self):
        paper_list = [['.']*self.get_size()[0] for _ in range(self.get_size()[1])]

        for coord in self.coords:
            paper_list[coord[0]][coord[1]] = '#'

        paper_string = ''
        for row in range(len(paper_list)):
            paper_string += '\n'
            for col in paper_list[row]:
                paper_string += col

        return paper_string

    def fold(self, fold_plane, fold_line):
        to_add = set()
        to_remove = set()
        for coord in self.coords:
            row = coord[0]
            col = coord[1]
            if fold_plane == 'x' and col > fold_line:
                new_col = fold_line - (col - fold_line)
                to_add.add((row, new_col))
                to_remove.add(coord)
            elif fold_plane == 'y' and row > fold_line:
                new_row = fold_line - (row - fold_line)
                to_add.add((new_row, col))
                to_remove.add(coord)

        for coord in to_remove:
            self.coords.remove(coord)
        for coord in to_add:
            self.coords.add(coord)

coords = set()
with open("AoC_13_input.txt") as f:
    lines = f.readlines()
temp_coords = [x[:-1] for x in lines[:lines.index('\n')]]
fold_instructions = [x[len('fold along '):-1] for x in lines[lines.index('\n') + 1:]]

temp_coords = [x.split(',') for x in temp_coords]
fold_instructions = [x.split('=') for x in fold_instructions]

# need to swap x, y
for coord in temp_coords:
    coords.add((int(coord[1]), int(coord[0])))
for row in range(len(fold_instructions)):
    fold_instructions[row][1] = int(fold_instructions[row][1])

paper = Paper(coords)
for fold in fold_instructions:
    paper.fold(fold[0], fold[1])
print(paper)
print(len(paper.coords))
