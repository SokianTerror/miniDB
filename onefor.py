from table import Table
from __future__ import annotations
from tabulate import tabulate
import pickle
import os
from misc import get_op, split_condition


def _left_outer_join(self, table_right: Table, condition):
            print(f'outter join')
            column_name_left, operator, column_name_right = self._parse_condition(condition, join=True)
            try:
                column_index_left = self.column_names.index(column_name_left)
                column_index_right = self.column_names.index(column_name_right)
            except:
                raise Exception(f'Columns does not exist in one or both tables') 
            left_names = [f'{self.name}_{colname}' for colname in self.column_names]
            right_names = [f'{table_right._name}_{colname}' for colname in table_right.column_names]
            join_table_name = f'{self._name}_join_{table_right._name}'
            join_table_colnames = left_names + right_names
            join_table_coltypes = self.column_types + table_right.column_types
            join_table = Table(name=join_table_name, column_names=join_table_colnames, column_types=join_table_coltypes)
            no_of_ops = 0
            for  row_right in table_right.data:
                right_value = row_right[column_index_right]
                for row_left in self.data:
                    left_value = row_left[column_index_left]
                    exist = True
                    no_of_ops+=1
                    if get_op(operator, left_value, right_value): #EQ_OP
                        join_table._insert(row_left+row_right)
                if exist != True:
                    none_values = []
                    for i in range(len(self.columns)):
                        none_values.append('null')
                    join_table._insert(row_left + none_values)

            print(f'## Select ops no. -> {no_of_ops}')
            print(f'# Left table size. -> {len(self.data)}')
            print(f'# Right table size. -> {len(table_right.data)}')

            return left_outer_join
