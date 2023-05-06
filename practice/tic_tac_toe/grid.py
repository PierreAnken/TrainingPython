class Grid:

    def __init__(self):
        cells = []
        for _ in range(3):
            cells.append([' ', ' ', ' '])

        self.cells = cells

    def __str__(self):
        rep = ''
        for x in range(3):
            for y in range(3):
                rep += f'[{self.cells[x][y]}]'
            rep += '\n'
        return rep

    def check_grid_result(self):
        # return None if no result, False if draw, else the player who won
        grid_lines = self.cells

        # Pour chacun des joueurs, on vérifie s'il a gagné
        for sign in ['o', 'x']:

            # test lines
            player_sign_3 = sign * 3

            line_1_as_str = ''.join(grid_lines[0])
            line_2_as_str = ''.join(grid_lines[1])
            line_3_as_str = ''.join(grid_lines[2])
            lines_as_list = [line_1_as_str, line_2_as_str, line_3_as_str]

            if player_sign_3 in lines_as_list:
                return sign

            # test columns
            col_1_as_str = f'{grid_lines[0][0]}{grid_lines[1][0]}{grid_lines[2][0]}'
            col_2_as_str = f'{grid_lines[0][1]}{grid_lines[1][1]}{grid_lines[2][1]}'
            col_3_as_str = f'{grid_lines[0][2]}{grid_lines[1][2]}{grid_lines[2][2]}'
            cols_as_list = [col_1_as_str, col_2_as_str, col_3_as_str]

            if player_sign_3 in cols_as_list:
                return sign

            # test diagonals
            diag_hgbd_str = f'{grid_lines[0][0]}{grid_lines[1][1]}{grid_lines[2][2]}'
            diag_hdbg_str = f'{grid_lines[0][2]}{grid_lines[1][1]}{grid_lines[2][0]}'

            if player_sign_3 in [diag_hdbg_str, diag_hgbd_str]:
                return sign

        # Check if grid is full
        lines_as_list_str = ''.join(lines_as_list)
        if ' ' in lines_as_list_str:
            return None

        return False
