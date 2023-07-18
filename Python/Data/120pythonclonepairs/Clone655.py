def splitListToRows(row, row_accumulator, target_column, separator) :
	split_row = row [target_column].split(separator)
	for s in split_row :
		new_row = row.to_dict()
		new_row [target_column] = s
		row_accumulator.append(new_row)


def splitListToRows(row, row_accumulator, target_columns, separator) :
	split_rows = []
	for target_column in target_columns :
		split_rows.append(row [target_column].split(separator))
	for i in range(len(split_rows [0])) :
		new_row = row.to_dict()
		for j in range(len(split_rows)) :
			new_row [target_columns [j]] = split_rows [j] [i]
		row_accumulator.append(new_row)

